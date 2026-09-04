from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .model import (
    ActionClass,
    AttentionHistory,
    AttentionSelection,
    BrainArchitecture,
    BrainSlot,
    Expression,
    Source,
    SourceState,
)
from .rng import SeededRNG

_STATE_RANK: dict[SourceState, int] = {
    SourceState.OFFLINE: 0,
    SourceState.DESPERATE: 1,
    SourceState.STRAINED: 2,
    SourceState.FULL: 3,
}


@dataclass(frozen=True)
class AttentionPolicy:
    recency_factor: float = 0.65
    strained_factor: float = 0.75
    desperate_factor: float = 0.45
    focus_bias: float = 3.0

    def __post_init__(self) -> None:
        for value in (
            self.recency_factor,
            self.strained_factor,
            self.desperate_factor,
            self.focus_bias,
        ):
            if value < 0:
                raise ValueError("Attention factors must be non-negative")


def expression_is_legal(expression: Expression, sources: dict[str, Source]) -> bool:
    for source_id in expression.source_ids:
        source = sources.get(source_id)
        if source is None or not source.usable:
            return False
        if _STATE_RANK[source.state] < _STATE_RANK[expression.min_state]:
            return False
    return True


def source_state_factor(expression: Expression, sources: dict[str, Source], policy: AttentionPolicy) -> float:
    factor = 1.0
    for source_id in expression.source_ids:
        state = sources[source_id].state
        if state is SourceState.STRAINED:
            factor *= policy.strained_factor
        elif state is SourceState.DESPERATE:
            factor *= policy.desperate_factor
        elif state is SourceState.OFFLINE:
            return 0.0
    return factor


def slot_role(slot: BrainSlot, rng: SeededRNG) -> ActionClass | None:
    if slot.guaranteed_duty:
        return slot.duty
    if slot.duty is not None and not slot.flexible_weights:
        return slot.duty
    if not slot.flexible_weights:
        return None
    classes = tuple(slot.flexible_weights)
    weights = tuple(slot.flexible_weights[c] for c in classes)
    if sum(weights) <= 0:
        return None
    return rng.choice_weighted(classes, weights)


def coverage_report(
    architecture: BrainArchitecture,
    expressions: Iterable[Expression],
    sources: dict[str, Source],
) -> dict[ActionClass, tuple[int, int]]:
    legal = [e for e in expressions if expression_is_legal(e, sources)]
    required: dict[ActionClass, int] = {}
    available: dict[ActionClass, int] = {}
    for slot in architecture.slots:
        if slot.guaranteed_duty and slot.duty is not None:
            required[slot.duty] = required.get(slot.duty, 0) + 1
    for expression in legal:
        available[expression.action_class] = available.get(expression.action_class, 0) + 1
    return {
        duty: (available.get(duty, 0), count)
        for duty, count in required.items()
    }


class AttentionResolver:
    def __init__(self, policy: AttentionPolicy | None = None) -> None:
        self.policy = policy or AttentionPolicy()

    def _weight(
        self,
        expression: Expression,
        slot: BrainSlot,
        sources: dict[str, Source],
        history: AttentionHistory,
        focus_source_id: str | None,
    ) -> float:
        weight = expression.base_weight
        for tag, bias in slot.tag_biases.items():
            if tag in expression.tags:
                weight *= bias
        if history.surfaced_count.get(expression.id, 0) > 0:
            weight *= self.policy.recency_factor ** history.surfaced_count[expression.id]
        weight *= source_state_factor(expression, sources, self.policy)
        if focus_source_id is not None and focus_source_id in expression.source_ids:
            weight *= self.policy.focus_bias
        return max(0.0, weight)

    def resolve(
        self,
        architecture: BrainArchitecture,
        expressions: Iterable[Expression],
        sources: dict[str, Source],
        history: AttentionHistory,
        rng: SeededRNG,
        focus_source_id: str | None = None,
    ) -> tuple[AttentionSelection, ...]:
        legal = tuple(e for e in expressions if expression_is_legal(e, sources))
        used_expression_ids: set[str] = set()
        results: list[AttentionSelection] = []

        for slot in architecture.slots:
            duty = slot_role(slot, rng)
            candidates = tuple(
                e
                for e in legal
                if e.id not in used_expression_ids
                and (duty is None or e.action_class is duty)
            )
            weighted = tuple(
                (e, self._weight(e, slot, sources, history, focus_source_id))
                for e in candidates
            )
            weighted = tuple(pair for pair in weighted if pair[1] > 0)

            if not weighted:
                results.append(
                    AttentionSelection(
                        slot_id=slot.id,
                        duty=duty,
                        expression_id=None,
                        shaded=True,
                        candidates=tuple(e.id for e in candidates),
                        normalized_weights=(),
                        reason="no_legal_expression_for_duty",
                    )
                )
                continue

            total = sum(weight for _, weight in weighted)
            normalized = tuple((e.id, weight / total) for e, weight in weighted)
            selected = rng.choice_weighted(
                tuple(e for e, _ in weighted),
                tuple(weight for _, weight in weighted),
            )
            used_expression_ids.add(selected.id)
            history.note(selected.id)
            results.append(
                AttentionSelection(
                    slot_id=slot.id,
                    duty=duty,
                    expression_id=selected.id,
                    shaded=False,
                    candidates=tuple(e.id for e, _ in weighted),
                    normalized_weights=normalized,
                    reason="selected_from_legal_weighted_pool",
                )
            )

        return tuple(results)


def redraw(
    selection: AttentionSelection,
    slot: BrainSlot,
    expressions: Iterable[Expression],
    sources: dict[str, Source],
    history: AttentionHistory,
    rng: SeededRNG,
    policy: AttentionPolicy,
) -> AttentionSelection:
    """Reroll one slot without spending Blood if no legal alternative exists.

    Blood accounting belongs to the caller/rule engine; this function reports
    whether a legal alternative exists by returning ``reason=no_legal_alternative``.
    """
    current = selection.expression_id
    duty = selection.duty
    legal_alternatives = tuple(
        e
        for e in expressions
        if e.id != current
        and expression_is_legal(e, sources)
        and (duty is None or e.action_class is duty)
    )
    if not legal_alternatives:
        return AttentionSelection(
            slot_id=selection.slot_id,
            duty=duty,
            expression_id=current,
            shaded=selection.shaded,
            candidates=(),
            normalized_weights=(),
            reason="no_legal_alternative",
        )
    resolver = AttentionResolver(policy)
    temporary_architecture = BrainArchitecture(id="redraw", slots=(slot,))
    resolved = resolver.resolve(
        temporary_architecture,
        legal_alternatives,
        sources,
        history,
        rng,
    )[0]
    return AttentionSelection(
        slot_id=selection.slot_id,
        duty=selection.duty,
        expression_id=resolved.expression_id,
        shaded=resolved.shaded,
        candidates=resolved.candidates,
        normalized_weights=resolved.normalized_weights,
        reason="redraw_selected_legal_alternative",
    )
