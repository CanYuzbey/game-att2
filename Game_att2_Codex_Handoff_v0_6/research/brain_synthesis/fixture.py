"""Isolated diagnostic model for Brain/card ownership comparisons.

This module is research-only. It does not import, configure, or alter the production
simulator. Numeric values are neutral diagnostic fixtures, not game balance values.
"""

from __future__ import annotations

import random
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass
from enum import Enum


class Variant(str, Enum):
    OWNER_ORIGINAL = "owner_original"
    ACTIVE_DECK = "active_deck"
    SYNTHESIS = "synthesis"


class Origin(str, Enum):
    BODY = "body"
    TECHNIQUE = "technique"
    INVENTORY = "inventory"


class Timing(str, Enum):
    PREPARATION = "preparation"
    MAIN = "main"


class Category(str, Enum):
    ATTACK = "attack"
    DEFENCE = "defence"
    UTILITY = "utility"


class BrainLever(str, Enum):
    NONE = "none"
    ACCESS = "access"
    EXECUTION = "execution"


SOURCES = ("head", "torso", "left_arm", "right_arm", "legs", "core")


@dataclass(frozen=True)
class Card:
    card_id: str
    origin: Origin
    timing: Timing
    category: Category
    sources: tuple[str, ...]
    diagnostic_value: float = 1.0

    def is_legal(self, active_sources: set[str]) -> bool:
        return all(source in active_sources for source in self.sources)


@dataclass(frozen=True)
class BrainPart:
    part_id: str
    lever: BrainLever
    buff: float
    nerf: float
    favoured_category: Category | None = None
    disfavoured_category: Category | None = None

    def __post_init__(self) -> None:
        if self.lever is BrainLever.NONE:
            if self.buff != 0 or self.nerf != 0:
                raise ValueError("a no-op Brain Part cannot carry a buff or nerf")
            return
        if self.buff <= 0 or self.nerf <= 0:
            raise ValueError("a Brain Part requires both a positive buff and nerf")
        if self.lever is BrainLever.ACCESS and self.favoured_category is None:
            raise ValueError("an Access Brain Part requires a favoured category")

    def access_weight(self, card: Card) -> float:
        if self.lever is not BrainLever.ACCESS:
            return 1.0
        if card.category is self.favoured_category:
            return 1.0 + self.buff
        if self.disfavoured_category is not None and card.category is self.disfavoured_category:
            return max(0.05, 1.0 - self.nerf)
        return 1.0

    def evaluated_execution_delta(self, risk_weight: float) -> float:
        if self.lever is not BrainLever.EXECUTION:
            return 0.0
        return self.buff - (self.nerf * risk_weight)


NO_BRAIN = BrainPart("none", BrainLever.NONE, 0.0, 0.0)
ACCESS_BRAIN = BrainPart(
    "aggressive_attention_fixture",
    BrainLever.ACCESS,
    buff=0.60,
    nerf=0.35,
    favoured_category=Category.ATTACK,
    disfavoured_category=Category.DEFENCE,
)
EXECUTION_BRAIN = BrainPart(
    "paired_execution_fixture",
    BrainLever.EXECUTION,
    buff=0.25,
    nerf=0.25,
)


BODY_CARDS: tuple[Card, ...] = (
    Card("body_right_strike", Origin.BODY, Timing.MAIN, Category.ATTACK, ("right_arm",)),
    Card("body_left_guard", Origin.BODY, Timing.PREPARATION, Category.DEFENCE, ("left_arm",)),
    Card("body_legs_drive", Origin.BODY, Timing.MAIN, Category.UTILITY, ("legs",)),
    Card("body_core_surge", Origin.BODY, Timing.MAIN, Category.ATTACK, ("core",)),
    Card("body_torso_brace", Origin.BODY, Timing.PREPARATION, Category.DEFENCE, ("torso",)),
    Card("body_head_focus", Origin.BODY, Timing.PREPARATION, Category.UTILITY, ("head",)),
)

