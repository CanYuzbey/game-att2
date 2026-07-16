from __future__ import annotations

import pytest

from game_att2_sim.config_loader import load_config
from game_att2_sim.enums import HarvestQuality, LimbState, LimbTag, Slot
from game_att2_sim.errors import IllegalActionError, InsufficientBloodError
from game_att2_sim.events import EventLog
from game_att2_sim.factory import enemy_from_config, player_from_start
from game_att2_sim.models import HarvestedLimb, ScenarioMetrics
from game_att2_sim.rng import ScriptedRNG
from game_att2_sim.rules import RuleEngine, apply_damage, effectiveness, spend_blood
from game_att2_sim.scenarios import blood_bag_overlay


def engine(rolls: list[int] | None = None) -> tuple[RuleEngine, object, object]:
    config = load_config()
    player = player_from_start(config)
    log = EventLog()
    metrics = ScenarioMetrics("unit", 1, "balanced")
    resolver = RuleEngine(config, ScriptedRNG(rolls or [6]), log, metrics, tutorial=True)
    return resolver, player, metrics


def test_config_loads_and_has_all_slots() -> None:
    config = load_config()
    assert set(config.limbs)
    assert set(Slot(slot) for slot in config.starting_bodies["s001"]["slots"]) == set(Slot)
    assert not config.actions["grip_strike"].can_clean_sever


def test_limb_thresholds_and_basic_zero_is_ruined() -> None:
    resolver, player, _ = engine()
    jeff = enemy_from_config(resolver.config, "jeff")
    limb = jeff.body.slots[Slot.RIGHT_ARM]
    apply_damage(jeff, limb, 10, "test", resolver.log)
    assert limb.state is LimbState.DAMAGED
    apply_damage(jeff, limb, 10, "test", resolver.log)
    assert limb.state is LimbState.CRITICAL
    assert apply_damage(jeff, limb, 10, "Grip Strike", resolver.log) is HarvestQuality.RUINED
    assert limb.state is LimbState.RUINED
    assert effectiveness(player.body.slots[Slot.LEFT_ARM]) == 1


def test_clean_scissors_and_marked_harvest() -> None:
    resolver, player, metrics = engine()
    jeff = enemy_from_config(resolver.config, "jeff")
    target = jeff.body.slots[Slot.LEFT_ARM]
    resolver.start_round(player)
    resolver.claim(player, target)
    resolver.start_round(player)
    target.integrity = 6
    target.state = LimbState.CRITICAL
    assert resolver.scissors(player, jeff, target) is HarvestQuality.CLEAN
    harvested = resolver.harvest(target, HarvestQuality.CLEAN)
    assert harvested.quality is HarvestQuality.CLEAN
    assert metrics.clean_harvests == 1


def test_source_impairment_and_unusable_source() -> None:
    resolver, player, _ = engine()
    source = player.body.slots[Slot.LEFT_ARM]
    source.integrity = 20
    source.state = LimbState.DAMAGED
    assert resolver.config.actions["grip_strike"].damage * effectiveness(source) == 7.5
    source.state = LimbState.DISABLED
    with pytest.raises(IllegalActionError):
        resolver.grip(player, player, player.body.slots[Slot.TORSO])


def test_panic_pulse_and_soft_collapse_are_logged() -> None:
    resolver, player, metrics = engine([0])
    player.blood = 30
    spend_blood(player, 7, "test", resolver.config, resolver.log, metrics, True, resolver.rng)
    assert player.blood == 33
    assert player.panic_pulse_used
    player.blood = 5
    spend_blood(player, 5, "test collapse", resolver.config, resolver.log, metrics, True, resolver.rng)
    assert player.blood == 12
    assert player.soft_collapse_used
    assert any(event.event_type == "soft_collapse" for event in resolver.log.events)


def test_insufficient_blood_fails_loudly() -> None:
    resolver, player, metrics = engine()
    player.blood = 1
    with pytest.raises(InsufficientBloodError):
        spend_blood(player, 2, "invalid", resolver.config, resolver.log, metrics)


def test_focus_fast_and_consumable_limits() -> None:
    resolver, player, _ = engine()
    resolver.start_round(player)
    assert "Surgical Jab" in resolver.focus(player, "Surgical Jab against torso")
    resolver.fast_item(player, "blood_bag")
    with pytest.raises(IllegalActionError):
        resolver.fast_item(player, "clotting_cream", player.body.slots[Slot.TORSO])
    with pytest.raises(IllegalActionError):
        resolver.focus(player, "again")


def test_enemy_cancels_when_source_is_disabled() -> None:
    resolver, player, _ = engine()
    anna = enemy_from_config(resolver.config, "anna")
    anna.body.slots[Slot.RIGHT_ARM].state = LimbState.DISABLED
    resolver.enemy_attack(anna, player, Slot.RIGHT_ARM, Slot.TORSO, 8)
    assert resolver.log.events[-1].event_type == "enemy_action_cancelled"


@pytest.mark.parametrize(
    ("roll", "expected"), [(1, "twitch"), (2, "works"), (5, "ache"), (6, "surge")]
)
def test_unstable_branches(roll: int, expected: str) -> None:
    resolver, player, _ = engine([roll])
    arm = player.body.slots[Slot.RIGHT_ARM]
    arm.state = LimbState.INTACT
    arm.tags.add(LimbTag.UNSTABLE)
    resolver.start_round(player)
    assert arm.unstable_result == expected


