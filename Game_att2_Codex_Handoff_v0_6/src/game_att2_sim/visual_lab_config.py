"""Validated configuration for the isolated visual interaction lab."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from itertools import pairwise
from pathlib import Path
from types import MappingProxyType
from typing import Any, cast

import yaml  # type: ignore[import-untyped]

from .errors import ConfigValidationError


@dataclass(frozen=True)
class VisualLabTimingBand:
    grade: str
    max_absolute_offset_ms: int


@dataclass(frozen=True)
class VisualLabTimingProfile:
    id: str
    assisted: bool
    bands: tuple[VisualLabTimingBand, ...]


@dataclass(frozen=True)
class VisualLabFixtureConfig:
    fixture_id: str
    incoming_action: str
    attacker_id: str
    attacker_source: str
    target: str
    blocking_source: str
    guard_action: str
    base_damage: int
    blocking_source_integrity: int
    normal_blood: int
    low_blood: int


@dataclass(frozen=True)
class VisualLabTelegraphConfig:
    duration_ms: int
    contact_ms: int
    practice_attempts_required: int
    recorded_order: tuple[str, ...]


@dataclass(frozen=True)
class ReadinessBandConfig:
    id: str
    minimum: int


@dataclass(frozen=True)
class VisualLabReadinessConfig:
    maximum: int
    bands: tuple[ReadinessBandConfig, ...]
    block_cost: int
    repeated_block_extra_cost: int
    low_blood_threshold: int
    low_blood_cost_multiplier_basis_points: int
    modest_recovery: int
    pressure_break_recovery: int
    menu_item_recovery: int

    def band_for(self, value: int) -> str:
        for band in self.bands:
            if value >= band.minimum:
                return band.id
        raise ConfigValidationError(f"readiness value {value} has no configured band")


@dataclass(frozen=True)
class VisualLabTimingConfig:
    profiles: Mapping[str, VisualLabTimingProfile]
    prepared_tolerance_bonus_ms: int
    vague_intent_penalty_ms: int
    repeated_block_penalty_ms: int
    low_blood_penalty_ms: int
    readiness_band_penalty_ms: Mapping[str, int]


@dataclass(frozen=True)
class VisualLabConfig:
    schema_version: str
    plan_version: str
    implementation_status: str
    provisional_label: str
    fixture: VisualLabFixtureConfig
    telegraph: VisualLabTelegraphConfig
    readiness: VisualLabReadinessConfig
    timing: VisualLabTimingConfig
    mitigation_basis_points: Mapping[str, int]
    high_risk_exposure_damage: Mapping[str, int]

    def profile(self, profile_id: str) -> VisualLabTimingProfile:
        try:
            return self.timing.profiles[profile_id]
        except KeyError as error:
            raise ConfigValidationError(f"unknown visual-lab timing profile: {profile_id}") from error


class _UniqueKeyLoader(yaml.SafeLoader):  # type: ignore[misc]
    pass


def _construct_unique_mapping(
    loader: _UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict[object, object]:
    mapping: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ConfigValidationError(f"duplicate visual-lab configuration key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def default_visual_lab_config_path() -> Path:
    return Path(__file__).resolve().parents[2] / "config" / "visual_lab_v0_1.yaml"


def _mapping(raw: object, label: str) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ConfigValidationError(f"{label} must be a mapping")
    return cast(dict[str, Any], raw)


def _exact_keys(raw: Mapping[str, Any], expected: set[str], label: str) -> None:
    if set(raw) != expected:
        raise ConfigValidationError(
            f"{label} keys mismatch; missing={sorted(expected - set(raw))}, "
            f"extra={sorted(set(raw) - expected)}"
        )


def _non_negative_int(raw: object, label: str) -> int:
    if not isinstance(raw, int) or isinstance(raw, bool) or raw < 0:
        raise ConfigValidationError(f"{label} must be a non-negative integer")
    return raw


def _positive_int(raw: object, label: str) -> int:
    value = _non_negative_int(raw, label)
    if value == 0:
        raise ConfigValidationError(f"{label} must be positive")
    return value


def _reject_prohibited_keys(value: object, path: str = "root") -> None:
    prohibited = {
        "wound",
        "wounds",
        "wound_to_blood",
        "ruined_torso",
        "warden",
        "encounter_3",
        "production_content",
        "movement",
        "dodge",
        "parry",
        "counter",
    }
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in prohibited:
                raise ConfigValidationError(f"prohibited visual-lab key at {path}: {key}")
            _reject_prohibited_keys(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_prohibited_keys(child, f"{path}[{index}]")


def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        loaded = yaml.load(path.read_text(encoding="utf-8"), Loader=_UniqueKeyLoader)
    except ConfigValidationError:
        raise
    except OSError as error:
        raise ConfigValidationError(f"cannot read {path}: {error}") from error
    except yaml.YAMLError as error:
        raise ConfigValidationError(f"invalid visual-lab YAML in {path}: {error}") from error
    return _mapping(loaded, "visual-lab configuration")


def _grade_map(raw: object, label: str, maximum: int | None = None) -> Mapping[str, int]:
    grades = ("miss", "limited", "strong", "exceptional")
    data = _mapping(raw, label)
    _exact_keys(data, set(grades), label)
    result: dict[str, int] = {}
    for grade in grades:
        value = _non_negative_int(data[grade], f"{label}.{grade}")
        if maximum is not None and value > maximum:
            raise ConfigValidationError(f"{label}.{grade} must be <= {maximum}")
        result[grade] = value
    return MappingProxyType(result)


def load_visual_lab_config(path: Path | None = None) -> VisualLabConfig:
    raw = _load_yaml(path or default_visual_lab_config_path())
    _reject_prohibited_keys(raw)
    _exact_keys(
        raw,
        {
            "schema_version",
            "plan_version",
            "implementation_status",
            "provisional_label",
            "fixture",
            "telegraph",
            "readiness",
            "timing",
            "mitigation_basis_points",
            "high_risk_exposure_damage",
        },
        "visual-lab root",
    )
    if raw["schema_version"] != "visual-lab-config-0.1":
        raise ConfigValidationError("unsupported visual-lab schema_version")
    if raw["plan_version"] != "VL-0.1":
        raise ConfigValidationError("unsupported visual-lab plan_version")
    if raw["implementation_status"] != "research_only":
        raise ConfigValidationError("visual-lab implementation_status must be research_only")
    if raw["provisional_label"] != "PROVISIONAL_VISUAL_LAB_ONLY":
        raise ConfigValidationError("visual-lab values must remain provisional")

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
        "blocking_source_integrity",
        "normal_blood",
        "low_blood",
    }
    _exact_keys(fixture_raw, fixture_keys, "fixture")
    fixture = VisualLabFixtureConfig(
        fixture_id=str(fixture_raw["fixture_id"]),
        incoming_action=str(fixture_raw["incoming_action"]),
        attacker_id=str(fixture_raw["attacker_id"]),
        attacker_source=str(fixture_raw["attacker_source"]),
        target=str(fixture_raw["target"]),
        blocking_source=str(fixture_raw["blocking_source"]),
        guard_action=str(fixture_raw["guard_action"]),
        base_damage=_positive_int(fixture_raw["base_damage"], "fixture.base_damage"),
        blocking_source_integrity=_positive_int(
            fixture_raw["blocking_source_integrity"], "fixture.blocking_source_integrity"
        ),
        normal_blood=_positive_int(fixture_raw["normal_blood"], "fixture.normal_blood"),
        low_blood=_positive_int(fixture_raw["low_blood"], "fixture.low_blood"),
    )
    if (
        fixture.fixture_id != "H1-F0"
        or fixture.incoming_action != "surgical_jab"
        or fixture.attacker_id != "anna"
        or fixture.attacker_source != "right_arm"
        or fixture.target != "torso"
        or fixture.blocking_source != "right_arm"
        or fixture.guard_action != "guard_flesh"
    ):
        raise ConfigValidationError("visual lab must reuse the exact H1-F0 Block fixture")

    telegraph_raw = _mapping(raw["telegraph"], "telegraph")
    _exact_keys(
        telegraph_raw,
        {"duration_ms", "contact_ms", "practice_attempts_required", "recorded_order"},
        "telegraph",
    )
    order_raw = telegraph_raw["recorded_order"]
    if not isinstance(order_raw, list) or any(value not in {"a", "b"} for value in order_raw):
        raise ConfigValidationError("telegraph.recorded_order must contain only a/b")
    telegraph = VisualLabTelegraphConfig(
        duration_ms=_positive_int(telegraph_raw["duration_ms"], "telegraph.duration_ms"),
        contact_ms=_positive_int(telegraph_raw["contact_ms"], "telegraph.contact_ms"),
        practice_attempts_required=_positive_int(
            telegraph_raw["practice_attempts_required"], "telegraph.practice_attempts_required"
        ),
        recorded_order=tuple(str(value) for value in order_raw),
    )
    if telegraph.contact_ms >= telegraph.duration_ms:
        raise ConfigValidationError("telegraph contact must occur before duration ends")
    if telegraph.recorded_order != ("a", "b", "b", "a"):
        raise ConfigValidationError("visual lab requires the counterbalanced a/b/b/a order")

    readiness_raw = _mapping(raw["readiness"], "readiness")
    readiness_keys = {
        "maximum",
        "bands",
        "block_cost",
        "repeated_block_extra_cost",
        "low_blood_threshold",
        "low_blood_cost_multiplier_basis_points",
        "modest_recovery",
        "pressure_break_recovery",
        "menu_item_recovery",
    }
    _exact_keys(readiness_raw, readiness_keys, "readiness")
    maximum = _positive_int(readiness_raw["maximum"], "readiness.maximum")
    bands_raw = readiness_raw["bands"]
    if not isinstance(bands_raw, list) or len(bands_raw) != 3:
        raise ConfigValidationError("readiness must define Ready, Strained, and Exhausted")
    bands: list[ReadinessBandConfig] = []
    for index, value in enumerate(bands_raw):
        band = _mapping(value, f"readiness.bands[{index}]")
        _exact_keys(band, {"id", "minimum"}, "readiness band")
        bands.append(
            ReadinessBandConfig(
                id=str(band["id"]),
                minimum=_non_negative_int(band["minimum"], "readiness band minimum"),
            )
        )
    if tuple(band.id for band in bands) != ("ready", "strained", "exhausted"):
        raise ConfigValidationError("readiness bands must be ready, strained, exhausted")
    if not (maximum >= bands[0].minimum > bands[1].minimum > bands[2].minimum == 0):
        raise ConfigValidationError("readiness band minimums must descend to zero")
    readiness = VisualLabReadinessConfig(
        maximum=maximum,
        bands=tuple(bands),
        block_cost=_positive_int(readiness_raw["block_cost"], "readiness.block_cost"),
        repeated_block_extra_cost=_non_negative_int(
            readiness_raw["repeated_block_extra_cost"],
            "readiness.repeated_block_extra_cost",
        ),
        low_blood_threshold=_positive_int(
            readiness_raw["low_blood_threshold"], "readiness.low_blood_threshold"
        ),
        low_blood_cost_multiplier_basis_points=_positive_int(
            readiness_raw["low_blood_cost_multiplier_basis_points"],
            "readiness.low_blood_cost_multiplier_basis_points",
        ),
        modest_recovery=_non_negative_int(
            readiness_raw["modest_recovery"], "readiness.modest_recovery"
        ),
        pressure_break_recovery=_non_negative_int(
            readiness_raw["pressure_break_recovery"], "readiness.pressure_break_recovery"
        ),
        menu_item_recovery=_non_negative_int(
            readiness_raw["menu_item_recovery"], "readiness.menu_item_recovery"
        ),
    )
    if readiness.low_blood_cost_multiplier_basis_points < 10000:
        raise ConfigValidationError("low-Blood multiplier cannot reduce readiness cost")
    if readiness.pressure_break_recovery <= readiness.modest_recovery:
        raise ConfigValidationError("pressure-break recovery must exceed modest recovery")
    if readiness.menu_item_recovery != 0:
        raise ConfigValidationError("menu/item use cannot restore readiness")

    timing_raw = _mapping(raw["timing"], "timing")
    timing_keys = {
        "profiles",
        "prepared_tolerance_bonus_ms",
        "vague_intent_penalty_ms",
        "repeated_block_penalty_ms",
        "low_blood_penalty_ms",
        "readiness_band_penalty_ms",
    }
    _exact_keys(timing_raw, timing_keys, "timing")
    profiles_raw = _mapping(timing_raw["profiles"], "timing.profiles")
    if set(profiles_raw) != {"precise", "assisted"}:
        raise ConfigValidationError("visual lab requires precise and assisted profiles")
    profiles: dict[str, VisualLabTimingProfile] = {}
    for profile_id, value in profiles_raw.items():
        profile_raw = _mapping(value, f"timing.profiles.{profile_id}")
        _exact_keys(profile_raw, {"assisted", "bands"}, "timing profile")
        if not isinstance(profile_raw["assisted"], bool):
            raise ConfigValidationError("timing profile assisted must be boolean")
        band_values = profile_raw["bands"]
        if not isinstance(band_values, list) or len(band_values) != 4:
            raise ConfigValidationError("each timing profile must define four grade bands")
        timing_bands: list[VisualLabTimingBand] = []
        for band_value in band_values:
            band = _mapping(band_value, "timing band")
            _exact_keys(band, {"grade", "max_absolute_offset_ms"}, "timing band")
            timing_bands.append(
                VisualLabTimingBand(
                    grade=str(band["grade"]),
                    max_absolute_offset_ms=_non_negative_int(
                        band["max_absolute_offset_ms"], "timing band maximum"
                    ),
                )
            )
        if tuple(band.grade for band in timing_bands) != (
            "exceptional",
            "strong",
            "limited",
            "miss",
        ):
            raise ConfigValidationError("timing bands must be exceptional, strong, limited, miss")
        maxima = tuple(band.max_absolute_offset_ms for band in timing_bands)
        if any(left >= right for left, right in pairwise(maxima)):
            raise ConfigValidationError("timing band maxima must be strictly increasing")
        profiles[profile_id] = VisualLabTimingProfile(
            profile_id,
            bool(profile_raw["assisted"]),
            tuple(timing_bands),
        )
    if profiles["precise"].assisted or not profiles["assisted"].assisted:
        raise ConfigValidationError("precise/assisted profile markers are inconsistent")
    penalties_raw = _mapping(
        timing_raw["readiness_band_penalty_ms"], "timing.readiness_band_penalty_ms"
    )
    _exact_keys(penalties_raw, {band.id for band in bands}, "readiness timing penalties")
    timing = VisualLabTimingConfig(
        profiles=MappingProxyType(profiles),
        prepared_tolerance_bonus_ms=_non_negative_int(
            timing_raw["prepared_tolerance_bonus_ms"], "prepared timing bonus"
        ),
        vague_intent_penalty_ms=_non_negative_int(
            timing_raw["vague_intent_penalty_ms"], "vague intent penalty"
        ),
        repeated_block_penalty_ms=_non_negative_int(
            timing_raw["repeated_block_penalty_ms"], "repeated Block penalty"
        ),
        low_blood_penalty_ms=_non_negative_int(
            timing_raw["low_blood_penalty_ms"], "low-Blood penalty"
        ),
        readiness_band_penalty_ms=MappingProxyType(
            {
                key: _non_negative_int(value, f"readiness penalty {key}")
                for key, value in penalties_raw.items()
            }
        ),
    )

    return VisualLabConfig(
        schema_version=str(raw["schema_version"]),
        plan_version=str(raw["plan_version"]),
        implementation_status=str(raw["implementation_status"]),
        provisional_label=str(raw["provisional_label"]),
        fixture=fixture,
        telegraph=telegraph,
        readiness=readiness,
        timing=timing,
        mitigation_basis_points=_grade_map(
            raw["mitigation_basis_points"], "mitigation_basis_points", 10000
        ),
        high_risk_exposure_damage=_grade_map(
            raw["high_risk_exposure_damage"], "high_risk_exposure_damage"
        ),
    )
