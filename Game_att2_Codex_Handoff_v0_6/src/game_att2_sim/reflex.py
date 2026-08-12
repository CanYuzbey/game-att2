"""Pure H1 reflex contracts and deterministic resolution.

This module never mutates combat state, spends Blood, prints, uses RNG, or chooses an
encounter outcome. It converts already-recorded state facts and timing input into a
validated attack modifier for the shared rule engine.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

from .enums import IntentClarity, Slot

if TYPE_CHECKING:
    from .h1_config import H1Config


class ReflexTier(str, Enum):
    ROUTINE = "routine"
    SIGNIFICANT = "significant"
    CRITICAL = "critical"


class ExecutionGrade(str, Enum):
    MISS = "miss"
    LIMITED = "limited"
    STRONG = "strong"
    EXCEPTIONAL = "exceptional"


class RiskClass(str, Enum):
    ORDINARY = "ordinary"
    HIGH_RISK = "high_risk"


@dataclass(frozen=True)
class TimingBand:
    grade: ExecutionGrade
    max_error: int


@dataclass(frozen=True)
class TimingProfile:
    id: str
    assisted: bool
    bands: tuple[TimingBand, ...]


@dataclass(frozen=True)
class ReflexContext:
    incoming_action: str
    attacking_source: Slot
    target_slot: Slot
    blocking_source: Slot
    intent_clarity: IntentClarity
    tier: ReflexTier
    attack_exists: bool = True
    attack_blockable: bool = True
    attacking_source_usable: bool = True
    telegraph_available: bool = True
    blocking_source_present: bool = True
    blocking_source_usable: bool = True
    blocking_source_reachable: bool = True
    blocking_source_compatible: bool = True
    cost_affordable: bool = True
    actor_downed: bool = False
    prepared: bool = False


@dataclass(frozen=True)
class ReflexAttempt:
    profile_id: str
    timing_error: int
    risk_class: RiskClass = RiskClass.ORDINARY
    high_risk_acknowledged: bool = False


@dataclass(frozen=True)
class ReflexAvailability:
    legal: bool
    reason: str | None = None


@dataclass(frozen=True)
class AttackModifier:
    damage_reduction_basis_points: int = 0
    required_source: Slot | None = None
    exposed_source: Slot | None = None
    source_exposure_damage: int = 0
    grade: ExecutionGrade | None = None
    profile_id: str | None = None
    risk_class: RiskClass | None = None

    @classmethod
    def neutral(cls) -> AttackModifier:
        return cls()


@dataclass(frozen=True)
class ReflexResolution:
    availability: ReflexAvailability
    grade: ExecutionGrade | None
    modifier: AttackModifier
    raw_timing_error: int
    effective_timing_error: int | None
    profile_id: str
    risk_class: RiskClass


def check_reflex_availability(
    context: ReflexContext, attempt: ReflexAttempt
) -> ReflexAvailability:
    checks = (
        (context.attack_exists, "incoming_action_missing"),
        (context.attack_blockable, "incoming_action_not_blockable"),
        (context.attacking_source_usable, "attacking_source_unusable"),
        (context.telegraph_available, "telegraph_unavailable"),
        (context.blocking_source_present, "blocking_source_missing"),
        (context.blocking_source_usable, "blocking_source_unusable"),
        (context.blocking_source_reachable, "blocking_source_unreachable"),
        (context.blocking_source_compatible, "blocking_source_incompatibly_committed"),
        (context.cost_affordable, "required_cost_unaffordable"),
        (not context.actor_downed, "actor_downed"),
    )
    for legal, reason in checks:
        if not legal:
            return ReflexAvailability(False, reason)
    if attempt.timing_error < 0:
        return ReflexAvailability(False, "negative_timing_error")
    if attempt.risk_class is RiskClass.HIGH_RISK and not attempt.high_risk_acknowledged:
        return ReflexAvailability(False, "high_risk_not_acknowledged")
    return ReflexAvailability(True)


def _grade_for_error(profile: TimingProfile, error: int) -> ExecutionGrade:
    for band in profile.bands:
        if error <= band.max_error:
            return band.grade
    return ExecutionGrade.MISS


def _raise_to_floor(
    grade: ExecutionGrade,
    floor: ExecutionGrade,
    grade_order: tuple[ExecutionGrade, ...],
) -> ExecutionGrade:
    if grade_order.index(grade) >= grade_order.index(floor):
        return grade
    return floor


def resolve_reflex(
    config: H1Config,
    context: ReflexContext,
    attempt: ReflexAttempt,
) -> ReflexResolution:
    """Resolve legality and timing into a state modifier without mutating state."""
    availability = check_reflex_availability(context, attempt)
    if not availability.legal:
        return ReflexResolution(
            availability=availability,
            grade=None,
            modifier=AttackModifier.neutral(),
            raw_timing_error=attempt.timing_error,
            effective_timing_error=None,
            profile_id=attempt.profile_id,
            risk_class=attempt.risk_class,
        )

    profile = config.profile(attempt.profile_id)
    effective_error = max(
        0,
        attempt.timing_error
        + config.intent_error_penalty[context.intent_clarity]
        - (config.prepared_error_bonus if context.prepared else 0),
    )
    grade = _grade_for_error(profile, effective_error)
    if context.prepared:
        grade = _raise_to_floor(grade, config.prepared_min_grade, config.grade_order)

    exposure = config.ordinary_exposure_damage[grade]
    exposed_source: Slot | None = None
    if attempt.risk_class is RiskClass.HIGH_RISK:
        exposure = config.high_risk_exposure_damage[grade]
        exposed_source = config.high_risk_affected_source

    modifier = AttackModifier(
        damage_reduction_basis_points=config.mitigation_basis_points[context.tier][grade],
        required_source=context.blocking_source,
        exposed_source=exposed_source,
        source_exposure_damage=exposure,
        grade=grade,
        profile_id=profile.id,
        risk_class=attempt.risk_class,
    )
    return ReflexResolution(
        availability=availability,
        grade=grade,
        modifier=modifier,
        raw_timing_error=attempt.timing_error,
        effective_timing_error=effective_error,
        profile_id=profile.id,
        risk_class=attempt.risk_class,
    )
