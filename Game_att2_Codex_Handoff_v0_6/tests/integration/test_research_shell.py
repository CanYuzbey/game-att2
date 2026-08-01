from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest
import yaml

from game_att2_sim.config_loader import load_config
from game_att2_sim.encounter_goals import OutcomeLevel, ResolutionKind
from game_att2_sim.enums import LimbState, Slot
from game_att2_sim.errors import ConfigValidationError
from game_att2_sim.research_shell import (
    EvidenceClass,
    InteractiveResearchSession,
    SessionMetadata,
    replay_session,
)

FIXED_TIMESTAMP = "2026-07-23T12:00:00+03:00"
FULL_SEQUENCE = [
    {"action": "claim_the_cut:right_arm", "confirmed": True},
    {"action": "accept_jeff_bargain", "confirmed": True},
    {"action": "emergency_graft", "confirmed": True},
    {"action": "focus"},
    {"action": "guard_flesh", "confirmed": True},
    {"action": "grip_strike:right_arm", "confirmed": True},
    {"action": "grip_strike:right_arm", "confirmed": True},
    {"action": "accept_anna_trade", "confirmed": True},
    {"action": "table:integrate_arm", "confirmed": True},
]


def metadata(
    session_id: str = "AUTO-SHELL-001",
    evidence_class: EvidenceClass = EvidenceClass.AUTOMATED_REGRESSION,
    participant_code: str = "AUTO-SHELL",
) -> SessionMetadata:
    return SessionMetadata.create(
        session_id,
        evidence_class,
        42,
        participant_code,
        timestamp=FIXED_TIMESTAMP,
        strategy_intention="body_progression",
    )


def offers_by_id(session: InteractiveResearchSession) -> dict[str, object]:
    return {offer.action_id: offer for offer in session.offers()}


def test_shell_derives_enabled_and_disabled_actions_with_reasons() -> None:
    session = InteractiveResearchSession(metadata())
    offers = offers_by_id(session)
    assert offers["grip_strike:right_arm"].enabled  # type: ignore[union-attr]
    assert not offers["guard_flesh"].enabled  # type: ignore[union-attr]
    assert offers["guard_flesh"].reason == "Right Arm source is unavailable"  # type: ignore[union-attr]
    assert not offers["bone_scissors:right_arm"].enabled  # type: ignore[union-attr]
    assert offers["bone_scissors:right_arm"].reason  # type: ignore[union-attr]


def test_disabled_action_cannot_execute_or_commit() -> None:
    session = InteractiveResearchSession(metadata())
    before = (session.player.blood, session.player.normal_action_consumed)
    result = session.perform("guard_flesh", confirmed=True)
    assert "unavailable" in result
    assert (session.player.blood, session.player.normal_action_consumed) == before
    assert not any(event.event_type == "main_action_committed" for event in session.log.events)


def test_confirmation_cancellation_preserves_gameplay_and_rng() -> None:
    session = InteractiveResearchSession(metadata())
    target = session.enemy.body.slots[Slot.RIGHT_ARM]  # type: ignore[union-attr]
    before = (
        session.player.blood,
        dict(session.player.inventory),
        target.integrity,
        set(target.tags),
        session.player.normal_action_consumed,
        session.rng.state_token(),  # type: ignore[union-attr]
    )
    assert session.perform("claim_the_cut:right_arm", confirmed=False) == (
        "Cancelled before commitment"
    )
    after = (
        session.player.blood,
        session.player.inventory,
        target.integrity,
        target.tags,
        session.player.normal_action_consumed,
        session.rng.state_token(),  # type: ignore[union-attr]
    )
    assert after == before
    assert session.decisions[-1].disposition == "CANCELLED"


def test_confirmed_main_commits_once_and_focus_fast_remain_non_main() -> None:
    session = InteractiveResearchSession(metadata())
    assert "unclear" in session.current_intent
    session.perform("focus")
    assert session.current_intent == session.exact_intent
    assert "left_arm against left_arm" in session.current_intent
    session.perform("blood_bag")
    assert not session.player.normal_action_consumed
    session.perform("grip_strike:right_arm", confirmed=True)
    commits = [
        event for event in session.log.events if event.event_type == "main_action_committed"
    ]
    assert len(commits) == 1
    assert commits[0].payload["action"] == "grip_strike"


