from __future__ import annotations

from game_att2_v3.attention import AttentionResolver
from game_att2_v3.fixtures import balanced_brain, prototype_expressions, prototype_sources
from game_att2_v3.hand import AttentionHand
from game_att2_v3.model import AttentionHistory, Source, SourceState
from game_att2_v3.rng import SeededRNG


def make_hand() -> tuple[AttentionHand, AttentionHistory]:
    hand = AttentionHand()
    history = AttentionHistory()
    hand.decision_refresh(
        balanced_brain(),
        prototype_expressions(),
        prototype_sources(),
        history,
        SeededRNG(42),
        AttentionResolver(),
    )
    return hand, history


def test_unused_legal_cards_persist_across_decision_refresh() -> None:
    hand, history = make_hand()
    before = dict(hand.selections)
    hand.decision_refresh(
        balanced_brain(),
        prototype_expressions(),
        prototype_sources(),
        history,
        SeededRNG(99),
        AttentionResolver(),
    )
    assert hand.selections == before


def test_played_slot_waits_until_explicit_refresh_then_refills() -> None:
    hand, history = make_hand()
    hand.play("attack_1")
    assert "attack_1" not in hand.selections
    assert hand.open_reasons["attack_1"] == "spent"
    hand.decision_refresh(
        balanced_brain(),
        prototype_expressions(),
        prototype_sources(),
        history,
        SeededRNG(100),
        AttentionResolver(),
    )
    assert "attack_1" in hand.selections


def test_drop_does_not_instantly_fish_replacement() -> None:
    hand, _history = make_hand()
    hand.drop("attack_1")
    assert "attack_1" not in hand.selections
    assert hand.open_reasons["attack_1"] == "dropped"


def test_source_invalidation_removes_held_card_without_mid_exchange_replacement() -> None:
    hand, _history = make_hand()
    expression_by_id = {e.id: e for e in prototype_expressions()}
    target_slot = next(
        slot_id
        for slot_id, selection in hand.selections.items()
        if selection.expression_id in {"minotaur_smash", "minotaur_brutal_guard"}
    )
    sources = prototype_sources()
    sources["minotaur_left_arm"] = Source("minotaur_left_arm", SourceState.OFFLINE)
    invalidated = hand.revalidate(expression_by_id, sources)
    assert target_slot in invalidated
    assert target_slot not in hand.selections
    assert hand.open_reasons[target_slot] == "source_invalidated"