TECHNIQUE_CARDS: tuple[Card, ...] = (
    Card("tech_right_cut", Origin.TECHNIQUE, Timing.MAIN, Category.ATTACK, ("right_arm",)),
    Card("tech_left_counter", Origin.TECHNIQUE, Timing.MAIN, Category.DEFENCE, ("left_arm",)),
    Card("tech_legs_sweep", Origin.TECHNIQUE, Timing.MAIN, Category.UTILITY, ("legs",)),
    Card("tech_core_overdraw", Origin.TECHNIQUE, Timing.PREPARATION, Category.UTILITY, ("core",)),
    Card("tech_torso_cover", Origin.TECHNIQUE, Timing.PREPARATION, Category.DEFENCE, ("torso",)),
    Card("tech_head_read", Origin.TECHNIQUE, Timing.PREPARATION, Category.UTILITY, ("head",)),
)

ITEM_CARDS: tuple[Card, ...] = (
    Card("item_blood_bag", Origin.INVENTORY, Timing.PREPARATION, Category.UTILITY, ("left_arm",)),
    Card("item_clotting_cream", Origin.INVENTORY, Timing.PREPARATION, Category.UTILITY, ("left_arm",)),
)

ALL_BY_ID = {card.card_id: card for card in BODY_CARDS + TECHNIQUE_CARDS + ITEM_CARDS}

TECHNIQUE_PROFILES: dict[str, tuple[str, ...]] = {
    "balanced": ("tech_right_cut", "tech_left_counter", "tech_head_read"),
    "aggressive": ("tech_right_cut", "tech_legs_sweep", "tech_core_overdraw"),
    "defensive": ("tech_left_counter", "tech_torso_cover", "tech_head_read"),
}

ACTIVE_DECK_PROFILES: dict[str, tuple[str, ...]] = {
    "balanced": (
        "body_right_strike",
        "body_left_guard",
        "body_legs_drive",
        "tech_left_counter",
        "tech_core_overdraw",
        "tech_torso_cover",
    ),
    "aggressive": (
        "body_right_strike",
        "body_legs_drive",
        "body_core_surge",
        "tech_right_cut",
        "tech_legs_sweep",
        "tech_core_overdraw",
    ),
    "defensive": (
        "body_left_guard",
        "body_torso_brace",
        "body_head_focus",
        "tech_left_counter",
        "tech_torso_cover",
        "tech_head_read",
    ),
}


@dataclass(frozen=True)
class FixtureConfig:
    variant: Variant
    attention_slots: int = 3
    rounds: int = 6
    source_loss_round: int = 3
    lost_source: str = "right_arm"
    technique_profile: str = "balanced"
    technique_ids: tuple[str, ...] | None = None
    commitment_guarantee: bool = False
    item_uses_attention_slot: bool = True
    brain: BrainPart = NO_BRAIN

    def __post_init__(self) -> None:
        if self.attention_slots < 2:
            raise ValueError("the fixture requires at least two Attention Slots")
        if self.rounds < 1:
            raise ValueError("rounds must be positive")
        if self.source_loss_round < 1 or self.source_loss_round > self.rounds:
            raise ValueError("source_loss_round must occur inside the fixture")
        if self.lost_source not in SOURCES:
            raise ValueError(f"unknown source: {self.lost_source}")
        if self.technique_ids is None and self.technique_profile not in TECHNIQUE_PROFILES:
            raise ValueError(f"unknown technique profile: {self.technique_profile}")
        if self.technique_ids is not None:
            if len(set(self.technique_ids)) != len(self.technique_ids):
                raise ValueError("custom technique ids must be unique")
            valid_ids = {card.card_id for card in TECHNIQUE_CARDS}
            unknown = set(self.technique_ids) - valid_ids
            if unknown:
                raise ValueError(f"unknown technique cards: {sorted(unknown)}")

    @property
    def uses_readied_item_card(self) -> bool:
        return self.variant in {Variant.OWNER_ORIGINAL, Variant.SYNTHESIS}

    @property
    def action_slot_count(self) -> int:
        return self.attention_slots - int(
            self.uses_readied_item_card and self.item_uses_attention_slot
        )


def deck_for(config: FixtureConfig) -> tuple[Card, ...]:
    if config.variant is Variant.OWNER_ORIGINAL:
        return BODY_CARDS + TECHNIQUE_CARDS
    if config.variant is Variant.ACTIVE_DECK:
        return tuple(ALL_BY_ID[card_id] for card_id in ACTIVE_DECK_PROFILES[config.technique_profile])
    selected_ids = config.technique_ids or TECHNIQUE_PROFILES[config.technique_profile]
    selected = tuple(ALL_BY_ID[card_id] for card_id in selected_ids)
    return BODY_CARDS + selected


