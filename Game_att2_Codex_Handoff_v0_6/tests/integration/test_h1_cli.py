from __future__ import annotations

import json
from pathlib import Path

import pytest

from game_att2_sim.h1_cli import ALL_VARIANT_IDS, VARIANT_PROMPTS, main

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = PROJECT_ROOT / "examples" / "h1_scripted_comparisons.json"


def test_every_owner_diagnostic_variant_explains_what_is_being_tested() -> None:
    assert set(VARIANT_PROMPTS) == ALL_VARIANT_IDS
    assert all("TEST " in prompt for prompt in VARIANT_PROMPTS.values())
    assert "strategy" in VARIANT_PROMPTS["H1-C1-prepared"]
    assert "extra punishment" in VARIANT_PROMPTS["H1-C3-ordinary"]
    assert "accommodation" in VARIANT_PROMPTS["H1-C5-assisted"]


def test_h1_cli_all_comparisons_returns_machine_readable_json(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert (
        main(
            [
                "--all-comparisons",
                "--script",
                str(SCRIPT),
                "--format",
                "json",
            ]
        )
        == 0
    )

    payload = json.loads(capsys.readouterr().out)
    assert payload["evidence_class"] == "AUTOMATED_REGRESSION"
    assert len(payload["runs"]) == 12
    assert "does not establish fun" in payload["claims_boundary"]


def test_h1_cli_single_comparison_supports_markdown_and_profile_override(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert (
        main(
            [
                "--comparison",
                "H1-C1",
                "--script",
                str(SCRIPT),
                "--profile",
                "assisted",
                "--format",
                "markdown",
            ]
        )
        == 0
    )

    output = capsys.readouterr().out
    assert output.startswith("# Game att2 H1 Research Evidence")
    assert "H1-C1-unprepared" in output
    assert "H1-C2" not in output


def test_h1_cli_rejects_malformed_script_without_partial_stdout(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    script = tmp_path / "bad.json"
    script.write_text('{"schema_version": "wrong"}', encoding="utf-8")

    with pytest.raises(SystemExit) as error:
        main(["--comparison", "H1-C1", "--script", str(script), "--format", "json"])

    captured = capsys.readouterr()
    assert error.value.code == 2
    assert captured.out == ""
    assert "requires schema_version" in captured.err


def test_h1_cli_requires_script_for_automated_evidence() -> None:
    with pytest.raises(SystemExit) as error:
        main(
            [
                "--comparison",
                "H1-C1",
                "--evidence-class",
                "AUTOMATED_REGRESSION",
            ]
        )

    assert error.value.code == 2


def test_owner_diagnostic_requires_session_and_consent() -> None:
    with pytest.raises(SystemExit) as error:
        main(["--comparison", "H1-C1", "--evidence-class", "OWNER_DIAGNOSTIC"])

    assert error.value.code == 2


def test_owner_diagnostic_saves_clean_non_overwriting_evidence(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "game_att2_sim.h1_cli._capture_timing_error",
        lambda _variant_id: 100,
    )
    output = tmp_path / "OWNER-H1-DIAG-TEST.json"
    arguments = [
        "--comparison",
        "H1-C1",
        "--comparison",
        "H1-C3",
        "--session-id",
        "OWNER-H1-DIAG-TEST",
        "--consent-confirmed",
        "--evidence-class",
        "OWNER_DIAGNOSTIC",
        "--format",
        "json",
        "--output",
        str(output),
    ]

    assert main(arguments) == 0
    captured = capsys.readouterr()
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert captured.out == ""
    assert "Saved H1 evidence" in captured.err
    assert payload["session_metadata"] == {
        "consent_confirmed": True,
        "facilitator_deviations": [],
        "input_mode": "terminal_timing_capture",
        "participant_identity_collected": False,
        "selected_comparisons": ["H1-C1", "H1-C3"],
        "session_id": "OWNER-H1-DIAG-TEST",
    }

    with pytest.raises(SystemExit) as error:
        main(arguments)
    assert error.value.code == 2


def test_h1_cli_scripted_output_is_identical_across_replays(
    capsys: pytest.CaptureFixture[str],
) -> None:
    arguments = [
        "--all-comparisons",
        "--script",
        str(SCRIPT),
        "--format",
        "json",
    ]
    assert main(arguments) == 0
    first = capsys.readouterr().out
    assert main(arguments) == 0
    second = capsys.readouterr().out

    assert first == second
