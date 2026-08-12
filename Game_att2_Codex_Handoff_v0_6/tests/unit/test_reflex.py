from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest

from game_att2_sim.enums import IntentClarity, Slot
from game_att2_sim.h1_config import load_h1_config
from game_att2_sim.reflex import (
    ExecutionGrade,
    ReflexAttempt,
    ReflexContext,
    ReflexTier,
    RiskClass,
    resolve_reflex,
)


def context(**overrides: object) -> ReflexContext:
    values: dict[str, object] = {
        "incoming_action": "surgical_jab",
        "attacking_source": Slot.RIGHT_ARM,
        "target_slot": Slot.TORSO,
        "blocking_source": Slot.RIGHT_ARM,
        "intent_clarity": IntentClarity.EXACT,
        "tier": ReflexTier.ROUTINE,
    }
    values.update(overrides)
    return ReflexContext(**values)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("error", "grade"),
    [
        (0, ExecutionGrade.EXCEPTIONAL),
        (40, ExecutionGrade.EXCEPTIONAL),
        (41, ExecutionGrade.STRONG),
        (90, ExecutionGrade.STRONG),
        (91, ExecutionGrade.LIMITED),
        (160, ExecutionGrade.LIMITED),
        (161, ExecutionGrade.MISS),
        (999, ExecutionGrade.MISS),
    ],
)
def test_precise_grade_boundaries(error: int, grade: ExecutionGrade) -> None:
    resolution = resolve_reflex(
        load_h1_config(), context(), ReflexAttempt("precise", error)
    )

    assert resolution.availability.legal
    assert resolution.grade is grade


def test_strategy_and_intent_change_grade_without_changing_input() -> None:
    config = load_h1_config()
    attempt = ReflexAttempt("precise", 120)

    vague = resolve_reflex(
        config,
        context(intent_clarity=IntentClarity.VAGUE),
        attempt,
    )
    prepared_exact = resolve_reflex(
        config,
        context(
            intent_clarity=IntentClarity.EXACT,
            tier=ReflexTier.SIGNIFICANT,
            prepared=True,
        ),
        attempt,
    )

    assert vague.grade is ExecutionGrade.MISS
    assert prepared_exact.grade is ExecutionGrade.STRONG
    assert prepared_exact.modifier.damage_reduction_basis_points > (
        vague.modifier.damage_reduction_basis_points
    )


@pytest.mark.parametrize(
    ("override", "reason"),
    [
        ({"attack_exists": False}, "incoming_action_missing"),
        ({"attacking_source_usable": False}, "attacking_source_unusable"),
        ({"telegraph_available": False}, "telegraph_unavailable"),
        ({"blocking_source_present": False}, "blocking_source_missing"),
        ({"blocking_source_usable": False}, "blocking_source_unusable"),
        ({"blocking_source_reachable": False}, "blocking_source_unreachable"),
        ({"blocking_source_compatible": False}, "blocking_source_incompatibly_committed"),
        ({"cost_affordable": False}, "required_cost_unaffordable"),
        ({"actor_downed": True}, "actor_downed"),
    ],
)
def test_illegal_state_rejects_exceptional_input(
    override: dict[str, object], reason: str
) -> None:
    result = resolve_reflex(
        load_h1_config(), context(**override), ReflexAttempt("precise", 0)
    )

    assert not result.availability.legal
    assert result.availability.reason == reason
    assert result.grade is None
    assert result.modifier.damage_reduction_basis_points == 0
    assert result.modifier.source_exposure_damage == 0


def test_ordinary_miss_adds_no_exposure() -> None:
    result = resolve_reflex(
        load_h1_config(), context(), ReflexAttempt("precise", 999)
    )

    assert result.grade is ExecutionGrade.MISS
    assert result.modifier.source_exposure_damage == 0
    assert result.modifier.exposed_source is None


def test_high_risk_requires_acknowledgement_before_input_is_accepted() -> None:
    result = resolve_reflex(
        load_h1_config(),
        context(tier=ReflexTier.CRITICAL),
        ReflexAttempt("precise", 999, RiskClass.HIGH_RISK),
    )

    assert not result.availability.legal
    assert result.availability.reason == "high_risk_not_acknowledged"
    assert result.grade is None


def test_acknowledged_high_risk_miss_exposes_only_right_arm() -> None:
    result = resolve_reflex(
        load_h1_config(),
        context(tier=ReflexTier.CRITICAL),
        ReflexAttempt("precise", 999, RiskClass.HIGH_RISK, True),
    )

    assert result.grade is ExecutionGrade.MISS
    assert result.modifier.exposed_source is Slot.RIGHT_ARM
    assert result.modifier.source_exposure_damage == 30


def test_assisted_profile_uses_same_legality_and_only_changes_grade() -> None:
    config = load_h1_config()
    precise = resolve_reflex(config, context(), ReflexAttempt("precise", 120))
    assisted = resolve_reflex(config, context(), ReflexAttempt("assisted", 120))

    assert precise.availability == assisted.availability
    assert precise.grade is ExecutionGrade.LIMITED
    assert assisted.grade is ExecutionGrade.STRONG
    assert precise.modifier.exposed_source == assisted.modifier.exposed_source


def test_reflex_contracts_are_immutable() -> None:
    attempt = ReflexAttempt("precise", 10)

    with pytest.raises(FrozenInstanceError):
        attempt.timing_error = 20  # type: ignore[misc]
