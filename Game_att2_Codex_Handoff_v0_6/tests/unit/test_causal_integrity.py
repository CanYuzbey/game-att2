from __future__ import annotations

from collections import Counter

import pytest

from game_att2_sim.config_loader import load_config
from game_att2_sim.enums import HarvestQuality, LimbState, LimbTag, Slot
from game_att2_sim.errors import IllegalActionError, InsufficientBloodError, InvalidTargetError
from game_att2_sim.events import EventLog
from game_att2_sim.factory import enemy_from_config, player_from_start
from game_att2_sim.models import CombatantRuntime, HarvestedLimb, ScenarioMetrics
from game_att2_sim.rng import ScriptedRNG
from game_att2_sim.rules import RuleEngine
from game_att2_sim.scenarios import run_all


def make_engine(rolls: list[int] | None = None) -> tuple[RuleEngine, CombatantRuntime]:
    config = load_config()
    player = player_from_start(config)
    engine = RuleEngine(
        config,
        ScriptedRNG(rolls or [6]),
        EventLog(),
        ScenarioMetrics("causal_integrity", 1, "balanced"),
        tutorial=True,
    )
    return engine, player


def graft_right_arm(engine: RuleEngine, player: CombatantRuntime) -> None:
    jeff = enemy_from_config(engine.config, "jeff")
    harvested = HarvestedLimb(jeff.body.slots[Slot.RIGHT_ARM], HarvestQuality.CLEAN)
    engine.emergency_graft(player, harvested, Slot.RIGHT_ARM)


def committed_actions(engine: RuleEngine) -> list[str]:
    return [
        str(event.payload["action"])
        for event in engine.log.events
        if event.event_type == "main_action_committed"
    ]


@pytest.mark.parametrize(
    ("action", "expected_id"),
    [
        ("claim", "claim_the_cut"),
        ("grip", "grip_strike"),
        ("scissors", "bone_scissors"),
        ("saw", "hell_saw"),
        ("guard", "guard_flesh"),
        ("stand", "stand"),
        ("brace", "brace"),
    ],
)
def test_every_main_action_commits_exactly_once(action: str, expected_id: str) -> None:
    engine, player = make_engine()
    jeff = enemy_from_config(engine.config, "jeff")
    engine.start_round(player)

    if action == "claim":
        engine.claim(player, jeff.body.slots[Slot.RIGHT_ARM])
    elif action == "grip":
        engine.grip(player, jeff, jeff.body.slots[Slot.RIGHT_ARM])
    elif action == "scissors":
        target = jeff.body.slots[Slot.LEFT_ARM]
        target.integrity = 10
        target.state = LimbState.DAMAGED
        engine.scissors(player, jeff, target)
    elif action == "saw":
        target = jeff.body.slots[Slot.RIGHT_ARM]
        target.integrity = 20
        target.state = LimbState.DAMAGED
        engine.saw(player, jeff, target)
    elif action == "guard":
        graft_right_arm(engine, player)
        engine.guard_flesh(player)
    elif action == "stand":
        player.downed = True
        engine.stand(player)
    elif action == "brace":
        engine.start_encounter(player)
        engine.brace(player)

    assert player.normal_action_consumed
    assert committed_actions(engine) == [expected_id]


def test_second_main_action_is_rejected_without_partial_mutation() -> None:
    engine, player = make_engine()
    jeff = enemy_from_config(engine.config, "jeff")
    right = jeff.body.slots[Slot.RIGHT_ARM]
    left = jeff.body.slots[Slot.LEFT_ARM]
    engine.start_round(player)
    engine.grip(player, jeff, right)
    before = (left.integrity, player.blood, dict(player.inventory), set(left.tags))

    with pytest.raises(IllegalActionError):
        engine.grip(player, jeff, left)

    assert (left.integrity, player.blood, player.inventory, left.tags) == before
    assert committed_actions(engine) == ["grip_strike"]


def test_rejected_main_action_does_not_commit_or_mutate() -> None:
    engine, player = make_engine()
    anna = enemy_from_config(engine.config, "anna")
    target = anna.body.slots[Slot.RIGHT_ARM]
    engine.start_round(player)
    before = (target.integrity, target.state, set(target.tags), player.blood, dict(player.inventory))

    with pytest.raises(InvalidTargetError):
        engine.scissors(player, anna, target)

    assert (target.integrity, target.state, target.tags, player.blood, player.inventory) == before
    assert not player.normal_action_consumed
    assert committed_actions(engine) == []


