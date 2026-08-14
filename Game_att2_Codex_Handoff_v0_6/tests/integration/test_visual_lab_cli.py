from __future__ import annotations

import json
from pathlib import Path

import pytest

from game_att2_sim.visual_lab_cli import main

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = PROJECT_ROOT / "examples" / "visual_lab_scripted_comparisons.json"


def test_cli_renders_all_scripted_comparisons_as_json(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert main(["--script", str(SCRIPT), "--all-comparisons", "--format", "json"]) == 0

    payload = json.loads(capsys.readouterr().out)
    assert len(payload["runs"]) == 20
    assert payload["artifact"] == "game-att2-visual-interaction-lab-evidence-0.1"


def test_cli_builds_local_fragment_with_required_controls(tmp_path: Path) -> None:
    output = tmp_path / "visual-lab.html"

    assert main(["--page", "--output", str(output)]) == 0
    fragment = output.read_text(encoding="utf-8")

    assert fragment.startswith('<div id="game-att2-readiness-lab">')
    assert "<!doctype" not in fragment.lower()
    assert "__VISUAL_LAB_CONFIG__" not in fragment
    assert "Start telegraph" in fragment
    assert "Block / Space" in fragment
    assert "Practice 0 / 2" in fragment
    assert "signedOffsetMs" in fragment
    assert "vl-cursor" in fragment
    assert "Jab is moving toward the contact line" in fragment
    assert "Preparation / intent" in fragment
    assert "Right Arm after" in fragment
    assert "vl-high-risk-ack" in fragment
    assert "High-risk acknowledgement required" in fragment
    assert "practiceTrials" in fragment
    assert "recordedTrials" in fragment
    assert "Diagnostic debrief" in fragment
    assert 'evidenceClass: "OWNER_DIAGNOSTIC_DEFERRED"' in fragment
    assert "OWNER_DIAGNOSTIC_PENDING_SEPARATE_APPROVAL" not in fragment
    assert "fetch(" not in fragment
    assert "WebSocket" not in fragment


def test_cli_refuses_to_overwrite_evidence_or_page(tmp_path: Path) -> None:
    output = tmp_path / "existing.html"
    output.write_text("preserve", encoding="utf-8")

    with pytest.raises(SystemExit) as error:
        main(["--page", "--output", str(output)])

    assert error.value.code == 2
    assert output.read_text(encoding="utf-8") == "preserve"
