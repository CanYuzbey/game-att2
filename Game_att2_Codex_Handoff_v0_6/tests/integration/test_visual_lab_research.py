from __future__ import annotations

import json
from pathlib import Path

from game_att2_sim.scenarios import run_all
from game_att2_sim.visual_lab import (
    comparison_payload,
    run_visual_lab_comparisons,
)
from game_att2_sim.visual_lab_cli import load_visual_lab_script

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = PROJECT_ROOT / "examples" / "visual_lab_scripted_comparisons.json"


def results() -> dict[str, object]:
    _, offsets = load_visual_lab_script(SCRIPT)
    runs = run_visual_lab_comparisons(tuple(f"VL-C{i}" for i in range(1, 11)), offsets)
    return {run.request.variant_id: run for run in runs}


def test_all_ten_comparisons_emit_twenty_traceable_variants() -> None:
    runs = results()

    assert len(runs) == 20
    assert {run.request.comparison_id for run in runs.values()} == {
        f"VL-C{i}" for i in range(1, 11)
    }
    assert all(run.evidence_class == "AUTOMATED_REGRESSION" for run in runs.values())
    assert all(run.provisional_label == "PROVISIONAL_VISUAL_LAB_ONLY" for run in runs.values())


def test_required_comparison_boundaries_are_causal() -> None:
    runs = results()

    assert runs["VL-C1-repeated"].effective_absolute_offset_ms > runs["VL-C1-first"].effective_absolute_offset_ms
    assert "low_blood_amplifier" in runs["VL-C2-low-blood"].causal_factors
    assert runs["VL-C3-prepared"].target_damage < runs["VL-C3-unprepared"].target_damage
    assert runs["VL-C4-exact"].effective_absolute_offset_ms < runs["VL-C4-vague"].effective_absolute_offset_ms
    assert runs["VL-C5-precise"].grade != runs["VL-C5-assisted"].grade
    assert runs["VL-C6-early"].grade == runs["VL-C6-late"].grade
    assert runs["VL-C7-forgo"].readiness_after > runs["VL-C7-block"].readiness_after
    assert runs["VL-C8-pressure-break"].readiness_after > runs["VL-C8-continued-pressure"].readiness_after
    assert runs["VL-C9-unusable"].legal is False
    assert runs["VL-C10-ordinary"].source_exposure_damage == 0
    assert runs["VL-C10-high-risk"].source_exposure_damage == 30


def test_visual_lab_payload_is_byte_identical_and_claim_bounded() -> None:
    evidence_class, offsets = load_visual_lab_script(SCRIPT)
    comparison_ids = tuple(f"VL-C{i}" for i in range(1, 11))
    first = comparison_payload(run_visual_lab_comparisons(comparison_ids, offsets, evidence_class))
    second = comparison_payload(run_visual_lab_comparisons(comparison_ids, offsets, evidence_class))

    assert json.dumps(first, sort_keys=True) == json.dumps(second, sort_keys=True)
    assert "does not establish fun" in str(first["claims_boundary"])
    assert all(run["blood_delta"] == 0 for run in first["runs"])  # type: ignore[index]


def test_visual_lab_does_not_change_approved_scenario_catalog() -> None:
    assert [run.metrics.scenario for run in run_all(42)] == [
        "jeff_baseline",
        "jeff_no_spend",
        "failed_hell_saw",
        "anna_stabilization",
        "anna_greed",
        "mini_campaign",
        "blood_bag_balance",
    ]
