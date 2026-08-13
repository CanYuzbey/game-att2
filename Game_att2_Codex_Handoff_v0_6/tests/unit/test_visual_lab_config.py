from __future__ import annotations

from pathlib import Path

import pytest

from game_att2_sim.errors import ConfigValidationError
from game_att2_sim.visual_lab_config import load_visual_lab_config


def test_visual_lab_config_is_isolated_and_provisional() -> None:
    config = load_visual_lab_config()

    assert config.implementation_status == "research_only"
    assert config.provisional_label == "PROVISIONAL_VISUAL_LAB_ONLY"
    assert config.fixture.fixture_id == "H1-F0"
    assert config.telegraph.recorded_order == ("a", "b", "b", "a")
    assert config.readiness.menu_item_recovery == 0
    assert config.profile("assisted").assisted is True


@pytest.mark.parametrize(
    ("needle", "replacement", "message"),
    [
        ("implementation_status: research_only", "implementation_status: production", "research_only"),
        ("menu_item_recovery: 0", "menu_item_recovery: 1", "menu/item"),
        ("fixture_id: H1-F0", "fixture_id: NEW-FIXTURE", "H1-F0"),
        ("low_blood: 18", "wound_to_blood: 18", "prohibited"),
    ],
)
def test_visual_lab_config_rejects_scope_or_contract_drift(
    tmp_path: Path,
    needle: str,
    replacement: str,
    message: str,
) -> None:
    source = Path(__file__).resolve().parents[2] / "config" / "visual_lab_v0_1.yaml"
    changed = source.read_text(encoding="utf-8").replace(needle, replacement)
    path = tmp_path / "invalid.yaml"
    path.write_text(changed, encoding="utf-8")

    with pytest.raises(ConfigValidationError, match=message):
        load_visual_lab_config(path)
