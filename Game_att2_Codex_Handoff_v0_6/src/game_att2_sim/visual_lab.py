"""Pure shared-readiness and timed-Block contracts for visual-lab research.

The module is isolated from the approved campaign. It does not use RNG, mutate the
runtime simulator, print, create wounds, change Blood, or resolve an encounter.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from .visual_lab_config import VisualLabConfig, load_visual_lab_config


class LabAction(str, Enum):
    BLOCK = "block"
    FORGO_BLOCK = "forgo_block"
    MENU_ITEM = "menu_item"


class LabRisk(str, Enum):
    ORDINARY = "ordinary"
    HIGH_RISK = "high_risk"


@dataclass(frozen=True)
class VisualLabTrialRequest:
    comparison_id: str
    variant_id: str
    signed_offset_ms: int
    profile_id: str
    blood: int
    readiness_before: int
    repeated_block_count: int
    prepared: bool = False
    exact_intent: bool = True
    source_usable: bool = True
    action: LabAction = LabAction.BLOCK
    risk: LabRisk = LabRisk.ORDINARY
    high_risk_acknowledged: bool = False
    material_pressure_break: bool = False
    practice: bool = False


@dataclass(frozen=True)
class VisualLabTrialResult:
    request: VisualLabTrialRequest
    evidence_class: str
    provisional_label: str
    legal: bool
    disabled_reason: str | None
    signed_offset_ms: int
    effective_absolute_offset_ms: int | None
    grade: str | None
    original_damage: int
    target_damage: int
    mitigation: int
    source_exposure_damage: int
    source_capability_retained: bool
    readiness_before: int
    readiness_after: int
    readiness_band_before: str
    readiness_band_after: str
    readiness_cost: int
    readiness_recovery: int
    repeated_block_count_after: int
    blood_delta: int
    causal_factors: tuple[str, ...]
    explanation: str
    events: tuple[dict[str, object], ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "comparison_id": self.request.comparison_id,
            "variant_id": self.request.variant_id,
            "evidence_class": self.evidence_class,
            "provisional_label": self.provisional_label,
            "practice": self.request.practice,
            "action": self.request.action.value,
            "risk": self.request.risk.value,
            "high_risk_acknowledged": self.request.high_risk_acknowledged,
            "profile_id": self.request.profile_id,
            "blood": self.request.blood,
            "prepared": self.request.prepared,
            "exact_intent": self.request.exact_intent,
            "source_usable": self.request.source_usable,
            "legal": self.legal,
            "disabled_reason": self.disabled_reason,
            "signed_offset_ms": self.signed_offset_ms,
            "effective_absolute_offset_ms": self.effective_absolute_offset_ms,
            "grade": self.grade,
            "original_damage": self.original_damage,
            "target_damage": self.target_damage,
            "mitigation": self.mitigation,
            "source_exposure_damage": self.source_exposure_damage,
            "source_capability_retained": self.source_capability_retained,
            "readiness_before": self.readiness_before,
            "readiness_after": self.readiness_after,
            "readiness_band_before": self.readiness_band_before,
            "readiness_band_after": self.readiness_band_after,
            "readiness_cost": self.readiness_cost,
            "readiness_recovery": self.readiness_recovery,
            "repeated_block_count_before": self.request.repeated_block_count,
            "repeated_block_count_after": self.repeated_block_count_after,
            "blood_delta": self.blood_delta,
            "causal_factors": list(self.causal_factors),
            "explanation": self.explanation,
            "events": list(self.events),
        }


def _grade(profile_id: str, effective_offset: int, config: VisualLabConfig) -> str:
    for band in config.profile(profile_id).bands:
        if effective_offset <= band.max_absolute_offset_ms:
            return band.grade
    return "miss"


def _rounded_damage(base_damage: int, mitigation_basis_points: int) -> int:
    return (base_damage * (10000 - mitigation_basis_points) + 5000) // 10000


def _readiness_cost(request: VisualLabTrialRequest, config: VisualLabConfig) -> int:
    readiness = config.readiness
    cost = readiness.block_cost + (
        request.repeated_block_count * readiness.repeated_block_extra_cost
    )
    if request.blood <= readiness.low_blood_threshold:
        cost = (cost * readiness.low_blood_cost_multiplier_basis_points + 9999) // 10000
    return cost


def _base_event(request: VisualLabTrialRequest, event_type: str, **facts: object) -> dict[str, object]:
    return {
        "type": event_type,
        "fixture_id": "H1-F0",
        "comparison_id": request.comparison_id,
        "variant_id": request.variant_id,
        **facts,
    }


def resolve_visual_lab_trial(
    request: VisualLabTrialRequest,
    config: VisualLabConfig | None = None,
    evidence_class: str = "AUTOMATED_REGRESSION",
) -> VisualLabTrialResult:
    """Resolve one visual-lab trial from explicit state facts and signed input."""
    lab = config or load_visual_lab_config()
    if request.comparison_id not in {f"VL-C{index}" for index in range(1, 11)}:
        raise ValueError(f"unknown visual-lab comparison: {request.comparison_id}")
    if request.blood < 0:
        raise ValueError("visual-lab Blood cannot be negative")
    if not 0 <= request.readiness_before <= lab.readiness.maximum:
        raise ValueError("visual-lab readiness is outside the configured range")
    if request.repeated_block_count < 0:
        raise ValueError("visual-lab repeated Block count cannot be negative")
    lab.profile(request.profile_id)
    if request.risk is LabRisk.HIGH_RISK and not request.high_risk_acknowledged:
        raise ValueError("high-risk visual-lab response must be acknowledged")

    readiness = lab.readiness
    band_before = readiness.band_for(request.readiness_before)
    original_damage = lab.fixture.base_damage
    events: list[dict[str, object]] = [
        _base_event(
            request,
            "trial_started",
            action=request.action.value,
            blood=request.blood,
            readiness=request.readiness_before,
            repeated_block_count=request.repeated_block_count,
        )
    ]

    if request.action is LabAction.MENU_ITEM:
        events.append(
            _base_event(
                request,
                "menu_item_observed",
                readiness_recovery=readiness.menu_item_recovery,
                threat_resolved=False,
            )
        )
        return VisualLabTrialResult(
            request=request,
            evidence_class=evidence_class,
            provisional_label=lab.provisional_label,
            legal=True,
            disabled_reason=None,
            signed_offset_ms=request.signed_offset_ms,
            effective_absolute_offset_ms=None,
            grade=None,
            original_damage=original_damage,
            target_damage=0,
            mitigation=0,
            source_exposure_damage=0,
            source_capability_retained=request.source_usable,
            readiness_before=request.readiness_before,
            readiness_after=request.readiness_before,
            readiness_band_before=band_before,
            readiness_band_after=band_before,
            readiness_cost=0,
            readiness_recovery=0,
            repeated_block_count_after=request.repeated_block_count,
            blood_delta=0,
            causal_factors=("menu_item_no_recovery", "threat_unresolved"),
            explanation="The menu or item did not resolve Anna's threat and restored no readiness.",
            events=tuple(events),
        )

    if request.action is LabAction.FORGO_BLOCK:
        recovery = (
            readiness.pressure_break_recovery
            if request.material_pressure_break
            else readiness.modest_recovery
        )
        after = min(readiness.maximum, request.readiness_before + recovery)
        events.extend(
            (
                _base_event(
                    request,
                    "original_consequence_applied",
                    target_damage=original_damage,
                    block_used=False,
                ),
                _base_event(
                    request,
                    "readiness_recovered",
                    amount=recovery,
                    cause=(
                        "material_pressure_break"
                        if request.material_pressure_break
                        else "resolved_threat_without_block"
                    ),
                ),
                _base_event(request, "threat_resolved", readiness_after=after),
            )
        )
        cause = "material_pressure_break" if request.material_pressure_break else "forgone_block"
        return VisualLabTrialResult(
            request=request,
            evidence_class=evidence_class,
            provisional_label=lab.provisional_label,
            legal=True,
            disabled_reason=None,
            signed_offset_ms=request.signed_offset_ms,
            effective_absolute_offset_ms=None,
            grade=None,
            original_damage=original_damage,
            target_damage=original_damage,
            mitigation=0,
            source_exposure_damage=0,
            source_capability_retained=request.source_usable,
            readiness_before=request.readiness_before,
            readiness_after=after,
            readiness_band_before=band_before,
            readiness_band_after=readiness.band_for(after),
            readiness_cost=0,
            readiness_recovery=recovery,
            repeated_block_count_after=0,
            blood_delta=0,
            causal_factors=(cause, "recovery_after_threat_resolution"),
            explanation=(
                "The original Jab landed, but the explicit pressure break restored more readiness."
                if request.material_pressure_break
                else "The original Jab landed; forgoing Block restored limited readiness after the threat resolved."
            ),
            events=tuple(events),
        )

    if not request.source_usable:
        events.extend(
            (
                _base_event(
                    request,
                    "block_denied",
                    reason="blocking_source_unusable",
                ),
                _base_event(
                    request,
                    "original_consequence_applied",
                    target_damage=original_damage,
                ),
                _base_event(request, "threat_resolved", readiness_after=request.readiness_before),
            )
        )
        return VisualLabTrialResult(
            request=request,
            evidence_class=evidence_class,
            provisional_label=lab.provisional_label,
            legal=False,
            disabled_reason="blocking_source_unusable",
            signed_offset_ms=request.signed_offset_ms,
            effective_absolute_offset_ms=None,
            grade=None,
            original_damage=original_damage,
            target_damage=original_damage,
            mitigation=0,
            source_exposure_damage=0,
            source_capability_retained=False,
            readiness_before=request.readiness_before,
            readiness_after=request.readiness_before,
            readiness_band_before=band_before,
            readiness_band_after=band_before,
            readiness_cost=0,
            readiness_recovery=0,
            repeated_block_count_after=request.repeated_block_count,
            blood_delta=0,
            causal_factors=("blocking_source_unusable",),
            explanation="Perfect timing could not replace the unusable grafted Right Arm.",
            events=tuple(events),
        )

    timing = lab.timing
    factors: list[str] = ["signed_symmetric_timing", f"readiness_{band_before}"]
    effective = abs(request.signed_offset_ms)
    effective += request.repeated_block_count * timing.repeated_block_penalty_ms
    if request.repeated_block_count:
        factors.append("repeated_block_strain")
    if request.blood <= readiness.low_blood_threshold:
        effective += timing.low_blood_penalty_ms
        factors.append("low_blood_amplifier")
    effective += timing.readiness_band_penalty_ms[band_before]
    if request.prepared:
        effective = max(0, effective - timing.prepared_tolerance_bonus_ms)
        factors.append("guard_flesh_prepared")
    if not request.exact_intent:
        effective += timing.vague_intent_penalty_ms
        factors.append("vague_intent")
    if request.readiness_before == 0:
        factors.append("readiness_exhausted")

    grade = _grade(request.profile_id, effective, lab)
    mitigation_bps = lab.mitigation_basis_points[grade]
    target_damage = _rounded_damage(original_damage, mitigation_bps)
    source_damage = (
        lab.high_risk_exposure_damage[grade]
        if request.risk is LabRisk.HIGH_RISK
        else 0
    )
    cost = _readiness_cost(request, lab)
    after = max(0, request.readiness_before - cost)
    retained = source_damage < lab.fixture.blocking_source_integrity
    events.extend(
        (
            _base_event(
                request,
                "signed_input_recorded",
                signed_offset_ms=request.signed_offset_ms,
                effective_absolute_offset_ms=effective,
            ),
            _base_event(
                request,
                "block_resolved",
                grade=grade,
                mitigation_basis_points=mitigation_bps,
                target_damage=target_damage,
            ),
            _base_event(
                request,
                "readiness_spent",
                amount=cost,
                readiness_after=after,
            ),
        )
    )
    if source_damage:
        events.append(
            _base_event(
                request,
                "blocking_source_exposed",
                source="right_arm",
                damage=source_damage,
                capability_retained=retained,
            )
        )
    events.append(_base_event(request, "threat_resolved", readiness_after=after))
    return VisualLabTrialResult(
        request=request,
        evidence_class=evidence_class,
        provisional_label=lab.provisional_label,
        legal=True,
        disabled_reason=None,
        signed_offset_ms=request.signed_offset_ms,
        effective_absolute_offset_ms=effective,
        grade=grade,
        original_damage=original_damage,
        target_damage=target_damage,
        mitigation=original_damage - target_damage,
        source_exposure_damage=source_damage,
        source_capability_retained=retained,
        readiness_before=request.readiness_before,
        readiness_after=after,
        readiness_band_before=band_before,
        readiness_band_after=readiness.band_for(after),
        readiness_cost=cost,
        readiness_recovery=0,
        repeated_block_count_after=request.repeated_block_count + 1,
        blood_delta=0,
        causal_factors=tuple(factors),
        explanation=(
            f"The {grade} Block reduced the Jab from {original_damage} to {target_damage} "
            f"Torso integrity damage and used {cost} readiness."
        ),
        events=tuple(events),
    )


def visual_lab_variant_ids() -> dict[str, tuple[str, str]]:
    return {
        "VL-C1": ("VL-C1-first", "VL-C1-repeated"),
        "VL-C2": ("VL-C2-normal-blood", "VL-C2-low-blood"),
        "VL-C3": ("VL-C3-unprepared", "VL-C3-prepared"),
        "VL-C4": ("VL-C4-exact", "VL-C4-vague"),
        "VL-C5": ("VL-C5-precise", "VL-C5-assisted"),
        "VL-C6": ("VL-C6-early", "VL-C6-late"),
        "VL-C7": ("VL-C7-block", "VL-C7-forgo"),
        "VL-C8": ("VL-C8-continued-pressure", "VL-C8-pressure-break"),
        "VL-C9": ("VL-C9-usable", "VL-C9-unusable"),
        "VL-C10": ("VL-C10-ordinary", "VL-C10-high-risk"),
    }


def visual_lab_comparison_requests(
    comparison_id: str,
    signed_offsets: dict[str, int],
    config: VisualLabConfig | None = None,
) -> tuple[VisualLabTrialRequest, VisualLabTrialRequest]:
    lab = config or load_visual_lab_config()
    try:
        first_id, second_id = visual_lab_variant_ids()[comparison_id]
    except KeyError as error:
        raise ValueError(f"unknown visual-lab comparison: {comparison_id}") from error

    base: dict[str, Any] = {
        "comparison_id": comparison_id,
        "profile_id": "precise",
        "blood": lab.fixture.normal_blood,
        "readiness_before": lab.readiness.maximum,
        "repeated_block_count": 0,
    }
    variants: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {
        "VL-C1": ({}, {"readiness_before": 52, "repeated_block_count": 2}),
        "VL-C2": (
            {"readiness_before": 70, "repeated_block_count": 1},
            {
                "blood": lab.fixture.low_blood,
                "readiness_before": 70,
                "repeated_block_count": 1,
            },
        ),
        "VL-C3": ({}, {"prepared": True}),
        "VL-C4": ({"exact_intent": True}, {"exact_intent": False}),
        "VL-C5": ({"profile_id": "precise"}, {"profile_id": "assisted"}),
        "VL-C6": ({}, {}),
        "VL-C7": (
            {"readiness_before": 40, "repeated_block_count": 2},
            {
                "action": LabAction.FORGO_BLOCK,
                "readiness_before": 40,
                "repeated_block_count": 2,
            },
        ),
        "VL-C8": (
            {
                "action": LabAction.FORGO_BLOCK,
                "readiness_before": 40,
                "repeated_block_count": 2,
            },
            {
                "action": LabAction.FORGO_BLOCK,
                "readiness_before": 40,
                "repeated_block_count": 2,
                "material_pressure_break": True,
            },
        ),
        "VL-C9": ({"source_usable": True}, {"source_usable": False}),
        "VL-C10": (
            {},
            {"risk": LabRisk.HIGH_RISK, "high_risk_acknowledged": True},
        ),
    }
    first_changes, second_changes = variants[comparison_id]
    requests: list[VisualLabTrialRequest] = []
    for variant_id, changes in ((first_id, first_changes), (second_id, second_changes)):
        if variant_id not in signed_offsets:
            raise ValueError(f"missing visual-lab signed offset for {variant_id}")
        values = {**base, **changes}
        values.update(
            {
                "variant_id": variant_id,
                "signed_offset_ms": signed_offsets[variant_id],
            }
        )
        requests.append(VisualLabTrialRequest(**values))
    return requests[0], requests[1]


def run_visual_lab_comparisons(
    comparison_ids: tuple[str, ...],
    signed_offsets: dict[str, int],
    evidence_class: str = "AUTOMATED_REGRESSION",
    config: VisualLabConfig | None = None,
) -> list[VisualLabTrialResult]:
    lab = config or load_visual_lab_config()
    results: list[VisualLabTrialResult] = []
    for comparison_id in comparison_ids:
        for request in visual_lab_comparison_requests(comparison_id, signed_offsets, lab):
            results.append(resolve_visual_lab_trial(request, lab, evidence_class))
    return results


def comparison_payload(results: list[VisualLabTrialResult]) -> dict[str, object]:
    return {
        "artifact": "game-att2-visual-interaction-lab-evidence-0.1",
        "fixture_id": "H1-F0",
        "plan_version": "VL-0.1",
        "evidence_class": (
            results[0].evidence_class if results else "AUTOMATED_REGRESSION"
        ),
        "claims_boundary": (
            "Automation proves fidelity and determinism only; it does not establish fun, "
            "comprehension, accessibility, fairness, balance, or production readiness."
        ),
        "runs": [result.to_dict() for result in results],
    }