def test_replay_is_byte_identical_and_exports_required_fields() -> None:
    first = replay_session(metadata(), FULL_SEQUENCE)
    second = replay_session(metadata(), FULL_SEQUENCE)
    assert first.export_json() == second.export_json()
    payload = json.loads(first.export_json())
    assert payload["metadata"]["parent_baseline"].startswith("9b3f72b")
    assert payload["metadata"]["interface_version"] == "0.2"
    assert payload["metadata"]["rules_version"] == "0.5"
    assert payload["decision_points"]
    assert payload["events"]
    assert payload["outcome"] == "COMPLETED"
    assert payload["anna_path"] == "stabilization_trade"
    assert payload["table_choice"] == "integrate_arm"


def test_different_legal_choices_produce_different_trajectories() -> None:
    intended = replay_session(metadata("AUTO-INTENDED"), FULL_SEQUENCE)
    no_spend = replay_session(
        metadata("AUTO-NO-SPEND"),
        [
            {"action": "grip_strike:right_arm", "confirmed": True},
            {"action": "grip_strike:right_arm", "confirmed": True},
            {"action": "grip_strike:right_arm", "confirmed": True},
            {"action": "grip_strike:left_arm", "confirmed": True},
            {"action": "grip_strike:left_arm", "confirmed": True},
            {"action": "end_session", "confirmed": True},
        ],
    )
    assert intended.outcome == "COMPLETED"
    assert no_spend.outcome == "ENDED_BY_PARTICIPANT"
    assert intended.export_json() != no_spend.export_json()


def test_destroyed_source_immediately_changes_affordances() -> None:
    session = InteractiveResearchSession(metadata())
    session.player.body.slots[Slot.LEFT_ARM].state = LimbState.RUINED
    grip = offers_by_id(session)["grip_strike:right_arm"]
    assert not grip.enabled  # type: ignore[union-attr]
    assert grip.reason == "Left Arm source is unavailable"  # type: ignore[union-attr]
    session.perform("grip_strike:right_arm", confirmed=True)
    assert not any(event.event_type == "main_action_committed" for event in session.log.events)


def test_research_shell_revalidates_declared_jeff_source_without_fallback() -> None:
    session = InteractiveResearchSession(metadata())
    assert session.current_intent_source is Slot.LEFT_ARM
    source = session.enemy.body.slots[Slot.LEFT_ARM]  # type: ignore[union-attr]
    source.integrity = 5
    source.state = LimbState.CRITICAL
    player_left_arm = session.player.body.slots[Slot.LEFT_ARM]
    before = player_left_arm.integrity

    session.perform("grip_strike:left_arm", confirmed=True)

    assert player_left_arm.integrity == before
    assert any(
        event.event_type == "enemy_action_cancelled"
        and event.payload["source_slot"] == Slot.LEFT_ARM.value
        for event in session.log.events
    )


def test_marked_arm_and_available_cream_create_a_state_derived_bargain() -> None:
    session = InteractiveResearchSession(metadata())
    session.perform("claim_the_cut:right_arm", confirmed=True)

    assert session.current_intent_action == "jeff_bargain"
    assert offers_by_id(session)["accept_jeff_bargain"].enabled  # type: ignore[union-attr]
    assert session.jeff_bargain_offered


def test_bargain_disables_when_required_asset_is_no_longer_owned() -> None:
    session = InteractiveResearchSession(metadata())
    session.perform("claim_the_cut:right_arm", confirmed=True)
    session.player.inventory["clotting_cream"] = 0

    bargain = offers_by_id(session)["accept_jeff_bargain"]
    assert not bargain.enabled  # type: ignore[union-attr]
    assert "unavailable" in bargain.reason  # type: ignore[union-attr]
    assert session.perform("accept_jeff_bargain", confirmed=True) != "executed"


def test_accepting_jeff_bargain_records_mutual_success() -> None:
    session = InteractiveResearchSession(metadata())
    session.perform("claim_the_cut:right_arm", confirmed=True)

    assert session.perform("accept_jeff_bargain", confirmed=True) == "executed"

    assert session.encounter == "Post-Jeff"
    assert session.player.inventory["clotting_cream"] == 0
    assert session.harvested_jeff_arm is not None
    assert session.harvested_jeff_arm.quality.value == "clean"
    outcome = session.encounter_outcomes[-1]
    assert outcome.resolution is ResolutionKind.BARGAIN
    assert {actor.actor: actor.level for actor in outcome.actors} == {
        "player": OutcomeLevel.COMPLETE,
        "enemy": OutcomeLevel.COMPLETE,
    }


