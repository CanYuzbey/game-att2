from __future__ import annotations

import json
from pathlib import Path

import pytest

from game_att2_sim.research_cli import main

BASE_ARGS = [
    "--session-id",
    "AUTO-CLI-001",
    "--evidence-class",
    "AUTOMATED_REGRESSION",
    "--participant-code",
    "AUTO-CODEX",
]


def test_scripted_research_cli_writes_paired_exports(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    script = tmp_path / "actions.json"
    script.write_text(json.dumps([{"action": "focus"}]), encoding="utf-8")
    json_output = tmp_path / "nested" / "session.json"
    summary_output = tmp_path / "nested" / "session.md"

    assert (
        main(
            [
                *BASE_ARGS,
                "--script",
                str(script),
                "--json-output",
                str(json_output),
                "--summary-output",
                str(summary_output),
            ]
        )
        == 0
    )
    assert json.loads(json_output.read_text(encoding="utf-8"))["metadata"]["session_id"] == (
        "AUTO-CLI-001"
    )
    assert summary_output.read_text(encoding="utf-8").startswith("Session AUTO-CLI-001")
    assert "Session AUTO-CLI-001" in capsys.readouterr().out


def test_research_cli_requires_paired_exports(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as error:
        main([*BASE_ARGS, "--json-output", str(tmp_path / "session.json")])
    assert error.value.code == 2


def test_research_cli_rejects_missing_script_without_traceback(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as error:
        main([*BASE_ARGS, "--script", str(tmp_path / "missing.json")])
    assert error.value.code == 2


def test_research_script_must_contain_a_list(tmp_path: Path) -> None:
    script = tmp_path / "actions.json"
    script.write_text(json.dumps({"action": "focus"}), encoding="utf-8")
    with pytest.raises(SystemExit) as error:
        main([*BASE_ARGS, "--script", str(script)])
    assert error.value.code == 2
