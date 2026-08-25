from __future__ import annotations

import unittest

from fixture import (
    ACCESS_BRAIN,
    ALL_BY_ID,
    EXECUTION_BRAIN,
    NO_BRAIN,
    BrainLever,
    BrainPart,
    Category,
    DiagnosticSession,
    FixtureConfig,
    Origin,
    Variant,
    deck_for,
    run_session,
)


class DiagnosticFixtureTests(unittest.TestCase):
    def test_same_seed_is_deterministic(self) -> None:
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=4,
            commitment_guarantee=True,
            brain=EXECUTION_BRAIN,
        )
        self.assertEqual(run_session(config, 42), run_session(config, 42))

    def test_source_loss_never_allows_invalid_action_attempt(self) -> None:
        for variant in Variant:
            with self.subTest(variant=variant.value):
                config = FixtureConfig(
                    variant,
                    attention_slots=4,
                    commitment_guarantee=variant is not Variant.ACTIVE_DECK,
                    brain=ACCESS_BRAIN if variant is Variant.OWNER_ORIGINAL else EXECUTION_BRAIN,
                )
                result = run_session(config, 7)
                self.assertTrue(
                    all(
                        observation.invalid_action_attempts == 0
                        for observation in result.observations
                    )
                )

    def test_synthesis_contains_all_body_core_and_only_selected_techniques(self) -> None:
        config = FixtureConfig(Variant.SYNTHESIS, technique_profile="balanced")
        deck = deck_for(config)
        body_ids = {card.card_id for card in deck if card.origin is Origin.BODY}
        technique_ids = {card.card_id for card in deck if card.origin is Origin.TECHNIQUE}
        self.assertEqual(len(body_ids), 6)
        self.assertEqual(
            technique_ids,
            {"tech_right_cut", "tech_left_counter", "tech_head_read"},
        )

    def test_custom_technique_package_is_validated_and_used(self) -> None:
        ids = ("tech_right_cut", "tech_torso_cover")
        config = FixtureConfig(Variant.SYNTHESIS, technique_ids=ids)
        technique_ids = {
            card.card_id for card in deck_for(config) if card.origin is Origin.TECHNIQUE
        }
        self.assertEqual(technique_ids, set(ids))
        with self.assertRaises(ValueError):
            FixtureConfig(
                Variant.SYNTHESIS,
                technique_ids=("tech_right_cut", "tech_right_cut"),
            )

    def test_item_card_is_visible_but_not_in_synthesis_draw_deck(self) -> None:
        config = FixtureConfig(Variant.SYNTHESIS, attention_slots=3)
        self.assertTrue(all(card.origin is not Origin.INVENTORY for card in deck_for(config)))
        result = run_session(config, 1)
        self.assertTrue(all(observation.item_card_visible for observation in result.observations[:4]))
        self.assertTrue(
            all(not observation.item_card_visible for observation in result.observations[4:])
        )

    def test_used_readied_item_does_not_auto_ready_the_next_inventory_item(self) -> None:
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=4,
            commitment_guarantee=True,
        )
        result = run_session(config, 4)
        self.assertEqual(sum(o.item_actions for o in result.observations), 1)
        self.assertTrue(all(not o.item_card_visible for o in result.observations[4:]))

    def test_separate_readied_item_lane_does_not_reduce_attention_capacity(self) -> None:
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=4,
            item_uses_attention_slot=False,
        )
        result = run_session(config, 11)
        self.assertTrue(
            all(observation.legal_action_cards <= 4 for observation in result.observations)
        )
        self.assertEqual(config.action_slot_count, 4)

    def test_active_deck_inventory_is_direct_not_a_card_slot(self) -> None:
        config = FixtureConfig(Variant.ACTIVE_DECK, attention_slots=3)
        result = run_session(config, 2)
        self.assertTrue(all(observation.item_card_visible for observation in result.observations))
        self.assertTrue(
            all(observation.legal_action_cards <= 3 for observation in result.observations)
        )

    def test_action_budget_never_exceeds_one_preparation_main_or_item(self) -> None:
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=4,
            commitment_guarantee=True,
            brain=EXECUTION_BRAIN,
        )
        result = run_session(config, 3)
        for observation in result.observations:
            self.assertLessEqual(observation.preparations_used, 1)
            self.assertLessEqual(observation.mains_used, 1)
            self.assertLessEqual(observation.item_actions, 1)
            self.assertLessEqual(observation.item_actions, observation.preparations_used)
            self.assertEqual(observation.source_commitment_violations, 0)

    def test_preparation_cannot_double_commit_its_source_to_main(self) -> None:
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=3,
            commitment_guarantee=False,
        )
        session = DiagnosticSession(config, 5)
        session.hand = [
            ALL_BY_ID["body_left_guard"],
            ALL_BY_ID["tech_left_counter"],
        ]
        session.item_card = None
        observation = session._observe(1)
        self.assertEqual(observation.compatible_prep_main_pairs, 0)
        session._play_round(observation)
        self.assertEqual(observation.preparations_used, 1)
        self.assertEqual(observation.mains_used, 0)

    def test_item_card_becomes_unavailable_when_its_exact_source_is_lost(self) -> None:
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=4,
            commitment_guarantee=True,
            lost_source="left_arm",
            brain=EXECUTION_BRAIN,
        )
        result = run_session(config, 3)
        self.assertTrue(all(o.item_card_visible for o in result.observations[:3]))
        self.assertTrue(all(not o.item_card_visible for o in result.observations[3:]))

    def test_commitment_guarantee_keeps_a_main_when_one_is_legal(self) -> None:
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=3,
            commitment_guarantee=True,
            brain=EXECUTION_BRAIN,
        )
        for seed in range(100):
            with self.subTest(seed=seed):
                result = run_session(config, seed)
                self.assertTrue(
                    all(observation.legal_main_cards >= 1 for observation in result.observations)
                )

    def test_execution_brain_is_balanced_only_when_nerf_is_valued(self) -> None:
        self.assertGreater(EXECUTION_BRAIN.evaluated_execution_delta(0.0), 0)
        self.assertGreater(EXECUTION_BRAIN.evaluated_execution_delta(0.5), 0)
        self.assertEqual(EXECUTION_BRAIN.evaluated_execution_delta(1.0), 0)

    def test_brain_part_requires_paired_buff_and_nerf(self) -> None:
        with self.assertRaises(ValueError):
            BrainPart("bad", BrainLever.EXECUTION, buff=0.25, nerf=0.0)

    def test_access_brain_has_visible_opposed_categories(self) -> None:
        self.assertIs(ACCESS_BRAIN.favoured_category, Category.ATTACK)
        self.assertIs(ACCESS_BRAIN.disfavoured_category, Category.DEFENCE)

    def test_access_brain_changes_synthesis_selection_distribution(self) -> None:
        no_brain_attack_draws = 0
        access_brain_attack_draws = 0
        attack_ids = {"body_right_strike", "body_core_surge", "tech_right_cut"}
        for seed in range(500):
            base = run_session(
                FixtureConfig(
                    Variant.SYNTHESIS,
                    attention_slots=4,
                    commitment_guarantee=True,
                    brain=NO_BRAIN,
                ),
                seed,
            )
            access = run_session(
                FixtureConfig(
                    Variant.SYNTHESIS,
                    attention_slots=4,
                    commitment_guarantee=True,
                    brain=ACCESS_BRAIN,
                ),
                seed,
            )
            no_brain_attack_draws += sum(base.selection_counts[card_id] for card_id in attack_ids)
            access_brain_attack_draws += sum(
                access.selection_counts[card_id] for card_id in attack_ids
            )
        self.assertGreater(access_brain_attack_draws, no_brain_attack_draws)


if __name__ == "__main__":
    unittest.main()
