"""Strict loader for the isolated H1 reflex research configuration."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, cast

import yaml  # type: ignore[import-untyped]

from .enums import IntentClarity, Slot
from .errors import ConfigValidationError
from .reflex import ExecutionGrade, ReflexTier, TimingBand, TimingProfile


@dataclass(frozen=True)
class H1FixtureConfig:
    fixture_id: str
    incoming_action: str
    attacker_id: str
    attacker_source: Slot
    target: Slot
    blocking_source: Slot
    guard_action: str
    base_damage: int
    normal_torso_integrity: int
    threshold_torso_integrity: int


@dataclass(frozen=True)
class H1Config:
    schema_version: str
    spec_version: str
    implementation_status: str
    provisional_label: str
    grade_order: tuple[ExecutionGrade, ...]
    timing_profiles: Mapping[str, TimingProfile]
    prepared_error_bonus: int
    prepared_min_grade: ExecutionGrade
    intent_error_penalty: Mapping[IntentClarity, int]
    mitigation_basis_points: Mapping[ReflexTier, Mapping[ExecutionGrade, int]]
    ordinary_exposure_damage: Mapping[ExecutionGrade, int]
    high_risk_affected_source: Slot
    high_risk_exposure_damage: Mapping[ExecutionGrade, int]
    fixture: H1FixtureConfig

    def profile(self, profile_id: str) -> TimingProfile:
        try:
            return self.timing_profiles[profile_id]
        except KeyError as error:
            raise ConfigValidationError(f"unknown H1 timing profile: {profile_id}") from error


class _UniqueKeyLoader(yaml.SafeLoader):  # type: ignore[misc]
    pass


def _construct_unique_mapping(
    loader: _UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict[object, object]:
    mapping: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ConfigValidationError(f"duplicate H1 configuration key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def default_h1_config_path() -> Path:
    return Path(__file__).resolve().parents[2] / "config" / "h1_reflex_v0_1.yaml"


def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        loaded = yaml.load(path.read_text(encoding="utf-8"), Loader=_UniqueKeyLoader)
    except ConfigValidationError:
        raise
    except OSError as error:
        raise ConfigValidationError(f"cannot read {path}: {error}") from error
    except yaml.YAMLError as error:
        raise ConfigValidationError(f"invalid H1 YAML in {path}: {error}") from error
    if not isinstance(loaded, dict):
        raise ConfigValidationError("H1 configuration must contain a mapping")
    return cast(dict[str, Any], loaded)


def _mapping(raw: object, label: str) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ConfigValidationError(f"{label} must be a mapping")
    return cast(dict[str, Any], raw)


def _non_negative_int(raw: object, label: str) -> int:
    if not isinstance(raw, int) or isinstance(raw, bool) or raw < 0:
        raise ConfigValidationError(f"{label} must be a non-negative integer")
    return raw


def _exact_keys(raw: Mapping[str, Any], expected: set[str], label: str) -> None:
    actual = set(raw)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ConfigValidationError(f"{label} keys mismatch; missing={missing}, extra={extra}")


def _reject_prohibited_keys(value: object, path: str = "root") -> None:
    prohibited = {
        "wound",
        "wounds",
        "wound_to_blood",
        "ruined_torso",
        "ruined_torso_lethality",
        "warden",
        "encounter_3",
        "production_content",
    }
    if isinstance(value, dict):
        for key, child in value.items():
            normalized = str(key).lower()
            if normalized in prohibited:
                raise ConfigValidationError(f"prohibited H1 key at {path}: {key}")
            _reject_prohibited_keys(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_prohibited_keys(child, f"{path}[{index}]")


def _grade_map(raw: object, label: str, maximum: int | None = None) -> Mapping[ExecutionGrade, int]:
    data = _mapping(raw, label)
    _exact_keys(data, {grade.value for grade in ExecutionGrade}, label)
    result: dict[ExecutionGrade, int] = {}
    for grade in ExecutionGrade:
        value = _non_negative_int(data[grade.value], f"{label}.{grade.value}")
        if maximum is not None and value > maximum:
            raise ConfigValidationError(f"{label}.{grade.value} must be <= {maximum}")
        result[grade] = value
    return MappingProxyType(result)


def load_h1_config(path: Path | None = None) -> H1Config:
    raw = _load_yaml(path or default_h1_config_path())
    _reject_prohibited_keys(raw)
    _exact_keys(
        raw,
        {
            "schema_version",
            "spec_version",
            "implementation_status",
            "provisional_label",
            "grade_order",
            "timing_profiles",
            "strategy_modifiers",
            "mitigation_basis_points",
            "ordinary_exposure_damage",
            "high_risk_exposure",
            "fixture",
        },
        "H1 root",
    )
    if raw["implementation_status"] != "research_only":
        raise ConfigValidationError("H1 v0.1 implementation_status must be research_only")
    if raw["schema_version"] != "h1-reflex-config-0.1":
        raise ConfigValidationError("unsupported H1 schema_version")
    if raw["spec_version"] != "H1-0.1":
        raise ConfigValidationError("unsupported H1 spec_version")
    if raw["provisional_label"] != "PROVISIONAL_H1_RESEARCH_ONLY":
        raise ConfigValidationError("H1 values must carry the provisional research label")

    try:
        grade_order = tuple(ExecutionGrade(str(value)) for value in raw["grade_order"])
    except (TypeError, ValueError) as error:
        raise ConfigValidationError("grade_order contains an unknown grade") from error
    if grade_order != tuple(ExecutionGrade):
        raise ConfigValidationError("grade_order must be miss, limited, strong, exceptional")

    profile_raw = _mapping(raw["timing_profiles"], "timing_profiles")
    if set(profile_raw) != {"precise", "assisted"}:
        raise ConfigValidationError("H1 requires exactly precise and assisted timing profiles")
    profiles: dict[str, TimingProfile] = {}
    for profile_id, profile_value in profile_raw.items():
        profile = _mapping(profile_value, f"timing_profiles.{profile_id}")
        _exact_keys(profile, {"assisted", "bands"}, f"timing_profiles.{profile_id}")
        if not isinstance(profile["assisted"], bool):
            raise ConfigValidationError(f"timing_profiles.{profile_id}.assisted must be boolean")
        bands_raw = profile["bands"]
        if not isinstance(bands_raw, list) or not bands_raw:
            raise ConfigValidationError(f"timing_profiles.{profile_id}.bands must be a list")
        bands: list[TimingBand] = []
        previous = -1
        seen: set[ExecutionGrade] = set()
        for index, band_value in enumerate(bands_raw):
            band = _mapping(band_value, f"timing_profiles.{profile_id}.bands[{index}]")
            _exact_keys(band, {"grade", "max_error"}, "timing band")
            try:
                grade = ExecutionGrade(str(band["grade"]))
            except ValueError as error:
                raise ConfigValidationError("timing band has an unknown grade") from error
            maximum = _non_negative_int(band["max_error"], "timing band max_error")
            if maximum <= previous or grade in seen:
                raise ConfigValidationError("timing bands must be strictly ordered and unique")
            previous = maximum
            seen.add(grade)
            bands.append(TimingBand(grade, maximum))
        if seen != set(ExecutionGrade):
            raise ConfigValidationError("each timing profile must define every grade")
        if tuple(band.grade for band in bands) != (
            ExecutionGrade.EXCEPTIONAL,
            ExecutionGrade.STRONG,
            ExecutionGrade.LIMITED,
            ExecutionGrade.MISS,
        ):
            raise ConfigValidationError(
                "timing bands must progress exceptional, strong, limited, miss"
            )
        profiles[profile_id] = TimingProfile(
            profile_id, bool(profile["assisted"]), tuple(bands)
        )
    if profiles["precise"].assisted or not profiles["assisted"].assisted:
        raise ConfigValidationError("precise/assisted profile markers are inconsistent")

    strategy = _mapping(raw["strategy_modifiers"], "strategy_modifiers")
    _exact_keys(
        strategy,
        {"prepared_error_bonus", "prepared_min_grade", "intent_error_penalty"},
        "strategy_modifiers",
    )
    prepared_bonus = _non_negative_int(
        strategy["prepared_error_bonus"], "prepared_error_bonus"
    )
    try:
        prepared_floor = ExecutionGrade(str(strategy["prepared_min_grade"]))
    except ValueError as error:
        raise ConfigValidationError("prepared_min_grade is unknown") from error
    intent_raw = _mapping(strategy["intent_error_penalty"], "intent_error_penalty")
    _exact_keys(intent_raw, {clarity.value for clarity in IntentClarity}, "intent_error_penalty")
    intent_penalties = MappingProxyType(
        {
            clarity: _non_negative_int(intent_raw[clarity.value], f"intent penalty {clarity.value}")
            for clarity in IntentClarity
        }
    )

    mitigation_raw = _mapping(raw["mitigation_basis_points"], "mitigation_basis_points")
    _exact_keys(mitigation_raw, {tier.value for tier in ReflexTier}, "mitigation_basis_points")
    mitigation = MappingProxyType(
        {
            tier: _grade_map(
                mitigation_raw[tier.value], f"mitigation_basis_points.{tier.value}", 10000
            )
            for tier in ReflexTier
        }
    )
    ordinary = _grade_map(raw["ordinary_exposure_damage"], "ordinary_exposure_damage")
    if any(ordinary.values()):
        raise ConfigValidationError("ordinary reflex attempts cannot add source exposure")

    risk = _mapping(raw["high_risk_exposure"], "high_risk_exposure")
    _exact_keys(risk, {"affected_source", "damage_by_grade"}, "high_risk_exposure")
    try:
        affected_source = Slot(str(risk["affected_source"]))
    except ValueError as error:
        raise ConfigValidationError("high-risk exposure source is not a body slot") from error
    if affected_source is not Slot.RIGHT_ARM:
        raise ConfigValidationError("H1 high-risk exposure must affect the blocking Right Arm")
    high_risk_damage = _grade_map(risk["damage_by_grade"], "high_risk damage")

    fixture_raw = _mapping(raw["fixture"], "fixture")
    fixture_keys = {
        "fixture_id",
        "incoming_action",
        "attacker_id",
        "attacker_source",
        "target",
        "blocking_source",
        "guard_action",
        "base_damage",
        "normal_torso_integrity",
        "threshold_torso_integrity",
    }
    _exact_keys(fixture_raw, fixture_keys, "fixture")
    try:
        fixture = H1FixtureConfig(
            fixture_id=str(fixture_raw["fixture_id"]),
            incoming_action=str(fixture_raw["incoming_action"]),
            attacker_id=str(fixture_raw["attacker_id"]),
            attacker_source=Slot(str(fixture_raw["attacker_source"])),
            target=Slot(str(fixture_raw["target"])),
            blocking_source=Slot(str(fixture_raw["blocking_source"])),
            guard_action=str(fixture_raw["guard_action"]),
            base_damage=_non_negative_int(fixture_raw["base_damage"], "fixture.base_damage"),
            normal_torso_integrity=_non_negative_int(
                fixture_raw["normal_torso_integrity"], "fixture.normal_torso_integrity"
            ),
            threshold_torso_integrity=_non_negative_int(
                fixture_raw["threshold_torso_integrity"], "fixture.threshold_torso_integrity"
            ),
        )
    except ValueError as error:
        raise ConfigValidationError(f"fixture contains an invalid body slot: {error}") from error
    if fixture.fixture_id != "H1-F0":
        raise ConfigValidationError("H1 v0.1 fixture_id must be H1-F0")
    if fixture.incoming_action != "surgical_jab" or fixture.attacker_id != "anna":
        raise ConfigValidationError("H1 fixture must reuse Anna's Surgical Jab")
    if fixture.attacker_source is not Slot.RIGHT_ARM or fixture.target is not Slot.TORSO:
        raise ConfigValidationError("H1 fixture source/target must remain Right Arm to Torso")
    if fixture.blocking_source is not Slot.RIGHT_ARM or fixture.guard_action != "guard_flesh":
        raise ConfigValidationError("H1 fixture must use Right-Arm Guard Flesh")
    if fixture.base_damage <= 0 or fixture.threshold_torso_integrity <= 0:
        raise ConfigValidationError("H1 fixture damage and threshold integrity must be positive")
    if fixture.threshold_torso_integrity >= fixture.normal_torso_integrity:
        raise ConfigValidationError("threshold Torso integrity must be below normal integrity")

    return H1Config(
        schema_version=str(raw["schema_version"]),
        spec_version=str(raw["spec_version"]),
        implementation_status=str(raw["implementation_status"]),
        provisional_label=str(raw["provisional_label"]),
        grade_order=grade_order,
        timing_profiles=MappingProxyType(profiles),
        prepared_error_bonus=prepared_bonus,
        prepared_min_grade=prepared_floor,
        intent_error_penalty=intent_penalties,
        mitigation_basis_points=mitigation,
        ordinary_exposure_damage=ordinary,
        high_risk_affected_source=affected_source,
        high_risk_exposure_damage=high_risk_damage,
        fixture=fixture,
    )
