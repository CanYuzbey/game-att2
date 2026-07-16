"""YAML loading and startup validation for the checked-in simulator data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]

from .enums import LimbState, Slot
from .errors import ConfigValidationError
from .models import ActionDefinition, LimbDefinition


@dataclass(frozen=True)
class SimulatorConfig:
    rules: dict[str, Any]
    limbs: dict[str, LimbDefinition]
    actions: dict[str, ActionDefinition]
    items: dict[str, dict[str, Any]]
    starting_bodies: dict[str, dict[str, Any]]
    enemies: dict[str, dict[str, Any]]
    table_options: dict[str, dict[str, Any]]
    scenarios: dict[str, dict[str, Any]]


def default_config_directory() -> Path:
    return Path(__file__).resolve().parents[2] / "config"


def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except OSError as error:
        raise ConfigValidationError(f"cannot read {path}: {error}") from error
    except yaml.YAMLError as error:
        raise ConfigValidationError(f"invalid YAML in {path}: {error}") from error
    if not isinstance(data, dict):
        raise ConfigValidationError(f"{path} must contain a mapping")
    return data


def _slot(value: str) -> Slot:
    try:
        return Slot(value)
    except ValueError as error:
        raise ConfigValidationError(f"invalid body slot: {value}") from error


def load_config(directory: Path | None = None) -> SimulatorConfig:
    directory = directory or default_config_directory()
    rules = _load_yaml(directory / "combat_rules_v0_4.yaml")
    content = _load_yaml(directory / "content_v0_1.yaml")
    scenario_file = _load_yaml(directory / "scenarios_v0_1.yaml")
    limb_data = content.get("limbs", {})
    if not isinstance(limb_data, dict):
        raise ConfigValidationError("limbs must be a mapping")
    limbs: dict[str, LimbDefinition] = {}
    for limb_id, raw in limb_data.items():
        if limb_id in limbs or not isinstance(raw, dict):
            raise ConfigValidationError(f"invalid duplicate or malformed limb: {limb_id}")
        maximum = raw.get("max_integrity")
        if not isinstance(maximum, int) or maximum <= 0:
            raise ConfigValidationError(f"limb {limb_id} has invalid max_integrity")
        initial = LimbState(raw.get("initial_state", "intact"))
        limbs[limb_id] = LimbDefinition(
            id=limb_id,
            name=str(raw.get("name", limb_id)),
            slot=_slot(str(raw.get("slot"))),
            max_integrity=maximum,
            size=str(raw.get("size", "medium")),
            actions=tuple(raw.get("actions", [])),
            passives=tuple(raw.get("passives", [])),
            initial_state=initial,
        )
    action_data = content.get("actions", {})
    if not isinstance(action_data, dict):
        raise ConfigValidationError("actions must be a mapping")
    actions: dict[str, ActionDefinition] = {}
    for action_id, raw in action_data.items():
        if action_id in actions or not isinstance(raw, dict):
            raise ConfigValidationError(f"invalid duplicate or malformed action: {action_id}")
        cost = raw.get("cost", 0)
        if not isinstance(cost, int) or cost < 0:
            raise ConfigValidationError(f"action {action_id} has invalid cost")
        actions[action_id] = ActionDefinition(
            id=action_id,
            name=str(raw.get("name", action_id)),
            timing=str(raw.get("timing")),
            cost=cost,
            source_slot=_slot(raw["source_slot"]) if "source_slot" in raw else None,
            damage=int(raw.get("damage", 0)),
            damage_type=raw.get("damage_type"),
            reduction=float(raw.get("reduction", 0.0)),
            can_clean_sever=bool(raw.get("can_clean_sever", False)),
        )
    if actions.get("grip_strike") is None or actions["grip_strike"].can_clean_sever:
        raise ConfigValidationError("Grip Strike must exist and cannot clean sever")
    slots = set(Slot)
    for body_id, raw in content.get("starting_bodies", {}).items():
        body_slots = {_slot(slot) for slot in raw.get("slots", {})}
        if body_slots != slots:
            raise ConfigValidationError(f"starting body {body_id} must define all six slots")
        for limb_id in raw["slots"].values():
            if limb_id not in limbs:
                raise ConfigValidationError(f"starting body {body_id} references {limb_id}")
    for option_id, raw in content.get("table_options", {}).items():
        if raw.get("cost", 0) < 0 or raw.get("gain", 0) < 0:
            raise ConfigValidationError(f"table option {option_id} has an invalid value")
    return SimulatorConfig(
        rules=rules,
        limbs=limbs,
        actions=actions,
        items=dict(content.get("items", {})),
        starting_bodies=dict(content.get("starting_bodies", {})),
        enemies=dict(content.get("enemies", {})),
        table_options=dict(content.get("table_options", {})),
        scenarios=dict(scenario_file.get("scenarios", {})),
    )