@dataclass
class RoundObservation:
    round_number: int
    legal_action_cards: int
    legal_main_cards: int
    legal_preparation_cards: int
    compatible_prep_main_pairs: int
    unique_sources: int
    attack_cards: int
    body_cards: int
    technique_cards: int
    item_card_visible: bool
    visible_options: int
    item_actions: int
    preparations_used: int
    mains_used: int
    invalid_action_attempts: int
    source_commitment_violations: int


@dataclass
class SessionResult:
    observations: list[RoundObservation]
    selection_counts: Counter[str]
    source_loss_removed: int
    execution_delta_if_risk_ignored: float
    execution_delta_if_risk_half_valued: float
    execution_delta_if_risk_fully_valued: float


class DiagnosticSession:
    def __init__(self, config: FixtureConfig, seed: int) -> None:
        self.config = config
        self.rng = random.Random(seed)
        self.active_sources = set(SOURCES)
        self.deck = deck_for(config)
        self.hand: list[Card | None] = [None] * config.action_slot_count
        self.item_card: Card | None = ITEM_CARDS[0] if config.uses_readied_item_card else None
        self.direct_inventory_visible = config.variant is Variant.ACTIVE_DECK
        self.item_uses: dict[str, int] = {card.card_id: 1 for card in ITEM_CARDS}
        self.draw_cycle: list[Card] = []
        self.selection_counts: Counter[str] = Counter()
        self.source_loss_removed = 0
        self._fill_empty_slots()

    def _eligible_deck(self) -> list[Card]:
        return [card for card in self.deck if card.is_legal(self.active_sources)]

    def _cards_in_hand(self) -> set[str]:
        return {card.card_id for card in self.hand if card is not None}

    def _weighted_choice(self, candidates: list[Card]) -> Card:
        weights = [self.config.brain.access_weight(card) for card in candidates]
        return self.rng.choices(candidates, weights=weights, k=1)[0]

    def _cycle_choice(self, candidates: list[Card]) -> Card:
        candidate_ids = {card.card_id for card in candidates}
        self.draw_cycle = [
            card
            for card in self.draw_cycle
            if card.card_id in candidate_ids and card.card_id not in self._cards_in_hand()
        ]
        if not self.draw_cycle:
            self.draw_cycle = list(candidates)
            self.rng.shuffle(self.draw_cycle)
        if self.config.brain.lever is BrainLever.ACCESS:
            weights = [self.config.brain.access_weight(card) for card in self.draw_cycle]
            chosen = self.rng.choices(self.draw_cycle, weights=weights, k=1)[0]
            self.draw_cycle.remove(chosen)
            return chosen
        return self.draw_cycle.pop()

    def _choose_for_slot(self, require_main: bool = False) -> Card | None:
        in_hand = self._cards_in_hand()
        candidates = [card for card in self._eligible_deck() if card.card_id not in in_hand]
        if require_main:
            candidates = [card for card in candidates if card.timing is Timing.MAIN]
        if not candidates:
            return None
        if self.config.variant is Variant.OWNER_ORIGINAL:
            return self._weighted_choice(candidates)
        return self._cycle_choice(candidates)

    def _fill_empty_slots(self) -> None:
        legal_main_present = any(
            card is not None
            and card.timing is Timing.MAIN
            and card.is_legal(self.active_sources)
            for card in self.hand
        )
        empty_indices = [index for index, card in enumerate(self.hand) if card is None]
        if self.config.commitment_guarantee and not legal_main_present and empty_indices:
            index = empty_indices.pop(0)
            card = self._choose_for_slot(require_main=True)
            if card is not None:
                self.hand[index] = card
                self.selection_counts[card.card_id] += 1
        for index in empty_indices:
            card = self._choose_for_slot()
            if card is not None:
                self.hand[index] = card
                self.selection_counts[card.card_id] += 1

    def _observe(self, round_number: int) -> RoundObservation:
        legal_cards = [
            card for card in self.hand if card is not None and card.is_legal(self.active_sources)
        ]
        sources = {source for card in legal_cards for source in card.sources}
        preparation_cards = [
            card for card in legal_cards if card.timing is Timing.PREPARATION
        ]
        main_cards = [card for card in legal_cards if card.timing is Timing.MAIN]
        compatible_pairs = sum(
            not (set(preparation.sources) & set(main.sources))
            for preparation in preparation_cards
            for main in main_cards
        )
        item_visible = (
            self.item_card is not None and self.item_card.is_legal(self.active_sources)
        ) or self.direct_inventory_visible
        visible_options = len(legal_cards) + int(item_visible)
        return RoundObservation(
            round_number=round_number,
            legal_action_cards=len(legal_cards),
            legal_main_cards=sum(card.timing is Timing.MAIN for card in legal_cards),
            legal_preparation_cards=sum(card.timing is Timing.PREPARATION for card in legal_cards),
            compatible_prep_main_pairs=compatible_pairs,
            unique_sources=len(sources),
            attack_cards=sum(card.category is Category.ATTACK for card in legal_cards),
            body_cards=sum(card.origin is Origin.BODY for card in legal_cards),
            technique_cards=sum(card.origin is Origin.TECHNIQUE for card in legal_cards),
            item_card_visible=item_visible,
            visible_options=visible_options,
            item_actions=0,
            preparations_used=0,
            mains_used=0,
            invalid_action_attempts=0,
            source_commitment_violations=0,
        )

    def _play_round(self, observation: RoundObservation) -> None:
        preparation_index = next(
            (
                index
                for index, card in enumerate(self.hand)
                if card is not None
                and card.is_legal(self.active_sources)
                and card.timing is Timing.PREPARATION
            ),
            None,
        )
        use_item = (
            observation.round_number == self.config.source_loss_round + 1
            and observation.item_card_visible
        )
        committed_sources: set[str] = set()
        if use_item:
            observation.preparations_used = 1
            observation.item_actions = 1
            if self.item_card is not None:
                committed_sources.update(self.item_card.sources)
                self.item_uses[self.item_card.card_id] -= 1
                self.item_card = None
        elif preparation_index is not None:
            observation.preparations_used = 1
            preparation_card = self.hand[preparation_index]
            if preparation_card is not None:
                committed_sources.update(preparation_card.sources)
            self.hand[preparation_index] = None

        main_index = next(
            (
                index
                for index, card in enumerate(self.hand)
                if card is not None
                and card.is_legal(self.active_sources)
                and card.timing is Timing.MAIN
                and not (set(card.sources) & committed_sources)
            ),
            None,
        )
        if main_index is not None:
            observation.mains_used = 1
            self.hand[main_index] = None

    def _apply_source_loss(self) -> None:
        self.active_sources.discard(self.config.lost_source)
        for index, card in enumerate(self.hand):
            if card is not None and not card.is_legal(self.active_sources):
                self.hand[index] = None
                self.source_loss_removed += 1
        if self.item_card is not None and not self.item_card.is_legal(self.active_sources):
            self.item_card = None

    def _decision_refresh(self) -> None:
        for index, card in enumerate(self.hand):
            if card is not None and not card.is_legal(self.active_sources):
                self.hand[index] = None
        self._fill_empty_slots()

    def run(self) -> SessionResult:
        observations: list[RoundObservation] = []
        for round_number in range(1, self.config.rounds + 1):
            observation = self._observe(round_number)
            self._play_round(observation)
            observations.append(observation)
            if round_number == self.config.source_loss_round:
                self._apply_source_loss()
            self._decision_refresh()

        return SessionResult(
            observations=observations,
            selection_counts=self.selection_counts,
            source_loss_removed=self.source_loss_removed,
            execution_delta_if_risk_ignored=self.config.brain.evaluated_execution_delta(0.0),
            execution_delta_if_risk_half_valued=self.config.brain.evaluated_execution_delta(0.5),
            execution_delta_if_risk_fully_valued=self.config.brain.evaluated_execution_delta(1.0),
        )


def run_session(config: FixtureConfig, seed: int) -> SessionResult:
    return DiagnosticSession(config, seed).run()


def validate_no_illegal_cards(result: SessionResult) -> bool:
    return all(observation.invalid_action_attempts == 0 for observation in result.observations)


def cards_by_origin(cards: Iterable[Card], origin: Origin) -> tuple[Card, ...]:
    return tuple(card for card in cards if card.origin is origin)
