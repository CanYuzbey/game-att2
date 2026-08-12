from __future__ import annotations

import json
from pathlib import Path

from game_att2_sim.enums import LimbState
from game_att2_sim.h1_research import (
    H1RunRequest,
    comparison_payload,
    run_comparisons,
    run_h1_attempt,
)
from game_att2_sim.reflex import ReflexTier
from game_att2_sim.scenarios import run_all

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def scripted_inputs() -> dict[str, int]:
    payload = json.loads(
        (PROJECT_ROOT / "examples" / "h1_scripted_comparisons.json").read_text(
            encoding="utf-8"
        )
    )
    return {str(key): int(value) for key, value in payload["inputs"].items()}


def all_results() -> dict[str, object]:
    results = run_comparisons(
        tuple(f"H1-C{index}" for index in range(1, 7)),
        scripted_inputs(),
    )
    return {result.request.variant_id: result for result in results}


def test_all_six_comparisons_emit_twelve_traceable_variants() -> None:
    results = all_results()

    assert len(results) == 12
    assert {str(result.request.comparison_id) for result in results.values()} == {
        f"H1-C{index}" for index in range(1, 7)
    }
    for result in results.values():
        event_types = {event.event_type for event in result.events}
        assert "h1_fixture_started" in event_types
        assert "h1_comparison_completed" in event_types
        assert result.evidence_class == "AUTOMATED_REGRESSION"
        assert result.deferred == (
            "wound_class",
            "wound_to_blood_mapping",
            "ruined_torso_downstream_result",
        )


def test_c1_preparation_improves_result_and_guard_is_consumed_once() -> None:
    results = all_results()
    unprepared = results["H1-C1-unprepared"]
    prepared = results["H1-C1-prepared"]

    assert prepared.metrics["target_damage"] < unprepared.metrics["target_damage"]
    assert prepared.metrics["grade"] == "strong"
    assert unprepared.metrics["grade"] == "limited"
    assert sum(event.event_type == "guard_consumed" for event in prepared.events) == 1
    assert sum(event.event_type == "reflex_modifier_applied" for event in prepared.events) == 1


def test_c2_exceptional_input_cannot_bypass_unusable_body_source() -> None:
    results = all_results()
    usable = results["H1-C2-usable"]
    unusable = results["H1-C2-unusable"]

    assert usable.resolution.grade is not None
    assert unusable.resolution.grade is None
    assert unusable.resolution.availability.reason == "blocking_source_unusable"
    assert unusable.metrics["target_damage"] == 8
    assert unusable.metrics["capability_retained"] is False


def test_c3_ordinary_miss_is_neutral_and_high_risk_miss_uses_previewed_source() -> None:
    results = all_results()
    ordinary = results["H1-C3-ordinary"]
    high_risk = results["H1-C3-high-risk"]

    assert ordinary.metrics["grade"] == high_risk.metrics["grade"] == "miss"
    assert ordinary.metrics["target_damage"] == high_risk.metrics["target_damage"] == 8
    assert ordinary.metrics["blocking_source_damage"] == 0
    assert high_risk.metrics["blocking_source_damage"] == 30
    assert high_risk.final_state["blocking_source_state"] == "ruined"
    assert high_risk.metrics["capability_retained"] is False
    types = [event.event_type for event in high_risk.events]
    assert types.index("reflex_risk_previewed") < types.index("reflex_input_recorded")
    exposure = next(event for event in high_risk.events if event.event_type == "reflex_source_exposed")
    assert exposure.payload["source"] == "right_arm"


def test_c4_and_c5_change_grade_without_changing_legality_pipeline() -> None:
    results = all_results()

    assert results["H1-C4-vague"].metrics["grade"] == "miss"
    assert results["H1-C4-exact"].metrics["grade"] == "limited"
    assert results["H1-C5-precise"].metrics["grade"] == "limited"
    assert results["H1-C5-assisted"].metrics["grade"] == "strong"
    for variant_id in ("H1-C5-precise", "H1-C5-assisted"):
        assert results[variant_id].resolution.availability.legal
        event_types = [event.event_type for event in results[variant_id].events]
        assert "reflex_opportunity_offered" in event_types
        assert "reflex_input_recorded" in event_types
        assert "reflex_grade_resolved" in event_types
        assert "reflex_modifier_applied" in event_types


