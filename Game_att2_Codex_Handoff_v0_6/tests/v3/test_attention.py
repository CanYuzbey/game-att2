from __future__ import annotations

from collections import Counter

from game_att2_v3.attention import AttentionPolicy, AttentionResolver, coverage_report, redraw
from game_att2_v3.fixtures import balanced_brain, prototype_expressions, prototype_sources
from game_att2_v3.model import ActionClass, AttentionHistory, Source, SourceState
from game_att2_v3.rng import SeededRNG


def resolve_seed(seed: int, sources=None, history=None):
    sources = sources or prototype_sources()
    history = history or AttentionHistory()
    return AttentionResolver().resolve(
        balanced_brain(),
        prototype_expressions(),
        sources,
        history,
        SeededRNG(seed),
    )


def test_same_seed_same_attention() -> None:
    assert resolve_seed(42) == resolve_seed(42)


def test_illegal_source_never_leaks_into_attention() -> None:
    sources = prototype_sources()
    sources["minotaur_left_arm"] = Source("minotaur_left_arm", SourceState.OFFLINE)
    for seed in range(1000):
        assert all(
            result.expression_id not in {"minotaur_smash", "minotaur_brutal_guard"}
            for result in resolve_seed(seed, sources)
        )


def test_guaranteed_duty_never_substitutes_wrong_class() -> None:
    expressions = {e.id: e for e in prototype_expressions()}
    for seed in range(1000):
        for result in resolve_seed(seed):
            if result.shaded or result.duty is None:
                continue
            assert expressions[result.expression_id].action_class is result.duty


def test_guaranteed_duty_shades_when_body_cannot_supply_it() -> None:
    sources = prototype_sources()
    sources["human_right_arm"] = Source("human_right_arm", SourceState.OFFLINE)
    sources["minotaur_left_arm"] = Source("minotaur_left_arm", SourceState.OFFLINE)
    sources["human_legs"] = Source("human_legs", SourceState.OFFLINE)
    results = resolve_seed(1, sources)
    defence = next(result for result in results if result.slot_id == "defence_1")
    assert defence.shaded
    assert defence.expression_id is None
    assert defence.reason == "no_legal_expression_for_duty"


def test_coverage_report_exposes_unfillable_duty() -> None:
    sources = prototype_sources()
    sources["human_right_arm"] = Source("human_right_arm", SourceState.OFFLINE)
    sources["human_legs"] = Source("human_legs", SourceState.OFFLINE)
    report = coverage_report(balanced_brain(), prototype_expressions(), sources)
    available, required = report[ActionClass.ATTACK]
    assert required == 2
    assert available == 1


def test_recency_soft_suppresses_without_hard_cooldown() -> None:
    resolver = AttentionResolver(AttentionPolicy(recency_factor=0.25))
    sources = prototype_sources()
    expressions = prototype_expressions()
    brain = balanced_brain()
    baseline = Counter()
    recent = Counter()
    for seed in range(2000):
        base = resolver.resolve(brain, expressions, sources, AttentionHistory(), SeededRNG(seed))[0]
        baseline[base.expression_id] += 1
        hist = AttentionHistory({"minotaur_smash": 1})
        rec = resolver.resolve(brain, expressions, sources, hist, SeededRNG(seed))[0]
        recent[rec.expression_id] += 1
    assert recent["minotaur_smash"] < baseline["minotaur_smash"]
    assert recent["minotaur_smash"] > 0


def test_degraded_source_reduces_access_weight_without_illegalizing_it() -> None:
    resolver = AttentionResolver(AttentionPolicy(strained_factor=0.25))
    expressions = prototype_expressions()
    brain = balanced_brain()
    full_count = 0
    strained_count = 0
    for seed in range(2000):
        full_sources = prototype_sources()
        full = resolver.resolve(brain, expressions, full_sources, AttentionHistory(), SeededRNG(seed))[0]
        full_count += full.expression_id == "minotaur_smash"

        strained_sources = prototype_sources()
        strained_sources["minotaur_left_arm"] = Source("minotaur_left_arm", SourceState.STRAINED)
        strained = resolver.resolve(
            brain, expressions, strained_sources, AttentionHistory(), SeededRNG(seed)
        )[0]
        strained_count += strained.expression_id == "minotaur_smash"
    assert 0 < strained_count < full_count


def test_extreme_specialization_increases_consistency_but_can_shade_duplicate_duty() -> None:
    sources = prototype_sources()
    sources["human_right_arm"] = Source("human_right_arm", SourceState.OFFLINE)
    sources["human_legs"] = Source("human_legs", SourceState.OFFLINE)
    for seed in range(100):
        results = resolve_seed(seed, sources)
        assert results[0].expression_id == "minotaur_smash"
        assert results[1].shaded


def test_redraw_with_no_alternative_returns_no_spend_signal() -> None:
    sources = prototype_sources()
    sources["human_right_arm"] = Source("human_right_arm", SourceState.OFFLINE)
    sources["human_legs"] = Source("human_legs", SourceState.OFFLINE)
    selection = resolve_seed(3, sources)[0]
    new = redraw(
        selection,
        balanced_brain().slots[0],
        prototype_expressions(),
        sources,
        AttentionHistory(),
        SeededRNG(4),
        AttentionPolicy(),
    )
    assert new.expression_id == selection.expression_id
    assert new.reason == "no_legal_alternative"


def test_redraw_never_returns_current_when_alternative_exists() -> None:
    sources = prototype_sources()
    for seed in range(500):
        selection = resolve_seed(seed, sources)[0]
        new = redraw(
            selection,
            balanced_brain().slots[0],
            prototype_expressions(),
            sources,
            AttentionHistory(),
            SeededRNG(seed + 10000),
            AttentionPolicy(),
        )
        assert new.reason == "redraw_selected_legal_alternative"
        assert new.expression_id != selection.expression_id


def test_debug_trace_records_factors_rejections_and_roll() -> None:
    resolver = AttentionResolver()
    selections, traces = resolver.resolve_with_trace(
        balanced_brain(),
        prototype_expressions(),
        prototype_sources(),
        AttentionHistory(),
        SeededRNG(42),
    )
    assert len(selections) == len(traces)
    first = traces[0]
    assert first.roll is not None
    assert first.total_weight > 0
    assert first.selected_expression_id == selections[0].expression_id
    assert any(weight.expression_id == first.selected_expression_id for weight in first.weights)
    assert any(reason == "wrong_duty_class" for _expression, reason in first.rejected)


def test_coverage_warnings_only_report_shortfalls() -> None:
    from game_att2_v3.attention import coverage_warnings

    assert coverage_warnings(balanced_brain(), prototype_expressions(), prototype_sources()) == ()
    sources = prototype_sources()
    sources["human_right_arm"] = Source("human_right_arm", SourceState.OFFLINE)
    sources["human_legs"] = Source("human_legs", SourceState.OFFLINE)
    warnings = coverage_warnings(balanced_brain(), prototype_expressions(), sources)
    attack = next(w for w in warnings if w.duty is ActionClass.ATTACK)
    assert attack.available == 1
    assert attack.required == 2
    assert attack.shortfall == 1
