from __future__ import annotations

import json
from pathlib import Path

import pytest

from game_att2_sim.enums import HarvestQuality, LimbState, LimbTag, Slot
from game_att2_sim.play_cli import PlayConsole, main
from game_att2_sim.play_render import (
    localize_reason,
    render_report,
    render_state,
    render_summary,
)
from game_att2_sim.play_session import (
    ATTACK_ACTIONS,
    MenuCategory,
    PlayOutcome,
    PlaySession,
    blood_band,
)

#: Reaches Jeff's surrender: mark the arm, soften it, then saw it off.
WIN_SEQUENCE = [
    "claim_the_cut:right_arm",
    "grip_strike:right_arm",
    "hell_saw:right_arm",
    "grip_strike:left_arm",
    "grip_strike:left_arm",
]


def session(seed: int = 42, **kwargs: object) -> PlaySession:
    return PlaySession(seed=seed, **kwargs)  # type: ignore[arg-type]


def run(actions: list[str], seed: int = 42) -> PlaySession:
    play = session(seed)
    for action in actions:
        if play.complete:
            break
        play.perform(action)
    return play


# ----------------------------------------------------------------- scope lock


def test_session_locks_s001_body_and_jeff_enemy() -> None:
    play = session()
    assert play.player.id == "s001"
    assert play.enemy.id == "jeff"
    assert play.player.body.slots[Slot.RIGHT_ARM].state is LimbState.MISSING
    assert set(play.player.body.slots) == set(Slot)
    assert set(play.enemy.body.slots) == set(Slot)


def test_phase_two_content_is_not_reachable_from_this_interface() -> None:
    play = run(WIN_SEQUENCE)
    assert play.outcome is PlayOutcome.JEFF_YIELDED
    offered = {offer.action_id for offer in play.offers()}
    forbidden = {
        "emergency_graft",
        "accept_anna_trade",
        "table:integrate_arm",
        "table:repair_torso",
        "table:strengthen_legs",
        "table_loan",
        "table:leave",
    }
    assert not offered & forbidden
    for action in sorted(forbidden):
        assert not play.perform(action).accepted
    event_types = {event.event_type for event in play.log.events}
    assert not event_types & {"emergency_graft", "anna_trade_accepted", "table_choice"}
    assert play.metrics.table_choice == ""
    assert play.metrics.grafts_attempted == 0


def test_offer_categories_cover_the_four_decision_branches() -> None:
    play = session()
    categories = {offer.category for offer in play.offers()}
    assert {
        MenuCategory.ATTACK,
        MenuCategory.FOCUS,
        MenuCategory.ITEM,
        MenuCategory.DEFEND,
    } <= categories
    attacks = {offer.action_id.split(":", 1)[0] for offer in play.offers_in(MenuCategory.ATTACK)}
    assert attacks == set(ATTACK_ACTIONS)


# ------------------------------------------------------------- round sequence


def test_focus_and_fast_item_do_not_consume_the_main_action() -> None:
    play = session()
    assert play.perform("focus").accepted
    assert not play.player.normal_action_consumed
    assert play.log.round_number == 1
    assert play.perform("blood_bag").accepted
    assert not play.player.normal_action_consumed
    assert play.log.round_number == 1
    assert play.perform("grip_strike:right_arm").accepted
    assert play.log.round_number == 2


def test_focus_is_what_reveals_the_exact_intent() -> None:
    play = session()
    public = play.intent_text()
    assert not play.intent_is_revealed()
    assert "Sol Kol" not in public and "Gövde" not in public
    play.perform("focus")
    assert play.intent_is_revealed()
    assert play.intent_text() == play.exact_intent
    assert "Sol Kol" in play.intent_text()


def test_new_round_hides_the_intent_again() -> None:
    play = session()
    play.perform("focus")
    play.perform("grip_strike:torso")
    assert play.log.round_number == 2
    assert not play.intent_is_revealed()


def test_enemy_resolves_after_the_player_main_action() -> None:
    play = session()
    torso = play.player.body.slots[Slot.TORSO]
    before = torso.integrity
    result = play.perform("grip_strike:torso")
    assert len(result.reports) == 2
    assert result.reports[0].actor == "Sen"
    assert result.reports[1].actor == "Jeff"
    assert torso.integrity < before


# ------------------------------------------------------ illegal input refusal


