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
    schema_version: str
    content_version: str
    scenario_version: str


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
    config = SimulatorConfig(
        rules=rules,
        limbs=limbs,
        actions=actions,
        items=dict(content.get("items", {})),
        starting_bodies=dict(content.get("starting_bodies", {})),
        enemies=dict(content.get("enemies", {})),
        table_options=dict(content.get("table_options", {})),
        scenarios=dict(scenario_file.get("scenarios", {})),
        schema_version=str(content.get("schema_version", "")),
        content_version=str(content.get("content_version", "")),
        scenario_version=str(scenario_file.get("scenario_version", "")),
    )
    _validate_approved_sequence(config)
    return config


def _validate_approved_sequence(config: SimulatorConfig) -> None:
    """Reject every broken reference used by the approved interactive sequence."""
    required_actions = {
        "focus",
        "grip_strike",
        "guard_flesh",
        "brace",
        "desperate_swing",
        "surgical_jab",
        "cover_it",
        "black_stitch",
        "calm_guard",
        "trade_offer",
    }
    required_items = {
        "blood_bag",
        "clotting_cream",
        "claim_the_cut",
        "bone_scissors",
        "hell_saw",
    }
    required_enemies = {"jeff", "anna"}
    required_tables = {
        "integrate_arm",
        "repair_torso",
        "strengthen_legs",
        "table_loan",
        "leave",
    }
    for action_id in sorted(required_actions):
        if action_id not in config.actions:
            raise ConfigValidationError(f"approved sequence requires action {action_id}")
    for item_id in sorted(required_items):
        raw = config.items.get(item_id)
        if not isinstance(raw, dict):
            raise ConfigValidationError(f"approved sequence requires item {item_id}")
        for field in ("cost", "gain", "gain_if_bleeding", "uses_per_fight"):
            if field in raw and (not isinstance(raw[field], int) or raw[field] < 0):
                raise ConfigValidationError(f"item {item_id} has invalid {field}")
    for limb in config.limbs.values():
        for action_id in limb.actions:
            if action_id not in config.actions:
                raise ConfigValidationError(f"limb {limb.id} references unknown action {action_id}")
    for body_id, raw in config.starting_bodies.items():
        if not isinstance(raw.get("blood"), int) or raw["blood"] < 0:
            raise ConfigValidationError(f"starting body {body_id} has invalid blood")
        for item_id, count in raw.get("inventory", {}).items():
            if item_id not in config.items:
                raise ConfigValidationError(
                    f"starting body {body_id} references unknown item {item_id}"
                )
            if not isinstance(count, int) or count < 0:
                raise ConfigValidationError(
                    f"starting body {body_id} has invalid inventory count for {item_id}"
                )
    for enemy_id in sorted(required_enemies):
        enemy = config.enemies.get(enemy_id)
        if not isinstance(enemy, dict):
            raise ConfigValidationError(f"approved sequence requires enemy {enemy_id}")
        if {_slot(slot) for slot in enemy.get("limbs", {})} != set(Slot):
            raise ConfigValidationError(f"enemy {enemy_id} must define all six slots")
        for slot_name, limb_raw in enemy["limbs"].items():
            if not isinstance(limb_raw, dict):
                raise ConfigValidationError(f"enemy {enemy_id} has malformed limb {slot_name}")
            definition_id = limb_raw.get("definition")
            if definition_id is not None:
                if definition_id not in config.limbs:
                    raise ConfigValidationError(
                        f"enemy {enemy_id} references unknown limb {definition_id}"
                    )
                if config.limbs[str(definition_id)].slot is not _slot(slot_name):
                    raise ConfigValidationError(
                        f"enemy {enemy_id} limb {definition_id} is in the wrong slot"
                    )
            else:
                maximum = limb_raw.get("max_integrity")
                if not isinstance(maximum, int) or maximum <= 0 or not limb_raw.get("size"):
                    raise ConfigValidationError(
                        f"enemy {enemy_id} has invalid inline limb {slot_name}"
                    )
        for action_id in enemy.get("actions", []):
            if action_id not in config.actions:
                raise ConfigValidationError(
                    f"enemy {enemy_id} references unknown action {action_id}"
                )
    for option_id in sorted(required_tables):
        option = config.table_options.get(option_id)
        if not isinstance(option, dict):
            raise ConfigValidationError(f"approved sequence requires table option {option_id}")
        if not any(key in option for key in ("cost", "gain")):
            raise ConfigValidationError(f"table option {option_id} has no transaction field")
    for scenario_id, raw in config.scenarios.items():
        scenario_body_id = raw.get("start_body")
        if scenario_body_id is not None and scenario_body_id not in config.starting_bodies:
            raise ConfigValidationError(
                f"scenario {scenario_id} references unknown starting body {scenario_body_id}"
            )
        for scenario_enemy_id in raw.get("encounters", []):
            if scenario_enemy_id not in config.enemies:
                raise ConfigValidationError(
                    f"scenario {scenario_id} references unknown enemy {scenario_enemy_id}"
                )
