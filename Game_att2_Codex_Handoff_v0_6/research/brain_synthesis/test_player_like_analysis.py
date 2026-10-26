from __future__ import annotations

import unittest

from fixture import ACCESS_BRAIN, FixtureConfig, Variant
from player_like_analysis import (
    PERSONAS,
    PersonaSession,
    _plan_cards,
    category_distance,
    fuzz_state_invariants,
    run_persona_batch,
    search_technique_packages,
)


class PlayerLikeAnalysisTests(unittest.TestCase):
    def test_persona_session_is_deterministic(self) -> None:
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=4,
            commitment_guarantee=False,
            item_uses_attention_slot=False,
            brain=ACCESS_BRAIN,
        )
        left = PersonaSession(config, 42, PERSONAS[0])
        right = PersonaSession(config, 42, PERSONAS[0])
        self.assertEqual(left.run(), right.run())
        self.assertEqual(left.decisions, right.decisions)

    def test_selected_preparation_and_main_never_share_a_source(self) -> None:
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=4,
            commitment_guarantee=False,
            item_uses_attention_slot=False,
            brain=ACCESS_BRAIN,
        )
        for persona in PERSONAS:
            session = PersonaSession(config, 8, persona)
            for plan in session.legal_plans():
                cards = _plan_cards(session.hand, plan, session.item_card)
                sources = [source for card in cards for source in card.sources]
                self.assertEqual(len(sources), len(set(sources)))

    def test_package_search_covers_all_two_three_and_four_card_combinations(self) -> None:
        rows, three_card_packages = search_technique_packages(2)
        self.assertEqual([row.package_count for row in rows], [15, 20, 15])
        self.assertGreater(len(three_card_packages), 0)

    def test_personas_produce_distinct_category_distributions(self) -> None:
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=4,
            commitment_guarantee=False,
            item_uses_attention_slot=False,
            brain=ACCESS_BRAIN,
        )
        bruiser = run_persona_batch(PERSONAS[0], [config], 100)
        survivor = run_persona_batch(PERSONAS[1], [config], 100)
        self.assertGreater(category_distance(bruiser, survivor), 5.0)

    def test_generated_state_machine_cases_preserve_invariants(self) -> None:
        result = fuzz_state_invariants(500)
        self.assertEqual(result.invariant_failures, 0)


if __name__ == "__main__":
    unittest.main()