def test_hostile_main_naturally_rejects_bargain_then_uses_marked_arm() -> None:
    session = InteractiveResearchSession(metadata())
    session.perform("claim_the_cut:right_arm", confirmed=True)
    session.perform("grip_strike:right_arm", confirmed=True)

    assert session.jeff_bargain_rejected
    assert session.current_intent_action == "desperate_swing"
    assert session.current_intent_source is Slot.RIGHT_ARM
    resumed = next(
        event
        for event in session.log.events
        if event.event_type == "enemy_behavior_triggered"
    )
    assert resumed.payload["response"] == "resume_combat"
    assert resumed.payload["stat_modifier_applied"] is False
    assert any(
        event.event_type == "jeff_marked_source_selected"
        and event.payload["source_slot"] == Slot.RIGHT_ARM.value
        for event in session.log.events
    )


def test_jeff_target_selection_penalizes_exact_repetition() -> None:
    session = InteractiveResearchSession(metadata())
    assert session.current_intent_target is Slot.LEFT_ARM
    session.perform("grip_strike:right_arm", confirmed=True)
    assert session.current_intent_target is Slot.TORSO


def test_guard_bargain_and_outcome_resolution_are_exported() -> None:
    completed = replay_session(metadata(), FULL_SEQUENCE)
    event_types = [event.event_type for event in completed.log.events]
    assert "guard_consumed" in event_types
    assert "negotiated_exchange_completed" in event_types
    assert "encounter_outcome_evaluated" in event_types

    through_graft = replay_session(metadata("AUTO-GUARD-EXPIRY"), FULL_SEQUENCE[:3])
    through_graft.engine.guard_flesh(through_graft.player)
    through_graft.engine.end_round(through_graft.player)
    assert not through_graft.player.guard_active
    assert any(event.event_type == "guard_expired" for event in through_graft.log.events)


def test_evidence_classes_cannot_be_mislabeled() -> None:
    with pytest.raises(ValueError):
        metadata(
            "PILOT-BAD",
            EvidenceClass.EXTERNAL_PILOT,
            participant_code="OWNER-CAN",
        )
    with pytest.raises(ValueError):
        metadata(
            "OWNER-BAD",
            EvidenceClass.OWNER_DIAGNOSTIC,
            participant_code="P01",
        )
    owner = metadata(
        "OWNER-VALID",
        EvidenceClass.OWNER_DIAGNOSTIC,
        participant_code="OWNER-CAN",
    )
    assert owner.evidence_class is EvidenceClass.OWNER_DIAGNOSTIC
    play = metadata(
        "PLAY-VALID",
        EvidenceClass.UNCLASSIFIED_HUMAN_PLAY,
        participant_code="PLAY-P01",
    )
    assert play.evidence_class is EvidenceClass.UNCLASSIFIED_HUMAN_PLAY
    with pytest.raises(ValueError, match="PLAY- code"):
        metadata(
            "PLAY-BAD",
            EvidenceClass.UNCLASSIFIED_HUMAN_PLAY,
            participant_code="OWNER-CAN",
        )
    with pytest.raises(ValueError, match="unclassified"):
        metadata(
            "PILOT-BAD-PLAY",
            EvidenceClass.EXTERNAL_PILOT,
            participant_code="PLAY-P01",
        )


def test_broken_configuration_reference_fails_before_session(
    tmp_path: Path,
) -> None:
    source = Path(__file__).resolve().parents[2] / "config"
    destination = tmp_path / "config"
    shutil.copytree(source, destination)
    content_path = destination / "content_v0_1.yaml"
    content = yaml.safe_load(content_path.read_text(encoding="utf-8"))
    content["enemies"]["jeff"]["actions"].append("missing_action")
    content_path.write_text(yaml.safe_dump(content, sort_keys=False), encoding="utf-8")
    with pytest.raises(ConfigValidationError, match="unknown action missing_action"):
        load_config(destination)
