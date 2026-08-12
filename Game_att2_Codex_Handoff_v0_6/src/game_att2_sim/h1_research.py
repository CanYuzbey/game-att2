"""Deterministic H1 fixture, comparisons, and inspectable evidence exports."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any

from .config_loader import SimulatorConfig, load_config
from .enums import HarvestQuality, IntentClarity, LimbState, Slot
from .events import EventLog
from .factory import body_summary, enemy_from_config, player_from_start
from .h1_config import H1Config, load_h1_config
from .models import CombatantRuntime, Event, HarvestedLimb, ScenarioMetrics
from .reflex import (
    ReflexAttempt,
    ReflexContext,
    ReflexResolution,
    ReflexTier,
    RiskClass,
    resolve_reflex,
)
from .rng import ScriptedRNG
from .rules import RuleEngine, apply_damage, is_usable, recalculate_state

EVIDENCE_CLASSES = {"AUTOMATED_REGRESSION", "OWNER_DIAGNOSTIC"}


@dataclass(frozen=True)
class H1RunRequest:
    comparison_id: str
    variant_id: str
    changed_condition: str
    timing_error: int
    profile_id: str = "precise"
    intent_clarity: IntentClarity = IntentClarity.EXACT
    prepared: bool = False
    tier: ReflexTier = ReflexTier.ROUTINE
    risk_class: RiskClass = RiskClass.ORDINARY
    high_risk_acknowledged: bool = False
    blocking_source_state: LimbState | None = None
    blocking_source_compatible: bool = True
    threshold_pressure: bool = False
    invalidate_source_after_resolution: bool = False


@dataclass(frozen=True)
class H1RunResult:
    request: H1RunRequest
    evidence_class: str
    spec_version: str
    config_version: str
    prior_state: Mapping[str, object]
    resolution: ReflexResolution
    final_state: Mapping[str, object]
    metrics: Mapping[str, object]
    events: tuple[Event, ...]
    deferred: tuple[str, ...]

    def payload(self) -> dict[str, Any]:
        return {
            "evidence_class": self.evidence_class,
            "fixture_id": "H1-F0",
            "comparison_id": self.request.comparison_id,
            "variant_id": self.request.variant_id,
            "changed_condition": self.request.changed_condition,
            "spec_version": self.spec_version,
            "config_version": self.config_version,
            "request": _enum_values(asdict(self.request)),
            "prior_state": dict(self.prior_state),
            "resolution": _enum_values(asdict(self.resolution)),
            "final_state": dict(self.final_state),
            "metrics": dict(self.metrics),
            "events": [
                _event_payload(
                    event,
                    comparison_id=self.request.comparison_id,
                    variant_id=self.request.variant_id,
                    spec_version=self.spec_version,
                    config_version=self.config_version,
                )
                for event in self.events
            ],
            "deferred": list(self.deferred),
        }


def _enum_values(value: object) -> object:
    if isinstance(value, dict):
        return {str(key): _enum_values(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [_enum_values(child) for child in value]
    if isinstance(value, Enum):
        return value.value
    return value


def _event_payload(
    event: Event,
    *,
    comparison_id: str,
    variant_id: str,
    spec_version: str,
    config_version: str,
) -> dict[str, object]:
    return {
        "fixture_id": "H1-F0",
        "comparison_id": comparison_id,
        "variant_id": variant_id,
        "spec_version": spec_version,
        "config_version": config_version,
        "sequence": event.sequence,
        "round_number": event.round_number,
        "phase": event.phase,
        "event_type": event.event_type,
        "actor_id": event.actor_id,
        "target_id": event.target_id,
        "payload": _enum_values(event.payload),
    }


def _capability_available(player_arm_state: LimbState, actions: tuple[str, ...]) -> bool:
    return player_arm_state in {
        LimbState.INTACT,
        LimbState.DAMAGED,
        LimbState.CRITICAL,
    } and "guard_flesh" in actions


def _build_engine_and_fixture(
    simulator_config: SimulatorConfig,
) -> tuple[RuleEngine, CombatantRuntime, CombatantRuntime]:
    log = EventLog()
    metrics = ScenarioMetrics("h1_research", 42, "scripted")
    engine = RuleEngine(
        simulator_config,
        ScriptedRNG([6, 1], fallback=1),
        log,
        metrics,
        tutorial=False,
    )
    player = player_from_start(simulator_config)
    jeff = enemy_from_config(simulator_config, "jeff")
    harvested = HarvestedLimb(
        jeff.body.slots[Slot.RIGHT_ARM],
        HarvestQuality.CLEAN,
    )
    engine.emergency_graft(player, harvested, Slot.RIGHT_ARM)
    anna = enemy_from_config(simulator_config, "anna")
    return engine, player, anna


def _validate_fixture_references(
    simulator_config: SimulatorConfig,
    h1_config: H1Config,
) -> None:
    fixture = h1_config.fixture
    incoming = simulator_config.actions.get(fixture.incoming_action)
    guard = simulator_config.actions.get(fixture.guard_action)
    anna = simulator_config.enemies.get(fixture.attacker_id)
    torso = simulator_config.limbs["damaged_human_torso"]
    if (
        incoming is None
        or incoming.source_slot is not fixture.attacker_source
        or incoming.damage != fixture.base_damage
    ):
        raise ValueError("H1 fixture has drifted from the configured Surgical Jab")
    if guard is None or guard.source_slot is not fixture.blocking_source:
        raise ValueError("H1 fixture has drifted from configured Guard Flesh")
    if not isinstance(anna, dict) or fixture.incoming_action not in anna.get("actions", []):
        raise ValueError("H1 fixture attacker cannot perform the configured incoming action")
    if fixture.normal_torso_integrity > torso.max_integrity:
        raise ValueError("H1 normal Torso integrity exceeds the current definition")
    if fixture.threshold_torso_integrity > torso.max_integrity:
        raise ValueError("H1 threshold Torso integrity exceeds the current definition")


def run_h1_attempt(
    request: H1RunRequest,
    *,
    evidence_class: str = "AUTOMATED_REGRESSION",
    simulator_config: SimulatorConfig | None = None,
    h1_config: H1Config | None = None,
) -> H1RunResult:
    """Run one isolated post-Jeff versus Anna Block interaction."""
    if evidence_class not in EVIDENCE_CLASSES:
        raise ValueError(f"unsupported H1 evidence class: {evidence_class}")
    if request.comparison_id not in {f"H1-C{index}" for index in range(1, 7)}:
        raise ValueError(f"unknown H1 comparison: {request.comparison_id}")

    simulator_config = simulator_config or load_config()
    h1_config = h1_config or load_h1_config()
    _validate_fixture_references(simulator_config, h1_config)
    fixture = h1_config.fixture
    engine, player, anna = _build_engine_and_fixture(simulator_config)
    arm = player.body.slots[fixture.blocking_source]
    torso = player.body.slots[fixture.target]

    if request.blocking_source_state is not None:
        arm.state = request.blocking_source_state
        if arm.state in {LimbState.MISSING, LimbState.RUINED, LimbState.SEVERED}:
            arm.integrity = 0
    torso.integrity = (
        fixture.threshold_torso_integrity
        if request.threshold_pressure
        else fixture.normal_torso_integrity
    )
    torso.state = recalculate_state(torso)

    engine.start_encounter(player)
    engine.start_round(player)
    if request.prepared:
        engine.guard_flesh(player)
    else:
        engine.brace(player)

    prior_arm_integrity = arm.integrity
    prior_torso_integrity = torso.integrity
    prior_blood = player.blood
    prior_state: dict[str, object] = {
        "player_body": body_summary(player),
        "anna_body": body_summary(anna),
        "blood": player.blood,
        "guard_active": player.guard_active,
        "blocking_source_integrity": arm.integrity,
        "blocking_source_state": arm.state.value,
        "target_integrity": torso.integrity,
        "target_state": torso.state.value,
        "intent_clarity": request.intent_clarity.value,
        "preparation": "guard_flesh" if request.prepared else "brace",
    }
    engine.log.emit(
        "h1_fixture_started",
        player.id,
        target_id=anna.id,
        fixture_id=fixture.fixture_id,
        comparison_id=request.comparison_id,
        variant_id=request.variant_id,
        spec_version=h1_config.spec_version,
        config_version=h1_config.schema_version,
        incoming_action=fixture.incoming_action,
        attacking_source=fixture.attacker_source.value,
        target=fixture.target.value,
    )

    context = ReflexContext(
        incoming_action=fixture.incoming_action,
        attacking_source=fixture.attacker_source,
        target_slot=fixture.target,
        blocking_source=fixture.blocking_source,
        intent_clarity=request.intent_clarity,
        tier=request.tier,
        attacking_source_usable=is_usable(anna.body.slots[fixture.attacker_source]),
        blocking_source_present=arm.state is not LimbState.MISSING,
        blocking_source_usable=is_usable(arm),
        blocking_source_compatible=request.blocking_source_compatible,
        cost_affordable=True,
        actor_downed=player.downed,
        prepared=request.prepared,
    )
    attempt = ReflexAttempt(
        request.profile_id,
        request.timing_error,
        request.risk_class,
        request.high_risk_acknowledged,
    )
    resolution = resolve_reflex(h1_config, context, attempt)
    if resolution.availability.legal:
        engine.log.emit(
            "reflex_opportunity_offered",
            player.id,
            target_id=anna.id,
            fixture_id=fixture.fixture_id,
            comparison_id=request.comparison_id,
            variant_id=request.variant_id,
            tier=request.tier.value,
            prepared=request.prepared,
            intent_clarity=request.intent_clarity.value,
        )
        if request.risk_class is RiskClass.HIGH_RISK:
            engine.log.emit(
                "reflex_risk_previewed",
                player.id,
                source=h1_config.high_risk_affected_source.value,
                damage_by_grade={
                    grade.value: damage
                    for grade, damage in h1_config.high_risk_exposure_damage.items()
                },
                acknowledged=request.high_risk_acknowledged,
            )
        engine.log.emit(
            "reflex_input_recorded",
            player.id,
            profile_id=request.profile_id,
            assisted=h1_config.profile(request.profile_id).assisted,
            raw_timing_error=request.timing_error,
            effective_timing_error=resolution.effective_timing_error,
        )
        engine.log.emit(
            "reflex_grade_resolved",
            player.id,
            grade=(resolution.grade.value if resolution.grade else None),
            reduction_basis_points=resolution.modifier.damage_reduction_basis_points,
            state_modifier_only=True,
        )
    else:
        engine.log.emit(
            "reflex_opportunity_denied",
            player.id,
            target_id=anna.id,
            fixture_id=fixture.fixture_id,
            comparison_id=request.comparison_id,
            variant_id=request.variant_id,
            reason=resolution.availability.reason,
        )

    if request.invalidate_source_after_resolution and resolution.availability.legal:
        apply_damage(
            player,
            arm,
            arm.integrity,
            "H1 scripted source invalidation",
            engine.log,
        )

    engine.enemy_attack(
        anna,
        player,
        fixture.attacker_source,
        fixture.target,
        fixture.base_damage,
        can_bleed=True,
        modifier=resolution.modifier if resolution.availability.legal else None,
    )

    capability = _capability_available(arm.state, arm.definition.actions)
    engine.log.emit(
        "reflex_capability_recomputed",
        player.id,
        source=fixture.blocking_source.value,
        source_state=arm.state.value,
        guard_flesh_available=capability,
    )
    target_damage = prior_torso_integrity - torso.integrity
    source_damage = prior_arm_integrity - arm.integrity
    engine.log.emit(
        "h1_comparison_completed",
        player.id,
        target_id=anna.id,
        comparison_id=request.comparison_id,
        variant_id=request.variant_id,
        target_damage=target_damage,
        source_damage=source_damage,
        capability_retained=capability,
    )

    final_state: dict[str, object] = {
        "player_body": body_summary(player),
        "anna_body": body_summary(anna),
        "blood": player.blood,
        "guard_active": player.guard_active,
        "blocking_source_integrity": arm.integrity,
        "blocking_source_state": arm.state.value,
        "target_integrity": torso.integrity,
        "target_state": torso.state.value,
        "guard_flesh_available": capability,
    }
    metrics: dict[str, object] = {
        "opportunity_offered": resolution.availability.legal,
        "disabled_reason": resolution.availability.reason,
        "grade": resolution.grade.value if resolution.grade else None,
        "target_damage": target_damage,
        "target_damage_prevented_from_base": fixture.base_damage - target_damage,
        "blocking_source_damage": source_damage,
        "capability_retained": capability,
        "blood_delta_during_measured_interaction": player.blood - prior_blood,
        "threshold_preserved": request.threshold_pressure and torso.integrity > 0,
    }
    return H1RunResult(
        request=request,
        evidence_class=evidence_class,
        spec_version=h1_config.spec_version,
        config_version=h1_config.schema_version,
        prior_state=prior_state,
        resolution=resolution,
        final_state=final_state,
        metrics=metrics,
        events=tuple(engine.log.events),
        deferred=(
            "wound_class",
            "wound_to_blood_mapping",
            "ruined_torso_downstream_result",
        ),
    )


def comparison_requests(
    comparison_id: str,
    timing_inputs: Mapping[str, int],
    *,
    profile_override: str | None = None,
) -> tuple[H1RunRequest, H1RunRequest]:
    """Build the two spec-defined variants for one comparison."""
    builders: dict[str, tuple[dict[str, object], dict[str, object]]] = {
        "H1-C1": (
            {
                "variant_id": "H1-C1-unprepared",
                "changed_condition": "unprepared",
            },
            {
                "variant_id": "H1-C1-prepared",
                "changed_condition": "guard_flesh_prepared",
                "prepared": True,
                "tier": ReflexTier.SIGNIFICANT,
            },
        ),
        "H1-C2": (
            {
                "variant_id": "H1-C2-usable",
                "changed_condition": "usable_grafted_right_arm",
            },
            {
                "variant_id": "H1-C2-unusable",
                "changed_condition": "unusable_grafted_right_arm",
                "blocking_source_state": LimbState.DISABLED,
            },
        ),
        "H1-C3": (
            {
                "variant_id": "H1-C3-ordinary",
                "changed_condition": "ordinary_block",
                "threshold_pressure": True,
                "tier": ReflexTier.CRITICAL,
            },
            {
                "variant_id": "H1-C3-high-risk",
                "changed_condition": "disclosed_high_risk_block",
                "threshold_pressure": True,
                "tier": ReflexTier.CRITICAL,
                "risk_class": RiskClass.HIGH_RISK,
                "high_risk_acknowledged": True,
            },
        ),
        "H1-C4": (
            {
                "variant_id": "H1-C4-vague",
                "changed_condition": "vague_intent",
                "intent_clarity": IntentClarity.VAGUE,
            },
            {
                "variant_id": "H1-C4-exact",
                "changed_condition": "exact_intent",
                "intent_clarity": IntentClarity.EXACT,
            },
        ),
        "H1-C5": (
            {
                "variant_id": "H1-C5-precise",
                "changed_condition": "precise_profile",
                "profile_id": "precise",
            },
            {
                "variant_id": "H1-C5-assisted",
                "changed_condition": "assisted_profile",
                "profile_id": "assisted",
            },
        ),
        "H1-C6": (
            {
                "variant_id": "H1-C6-normal",
                "changed_condition": "normal_torso_pressure",
                "risk_class": RiskClass.HIGH_RISK,
                "high_risk_acknowledged": True,
            },
            {
                "variant_id": "H1-C6-threshold",
                "changed_condition": "threshold_torso_pressure",
                "threshold_pressure": True,
                "tier": ReflexTier.CRITICAL,
                "risk_class": RiskClass.HIGH_RISK,
                "high_risk_acknowledged": True,
            },
        ),
    }
    try:
        raw_pair = builders[comparison_id]
    except KeyError as error:
        raise ValueError(f"unknown H1 comparison: {comparison_id}") from error
    requests: list[H1RunRequest] = []
    for raw in raw_pair:
        variant_id = str(raw["variant_id"])
        if variant_id not in timing_inputs:
            raise ValueError(f"missing scripted timing input for {variant_id}")
        values = dict(raw)
        values["comparison_id"] = comparison_id
        values["timing_error"] = timing_inputs[variant_id]
        if profile_override is not None and comparison_id != "H1-C5":
            values["profile_id"] = profile_override
        requests.append(H1RunRequest(**values))  # type: ignore[arg-type]
    return requests[0], requests[1]


def run_comparisons(
    comparison_ids: tuple[str, ...],
    timing_inputs: Mapping[str, int],
    *,
    evidence_class: str = "AUTOMATED_REGRESSION",
    profile_override: str | None = None,
) -> list[H1RunResult]:
    results: list[H1RunResult] = []
    for comparison_id in comparison_ids:
        for request in comparison_requests(
            comparison_id, timing_inputs, profile_override=profile_override
        ):
            results.append(run_h1_attempt(request, evidence_class=evidence_class))
    return results


def comparison_payload(results: list[H1RunResult]) -> dict[str, object]:
    return {
        "artifact": "Game att2 H1 deterministic research evidence",
        "evidence_class": results[0].evidence_class if results else None,
        "claims_boundary": (
            "This evidence establishes implementation fidelity and determinism only; "
            "it does not establish fun, balance, comprehension, or accessibility."
        ),
        "runs": [result.payload() for result in results],
    }


def render_h1_markdown(results: list[H1RunResult]) -> str:
    lines = [
        "# Game att2 H1 Research Evidence",
        "",
        (
            "Implementation-fidelity evidence only. This does not establish fun, balance, "
            "comprehension, or accessibility."
        ),
        "",
        "| Comparison | Variant | Legal | Grade | Target damage | Source damage | Capability |",
        "|---|---|---:|---|---:|---:|---:|",
    ]
    for result in results:
        lines.append(
            "| {comparison} | {variant} | {legal} | {grade} | {target} | {source} | {capability} |".format(
                comparison=result.request.comparison_id,
                variant=result.request.variant_id,
                legal=str(result.resolution.availability.legal).lower(),
                grade=result.metrics["grade"] or "denied",
                target=result.metrics["target_damage"],
                source=result.metrics["blocking_source_damage"],
                capability=str(result.metrics["capability_retained"]).lower(),
            )
        )
    return "\n".join(lines) + "\n"
