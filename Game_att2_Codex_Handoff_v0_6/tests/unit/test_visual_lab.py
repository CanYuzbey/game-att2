from __future__ import annotations

import pytest

from game_att2_sim.visual_lab import (
    LabAction,
    LabRisk,
    VisualLabTrialRequest,
    resolve_visual_lab_trial,
)


def request(**overrides: object) -> VisualLabTrialRequest:
    values: dict[str, object] = {
        "comparison_id": "VL-C1",
        "variant_id": "test",
        "signed_offset_ms": 120,
        "profile_id": "precise",
        "blood": 65,
        "readiness_before": 100,
        "repeated_block_count": 0,
    }
    values.update(overrides)
    return VisualLabTrialRequest(**values)  # type: ignore[arg-type]


def test_signed_early_and_late_offsets_are_symmetric() -> None:
    early = resolve_visual_lab_trial(request(signed_offset_ms=-120))
    late = resolve_visual_lab_trial(request(signed_offset_ms=120))

    assert early.grade == late.grade
    assert early.target_damage == late.target_damage
    assert early.signed_offset_ms == -late.signed_offset_ms


def test_repeated_block_and_low_blood_are_visible_separate_inputs() -> None:
    first = resolve_visual_lab_trial(request())
    repeated = resolve_visual_lab_trial(
        request(readiness_before=82, repeated_block_count=2)
    )
    low_blood = resolve_visual_lab_trial(
        request(blood=18, readiness_before=82, repeated_block_count=2)
    )

    assert repeated.readiness_cost > first.readiness_cost
    assert repeated.effective_absolute_offset_ms > first.effective_absolute_offset_ms
    assert low_blood.readiness_cost > repeated.readiness_cost
    assert "low_blood_amplifier" in low_blood.causal_factors
    assert low_blood.blood_delta == 0


def test_empty_readiness_weakens_but_does_not_make_block_illegal() -> None:
    result = resolve_visual_lab_trial(request(readiness_before=0, signed_offset_ms=0))

    assert result.legal is True
    assert result.grade is not None
    assert "readiness_exhausted" in result.causal_factors


def test_unusable_source_cannot_be_bypassed_by_exceptional_input() -> None:
    result = resolve_visual_lab_trial(request(source_usable=False, signed_offset_ms=0))

    assert result.legal is False
    assert result.disabled_reason == "blocking_source_unusable"
    assert result.grade is None
    assert result.target_damage == 8
    assert result.readiness_cost == 0


def test_forgo_and_pressure_break_recover_only_after_threat_resolution() -> None:
    forgo = resolve_visual_lab_trial(
        request(action=LabAction.FORGO_BLOCK, readiness_before=40, repeated_block_count=2)
    )
    pressure_break = resolve_visual_lab_trial(
        request(
            action=LabAction.FORGO_BLOCK,
            readiness_before=40,
            repeated_block_count=2,
            material_pressure_break=True,
        )
    )
    menu = resolve_visual_lab_trial(
        request(action=LabAction.MENU_ITEM, readiness_before=40, repeated_block_count=2)
    )

    assert forgo.readiness_after == 52
    assert pressure_break.readiness_after == 75
    assert menu.readiness_after == 40
    assert menu.target_damage == 0
    assert forgo.events[-1]["type"] == "threat_resolved"
    assert pressure_break.events[-1]["type"] == "threat_resolved"


def test_ordinary_miss_has_no_exposure_and_high_risk_requires_acknowledgement() -> None:
    ordinary = resolve_visual_lab_trial(request(signed_offset_ms=500))
    high_risk = resolve_visual_lab_trial(
        request(
            signed_offset_ms=500,
            risk=LabRisk.HIGH_RISK,
            high_risk_acknowledged=True,
        )
    )

    assert ordinary.grade == high_risk.grade == "miss"
    assert ordinary.source_exposure_damage == 0
    assert high_risk.source_exposure_damage == 30

    with pytest.raises(ValueError, match="acknowledged"):
        resolve_visual_lab_trial(request(risk=LabRisk.HIGH_RISK))
