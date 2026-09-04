from __future__ import annotations

from .model import (
    ActionClass,
    BrainArchitecture,
    BrainSlot,
    Expression,
    Source,
    SourceState,
)


def prototype_sources() -> dict[str, Source]:
    return {
        "human_right_arm": Source("human_right_arm", SourceState.FULL, frozenset({"human", "precision"})),
        "minotaur_left_arm": Source("minotaur_left_arm", SourceState.FULL, frozenset({"monster", "heavy"})),
        "human_legs": Source("human_legs", SourceState.FULL, frozenset({"human", "mobility"})),
        "human_core": Source("human_core", SourceState.FULL, frozenset({"human", "physiology"})),
    }


def prototype_expressions() -> tuple[Expression, ...]:
    return (
        Expression(
            "human_jab",
            ActionClass.ATTACK,
            ("human_right_arm",),
            frozenset({"light", "precision"}),
            base_weight=1.0,
        ),
        Expression(
            "human_guard",
            ActionClass.DEFENCE,
            ("human_right_arm",),
            frozenset({"guard", "precision"}),
            base_weight=1.0,
        ),
        Expression(
            "minotaur_smash",
            ActionClass.ATTACK,
            ("minotaur_left_arm",),
            frozenset({"heavy", "high_damage"}),
            base_weight=2.0,
        ),
        Expression(
            "minotaur_brutal_guard",
            ActionClass.DEFENCE,
            ("minotaur_left_arm",),
            frozenset({"guard", "heavy"}),
            base_weight=1.15,
        ),
        Expression(
            "leg_kick",
            ActionClass.ATTACK,
            ("human_legs",),
            frozenset({"light", "mobility"}),
            base_weight=0.85,
        ),
        Expression(
            "brace",
            ActionClass.DEFENCE,
            ("human_legs",),
            frozenset({"guard", "anchor"}),
            base_weight=0.8,
        ),
        Expression(
            "blood_regulation",
            ActionClass.UTILITY,
            ("human_core",),
            frozenset({"physiology", "recovery"}),
            base_weight=1.0,
        ),
    )


def balanced_brain() -> BrainArchitecture:
    return BrainArchitecture(
        id="balanced_v3_fixture",
        slots=(
            BrainSlot("attack_1", ActionClass.ATTACK, True),
            BrainSlot("attack_2", ActionClass.ATTACK, True),
            BrainSlot("defence_1", ActionClass.DEFENCE, True),
            BrainSlot(
                "flex_1",
                None,
                False,
                flexible_weights={
                    ActionClass.ATTACK: 0.35,
                    ActionClass.DEFENCE: 0.30,
                    ActionClass.UTILITY: 0.35,
                },
            ),
        ),
    )


def aggressive_brain() -> BrainArchitecture:
    return BrainArchitecture(
        id="aggressive_v3_fixture",
        slots=(
            BrainSlot("attack_1", ActionClass.ATTACK, True, tag_biases={"heavy": 1.6}),
            BrainSlot("attack_2", ActionClass.ATTACK, True, tag_biases={"high_damage": 1.4}),
            BrainSlot("defence_1", ActionClass.DEFENCE, True),
            BrainSlot(
                "flex_1",
                None,
                False,
                flexible_weights={
                    ActionClass.ATTACK: 0.60,
                    ActionClass.DEFENCE: 0.20,
                    ActionClass.UTILITY: 0.20,
                },
                tag_biases={"heavy": 1.25},
            ),
        ),
    )