def test_unaffordable_main_action_does_not_commit_or_mutate() -> None:
    engine, player = make_engine()
    jeff = enemy_from_config(engine.config, "jeff")
    target = jeff.body.slots[Slot.RIGHT_ARM]
    player.blood = 0
    engine.start_round(player)
    inventory_before = dict(player.inventory)

    with pytest.raises(InsufficientBloodError):
        engine.claim(player, target)

    assert LimbTag.MARKED not in target.tags
    assert player.inventory == inventory_before
    assert not player.normal_action_consumed
    assert committed_actions(engine) == []


def test_focus_then_main_is_legal_and_focus_does_not_commit() -> None:
    engine, player = make_engine()
    jeff = enemy_from_config(engine.config, "jeff")
    engine.start_round(player)

    engine.focus(player, "Jeff attacks from left arm")
    assert not player.normal_action_consumed
    engine.grip(player, jeff, jeff.body.slots[Slot.RIGHT_ARM])

    assert committed_actions(engine) == ["grip_strike"]


def test_fast_then_main_is_legal_and_fast_does_not_commit() -> None:
    engine, player = make_engine()
    jeff = enemy_from_config(engine.config, "jeff")
    engine.start_round(player)

    engine.fast_item(player, "blood_bag")
    assert not player.normal_action_consumed
    engine.grip(player, jeff, jeff.body.slots[Slot.RIGHT_ARM])

    assert committed_actions(engine) == ["grip_strike"]


def test_stand_consumes_main_and_blocks_follow_up() -> None:
    engine, player = make_engine()
    jeff = enemy_from_config(engine.config, "jeff")
    player.downed = True
    engine.start_round(player)
    player.downed = True
    engine.stand(player)

    with pytest.raises(IllegalActionError):
        engine.grip(player, jeff, jeff.body.slots[Slot.RIGHT_ARM])

    assert committed_actions(engine) == ["stand"]


def test_guard_clears_when_used() -> None:
    engine, player = make_engine()
    graft_right_arm(engine, player)
    anna = enemy_from_config(engine.config, "anna")
    engine.start_round(player)
    engine.guard_flesh(player)

    engine.enemy_attack(anna, player, Slot.RIGHT_ARM, Slot.TORSO, 8)

    assert not player.guard_active
    assert any(event.event_type == "guard_consumed" for event in engine.log.events)


def test_unused_guard_expires_at_end_of_round() -> None:
    engine, player = make_engine()
    graft_right_arm(engine, player)
    engine.start_round(player)
    engine.guard_flesh(player)

    engine.end_round(player)

    assert not player.guard_active
    assert engine.log.events[-1].event_type == "guard_expired"


def test_guard_does_not_survive_cancelled_enemy_action() -> None:
    engine, player = make_engine()
    graft_right_arm(engine, player)
    anna = enemy_from_config(engine.config, "anna")
    anna.body.slots[Slot.RIGHT_ARM].state = LimbState.DISABLED
    engine.start_round(player)
    engine.guard_flesh(player)

    engine.enemy_attack(anna, player, Slot.RIGHT_ARM, Slot.TORSO, 8)
    engine.start_round(player)

    assert not player.guard_active
    event_types = [event.event_type for event in engine.log.events]
    assert "enemy_action_cancelled" in event_types
    assert "guard_expired" in event_types


def test_destroyed_action_source_cannot_resolve_or_commit() -> None:
    engine, player = make_engine()
    jeff = enemy_from_config(engine.config, "jeff")
    source = player.body.slots[Slot.LEFT_ARM]
    target = jeff.body.slots[Slot.RIGHT_ARM]
    source.state = LimbState.RUINED
    before = target.integrity
    engine.start_round(player)

    with pytest.raises(IllegalActionError):
        engine.grip(player, jeff, target)

    assert target.integrity == before
    assert not player.normal_action_consumed
    assert committed_actions(engine) == []


def test_approved_scenarios_never_commit_two_main_actions_for_an_actor_round() -> None:
    for result in run_all(42):
        keys = [
            (event.actor_id, event.round_number)
            for event in result.events
            if event.event_type == "main_action_committed"
        ]
        assert all(count == 1 for count in Counter(keys).values()), result.metrics.scenario
