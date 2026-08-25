"""Deterministic research-only guardrails for anatomical card scaling.

This module does not import or alter the production simulator.  Its default limits
are diagnostic proposal values, not approved card counts or balance thresholds.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from itertools import combinations, product


@dataclass(frozen=True)
class GuardrailConfig:
    """Provisional limits used to reject risky content before play simulation."""

    max_cards_per_source: int = 5
    max_labels_per_card: int = 3
    max_mechanic_atoms_per_card: int = 6
    max_signature_atoms_per_card: int = 1
    max_special_cards_per_exchange: int = 2
    near_duplicate_similarity: float = 0.82


@dataclass(frozen=True)
class CardSpec:
    card_id: str
    sources: tuple[str, ...]
    timing: str
    labels: frozenset[str]
    effect_atoms: frozenset[str]
    cost_atoms: frozenset[str]
    risk_atoms: frozenset[str]
    target_mode: str
    reflex_mode: str
    signature_atoms: frozenset[str]
    benefits: tuple[float, ...]
    burdens: tuple[float, ...]

    @property
    def mechanic_atoms(self) -> frozenset[str]:
        atoms = {
            f"timing:{self.timing}",
            f"target:{self.target_mode}",
            f"reflex:{self.reflex_mode}",
        }
        atoms.update(f"effect:{atom}" for atom in self.effect_atoms)
        atoms.update(f"cost:{atom}" for atom in self.cost_atoms)
        atoms.update(f"risk:{atom}" for atom in self.risk_atoms)
        return frozenset(atoms)

    @property
    def declared_atoms(self) -> frozenset[str]:
        return self.effect_atoms | self.cost_atoms | self.risk_atoms


@dataclass(frozen=True)
class DeckExchange:
    exchange_id: str
    remove_card_ids: tuple[str, ...]
    add_card_ids: tuple[str, ...]
    allow_size_change: bool = False


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    subject: str
    message: str


def jaccard_similarity(left: frozenset[str], right: frozenset[str]) -> float:
    union = left | right
    if not union:
        return 1.0
    return len(left & right) / len(union)


def _dominates(left: CardSpec, right: CardSpec) -> bool:
    if len(left.benefits) != len(right.benefits):
        return False
    if len(left.burdens) != len(right.burdens):
        return False
    benefits_no_worse = all(a >= b for a, b in zip(left.benefits, right.benefits))
    burdens_no_worse = all(a <= b for a, b in zip(left.burdens, right.burdens))
    strictly_better = any(a > b for a, b in zip(left.benefits, right.benefits)) or any(
        a < b for a, b in zip(left.burdens, right.burdens)
    )
    return benefits_no_worse and burdens_no_worse and strictly_better


def assess_catalog(
    cards: Sequence[CardSpec],
    exchanges: Sequence[DeckExchange],
    config: GuardrailConfig | None = None,
) -> tuple[Finding, ...]:
    """Run deterministic static gates over cards and Concept Deck exchanges."""

    config = config or GuardrailConfig()
    findings: list[Finding] = []
    by_id: dict[str, CardSpec] = {}
    source_counts: dict[str, int] = {}

    for card in cards:
        if card.card_id in by_id:
            findings.append(
                Finding("BLOCKER", "DUPLICATE_ID", card.card_id, "Card id is not unique.")
            )
            continue
        by_id[card.card_id] = card
        for source in card.sources:
            source_counts[source] = source_counts.get(source, 0) + 1
        if not card.sources or any(not source for source in card.sources):
            findings.append(
                Finding(
                    "BLOCKER",
                    "MISSING_SOURCE",
                    card.card_id,
                    "Card has no valid exact source set.",
                )
            )
        if len(set(card.sources)) != len(card.sources):
            findings.append(
                Finding(
                    "BLOCKER",
                    "DUPLICATE_SOURCE",
                    card.card_id,
                    "A source may appear only once in a card's exact source set.",
                )
            )
        if not card.labels:
            findings.append(
                Finding("HIGH", "MISSING_LABEL", card.card_id, "Card has no authored label.")
            )
        if len(card.labels) > config.max_labels_per_card:
            findings.append(
                Finding(
                    "HIGH",
                    "LABEL_OVERLOAD",
                    card.card_id,
                    f"Card has {len(card.labels)} labels; limit is {config.max_labels_per_card}.",
                )
            )
        if len(card.mechanic_atoms) > config.max_mechanic_atoms_per_card:
            findings.append(
                Finding(
                    "HIGH",
                    "MECHANIC_OVERLOAD",
                    card.card_id,
                    "Card carries too many independent mechanical atoms.",
                )
            )
        if len(card.signature_atoms) != config.max_signature_atoms_per_card:
            findings.append(
                Finding(
                    "HIGH",
                    "SIGNATURE_BUDGET",
                    card.card_id,
                    "A card must declare exactly one signature creativity atom.",
                )
            )
        if not card.signature_atoms <= card.declared_atoms:
            findings.append(
                Finding(
                    "BLOCKER",
                    "DECORATIVE_SIGNATURE",
                    card.card_id,
                    "Signature is not part of the card's causal effect, cost, or risk.",
                )
            )

    for source, count in sorted(source_counts.items()):
        if count > config.max_cards_per_source:
            findings.append(
                Finding(
                    "HIGH",
                    "SOURCE_CONTENT_CAP",
                    source,
                    (
                        f"Source owns {count} cards; diagnostic limit is "
                        f"{config.max_cards_per_source}."
                    ),
                )
            )

    for left, right in combinations(cards, 2):
        similarity = jaccard_similarity(left.mechanic_atoms, right.mechanic_atoms)
        if similarity >= config.near_duplicate_similarity:
            findings.append(
                Finding(
                    "HIGH",
                    "NEAR_DUPLICATE",
                    f"{left.card_id}|{right.card_id}",
                    f"Mechanical Jaccard similarity is {similarity:.3f}.",
                )
            )
        same_comparison_class = left.timing == right.timing and bool(left.labels & right.labels)
        if same_comparison_class and _dominates(left, right):
            findings.append(
                Finding(
                    "HIGH",
                    "PARETO_DOMINANCE",
                    f"{left.card_id}>{right.card_id}",
                    "First card is no worse on every declared benefit/burden axis.",
                )
            )
        elif same_comparison_class and _dominates(right, left):
            findings.append(
                Finding(
                    "HIGH",
                    "PARETO_DOMINANCE",
                    f"{right.card_id}>{left.card_id}",
                    "First card is no worse on every declared benefit/burden axis.",
                )
            )

    for exchange in exchanges:
        removed = set(exchange.remove_card_ids)
        added = set(exchange.add_card_ids)
        unknown = (removed | added) - by_id.keys()
        if unknown:
            findings.append(
                Finding(
                    "BLOCKER",
                    "UNKNOWN_EXCHANGE_CARD",
                    exchange.exchange_id,
                    f"Unknown cards: {sorted(unknown)}.",
                )
            )
        if not removed or not added:
            findings.append(
                Finding(
                    "BLOCKER",
                    "FREE_OR_EMPTY_EXCHANGE",
                    exchange.exchange_id,
                    "Every Concept Deck exchange needs both a sacrifice and a gain.",
                )
            )
        if removed & added:
            findings.append(
                Finding(
                    "BLOCKER",
                    "SELF_EXCHANGE",
                    exchange.exchange_id,
                    "The same card cannot be removed and added by one exchange.",
                )
            )
        if len(added) > config.max_special_cards_per_exchange:
            findings.append(
                Finding(
                    "HIGH",
                    "EXCHANGE_CONTENT_CAP",
                    exchange.exchange_id,
                    "Exchange adds too many special cards at once.",
                )
            )
        if not exchange.allow_size_change and len(removed) != len(added):
            findings.append(
                Finding(
                    "BLOCKER",
                    "UNDECLARED_SIZE_CHANGE",
                    exchange.exchange_id,
                    "Card-count change must be explicit rather than accidental.",
                )
            )

    return tuple(findings)


def apply_exchange_atomic(
    active_card_ids: Iterable[str],
    exchange: DeckExchange,
    card_by_id: Mapping[str, CardSpec],
    active_sources: set[str],
) -> tuple[str, ...]:
    """Apply all costs and gains together, or return the unchanged card set."""

    current = tuple(active_card_ids)
    current_set = set(current)
    removals = set(exchange.remove_card_ids)
    additions = set(exchange.add_card_ids)
    if not removals <= current_set:
        return current
    transaction_cards = removals | additions
    if any(card_id not in card_by_id for card_id in transaction_cards):
        return current
    if any(
        not set(card_by_id[card_id].sources) <= active_sources
        for card_id in transaction_cards
    ):
        return current
    remaining = [card_id for card_id in current if card_id not in removals]
    remaining.extend(exchange.add_card_ids)
    return tuple(remaining)


def generate_covering_cases(
    factors: Mapping[str, Sequence[str]],
    strength: int = 2,
    valid: Callable[[Mapping[str, str]], bool] | None = None,
) -> tuple[dict[str, str], ...]:
    """Generate a deterministic greedy t-way covering set for a bounded model."""

    names = tuple(sorted(factors))
    if strength < 1 or strength > len(names):
        raise ValueError("strength must be between one and the number of factors")
    candidates = [
        dict(zip(names, values))
        for values in product(*(factors[name] for name in names))
    ]
    if valid is not None:
        candidates = [case for case in candidates if valid(case)]
    if not candidates:
        return ()

    def interactions(case: Mapping[str, str]) -> frozenset[tuple[tuple[str, str], ...]]:
        return frozenset(
            tuple((name, case[name]) for name in subset)
            for subset in combinations(names, strength)
        )

    case_interactions = [(case, interactions(case)) for case in candidates]
    uncovered = set().union(*(items for _, items in case_interactions))
    selected: list[dict[str, str]] = []
    remaining = list(case_interactions)
    while uncovered:
        best_index = max(
            range(len(remaining)),
            key=lambda index: (len(remaining[index][1] & uncovered), -index),
        )
        case, covered = remaining.pop(best_index)
        selected.append(case)
        uncovered -= covered
    return tuple(selected)


def interaction_coverage(
    cases: Sequence[Mapping[str, str]],
    factors: Mapping[str, Sequence[str]],
    strength: int = 2,
    valid: Callable[[Mapping[str, str]], bool] | None = None,
) -> float:
    names = tuple(sorted(factors))
    required: set[tuple[tuple[str, str], ...]] = set()
    valid_cases = [
        dict(zip(names, values))
        for values in product(*(factors[name] for name in names))
    ]
    if valid is not None:
        valid_cases = [case for case in valid_cases if valid(case)]
    for case in valid_cases:
        for subset in combinations(names, strength):
            required.add(tuple((name, case[name]) for name in subset))
    if not required:
        return 1.0
    covered = {
        tuple((name, case[name]) for name in subset)
        for case in cases
        for subset in combinations(names, strength)
    }
    return len(required & covered) / len(required)