def test_unpresented_action_is_refused_without_touching_state() -> None:
    play = session()
    before = (play.player.blood, play.player.normal_action_consumed, play.log.round_number)
    result = play.perform("table:table_loan")
    assert not result.accepted
    assert (
        play.player.blood,
        play.player.normal_action_consumed,
        play.log.round_number,
    ) == before
    assert any(event.event_type == "play_invalid_attempt" for event in play.log.events)


def test_disabled_action_is_refused_and_never_commits() -> None:
    play = session()
    guard = play.find_offer("guard_flesh")
    assert guard is not None and not guard.enabled
    result = play.perform("guard_flesh")
    assert not result.accepted
    assert not any(
        event.event_type == "main_action_committed" for event in play.log.events
    )
    assert any(event.event_type == "play_disabled_attempt" for event in play.log.events)


def test_second_main_action_in_the_same_round_is_impossible() -> None:
    play = session()
    play.perform("grip_strike:head")
    round_two = play.log.round_number
    assert round_two == 2
    play.player.normal_action_consumed = True
    result = play.perform("grip_strike:head")
    assert not result.accepted
    assert play.log.round_number == round_two


def test_lost_left_arm_closes_grip_strike_immediately() -> None:
    play = session()
    play.player.body.slots[Slot.LEFT_ARM].state = LimbState.RUINED
    _, enabled, reason = play.attack_action_summaries()[0]
    assert not enabled
    assert reason == "Left Arm source is unavailable"
    assert not play.perform("grip_strike:right_arm").accepted


# ------------------------------------------------- Pillar 5 readability record


def test_every_report_answers_all_five_questions() -> None:
    play = run(WIN_SEQUENCE)
    assert play.reports
    for report in play.reports:
        pairs = report.as_pairs()
        assert len(pairs) == 5
        for _question, answers in pairs:
            assert answers
            assert all(answer.strip() for answer in answers)


def test_report_names_target_change_cost_gain_and_new_risk() -> None:
    play = session()
    report = play.perform("claim_the_cut:right_arm").reports[0]
    assert "Jeff Right Arm" in report.targeted and "Sağ Kol" in report.targeted
    assert any("işaretlendi" in line for line in report.changed)
    assert report.blood_cost.startswith("10 Blood")
    assert "85 -> 75" in report.blood_cost
    assert any("Claim the Cut" in line for line in report.gained)
    assert any("Marked" in line for line in report.new_risks)
    assert any("tükendi" in line for line in report.new_risks)


def test_free_action_reports_zero_cost_and_integrity_delta() -> None:
    play = session()
    report = play.perform("grip_strike:right_arm").reports[0]
    assert report.blood_cost.startswith("0 Blood")
    assert any("bütünlük 30 -> 20 (-10)" in line for line in report.changed)


def test_ruined_limb_is_reported_as_a_lost_harvest_risk() -> None:
    play = session()
    arm = play.enemy.body.slots[Slot.RIGHT_ARM]
    arm.integrity = 5
    arm.state = LimbState.CRITICAL
    report = play.perform("grip_strike:right_arm").reports[0]
    assert arm.state is LimbState.RUINED
    assert any("harap oldu" in line for line in report.new_risks)
    assert not play.harvests


def test_worsening_blood_band_is_reported_as_a_new_risk() -> None:
    play = session()
    play.player.blood = 55
    report = play.perform("hell_saw:torso").reports[0]
    assert blood_band(play.player.blood, play.rules) == "DANGEROUS"
    assert any("NORMAL -> DANGEROUS" in line for line in report.new_risks)


def test_bleeding_applied_to_the_player_surfaces_as_a_new_risk() -> None:
    play = session()
    torso = play.player.body.slots[Slot.TORSO]
    before_snapshot = play._snapshot()
    before_events = len(play.log.events)
    play.engine.apply_bleeding(play.player, torso, source=play.enemy.id, roll=6)
    report = play._report(
        actor="Jeff",
        action_label="Desperate Swing",
        targeted="test",
        before=before_snapshot,
        start=before_events,
    )
    assert any("Bleeding" in line for line in report.new_risks)


# ----------------------------------------------------------- outcomes and end


def test_jeff_yields_and_a_clean_right_arm_is_recorded() -> None:
    play = run(WIN_SEQUENCE)
    assert play.outcome is PlayOutcome.JEFF_YIELDED
    graft = play.graftable_right_arm
    assert graft is not None
    assert graft.slot is Slot.RIGHT_ARM
    assert graft.quality is HarvestQuality.CLEAN
    assert LimbTag.MARKED in play.enemy.body.slots[Slot.RIGHT_ARM].tags