def test_c6_exceptional_high_risk_block_preserves_only_known_integrity_threshold() -> None:
    results = all_results()
    normal = results["H1-C6-normal"]
    threshold = results["H1-C6-threshold"]

    assert normal.metrics["target_damage"] == 4
    assert threshold.metrics["target_damage"] == 0
    assert threshold.metrics["threshold_preserved"] is True
    assert threshold.final_state["target_integrity"] == 8
    assert threshold.metrics["blocking_source_damage"] == 4
    assert threshold.metrics["blood_delta_during_measured_interaction"] == 0
    assert not {
        "death",
        "victory",
        "survival_selected",
        "wound_applied",
    }.intersection(event.event_type for event in threshold.events)


def test_source_invalidation_after_grade_cancels_modifier_and_keeps_original_attack() -> None:
    request = H1RunRequest(
        comparison_id="H1-C2",
        variant_id="H1-C2-invalidated-after-offer",
        changed_condition="source_invalidated_after_resolution",
        timing_error=0,
        tier=ReflexTier.CRITICAL,
        invalidate_source_after_resolution=True,
    )

    result = run_h1_attempt(request)

    assert result.resolution.availability.legal
    assert result.metrics["target_damage"] == 8
    assert result.metrics["capability_retained"] is False
    assert "reflex_opportunity_cancelled" in {
        event.event_type for event in result.events
    }


def test_prepared_source_invalidation_cancels_guard_and_reflex_together() -> None:
    request = H1RunRequest(
        comparison_id="H1-C1",
        variant_id="H1-C1-prepared-invalidated",
        changed_condition="prepared_source_invalidated_after_resolution",
        timing_error=0,
        prepared=True,
        tier=ReflexTier.SIGNIFICANT,
        invalidate_source_after_resolution=True,
    )

    result = run_h1_attempt(request)

    assert result.metrics["target_damage"] == 8
    assert result.final_state["guard_active"] is False
    event_types = [event.event_type for event in result.events]
    assert "reflex_opportunity_cancelled" in event_types
    assert "guard_cancelled_source_unusable" in event_types
    assert "guard_consumed" not in event_types


def test_scripted_h1_payload_is_byte_reproducible() -> None:
    first = run_comparisons(("H1-C1", "H1-C6"), scripted_inputs())
    second = run_comparisons(("H1-C1", "H1-C6"), scripted_inputs())

    first_json = json.dumps(comparison_payload(first), sort_keys=True)
    second_json = json.dumps(comparison_payload(second), sort_keys=True)
    assert first_json == second_json
    events = comparison_payload(first)["runs"][0]["events"]  # type: ignore[index]
    assert all(event["fixture_id"] == "H1-F0" for event in events)  # type: ignore[index]
    assert all(event["comparison_id"] == "H1-C1" for event in events)  # type: ignore[index]


def test_h1_does_not_enter_the_seven_approved_scenario_runner() -> None:
    names = [result.metrics.scenario for result in run_all(42)]

    assert names == [
        "jeff_baseline",
        "jeff_no_spend",
        "failed_hell_saw",
        "anna_stabilization",
        "anna_greed",
        "mini_campaign",
        "blood_bag_balance",
    ]
    assert all("h1" not in name.lower() for name in names)


def test_missing_source_variant_uses_existing_missing_state_without_substitution() -> None:
    request = H1RunRequest(
        comparison_id="H1-C2",
        variant_id="H1-C2-missing",
        changed_condition="missing_right_arm",
        timing_error=0,
        blocking_source_state=LimbState.MISSING,
    )

    result = run_h1_attempt(request)

    assert result.resolution.availability.reason == "blocking_source_missing"
    assert result.metrics["target_damage"] == 8
    assert result.final_state["guard_flesh_available"] is False
