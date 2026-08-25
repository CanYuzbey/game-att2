from __future__ import annotations

import unittest

from assessor import (
    CardSpec,
    DeckExchange,
    apply_exchange_atomic,
    assess_catalog,
    generate_covering_cases,
    interaction_coverage,
)


def card(
    card_id: str,
    source: str,
    effect: str,
    signature: str,
    benefits: tuple[float, ...],
    burdens: tuple[float, ...],
    *,
    label: str = "attack",
    cost: str = "commit_source",
    risk: str = "interceptable",
) -> CardSpec:
    return CardSpec(
        card_id=card_id,
        sources=(source,),
        timing="main",
        labels=frozenset({label}),
        effect_atoms=frozenset({effect}),
        cost_atoms=frozenset({cost}),
        risk_atoms=frozenset({risk}),
        target_mode="aimed_limb",
        reflex_mode="bounded_intercept",
        signature_atoms=frozenset({signature}),
        benefits=benefits,
        burdens=burdens,
    )


class ScalingGuardrailTests(unittest.TestCase):
    def setUp(self) -> None:
        self.leg_defence = card(
            "leg_defence",
            "legs",
            "brace",
            "brace",
            (0.0, 2.0),
            (0.0, 1.0),
            label="defence",
            risk="rooted",
        )
        self.left_defence = card(
            "left_defence",
            "left_arm",
            "cover",
            "cover",
            (0.0, 1.5),
            (0.0, 0.5),
            label="defence",
            risk="source_exposed",
        )
        self.left_brutal = card(
            "left_brutal",
            "left_arm",
            "heavy_wound",
            "heavy_wound",
            (2.5, 0.0),
            (1.0, 2.0),
            cost="blood_cost",
            risk="defence_loss",
        )
        self.right_brutal = card(
            "right_brutal",
            "right_arm",
            "break_guard",
            "break_guard",
            (2.0, 0.0),
            (0.5, 2.5),
            cost="recovery_commitment",
            risk="source_exposed",
        )
        self.cards = (
            self.leg_defence,
            self.left_defence,
            self.left_brutal,
            self.right_brutal,
        )
        self.by_id = {candidate.card_id: candidate for candidate in self.cards}
        self.exchange = DeckExchange(
            "aggressive_conversion",
            ("leg_defence", "left_defence"),
            ("left_brutal", "right_brutal"),
        )

    def test_valid_catalog_has_no_blockers(self) -> None:
        findings = assess_catalog(self.cards, (self.exchange,))
        self.assertFalse([finding for finding in findings if finding.severity == "BLOCKER"])

    def test_free_exchange_is_blocked(self) -> None:
        findings = assess_catalog(
            self.cards,
            (DeckExchange("free_power", (), ("right_brutal",), allow_size_change=True),),
        )
        self.assertIn("FREE_OR_EMPTY_EXCHANGE", {finding.code for finding in findings})

    def test_exchange_is_atomic_when_a_sacrifice_is_missing(self) -> None:
        active = ("leg_defence",)
        result = apply_exchange_atomic(
            active,
            self.exchange,
            self.by_id,
            {"legs", "left_arm", "right_arm"},
        )
        self.assertEqual(result, active)

    def test_exchange_is_atomic_when_a_gain_source_is_missing(self) -> None:
        active = ("leg_defence", "left_defence")
        result = apply_exchange_atomic(
            active,
            self.exchange,
            self.by_id,
            {"legs", "left_arm"},
        )
        self.assertEqual(result, active)

    def test_exchange_cannot_pay_with_a_dormant_sacrifice(self) -> None:
        active = ("leg_defence", "left_defence")
        result = apply_exchange_atomic(
            active,
            self.exchange,
            self.by_id,
            {"left_arm", "right_arm"},
        )
        self.assertEqual(result, active)

    def test_exchange_applies_when_every_cost_and_source_is_valid(self) -> None:
        active = ("leg_defence", "left_defence")
        result = apply_exchange_atomic(
            active,
            self.exchange,
            self.by_id,
            {"legs", "left_arm", "right_arm"},
        )
        self.assertEqual(result, ("left_brutal", "right_brutal"))

    def test_near_duplicate_is_detected(self) -> None:
        duplicate = card(
            "duplicate",
            "other_arm",
            "heavy_wound",
            "heavy_wound",
            (2.5, 0.0),
            (1.0, 2.0),
            cost="blood_cost",
            risk="defence_loss",
        )
        findings = assess_catalog((self.left_brutal, duplicate), ())
        self.assertIn("NEAR_DUPLICATE", {finding.code for finding in findings})

    def test_pareto_dominance_is_detected(self) -> None:
        worse = card(
            "worse",
            "left_arm",
            "light_wound",
            "light_wound",
            (1.0, 0.0),
            (2.0, 3.0),
            cost="blood_cost",
            risk="long_recovery",
        )
        findings = assess_catalog((self.left_brutal, worse), ())
        self.assertIn("PARETO_DOMINANCE", {finding.code for finding in findings})

    def test_pairwise_generator_covers_every_pair(self) -> None:
        factors = {
            "brain": ("none", "attack_bias", "defence_bias"),
            "deck": ("balanced", "aggressive"),
            "source_state": ("intact", "disabled"),
            "reflex": ("none", "automatic", "prepared"),
        }
        cases = generate_covering_cases(factors, strength=2)
        exhaustive_count = 3 * 2 * 2 * 3
        self.assertLess(len(cases), exhaustive_count)
        self.assertEqual(interaction_coverage(cases, factors, strength=2), 1.0)

    def test_covering_generator_is_deterministic(self) -> None:
        factors = {"deck": ("a", "b"), "brain": ("x", "y"), "source": ("on", "off")}
        self.assertEqual(
            generate_covering_cases(factors, strength=2),
            generate_covering_cases(factors, strength=2),
        )

    def test_constrained_covering_model_ignores_impossible_interactions(self) -> None:
        factors = {
            "deck": ("aggressive", "defensive"),
            "source": ("armed", "armless"),
            "card": ("arm_attack", "retreat"),
        }

        def valid(case: dict[str, str]) -> bool:
            return not (case["source"] == "armless" and case["card"] == "arm_attack")

        cases = generate_covering_cases(factors, strength=2, valid=valid)
        self.assertEqual(interaction_coverage(cases, factors, strength=2, valid=valid), 1.0)
        self.assertTrue(all(valid(case) for case in cases))


if __name__ == "__main__":
    unittest.main()