def test_the_winning_action_reports_that_jeff_yielded() -> None:
    play = run(WIN_SEQUENCE[:-1])
    assert not play.complete
    final = play.perform(WIN_SEQUENCE[-1]).reports[0]
    assert play.outcome is PlayOutcome.JEFF_YIELDED
    assert any("pes etti" in line or "teslim oldu" in line for line in final.gained)


def test_grip_only_path_never_produces_a_graftable_arm() -> None:
    play = run(["grip_strike:right_arm"] * 6)
    assert play.graftable_right_arm is None
    assert play.enemy.body.slots[Slot.RIGHT_ARM].state is LimbState.RUINED


def test_collapse_in_the_pre_main_window_ends_the_session() -> None:
    play = session()
    # Exactly the Focus cost, so the spend lands on the collapse threshold.
    play.player.blood = 3
    play.player.panic_pulse_used = True
    play.player.soft_collapse_used = True
    assert play.perform("focus").accepted
    assert play.player.collapsed
    assert play.outcome is PlayOutcome.PLAYER_COLLAPSE
    assert not play.perform("grip_strike:torso").accepted


def test_end_session_stops_accepting_actions() -> None:
    play = session()
    assert play.perform("end_session").accepted
    assert play.outcome is PlayOutcome.ENDED_BY_PLAYER
    assert play.offers() == []
    assert not play.perform("grip_strike:torso").accepted


def test_round_limit_guard_terminates_a_stalling_session() -> None:
    play = session(round_limit=3)
    for _ in range(5):
        if play.complete:
            break
        play.perform("grip_strike:head")
    assert play.outcome is PlayOutcome.ROUND_LIMIT_REACHED
    assert play.log.round_number == 3


def test_round_limit_must_be_positive() -> None:
    with pytest.raises(ValueError):
        session(round_limit=0)


def test_forfeit_is_offered_only_when_no_main_action_is_legal() -> None:
    play = session()
    assert play.find_offer("forfeit_main") is None
    for slot in Slot:
        limb = play.player.body.slots[slot]
        limb.state = LimbState.RUINED
    play.player.blood = 0
    forfeit = play.find_offer("forfeit_main")
    assert forfeit is not None and forfeit.enabled
    assert play.perform("forfeit_main").accepted
    assert any(
        event.event_type == "play_main_action_forfeited" for event in play.log.events
    )


# ------------------------------------------------------------- determinism


def test_same_seed_and_actions_produce_the_same_session() -> None:
    def trace(play: PlaySession) -> list[tuple[str, object]]:
        return [(event.event_type, event.payload) for event in play.log.events]

    assert trace(run(WIN_SEQUENCE)) == trace(run(WIN_SEQUENCE))


def test_different_seeds_can_diverge_on_the_saw_roll() -> None:
    # Hell Saw only rolls against a Damaged/Critical large limb, so soften first.
    actions = ["grip_strike:right_arm", "hell_saw:right_arm"]
    rolls = {
        seed: tuple(
            event.payload["roll"]
            for event in run(actions, seed=seed).log.events
            if event.event_type == "hell_saw_roll"
        )
        for seed in (1, 2, 3, 4, 5, 6)
    }
    assert all(value and value[0] > 0 for value in rolls.values())
    assert len(set(rolls.values())) > 1


# ----------------------------------------------------------------- rendering


def test_state_render_shows_both_bodies_with_integrity_and_tags() -> None:
    play = session()
    play.player.body.slots[Slot.TORSO].tags.add(LimbTag.BLEEDING)
    text = render_state(play)
    for slot_name in ("Kafa", "Gövde", "Sol Kol", "Sağ Kol", "Bacaklar", "Çekirdek"):
        assert text.count(slot_name) >= 2  # once per body table
    assert "45/45" in text and "100%" in text
    assert "Bleeding" in text
    assert "BLOOD: 85  [NORMAL]" in text
    assert "Jeff Right Arm" in text


def test_report_render_numbers_the_five_questions() -> None:
    play = session()
    text = render_report(play.perform("claim_the_cut:right_arm").reports[0])
    for index, question in enumerate(
        (
            "Ne hedeflendi?",
            "Ne değişti?",
            "Kan maliyeti?",
            "Ne kazanıldı?",
            "Hangi yeni risk doğdu?",
        ),
        start=1,
    ):
        assert f"{index}. {question}" in text


