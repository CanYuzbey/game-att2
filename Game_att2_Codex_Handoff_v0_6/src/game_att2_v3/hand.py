from __future__ import annotations

from dataclasses import dataclass, field

from .attention import AttentionResolver, expression_is_legal
from .model import (
    AttentionHistory,
    AttentionSelection,
    BrainArchitecture,
    Expression,
    Source,
)
from .rng import SeededRNG


@dataclass
class AttentionHand:
    """Persistent V3-1 comparison hand.

    Unused legal selections persist. Played, dropped, or invalid selections leave an
    open slot. Open slots refill only at the next explicit Decision Refresh.
    """

    selections: dict[str, AttentionSelection] = field(default_factory=dict)
    open_reasons: dict[str, str] = field(default_factory=dict)

    def held_expression_ids(self) -> frozenset[str]:
        return frozenset(
            selection.expression_id
            for selection in self.selections.values()
            if selection.expression_id is not None
        )

    def play(self, slot_id: str) -> AttentionSelection:
        selection = self.selections.pop(slot_id)
        self.open_reasons[slot_id] = "spent"
        return selection

    def drop(self, slot_id: str) -> AttentionSelection:
        selection = self.selections.pop(slot_id)
        self.open_reasons[slot_id] = "dropped"
        return selection

    def revalidate(
        self,
        expression_by_id: dict[str, Expression],
        sources: dict[str, Source],
    ) -> tuple[str, ...]:
        invalidated: list[str] = []
        for slot_id, selection in tuple(self.selections.items()):
            expression_id = selection.expression_id
            if expression_id is None:
                continue
            expression = expression_by_id[expression_id]
            if not expression_is_legal(expression, sources):
                del self.selections[slot_id]
                self.open_reasons[slot_id] = "source_invalidated"
                invalidated.append(slot_id)
        return tuple(invalidated)

    def decision_refresh(
        self,
        architecture: BrainArchitecture,
        expressions: tuple[Expression, ...],
        sources: dict[str, Source],
        history: AttentionHistory,
        rng: SeededRNG,
        resolver: AttentionResolver,
        focus_source_id: str | None = None,
    ) -> tuple[AttentionSelection, ...]:
        slot_by_id = {slot.id: slot for slot in architecture.slots}
        missing_slot_ids = tuple(
            slot.id for slot in architecture.slots if slot.id not in self.selections
        )
        if not missing_slot_ids:
            return tuple(self.selections[slot.id] for slot in architecture.slots)

        sub_architecture = BrainArchitecture(
            id=f"{architecture.id}:refresh",
            slots=tuple(slot_by_id[slot_id] for slot_id in missing_slot_ids),
        )
        new = resolver.resolve(
            sub_architecture,
            expressions,
            sources,
            history,
            rng,
            focus_source_id,
            self.held_expression_ids(),
        )
        for selection in new:
            self.selections[selection.slot_id] = selection
            self.open_reasons.pop(selection.slot_id, None)
        return tuple(self.selections[slot.id] for slot in architecture.slots)