def test_emergency_graft_quality_and_integration() -> None:
    resolver, player, _ = engine([1])
    jeff = enemy_from_config(resolver.config, "jeff")
    harvested = HarvestedLimb(jeff.body.slots[Slot.RIGHT_ARM], HarvestQuality.CLEAN)
    resolver.emergency_graft(player, harvested, Slot.RIGHT_ARM)
    arm = player.body.slots[Slot.RIGHT_ARM]
    assert LimbTag.GRAFTED in arm.tags
    assert LimbTag.UNSTABLE in arm.tags
    assert "guard_flesh" in arm.definition.actions
    resolver.integrate(player, "integrate_arm")
    assert LimbTag.INTEGRATED in arm.tags
    assert LimbTag.UNSTABLE not in arm.tags


def test_emergency_graft_charges_configured_cost_once_with_transaction_event() -> None:
    resolver, player, metrics = engine([6])
    limb = enemy_from_config(resolver.config, "jeff").body.slots[Slot.RIGHT_ARM]
    resolver.emergency_graft(player, HarvestedLimb(limb, HarvestQuality.CLEAN), Slot.RIGHT_ARM)
    transactions = [
        event.payload
        for event in resolver.log.events
        if event.event_type == "blood_changed" and event.payload["reason"] == "Emergency graft"
    ]
    assert transactions == [{"reason": "Emergency graft", "before": 85, "delta": -12, "after": 73}]
    assert metrics.blood_spent == 12


def test_blood_bag_overlay_isolated_from_baseline_config() -> None:
    config = load_config()
    overlay = blood_bag_overlay(config, gain=20, gain_if_bleeding=12, cap=60)
    assert config.items["blood_bag"] == {"name": "Blood Bag", "timing": "fast", "consumable": True, "gain": 25, "gain_if_bleeding": 15}
    assert overlay.items["blood_bag"]["gain"] == 20
    assert overlay.items["blood_bag"]["cap"] == 60


def test_ruined_harvest_cannot_graft() -> None:
    resolver, player, _ = engine()
    limb = enemy_from_config(resolver.config, "jeff").body.slots[Slot.RIGHT_ARM]
    with pytest.raises(IllegalActionError):
        resolver.emergency_graft(player, HarvestedLimb(limb, HarvestQuality.RUINED), Slot.RIGHT_ARM)


@pytest.mark.parametrize(
    ("marked", "roll", "quality", "force_unstable"),
    [(True, 3, HarvestQuality.STRESSED, False), (True, 6, HarvestQuality.CLEAN, True), (False, 4, HarvestQuality.STRESSED, False), (False, 6, HarvestQuality.STRESSED, True)],
)
def test_salvage_distributions(
    marked: bool, roll: int, quality: HarvestQuality, force_unstable: bool
) -> None:
    resolver, player, _ = engine([roll])
    target = enemy_from_config(resolver.config, "jeff").body.slots[Slot.RIGHT_ARM]
    target.state = LimbState.RUINED
    if marked:
        target.tags.add(LimbTag.MARKED)
    harvested = resolver.salvage(player, target)
    assert harvested is not None
    assert harvested.quality is quality
    assert harvested.force_unstable is force_unstable


def test_stabilized_failure_becomes_hanging_disabled() -> None:
    resolver, player, _ = engine([1])
    anna = enemy_from_config(resolver.config, "anna")
    target = anna.body.slots[Slot.RIGHT_ARM]
    target.integrity = 10
    target.state = LimbState.CRITICAL
    target.tags.add(LimbTag.STABILIZED)
    resolver.start_round(player)
    assert resolver.scissors(player, anna, target) is None
    assert target.state is LimbState.DISABLED
    assert LimbTag.HANGING in target.tags


def test_unstable_costs_ache_disable_and_surge_fallback() -> None:
    resolver, player, _ = engine([1])
    arm = player.body.slots[Slot.LEFT_ARM]
    arm.unstable_result = "twitch"
    assert resolver.limb_action_cost(player, arm, 4, "test") == 7
    arm.unstable_result = "ache"
    resolver.limb_action_cost(player, arm, 4, "test")
    assert arm.disabled_rounds == 1
    arm.unstable_result = "surge"
    arm.surge_unused = True
    resolver.start_round(player)
    assert player.blood > 0


def test_plead_pressure_reaches_generic_threshold() -> None:
    resolver, _, _ = engine()
    jeff = enemy_from_config(resolver.config, "jeff")
    assert not resolver.add_plead_pressure(jeff, "clean arm")
    assert resolver.add_plead_pressure(jeff, "blood below 20")


def test_table_choices_and_missing_arm_validation() -> None:
    resolver, player, _ = engine()
    with pytest.raises(IllegalActionError):
        resolver.integrate(player, "integrate_arm")
    resolver.integrate(player, "table_loan")
    assert player.debt == 30
    resolver.integrate(player, "strengthen_legs")
    assert player.body.slots[Slot.LEGS].name == "Braced Human Legs"
