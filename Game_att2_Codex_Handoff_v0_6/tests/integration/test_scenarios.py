from __future__ import annotations

import json

import pytest

from game_att2_sim.reporting import render_json
from game_att2_sim.scenarios import STRATEGIES, run_batch, run_scenario


@pytest.mark.parametrize(
    "scenario",
    [
        "jeff_baseline",
        "jeff_no_spend",
        "failed_hell_saw",
        "anna_stabilization",
        "anna_greed",
        "mini_campaign",
        "blood_bag_balance",
    ],
)
def test_required_scenarios_execute(scenario: str) -> None:
    result = run_scenario(scenario, 42)
    assert result.metrics.result == "completed"
    assert result.events
    assert any(event.event_type == "blood_changed" for event in result.events) or scenario == "jeff_no_spend"


def test_baseline_grafts_right_arm_and_no_spend_does_not() -> None:
    baseline = run_scenario("jeff_baseline", 42)
    no_spend = run_scenario("jeff_no_spend", 42)
    assert baseline.metrics.clean_harvests == 1
    assert "grafted" in baseline.body_summary["right_arm"]
    saw_events = [event for event in baseline.events if event.event_type == "hell_saw_roll"]
    assert len(saw_events) == 1
    assert saw_events[0].payload["valid"] is True
    assert baseline.metrics.actions["hell_saw"] == 1
    assert "bone_scissors" not in baseline.metrics.actions
    assert no_spend.metrics.clean_harvests == 0
    assert "missing" in no_spend.body_summary["right_arm"]


def test_campaign_is_seed_reproducible_and_integrates_body_change() -> None:
    first = run_scenario("mini_campaign", 42)
    second = run_scenario("mini_campaign", 42)
    assert first.events == second.events
    assert first.metrics == second.metrics
    assert first.metrics.table_choice == "integrate_arm"
    assert "integrated" in first.body_summary["right_arm"]


def test_json_report_includes_machine_readable_events() -> None:
    payload = json.loads(render_json(run_scenario("anna_stabilization", 42)))
    assert payload["metrics"]["trade_accepted"]
    assert payload["events"]


@pytest.mark.parametrize("strategy", sorted(STRATEGIES))
def test_batch_runs_each_required_strategy(strategy: str) -> None:
    batch = run_batch(strategy, count=3, seed=42)
    assert batch["count"] == 3
    assert 0 <= batch["completion_rate"] <= 1
    assert "final_blood_bands" in batch
    assert "survival_without_soft_rescue_rate" in batch
