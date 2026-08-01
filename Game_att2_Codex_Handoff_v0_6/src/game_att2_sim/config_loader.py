"""YAML loading and startup validation for the checked-in simulator data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]

from .encounter_goals import (
    EncounterDesignDefinition,
    MotivationKind,
    MotivationProfile,
    OutcomeLevel,
    ResolutionKind,
    VictoryRouteDefinition,
    VictoryRouteKind,
)
from .enums import HarvestQuality, LimbState, Slot
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
    motivation_profiles: dict[str, MotivationProfile]
    encounter_designs: dict[str, EncounterDesignDefinition]
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
    rules = _load_yaml(directory / "combat_rules_v0_5.yaml")
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
        duration_rounds = raw.get("duration_rounds", 0)
        if (
            not isinstance(duration_rounds, int)
            or isinstance(duration_rounds, bool)
            or duration_rounds < 0
        ):
            raise ConfigValidationError(f"action {action_id} has invalid duration_rounds")
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
            duration_rounds=duration_rounds,
            implementation_status=str(raw.get("implementation_status", "implemented")),
        )
    if actions.get("grip_strike") is None or actions["grip_strike"].can_clean_sever:
        raise ConfigValidationError("Grip Strike must exist and cannot clean sever")
    cover_it = actions.get("cover_it")
    if cover_it is None or cover_it.duration_rounds != 1:
        raise ConfigValidationError("Cover It must declare exactly one round of duration")
    if cover_it.implementation_status != "deferred_until_protection_tradeoff_is_approved":
        raise ConfigValidationError(
            "Cover It must remain deferred until its protection trade-off is approved"
        )
    limb_for_life = rules.get("limb_for_life")
    if not isinstance(limb_for_life, dict):
        raise ConfigValidationError("rules require limb_for_life")
    blood_rules = rules.get("blood")
    if (
        not isinstance(blood_rules, dict)
        or blood_rules.get("zero_result") != "death"
        or blood_rules.get("death_at") != 0
    ):
        raise ConfigValidationError("Blood zero_result must be death")
    if limb_for_life.get("sacrifice_selection") != "seeded_random_usable_non_core_limb":
        raise ConfigValidationError("Limb for Life requires the approved sacrifice selection")
    if (
        limb_for_life.get("enabled") is not True
        or limb_for_life.get("max_uses_per_run") != 1
        or not isinstance(limb_for_life.get("restore_blood"), int)
        or int(limb_for_life["restore_blood"]) <= 0
    ):
        raise ConfigValidationError("Limb for Life must be enabled once with positive Blood")
    motivation_profiles = _load_motivation_profiles(content)
    encounter_designs = _load_encounter_designs(content, motivation_profiles)
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
        motivation_profiles=motivation_profiles,
        encounter_designs=encounter_designs,
        schema_version=str(content.get("schema_version", "")),
        content_version=str(content.get("content_version", "")),
        scenario_version=str(scenario_file.get("scenario_version", "")),
    )
    _validate_approved_sequence(config)
    return config


def _load_motivation_profiles(content: dict[str, Any]) -> dict[str, MotivationProfile]:
    raw_profiles = content.get("motivation_profiles", {})
    if not isinstance(raw_profiles, dict):
        raise ConfigValidationError("motivation_profiles must be a mapping")
    profiles: dict[str, MotivationProfile] = {}
    for profile_id, raw in raw_profiles.items():
        if not isinstance(raw, dict):
            raise ConfigValidationError(f"motivation profile {profile_id} must be a mapping")
        try:
            profile = MotivationProfile(
                id=str(profile_id),
                kind=MotivationKind(str(raw["kind"])),
                summary=str(raw["summary"]),
                desired_assets=tuple(str(value) for value in raw.get("desired_assets", [])),
                preserve_slots=tuple(_slot(str(value)) for value in raw.get("preserve_slots", [])),
                acceptable_resolutions=tuple(
                    ResolutionKind(str(value))
                    for value in raw.get("acceptable_resolutions", [])
                ),
                lethality=str(raw["lethality"]),
                escalation_triggers=tuple(
                    str(value) for value in raw.get("escalation_triggers", [])
                ),
            )
        except (KeyError, TypeError, ValueError) as error:
            raise ConfigValidationError(
                f"invalid motivation profile {profile_id}: {error}"
            ) from error
        if not profile.summary.strip() or not profile.lethality.strip():
            raise ConfigValidationError(
                f"motivation profile {profile_id} requires summary and lethality"
            )
        profiles[profile.id] = profile
    return profiles


def _load_encounter_designs(
    content: dict[str, Any],
    profiles: dict[str, MotivationProfile],
) -> dict[str, EncounterDesignDefinition]:
    raw_designs = content.get("encounter_designs", {})
    if not isinstance(raw_designs, dict):
        raise ConfigValidationError("encounter_designs must be a mapping")
    designs: dict[str, EncounterDesignDefinition] = {}
    for encounter_id, raw in raw_designs.items():
        if not isinstance(raw, dict) or not isinstance(raw.get("actor_motivations"), dict):
            raise ConfigValidationError(
                f"encounter design {encounter_id} requires actor_motivations"
            )
        actor_motivations = {
            str(actor): str(profile_id)
            for actor, profile_id in raw["actor_motivations"].items()
        }
        if set(actor_motivations) != {"player", "enemy"}:
            raise ConfigValidationError(
                f"encounter design {encounter_id} requires exactly player and enemy motivations"
            )
        raw_parameters = raw.get("parameters", {})
        if not isinstance(raw_parameters, dict):
            raise ConfigValidationError(
                f"encounter design {encounter_id} parameters must be a mapping"
            )
        for actor, profile_id in actor_motivations.items():
            if actor not in {"player", "enemy"}:
                raise ConfigValidationError(
                    f"encounter design {encounter_id} has invalid actor {actor}"
                )
            if profile_id not in profiles:
                raise ConfigValidationError(
                    f"encounter design {encounter_id} references unknown motivation {profile_id}"
                )
        routes: list[VictoryRouteDefinition] = []
        route_ids: set[str] = set()
        for raw_route in raw.get("victory_routes", []):
            if not isinstance(raw_route, dict):
                raise ConfigValidationError(
                    f"encounter design {encounter_id} has malformed victory route"
                )
            try:
                route = VictoryRouteDefinition(
                    id=str(raw_route["id"]),
                    actor=str(raw_route["actor"]),
                    kind=VictoryRouteKind(str(raw_route["kind"])),
                    predicate=str(raw_route["predicate"]),
                    success_level=OutcomeLevel(str(raw_route["success_level"])),
                )
            except (KeyError, ValueError) as error:
                raise ConfigValidationError(
                    f"invalid victory route in {encounter_id}: {error}"
                ) from error
            if route.id in route_ids or route.actor not in actor_motivations:
                raise ConfigValidationError(
                    f"encounter design {encounter_id} has duplicate/invalid route {route.id}"
                )
            if not route.predicate.strip():
                raise ConfigValidationError(f"victory route {route.id} requires a predicate")
            route_ids.add(route.id)
            routes.append(route)
        if not routes:
            raise ConfigValidationError(
                f"encounter design {encounter_id} requires at least one victory route"
            )
        designs[str(encounter_id)] = EncounterDesignDefinition(
            id=str(encounter_id),
            actor_motivations=actor_motivations,
            victory_routes=tuple(routes),
            parameters=dict(raw_parameters),
        )
    return designs


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
    jeff_design = config.encounter_designs.get("jeff")
    if jeff_design is None:
        raise ConfigValidationError("approved sequence requires Jeff encounter design")
    required_jeff_parameters: dict[str, type[Any]] = {
        "bargain_asset": str,
        "bargain_limb": str,
        "bargain_quality": str,
        "bargain_score": int,
        "offense_target": str,
        "offense_target_score": int,
        "pressure_target": str,
        "pressure_target_score": int,
        "repetition_penalty": int,
    }
    for parameter, expected_type in required_jeff_parameters.items():
        value = jeff_design.parameters.get(parameter)
        if not isinstance(value, expected_type) or (
            expected_type is int and isinstance(value, bool)
        ):
            raise ConfigValidationError(
                f"Jeff encounter design requires {parameter} as {expected_type.__name__}"
            )
    bargain_asset = str(jeff_design.parameters["bargain_asset"])
    if bargain_asset not in config.items:
        raise ConfigValidationError("Jeff bargain_asset must reference a configured item")
    bargain_slot = _slot(str(jeff_design.parameters["bargain_limb"]))
    if bargain_slot is not Slot.RIGHT_ARM:
        raise ConfigValidationError(
            "Jeff bargain_limb must remain right_arm in the approved campaign"
        )
    _slot(str(jeff_design.parameters["offense_target"]))
    _slot(str(jeff_design.parameters["pressure_target"]))
    try:
        bargain_quality = HarvestQuality(str(jeff_design.parameters["bargain_quality"]))
    except ValueError as error:
        raise ConfigValidationError("Jeff bargain_quality is invalid") from error
    if bargain_quality is not HarvestQuality.CLEAN:
        raise ConfigValidationError("Jeff approved bargain_quality must be clean")
    for score_name in (
        "bargain_score",
        "offense_target_score",
        "pressure_target_score",
        "repetition_penalty",
    ):
        score_value = jeff_design.parameters[score_name]
        if not isinstance(score_value, int) or isinstance(score_value, bool):
            raise ConfigValidationError(f"Jeff {score_name} must be an integer")
        if score_value < 0:
            raise ConfigValidationError(f"Jeff {score_name} must not be negative")
    jeff_profile = config.motivation_profiles[jeff_design.actor_motivations["enemy"]]
    if bargain_asset not in jeff_profile.desired_assets:
        raise ConfigValidationError("Jeff bargain_asset must be a desired motivation asset")
    if bargain_slot not in jeff_profile.preserve_slots:
        raise ConfigValidationError("Jeff bargain_limb must be preserved by his motivation")
    if "bargain_rejected" not in jeff_profile.escalation_triggers:
        raise ConfigValidationError(
            "Jeff motivation must declare bargain_rejected as an escalation trigger"
        )
    allowed_jeff_predicates = {
        "player_has_graftable_jeff_right_arm",
        "jeff_offensive_sources_unusable",
        "jeff_surrendered",
        "jeff_has_clotting_cream",
        "player_dead",
        "jeff_survived_resolution",
    }
    if any(
        route.predicate not in allowed_jeff_predicates
        for route in jeff_design.victory_routes
    ):
        raise ConfigValidationError(
            "Jeff victory route uses a predicate unsupported by the approved campaign"
        )
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
