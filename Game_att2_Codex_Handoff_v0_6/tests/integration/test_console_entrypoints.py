from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def run_module(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", *arguments],
        cwd=PROJECT_ROOT,
        capture_output=True,
        check=False,
        encoding="utf-8",
        errors="replace",
    )


def test_simulator_module_entrypoint_returns_machine_readable_json() -> None:
    result = run_module(
        "game_att2_sim",
        "--scenario",
        "jeff_baseline",
        "--seed",
        "42",
        "--format",
        "json",
    )
    assert result.returncode == 0
    assert json.loads(result.stdout)["metrics"]["scenario"] == "jeff_baseline"


def test_play_module_entrypoint_replays_the_example_sequence() -> None:
    result = run_module(
        "game_att2_sim.play_cli",
        "--seed",
        "42",
        "--script",
        str(PROJECT_ROOT / "examples" / "play_cli_win_sequence.json"),
    )
    assert result.returncode == 0
    assert "JEFF_YIELDED" in result.stdout


def test_research_module_entrypoint_replays_the_example_sequence() -> None:
    result = run_module(
        "game_att2_sim.research_cli",
        "--session-id",
        "AUTO-SUBPROCESS-001",
        "--evidence-class",
        "AUTOMATED_REGRESSION",
        "--participant-code",
        "AUTO-CODEX",
        "--script",
        str(PROJECT_ROOT / "research" / "interactive_shell" / "example_action_sequence.json"),
    )
    assert result.returncode == 0
    assert "Outcome: COMPLETED" in result.stdout


def test_entrypoint_input_error_is_clean_and_nonzero() -> None:
    result = run_module("game_att2_sim.play_cli", "--round-limit", "0")
    assert result.returncode == 2
    assert "must be positive" in result.stderr
    assert "Traceback" not in result.stderr
