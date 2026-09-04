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


@dataclass(frozen=True)
class WeightTrace:
    expression_id: str
    base: float
    brain: float
    recency: float
    state: float
    focus: float
    final: float


@dataclass(frozen=True)
class SlotResolutionTrace:
    slot_id: str
    duty: ActionClass | None
    rejected: tuple[tuple[str, str], ...]
    weights: tuple[WeightTrace, ...]
    roll: float | None
    total_weight: float
    selected_expression_id: str | None


@dataclass(frozen=True)
class CoverageWarning:
    duty: ActionClass
    available: int
    required: int

    @property
    def shortfall(self) -> int:
        return max(0, self.required - self.available)


def expression_is_legal(expression: Expression, sources: dict[str, Source]) -> bool:
    for source_id in expression.source_ids:
        source = sources.get(source_id)
        if source is None or not source.usable:
            return False
        if _STATE_RANK[source.state] < _STATE_RANK[expression.min_state]:
            return False
    return True


def source_state_factor(
    expression: Expression, sources: dict[str, Source], policy: AttentionPolicy
) -> float:
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
    return {duty: (available.get(duty, 0), count) for duty, count in required.items()}


def coverage_warnings(
    architecture: BrainArchitecture,
    expressions: Iterable[Expression],
    sources: dict[str, Source],
) -> tuple[CoverageWarning, ...]:
    report = coverage_report(architecture, expressions, sources)
    return tuple(
        CoverageWarning(duty=duty, available=available, required=required)
        for duty, (available, required) in report.items()
        if available < required
    )


class AttentionResolver:
    def __init__(self, policy: AttentionPolicy | None = None) -> None:
        self.policy = policy or AttentionPolicy()

    def _weight_trace(
        self,
        expression: Expression,
        slot: BrainSlot,
        sources: dict[str, Source],
        history: AttentionHistory,
        focus_source_id: str | None,
    ) -> WeightTrace:
        base = expression.base_weight
        brain = 1.0
        for tag, bias in slot.tag_biases.items():
            if tag in expression.tags:
                brain *= bias
        recency = self.policy.recency_factor ** history.surfaced_count.get(expression.id, 0)
        state = source_state_factor(expression, sources, self.policy)
        focus = (
            self.policy.focus_bias
            if focus_source_id is not None and focus_source_id in expression.source_ids
            else 1.0
        )
        final = max(0.0, base * brain * recency * state * focus)
        return WeightTrace(expression.id, base, brain, recency, state, focus, final)

    def resolve_with_trace(
        self,
        architecture: BrainArchitecture,
        expressions: Iterable[Expression],
        sources: dict[str, Source],
        history: AttentionHistory,
        rng: SeededRNG,
        focus_source_id: str | None = None,
        reserved_expression_ids: frozenset[str] = frozenset(),
    ) -> tuple[tuple[AttentionSelection, ...], tuple[SlotResolutionTrace, ...]]:
        all_expressions = tuple(expressions)
        used_expression_ids: set[str] = set(reserved_expression_ids)
        results: list[AttentionSelection] = []
        traces: list[SlotResolutionTrace] = []

        for slot in architecture.slots:
            duty = slot_role(slot, rng)
            rejected: list[tuple[str, str]] = []
            candidates: list[Expression] = []
            for expression in all_expressions:
                if expression.id in used_expression_ids:
                    rejected.append((expression.id, "already_selected_this_refresh"))
                    continue
                if not expression_is_legal(expression, sources):
                    rejected.append((expression.id, "source_or_state_illegal"))
                    continue
                if duty is not None and expression.action_class is not duty:
                    rejected.append((expression.id, "wrong_duty_class"))
                    continue
                candidates.append(expression)

            weight_traces = tuple(
                self._weight_trace(e, slot, sources, history, focus_source_id) for e in candidates
            )
            positive = tuple(t for t in weight_traces if t.final > 0)

            if not positive:
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
                traces.append(
                    SlotResolutionTrace(
                        slot_id=slot.id,
                        duty=duty,
                        rejected=tuple(rejected),
                        weights=weight_traces,
                        roll=None,
                        total_weight=0.0,
                        selected_expression_id=None,
                    )
                )
                continue

            positive_by_id = {trace.expression_id: trace for trace in positive}
            values = tuple(e for e in candidates if e.id in positive_by_id)
            weights = tuple(positive_by_id[e.id].final for e in values)
            total = sum(weights)
            normalized = tuple((e.id, positive_by_id[e.id].final / total) for e in values)
            selected, rng_trace = rng.choice_weighted_with_trace(values, weights)
            used_expression_ids.add(selected.id)
            history.note(selected.id)
            results.append(
                AttentionSelection(
                    slot_id=slot.id,
                    duty=duty,
                    expression_id=selected.id,
                    shaded=False,
                    candidates=tuple(e.id for e in values),
                    normalized_weights=normalized,
                    reason="selected_from_legal_weighted_pool",
                )
            )
            traces.append(
                SlotResolutionTrace(
                    slot_id=slot.id,
                    duty=duty,
                    rejected=tuple(rejected),
                    weights=weight_traces,
                    roll=rng_trace.roll,
                    total_weight=rng_trace.total_weight,
                    selected_expression_id=selected.id,
                )
            )

        return tuple(results), tuple(traces)

    def resolve(
        self,
        architecture: BrainArchitecture,
        expressions: Iterable[Expression],
        sources: dict[str, Source],
        history: AttentionHistory,
        rng: SeededRNG,
        focus_source_id: str | None = None,
        reserved_expression_ids: frozenset[str] = frozenset(),
    ) -> tuple[AttentionSelection, ...]:
        selections, _traces = self.resolve_with_trace(
            architecture,
            expressions,
            sources,
            history,
            rng,
            focus_source_id,
            reserved_expression_ids,
        )
        return selections


def redraw(
    selection: AttentionSelection,
    slot: BrainSlot,
    expressions: Iterable[Expression],
    sources: dict[str, Source],
    history: AttentionHistory,
    rng: SeededRNG,
    policy: AttentionPolicy,
) -> AttentionSelection:
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
        temporary_architecture, legal_alternatives, sources, history, rng
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
