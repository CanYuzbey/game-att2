from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml

from game_att2_sim.config_loader import load_config
from game_att2_sim.enums import IntentClarity, Slot
from game_att2_sim.errors import ConfigValidationError
from game_att2_sim.h1_config import default_h1_config_path, load_h1_config
from game_att2_sim.reflex import ExecutionGrade, ReflexTier


def write_config(tmp_path: Path, mutate: object) -> Path:
    raw: dict[str, Any] = yaml.safe_load(
        default_h1_config_path().read_text(encoding="utf-8")
    )
    assert isinstance(raw, dict)
    assert callable(mutate)
    mutate(raw)
    path = tmp_path / "h1.yaml"
    path.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    return path


def test_default_h1_config_is_isolated_and_valid() -> None:
    standard = load_config()
    config = load_h1_config()

    assert "h1" not in standard.scenarios
    assert "H1-F0" not in standard.scenarios
    assert config.implementation_status == "research_only"
    assert config.provisional_label == "PROVISIONAL_H1_RESEARCH_ONLY"
    assert config.profile("precise").assisted is False
    assert config.profile("assisted").assisted is True
    assert config.fixture.attacker_id == "anna"
    assert config.fixture.target is Slot.TORSO
    assert config.intent_error_penalty[IntentClarity.EXACT] == 0
    assert config.mitigation_basis_points[ReflexTier.CRITICAL][ExecutionGrade.EXCEPTIONAL] == 10000
    assert all(value == 0 for value in config.ordinary_exposure_damage.values())


@pytest.mark.parametrize(
    "mutate",
    [
        lambda raw: raw.__setitem__("schema_version", "future"),
        lambda raw: raw.__setitem__("implementation_status", "production"),
        lambda raw: raw["ordinary_exposure_damage"].__setitem__("miss", 1),
        lambda raw: raw["mitigation_basis_points"]["routine"].__setitem__(
            "exceptional", 10001
        ),
        lambda raw: raw.__setitem__("warden", {}),
        lambda raw: raw["timing_profiles"]["precise"]["bands"][1].__setitem__(
            "max_error", 20
        ),
        lambda raw: raw["timing_profiles"]["precise"]["bands"][0].__setitem__(
            "grade", "limited"
        ),
        lambda raw: raw["fixture"].__setitem__("target", "head"),
    ],
)
def test_invalid_or_out_of_scope_h1_config_fails(
    tmp_path: Path, mutate: object
) -> None:
    with pytest.raises(ConfigValidationError):
        load_h1_config(write_config(tmp_path, mutate))


def test_duplicate_yaml_keys_fail_loudly(tmp_path: Path) -> None:
    content = default_h1_config_path().read_text(encoding="utf-8")
    path = tmp_path / "duplicate.yaml"
    path.write_text(content + '\nschema_version: "duplicate"\n', encoding="utf-8")

    with pytest.raises(ConfigValidationError, match="duplicate"):
        load_h1_config(path)


def test_unknown_profile_fails_with_domain_error() -> None:
    with pytest.raises(ConfigValidationError, match="unknown H1 timing profile"):
        load_h1_config().profile("unknown")
