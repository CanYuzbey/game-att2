from __future__ import annotations

import json
from pathlib import Path

import pytest

from game_att2_sim.campaign_play import (
    CampaignConsole,
    campaign_session,
    campaign_snapshot,
    render_campaign_result,
    render_campaign_state,
    render_campaign_summary,
    run_campaign_actions,
)
from game_att2_sim.play_cli import main

FULL_SEQUENCE = [
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
]


def test_campaign_player_path_reaches_every_approved_phase() -> None:
    session = campaign_session(42)
    encountered = {session.encounter}
    output: list[str] = []
    for action in FULL_SEQUENCE:
        run_campaign_actions(session, [action], output.append)
        encountered.add(session.encounter)

    assert encountered == {"Jeff", "Post-Jeff", "Anna", "Grafting Table"}
    assert session.outcome == "COMPLETED"
    assert session.anna_path == "stabilization_trade"
    assert session.metrics.table_choice == "integrate_arm"
    assert session.player.blood == 25


def test_campaign_state_exposes_objective_and_causal_source_hint() -> None:
    session = campaign_session(42)
    text = render_campaign_state(session)
    assert "HEDEF:" in text
    assert "Desperate Swing kullanılabilir bir koldan gelir" in text
    assert "GÖRÜNEN NİYET:" in text
    assert "source and target unclear" in text


def test_campaign_result_answers_pillar_five_questions() -> None:
    session = campaign_session(42)
    before = campaign_snapshot(session)
    offer = next(
        offer for offer in session.offers() if offer.action_id == "grip_strike:right_arm"
    )
    event_start = len(session.log.events)
    session.perform(offer.action_id, confirmed=True)
    text = render_campaign_result(
        offer.label,
        before,
        session,
        session.log.events[event_start:],
    )
    for question in (
        "1. Ne hedeflendi?",
        "2. Ne değişti?",
        "3. Blood maliyeti?",
        "4. Ne kazanıldı?",
        "5. Hangi yeni risk doğdu?",
    ):
        assert question in text


def test_focus_result_reports_information_as_the_gained_state() -> None:
    session = campaign_session(42)
    before = campaign_snapshot(session)
    event_start = len(session.log.events)
    session.perform("focus", confirmed=True)
    text = render_campaign_result(
        "Focus",
        before,
        session,
        session.log.events[event_start:],
    )
    assert "Görünen niyet:" in text
    assert "left_arm against torso" in text
    assert "focus_resolved" in text


def test_campaign_menus_explain_causal_targets_and_low_value_brace() -> None:
    session = campaign_session(42)
    output: list[str] = []
    answers = iter(["1", "0"])
    console = CampaignConsole(
        session,
        input_fn=lambda _prompt: next(answers),
        output_fn=output.append,
    )
    console._attack_menu()
    assert any("nedensel hedef: Desperate Swing kaynağı olabilir" in line for line in output)

    output.clear()
    console = CampaignConsole(
        session,
        input_fn=lambda _prompt: "0",
        output_fn=output.append,
    )
    console._offer_menu(
        [offer for offer in session.offers() if offer.action_id == "brace"],
        "DEFANS",
    )
    assert any("mevcut düşman Knockdown kullanmıyor" in line for line in output)


def test_campaign_summary_does_not_claim_owner_or_external_evidence() -> None:
    summary = render_campaign_summary(campaign_session(42))
    assert "UNCLASSIFIED_HUMAN_PLAY" in summary
    assert "OWNER_DIAGNOSTIC" not in summary


def test_campaign_round_limit_is_an_explicit_cli_guard() -> None:
    session = campaign_session(42)
    run_campaign_actions(
        session,
        ["grip_strike:right_arm", "grip_strike:right_arm"],
        lambda _text: None,
        round_limit=1,
    )
    assert session.outcome == "ROUND_LIMIT_REACHED"
    assert any(
        event.event_type == "campaign_round_limit_reached" for event in session.log.events
    )


def test_default_play_cli_runs_full_campaign_script(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    script = tmp_path / "campaign.json"
    script.write_text(json.dumps(FULL_SEQUENCE), encoding="utf-8")
    assert main(["--seed", "42", "--script", str(script)]) == 0
    output = capsys.readouterr().out
    assert "Outcome: COMPLETED" in output
    assert "Final Blood: 25" in output
