from __future__ import annotations

import json

import pytest

from game_att2_sim.cli import main
from game_att2_sim.reporting import render_markdown, render_text
from game_att2_sim.scenarios import run_all, run_scenario


def test_cli_named_scenario_json_is_repeatable(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--scenario", "jeff_baseline", "--seed", "42", "--format", "json"]) == 0
    first = capsys.readouterr().out
    assert main(["--scenario", "jeff_baseline", "--seed", "42", "--format", "json"]) == 0
    second = capsys.readouterr().out
    assert first == second
    assert json.loads(first)["metrics"]["scenario"] == "jeff_baseline"


def test_cli_batch_and_nested_output_path(tmp_path: pytest.TempPathFactory) -> None:
    output = tmp_path / "nested" / "batch.json"
    assert main(["--batch", "3", "--strategy", "random_legal", "--format", "json", "--output", str(output)]) == 0
    assert json.loads(output.read_text(encoding="utf-8"))["count"] == 3


def test_cli_invalid_output_path_is_nonzero(tmp_path: pytest.TempPathFactory) -> None:
    with pytest.raises(SystemExit) as error:
        main(["--scenario", "jeff_baseline", "--output", str(tmp_path)])
    assert error.value.code == 2


def test_cli_batch_formats_are_human_readable(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--batch", "1", "--format", "text"]) == 0
    assert capsys.readouterr().out.startswith("Batch: strategy=balanced")
    assert main(["--batch", "1", "--format", "markdown"]) == 0
    markdown = capsys.readouterr().out
    assert markdown.startswith("# Game att2 Combat Simulator Results")
    assert "## Required Scenarios" not in markdown
    assert "| balanced |" in markdown


def test_cli_run_selectors_are_mutually_exclusive() -> None:
    with pytest.raises(SystemExit) as error:
        main(["--scenario", "jeff_baseline", "--batch", "1"])
    assert error.value.code == 2


def test_cli_invalid_input_is_nonzero() -> None:
    with pytest.raises(SystemExit) as error:
        main(["--scenario", "not-a-scenario"])
    assert error.value.code == 2


def test_cli_batch_count_must_be_positive() -> None:
    with pytest.raises(SystemExit) as error:
        main(["--batch", "0"])
    assert error.value.code == 2


def test_renderers_include_required_fields_and_markdown() -> None:
    result = run_scenario("mini_campaign", 42)
    text = render_text(result)
    assert "Scenario:" in text and "final blood:" in text and "Body:" in text
    markdown = render_markdown(run_all(42))
    assert "# Game att2 Combat Simulator Results v0.2" in markdown
    assert "mini_campaign" in markdown
