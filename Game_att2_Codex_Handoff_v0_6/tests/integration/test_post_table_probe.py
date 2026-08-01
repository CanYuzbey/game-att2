from __future__ import annotations

from dataclasses import replace

import pytest

from game_att2_sim.config_loader import load_config
from game_att2_sim.enums import LimbTag, Slot
from game_att2_sim.errors import IllegalActionError
from game_att2_sim.probe import (
    FIXTURES,
    PROBE_MARKER,
    THREAT_PROFILES,
    choose_table_option,
    run_post_table_probe,
    table_cost_overlay,
)
from game_att2_sim.scenarios import _session, run_scenario


def test_probe_is_noncanonical_and_does_not_change_campaign_regression() -> None:
    before = run_scenario("mini_campaign", 42)
    probe = run_post_table_probe(load_config(), 42, "integrate_arm", "graft_pressure")
    after = run_scenario("mini_campaign", 42)
    assert before.events == after.events
    assert PROBE_MARKER in probe.notes
    table_index = next(index for index, event in enumerate(probe.events) if event.event_type == "table_choice")
    assert not any(event.event_type == "harvest_created" for event in probe.events[table_index + 1 :])


@pytest.mark.parametrize("fixture", FIXTURES)
def test_controlled_fixtures_are_reported(fixture: str) -> None:
    result = run_post_table_probe(load_config(), 42, "leave", "graft_pressure", fixture)
    assert result.metrics.probe_metrics["fixture"] == fixture
    assert result.metrics.probe_metrics["marker"] == PROBE_MARKER


@pytest.mark.parametrize("profile", THREAT_PROFILES)
def test_each_pressure_profile_is_explicit(profile: str) -> None:
    result = run_post_table_probe(load_config(), 42, "leave", profile)
    if profile == "knockdown_pressure":
        assert result.metrics.result == "completed"
        assert result.metrics.probe_metrics["pressure"]["knockdown_attempts"] == 4
    else:
        assert result.metrics.probe_metrics["threat_profile"] == profile


def test_paired_seed_probe_is_reproducible() -> None:
    config = load_config()
    first = run_post_table_probe(config, 99, "integrate_arm", "mixed_unknown_pressure", "unstable_damaged_dangerous")
    second = run_post_table_probe(config, 99, "integrate_arm", "mixed_unknown_pressure", "unstable_damaged_dangerous")
    assert first.events == second.events
    assert first.metrics == second.metrics


def test_illegal_option_and_debt_settlement_are_distinguished() -> None:
    config = load_config()
    illegal = run_post_table_probe(config, 42, "integrate_arm", "graft_pressure", "graft_absent")
    debt = run_post_table_probe(config, 42, "leave", "torso_pressure", "existing_debt")
    assert illegal.metrics.result == "illegal"
    assert illegal.metrics.probe_metrics["legal_option"] is False
    assert debt.metrics.result == "debt_failed"
    assert debt.metrics.probe_metrics["debt_paid"] is False


def test_cost_overlay_isolated_and_probe_schema_is_machine_readable() -> None:
    config = load_config()
    overlay = table_cost_overlay(config, -3)
    assert config.table_options["integrate_arm"]["cost"] == 15
    assert overlay.table_options["integrate_arm"]["cost"] == 12
    result = run_post_table_probe(overlay, 42, "integrate_arm", "graft_pressure")
    assert {"legal_option", "debt_paid", "pressure", "unstable_events"} <= result.metrics.probe_metrics.keys()


def test_diagnostic_chooser_uses_only_declared_information() -> None:
    config = load_config()
    assert choose_table_option(config, "unstable_damaged_dangerous", "known_next_threat", "graft_pressure") == "integrate_arm"
    assert choose_table_option(config, "stable_damaged_comfortable", "unknown_next_threat") == "leave"


def test_brace_downed_fast_stand_and_action_rejection() -> None:
    session = _session("mini_campaign", 42, "balanced", load_config())
    player = session.player
    legs = player.body.slots[Slot.LEGS]
    legs.definition = replace(legs.definition, id="braced_human_legs", name="Braced Human Legs")
    session.engine.start_encounter(player)
    assert player.brace_charges == 1
    assert not session.engine.resolve_knockdown(player, "test", roll=6)
    assert player.brace_charges == 0 and not player.downed
    assert session.engine.resolve_knockdown(player, "test", roll=6)
    session.engine.fast_item(player, "blood_bag")
    assert player.downed
    session.engine.stand(player)
    with pytest.raises(IllegalActionError):
        session.engine.grip(player, player, player.body.slots[Slot.TORSO])
    assert any(event.event_type == "main_action_rejected" for event in session.log.events)


def test_failed_knockdown_preserves_brace_and_bleeding_can_kill() -> None:
    session = _session("mini_campaign", 42, "balanced", load_config())
    player = session.player
    legs = player.body.slots[Slot.LEGS]
    legs.definition = replace(legs.definition, id="braced_human_legs", name="Braced Human Legs")
    session.engine.start_encounter(player)
    assert not session.engine.resolve_knockdown(player, "test", roll=1)
    assert player.brace_charges == 1
    player.blood = 3
    player.body.slots[Slot.TORSO].tags.add(LimbTag.BLEEDING)
    session.engine.start_round(player)
    assert player.blood == 12 and player.limb_for_life_used
