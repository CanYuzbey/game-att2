from __future__ import annotations

from dataclasses import dataclass, field

from .attention import AttentionPolicy, redraw
from .model import AttentionHistory, AttentionSelection, BrainSlot, Expression, Source
from .rng import SeededRNG


@dataclass(frozen=True)
class BloodEvent:
    before: int
    delta: int
    after: int
    reason: str


@dataclass
class BloodAccount:
    amount: int
    events: list[BloodEvent] = field(default_factory=list)

    def spend(self, cost: int, reason: str) -> BloodEvent:
        if cost < 0:
            raise ValueError("cost must be non-negative")
        if self.amount < cost:
            raise ValueError("insufficient Blood")
        before = self.amount
        self.amount -= cost
        event = BloodEvent(before=before, delta=-cost, after=self.amount, reason=reason)
        self.events.append(event)
        return event


@dataclass(frozen=True)
class RedrawTransactionResult:
    selection: AttentionSelection
    blood_event: BloodEvent | None
    spent: bool
    reason: str


def execute_blood_redraw(
    *,
    current: AttentionSelection,
    slot: BrainSlot,
    expressions: tuple[Expression, ...],
    sources: dict[str, Source],
    history: AttentionHistory,
    rng: SeededRNG,
    policy: AttentionPolicy,
    account: BloodAccount,
    cost: int,
) -> RedrawTransactionResult:
    """Atomically reroll only when a distinct legal alternative exists.

    The exact Blood cost is injected by the caller/config because V3 balance is OPEN.
    This function owns the invariant that a no-op redraw spends nothing.
    """
    candidate = redraw(current, slot, expressions, sources, history, rng, policy)
    if candidate.reason == "no_legal_alternative":
        return RedrawTransactionResult(candidate, None, False, "no_legal_alternative_no_spend")
    if account.amount < cost:
        return RedrawTransactionResult(current, None, False, "insufficient_blood_no_mutation")
    event = account.spend(cost, "attention_redraw")
    return RedrawTransactionResult(candidate, event, True, "redraw_committed")
