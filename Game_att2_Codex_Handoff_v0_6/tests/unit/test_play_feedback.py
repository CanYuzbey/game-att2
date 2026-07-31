from __future__ import annotations

import json
from pathlib import Path

import pytest

from game_att2_sim.campaign_play import campaign_session
from game_att2_sim.play_cli import FeedbackConsole
from game_att2_sim.play_feedback import (
    FEEDBACK_SCHEMA_VERSION,
    build_feedback_record,
    write_feedback_record,
)
from game_att2_sim.play_session import PlayOutcome, PlaySession


def ended_phase_one_session() -> PlaySession:
    session = PlaySession(seed=42)
    session.perform("focus")
    session.perform("end_session")
    assert session.outcome is PlayOutcome.ENDED_BY_PLAYER
    return session


def completed_campaign_session():
    session = campaign_session(42)
    actions = (
        "claim_the_cut:right_arm",
        "grip_strike:right_arm",
        "hell_saw:right_arm",
        "grip_strike:left_arm",
        "grip_strike:left_arm",
        "emergency_graft",
        "focus",
        "guard_flesh",
        "accept_anna_trade",
        "table:integrate_arm",
    )
    for action in actions:
        assert session.perform(action, confirmed=True) == "executed"
    assert session.outcome == "COMPLETED"
    return session


def test_phase_one_feedback_combines_versions_gameplay_and_answers() -> None:
    record = build_feedback_record(
        ended_phase_one_session(),
        ratings={"goal_clarity": 4, "danger_pressure": 1},
        reflections={"blood_strategy": "Focus için harcadım."},
        model_training_consent=False,
        collection_status="complete",
        session_id="test-session",
        recorded_at_utc="2026-07-31T10:00:00+00:00",
    )

    assert record["schema_version"] == FEEDBACK_SCHEMA_VERSION
    assert record["consent"] == {
        "local_design_research": True,
        "model_training": False,
        "consent_text_version": "0.1",
    }
    gameplay = record["gameplay"]
    assert isinstance(gameplay, dict)
    assert gameplay["outcome"] == "ENDED_BY_PLAYER"
    assert gameplay["blood_spent"] == 3
    assert gameplay["current_pressure_model"]["jeff_direct_blood_loss"] is False


def test_campaign_feedback_covers_full_sequence_without_claiming_independence() -> None:
    record = build_feedback_record(
        completed_campaign_session(),
        ratings={"choice_meaningfulness": 4},
        reflections={"desired_change": "Daha belirgin risk."},
        model_training_consent=False,
        collection_status="complete",
        session_id="campaign-session",
        recorded_at_utc="2026-07-31T10:00:00+00:00",
    )

    assert record["record_type"] == "game_att2_full_campaign_playtest_feedback"
    source = record["source"]
    assert isinstance(source, dict)
    assert source["evidence_class"] == "UNCLASSIFIED_HUMAN_PLAY"
    assert source["participant_independence_verified"] is False
    gameplay = record["gameplay"]
    assert isinstance(gameplay, dict)
    assert gameplay["outcome"] == "COMPLETED"
    assert gameplay["anna_path"] == "stabilization_trade"
    assert gameplay["table_choice"] == "integrate_arm"
    pressure = gameplay["current_pressure_model"]
    assert pressure["jeff_blood_threat"] == "deferred_owner_decision"


def test_feedback_rejects_invalid_rating_and_status() -> None:
    session = ended_phase_one_session()
    with pytest.raises(ValueError, match="between 1 and 5"):
        build_feedback_record(
            session,
            ratings={"danger_pressure": 6},
            reflections={},
            model_training_consent=False,
            collection_status="complete",
        )
    with pytest.raises(ValueError, match="collection_status"):
        build_feedback_record(
            session,
            ratings={},
            reflections={},
            model_training_consent=False,
            collection_status="unknown",
        )


def test_feedback_file_is_utf8_json_and_never_overwritten(tmp_path: Path) -> None:
    record = build_feedback_record(
        completed_campaign_session(),
        ratings={"goal_clarity": 5},
        reflections={"desired_change": "Daha fazla tehdit."},
        model_training_consent=True,
        collection_status="complete",
        session_id="fixed-id",
        recorded_at_utc="2026-07-31T10:00:00+00:00",
    )
    path = write_feedback_record(record, tmp_path)
    loaded = json.loads(path.read_text(encoding="utf-8"))
    assert loaded["reflections"]["desired_change"] == "Daha fazla tehdit."
    with pytest.raises(FileExistsError):
        write_feedback_record(record, tmp_path)


def test_feedback_console_requires_opt_in() -> None:
    output: list[str] = []
    collector = FeedbackConsole(
        ended_phase_one_session(), input_fn=lambda _prompt: "", output_fn=output.append
    )
    assert collector.collect() is None
    assert any("kaydedilmedi" in line for line in output)


def test_feedback_console_saves_partial_answers_after_consented_eof() -> None:
    answers = iter(["e", "e", "4"])

    def input_fn(_prompt: str) -> str:
        try:
            return next(answers)
        except StopIteration as error:
            raise EOFError from error

    record = FeedbackConsole(
        completed_campaign_session(), input_fn=input_fn, output_fn=lambda _text: None
    ).collect()

    assert record is not None
    assert record["collection_status"] == "partial"
    assert record["ratings"] == {"goal_clarity": 4}