def test_summary_render_states_the_phase_one_lock() -> None:
    text = render_summary(run(WIN_SEQUENCE))
    assert "JEFF_YIELDED" in text
    assert "Graft edilebilir Sağ Kol" in text
    assert "Grafting Table bu arayüzün dışında" in text


def test_reason_localization_falls_back_to_the_rules_wording() -> None:
    assert localize_reason("Focus already used this round") == "Bu tur Focus zaten kullanıldı"
    assert localize_reason("Requires 18 Blood") == "18 Blood gerekiyor"
    assert localize_reason("Bone Scissors is unavailable") == (
        "Bone Scissors kullanılabilir değil"
    )
    assert localize_reason("a brand new rules reason") == "a brand new rules reason"
    assert localize_reason(None) == "sebep bildirilmedi"


# --------------------------------------------------------------- console loop


def console_run(keys: list[str], seed: int = 42) -> PlayConsole:
    pending = list(keys)
    output: list[str] = []

    def input_fn(_prompt: str) -> str:
        if not pending:
            raise EOFError
        return pending.pop(0)

    console = PlayConsole(
        session(seed), input_fn=input_fn, output_fn=output.append
    )
    console.run()
    return console


def test_console_drives_a_two_level_attack_selection() -> None:
    # 1 = Saldır, 1 = Grip Strike, 4 = Sağ Kol
    console = console_run(["1", "1", "4"])
    assert console.session.enemy.body.slots[Slot.RIGHT_ARM].integrity == 20
    assert any("RİTÜEL KAYDI" in line for line in console.transcript)


def test_console_back_option_resolves_nothing() -> None:
    console = console_run(["1", "0", "0"])
    assert console.session.log.round_number == 1
    assert console.session.outcome is PlayOutcome.ENDED_BY_PLAYER
    assert not console.session.reports


def test_console_rejects_out_of_range_and_non_numeric_input() -> None:
    console = console_run(["99", "abc", "", "0"])
    assert any("Geçersiz seçim" in line for line in console.transcript)
    assert not console.session.reports


def test_console_exhausted_input_ends_the_session_cleanly() -> None:
    console = console_run([])
    assert console.session.outcome is PlayOutcome.ENDED_BY_PLAYER
    assert any("OTURUM ÖZETİ" in line for line in console.transcript)


def test_console_focus_branch_and_state_reprint() -> None:
    console = console_run(["2", "5", "0"])
    assert console.session.intent_is_revealed()
    assert console.session.player.blood == 82


def test_console_item_and_defence_branches() -> None:
    # 3/1 = Blood Bag; 4/2 = Brace (defence entry 1, Guard Flesh, has no Right Arm)
    console = console_run(["3", "1", "4", "2", "0"])
    assert console.session.metrics.blood_bag_uses == 1
    assert any(
        event.event_type == "brace_activated" for event in console.session.log.events
    )


# ------------------------------------------------------------------ cli entry


def test_script_mode_replays_actions_and_writes_a_transcript(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    script = tmp_path / "actions.json"
    script.write_text(json.dumps(WIN_SEQUENCE), encoding="utf-8")
    transcript = tmp_path / "run.txt"
    exit_code = main(
        [
            "--seed",
            "42",
            "--script",
            str(script),
            "--transcript-output",
            str(transcript),
        ]
    )
    assert exit_code == 0
    printed = capsys.readouterr().out
    assert "JEFF_YIELDED" in printed
    assert "RİTÜEL KAYDI" in transcript.read_text(encoding="utf-8")


def test_script_mode_reports_refused_actions_without_aborting(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    script = tmp_path / "actions.json"
    script.write_text(json.dumps(["guard_flesh", "grip_strike:head"]), encoding="utf-8")
    assert main(["--script", str(script)]) == 0
    printed = capsys.readouterr().out
    assert "guard_flesh uygulanmadı" in printed


def test_script_must_contain_a_list(tmp_path: Path) -> None:
    script = tmp_path / "actions.json"
    script.write_text(json.dumps({"action": "focus"}), encoding="utf-8")
    with pytest.raises(SystemExit) as error:
        main(["--script", str(script)])
    assert error.value.code == 2


def test_cli_rejects_missing_script_without_traceback(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as error:
        main(["--script", str(tmp_path / "missing.json")])
    assert error.value.code == 2


def test_cli_round_limit_must_be_positive() -> None:
    with pytest.raises(SystemExit) as error:
        main(["--round-limit", "0"])
    assert error.value.code == 2
