"""NON_CANONICAL_VALIDATION_ONLY post-table consequence probe.

This module is a diagnostic continuation, not a combat encounter or content system.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import replace
from statistics import mean, median
from typing import Any, cast

from .config_loader import SimulatorConfig
from .enums import LimbState, LimbTag, Slot
from .errors import IllegalActionError, InsufficientBloodError, ScenarioDefinitionError
from .factory import body_summary
from .models import LimbRuntime, ScenarioResult
from .rng import SeededRNG
from .rules import apply_damage, spend_blood

PROBE_MARKER = "NON_CANONICAL_VALIDATION_ONLY"
THREAT_PROFILES = {"graft_pressure", "torso_pressure", "knockdown_pressure", "mixed_unknown_pressure"}
TABLE_CHOICES = {"integrate_arm", "repair_torso", "strengthen_legs", "table_loan", "leave"}
FIXTURES = {
    "campaign_pretable": "natural seed-42 pre-table state",
    "stable_damaged_comfortable": "controlled diagnostic fixture",
    "unstable_damaged_dangerous": "controlled diagnostic fixture",
    "stable_critical_dangerous": "controlled diagnostic fixture",
    "unstable_healthy_comfortable": "controlled diagnostic fixture",
    "stable_damaged_braced_low": "controlled diagnostic fixture",
    "graft_absent": "controlled diagnostic fixture",
    "existing_debt": "controlled diagnostic fixture",
}


def _pretable_session(config: SimulatorConfig, seed: int) -> Any:
    """Reproduce the accepted seed-42 campaign through Anna, stopping before table choice."""
    # Late import prevents scenarios -> probe -> scenarios initialization recursion.
    from .scenarios import _anna_stabilization, _jeff_baseline, _session

    session = _session("mini_campaign", 42, "balanced", config)
    if _jeff_baseline(session, graft=True) is None:
        raise ScenarioDefinitionError("seed-42 pre-table fixture did not acquire a graft")
    _anna_stabilization(session)
    session.name = "post_table_probe"
    session.metrics.scenario = "post_table_probe"
    session.metrics.seed = seed
    session.rng = SeededRNG(seed)
    session.engine.rng = session.rng
    return session


def _set_torso(player: Any, config: SimulatorConfig, state: LimbState) -> None:
    torso = player.body.slots[Slot.TORSO]
    torso.tags.discard(LimbTag.BLEEDING)
    if state is LimbState.INTACT:
        torso.integrity = torso.definition.max_integrity
    elif state is LimbState.DAMAGED:
        torso.integrity = 30
    else:
        torso.integrity = 10
    torso.state = state


def _fixture(config: SimulatorConfig, seed: int, fixture: str) -> Any:
    if fixture not in FIXTURES:
        raise ScenarioDefinitionError(f"unknown probe fixture: {fixture}")
    session = _pretable_session(config, seed)
    player = session.player
    arm = player.body.slots[Slot.RIGHT_ARM]
    if fixture == "campaign_pretable":
        return session
    if fixture == "stable_damaged_comfortable":
        player.blood = 70
        arm.tags.discard(LimbTag.UNSTABLE)
        _set_torso(player, config, LimbState.DAMAGED)
    elif fixture == "unstable_damaged_dangerous":
        player.blood = 35
        arm.tags.add(LimbTag.UNSTABLE)
        _set_torso(player, config, LimbState.DAMAGED)
    elif fixture == "stable_critical_dangerous":
        player.blood = 30
        arm.tags.discard(LimbTag.UNSTABLE)
        _set_torso(player, config, LimbState.CRITICAL)
    elif fixture == "unstable_healthy_comfortable":
        player.blood = 70
        arm.tags.add(LimbTag.UNSTABLE)
        _set_torso(player, config, LimbState.INTACT)
    elif fixture == "stable_damaged_braced_low":
        player.blood = 30
        arm.tags.discard(LimbTag.UNSTABLE)
        _set_torso(player, config, LimbState.DAMAGED)
        legs = player.body.slots[Slot.LEGS]
        legs.definition = replace(legs.definition, id="braced_human_legs", name="Braced Human Legs")
    elif fixture == "graft_absent":
        definition = config.limbs["missing_right_arm"]
        player.body.slots[Slot.RIGHT_ARM] = LimbRuntime(definition, 1, LimbState.MISSING)
        player.blood = 60
    elif fixture == "existing_debt":
        player.blood = 30
        player.debt = config.table_options["table_loan"]["debt"]
    return session


def _pressure(session: Any, slot: Slot, base_damage: int, profile: str, bleed: bool = False) -> int:
    """Apply existing limb damage/Guard/Bleeding rules without creating a content actor."""
    player = session.player
    target = player.body.slots[slot]
    damage = cast(
        int, session.engine.apply_guard_reduction(player, base_damage, source=PROBE_MARKER)
    )
    prevented = base_damage - damage
    apply_damage(player, target, damage, f"{PROBE_MARKER}:{profile}", session.log)
    session.log.emit(
        "noncanonical_probe_pressure",
        None,
        target_id=player.id,
        profile=profile,
        slot=slot.value,
        damage=damage,
        prevented=prevented,
    )
    if bleed:
        roll = session.rng.randint(1, 6)
        threshold = 4 if target.state in {LimbState.DAMAGED, LimbState.CRITICAL} else 5
        if roll >= threshold:
            session.engine.apply_bleeding(player, target, source=PROBE_MARKER, roll=roll)
    return prevented


def _graft_round(session: Any) -> dict[str, int]:
    arm = session.player.body.slots[Slot.RIGHT_ARM]
    available = int(arm.state not in {LimbState.DISABLED, LimbState.MISSING, LimbState.RUINED, LimbState.SEVERED})
    attempts = 0
    if available and session.player.blood >= session.config.actions["guard_flesh"].cost:
        try:
            session.engine.guard_flesh(session.player)
            attempts = 1
        except (IllegalActionError, InsufficientBloodError):
            pass
    return {"right_arm_available_rounds": available, "guard_attempts": attempts, "damage_prevented": _pressure(session, Slot.RIGHT_ARM, 8, "graft_pressure")}


def _torso_round(session: Any) -> dict[str, int]:
    torso = session.player.body.slots[Slot.TORSO]
    cream = 0
    if LimbTag.BLEEDING in torso.tags and session.player.inventory.get("clotting_cream", 0):
        try:
            session.engine.fast_item(session.player, "clotting_cream", torso)
            cream = 1
        except (IllegalActionError, InsufficientBloodError):
            pass
    return {"clotting_cream_uses": cream, "damage_prevented": _pressure(session, Slot.TORSO, 8, "torso_pressure", bleed=True)}


def _run_profile(session: Any, profile: str) -> tuple[dict[str, Any], list[str]]:
    if profile not in THREAT_PROFILES:
        raise ScenarioDefinitionError(f"unknown probe threat profile: {profile}")
    totals: dict[str, Any] = {"profile": profile, "rounds": 0, "damage_prevented": 0, "guard_attempts": 0, "right_arm_available_rounds": 0, "clotting_cream_uses": 0, "knockdown_attempts": 0, "failed_knockdowns": 0, "prevented_knockdowns": 0, "downed_applications": 0, "stand_actions": 0, "fast_while_downed": 0, "illegal_actions_rejected": 0}
    notes: list[str] = []
    sequence = [profile] * 4
    if profile == "mixed_unknown_pressure":
        options = list(session.config.scenarios["post_table_probe"]["pressure_distribution"])
        sequence = [session.rng.choice(options) for _ in range(4)]
        totals["selected_sequence"] = sequence
    for selected in sequence:
        try:
            session.engine.start_round(session.player)
        except InsufficientBloodError:
            # The baseline engine deliberately rejects unaffordable voluntary spends.  This
            # probe-only mapping makes unavoidable Bleeding pressure observable as collapse.
            session.player.blood = 0
            session.player.collapsed = True
            session.log.emit("noncanonical_probe_bleeding_collapse", session.player.id, marker=PROBE_MARKER)
            break
        totals["rounds"] = cast(int, totals["rounds"]) + 1
        if selected == "knockdown_pressure":
            totals["knockdown_attempts"] = cast(int, totals["knockdown_attempts"]) + 1
            downed = session.engine.resolve_knockdown(session.player, PROBE_MARKER, session.rng.randint(1, 6))
            if downed:
                totals["downed_applications"] = cast(int, totals["downed_applications"]) + 1
                if session.player.inventory.get("blood_bag", 0):
                    session.engine.fast_item(session.player, "blood_bag")
                    totals["fast_while_downed"] = cast(int, totals["fast_while_downed"]) + 1
                session.engine.stand(session.player)
                totals["stand_actions"] = cast(int, totals["stand_actions"]) + 1
                try:
                    session.engine.grip(session.player, session.player, session.player.body.slots[Slot.TORSO])
                except IllegalActionError:
                    totals["illegal_actions_rejected"] = cast(int, totals["illegal_actions_rejected"]) + 1
            elif session.player.brace_charges == 0:
                totals["prevented_knockdowns"] = cast(int, totals["prevented_knockdowns"]) + 1
            else:
                totals["failed_knockdowns"] = cast(int, totals["failed_knockdowns"]) + 1
            continue
        result = _graft_round(session) if selected == "graft_pressure" else _torso_round(session)
        for key, value in result.items():
            totals[key] = cast(int, totals.get(key, 0)) + value
        if session.player.collapsed:
            break
    return totals, sorted(set(notes))


def _settle_debt(session: Any) -> bool:
    player = session.player
    if not player.debt:
        return True
    due = player.debt
    if player.blood < due:
        session.log.emit("probe_debt_settlement_failed", player.id, due=due, blood=player.blood, marker=PROBE_MARKER)
        return False
    spend_blood(player, due, "Table Loan settlement", session.config, session.log, session.metrics, False, session.rng)
    player.debt = 0
    session.log.emit("probe_debt_settled", player.id, due=due, marker=PROBE_MARKER)
    return True


def run_post_table_probe(
    config: SimulatorConfig,
    seed: int = 42,
    table_choice: str = "integrate_arm",
    threat_profile: str = "graft_pressure",
    fixture: str = "campaign_pretable",
) -> ScenarioResult:
    if table_choice not in TABLE_CHOICES:
        raise ScenarioDefinitionError(f"unknown probe table choice: {table_choice}")
    session = _fixture(config, seed, fixture)
    notes = [PROBE_MARKER, FIXTURES[fixture]]
    legal = True
    probe_start = len(session.log.events)
    if table_choice == "table_loan" and session.player.debt:
        legal = False
        notes.append("illegal table choice: existing debt makes a second Table Loan probe-ineligible")
    elif table_choice == "strengthen_legs" and session.player.body.slots[Slot.LEGS].definition.id == "braced_human_legs":
        legal = False
        notes.append("illegal table choice: legs are already Braced in this diagnostic fixture")
    else:
        try:
            session.engine.integrate(session.player, table_choice)
        except (IllegalActionError, InsufficientBloodError) as error:
            legal = False
            notes.append(f"illegal table choice: {error}")
    pressure: dict[str, object] = {}
    if legal:
        session.engine.start_encounter(session.player)
        pressure, blocked = _run_profile(session, threat_profile)
        notes.extend(blocked)
    debt_paid = _settle_debt(session) if legal else True
    if not debt_paid:
        session.metrics.result = "debt_failed"
    elif not legal:
        session.metrics.result = "illegal"
    elif any(note.startswith("BLOCKED:") for note in notes):
        session.metrics.result = "not_identifiable"
    session.engine.end_round(session.player)
    session.metrics.final_blood = session.player.blood
    session.metrics.panic_pulse_used = session.player.panic_pulse_used
    session.metrics.soft_collapse_used = session.player.soft_collapse_used
    if session.player.collapsed:
        session.metrics.result = "collapsed"
    summary = body_summary(session.player)
    session.metrics.final_body_summary = "; ".join(f"{slot}: {value}" for slot, value in summary.items())
    events = session.log.events
    probe_events = events[probe_start:]
    session.metrics.probe_metrics = {
        "marker": PROBE_MARKER,
        "fixture": fixture,
        "fixture_classification": FIXTURES[fixture],
        "table_choice": table_choice,
        "threat_profile": threat_profile,
        "legal_option": legal,
        "debt_paid": debt_paid,
        "bleeding_rounds": sum(event.event_type == "blood_changed" and event.payload.get("reason") == "Bleeding" for event in probe_events),
        "unstable_events": sum(event.event_type == "unstable_check" for event in probe_events),
        "critical_body_states": sum("critical" in value for value in summary.values()),
        "pressure": pressure,
    }
    return ScenarioResult(session.metrics, events, summary, notes)


def run_probe_matrix(config: SimulatorConfig, seeds: int = 1000) -> list[dict[str, object]]:
    """Paired-seed aggregate rows; each option sees the same future RNG seed per state/profile."""
    rows: list[dict[str, object]] = []
    for fixture in FIXTURES:
        for profile in THREAT_PROFILES:
            for choice in TABLE_CHOICES:
                results = [run_post_table_probe(config, seed=42 + index, table_choice=choice, threat_profile=profile, fixture=fixture) for index in range(seeds)]
                legal = [result for result in results if result.metrics.probe_metrics["legal_option"]]
                blood = [result.metrics.final_blood for result in results]
                rows.append({
                    "fixture": fixture,
                    "threat_profile": profile,
                    "table_choice": choice,
                    "count": seeds,
                    "legal_option_rate": len(legal) / seeds,
                    "completion_rate": sum(result.metrics.result == "completed" for result in results) / seeds,
                    "collapse_rate": sum(result.metrics.result == "collapsed" for result in results) / seeds,
                    "debt_failure_rate": sum(result.metrics.result == "debt_failed" for result in results) / seeds,
                    "soft_collapse_rate": sum(result.metrics.soft_collapse_used for result in results) / seeds,
                    "minimum_final_blood": min(blood), "median_final_blood": median(blood), "average_final_blood": mean(blood), "maximum_final_blood": max(blood),
                    "panic_rate": sum(result.metrics.panic_pulse_used for result in results) / seeds,
                    "unstable_events": mean(cast(int, result.metrics.probe_metrics["unstable_events"]) for result in results),
                    "pressure": legal[0].metrics.probe_metrics["pressure"] if legal else {},
                })
    return rows


def table_cost_overlay(config: SimulatorConfig, delta: int) -> SimulatorConfig:
    """Isolated sensitivity overlay; baseline content remains immutable."""
    options = deepcopy(config.table_options)
    for choice in ("integrate_arm", "repair_torso", "strengthen_legs"):
        options[choice]["cost"] = max(0, int(options[choice]["cost"]) + delta)
    return replace(config, table_options=options)


def choose_table_option(
    config: SimulatorConfig,
    fixture: str,
    information_condition: str,
    known_profile: str | None = None,
) -> str:
    """Explicit diagnostic policy; it is not a behavioral claim about players."""
    if information_condition not in {"known_next_threat", "unknown_next_threat"}:
        raise ScenarioDefinitionError(f"unknown information condition: {information_condition}")
    session = _fixture(config, 42, fixture)
    player = session.player
    arm = player.body.slots[Slot.RIGHT_ARM]
    torso = player.body.slots[Slot.TORSO]
    if player.blood < 15 and not player.debt:
        return "table_loan"
    if information_condition == "known_next_threat":
        if known_profile == "graft_pressure" and LimbTag.UNSTABLE in arm.tags and player.blood >= 15:
            return "integrate_arm"
        if known_profile == "torso_pressure" and torso.state in {LimbState.DAMAGED, LimbState.CRITICAL} and player.blood >= 18:
            return "repair_torso"
        # Knockdown remains intentionally unoptimized until its consequence is approved.
        return "leave"
    if LimbTag.UNSTABLE in arm.tags and player.blood >= 50:
        return "integrate_arm"
    return "leave"


def run_policy_probe(config: SimulatorConfig, seeds: int = 100) -> list[dict[str, object]]:
    """Compare visible-state policy with known and unknown pressure information."""
    rows: list[dict[str, object]] = []
    for fixture in FIXTURES:
        for condition, profile in (("known_next_threat", "graft_pressure"), ("known_next_threat", "torso_pressure"), ("unknown_next_threat", "mixed_unknown_pressure")):
            choice = choose_table_option(config, fixture, condition, profile if condition == "known_next_threat" else None)
            results = [run_post_table_probe(config, 42 + seed, choice, profile, fixture) for seed in range(seeds)]
            rows.append({
                "fixture": fixture,
                "information_condition": condition,
                "known_profile": profile if condition == "known_next_threat" else None,
                "policy_choice": choice,
                "completion_rate": sum(result.metrics.result == "completed" for result in results) / seeds,
                "debt_failure_rate": sum(result.metrics.result == "debt_failed" for result in results) / seeds,
                "mean_final_blood": mean(result.metrics.final_blood for result in results),
            })
    return rows
