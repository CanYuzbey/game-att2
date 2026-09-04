from __future__ import annotations

from game_att2_v3.attention import AttentionPolicy, AttentionResolver
from game_att2_v3.blood import BloodAccount, execute_blood_redraw
from game_att2_v3.fixtures import balanced_brain, prototype_expressions, prototype_sources
from game_att2_v3.model import AttentionHistory, Source, SourceState
from game_att2_v3.rng import SeededRNG


def initial_selection(seed: int, sources):
    return AttentionResolver().resolve(
        balanced_brain(),
        prototype_expressions(),
        sources,
        AttentionHistory(),
        SeededRNG(seed),
    )[0]


def test_no_alternative_redraw_spends_nothing() -> None:
    sources = prototype_sources()
    sources["human_right_arm"] = Source("human_right_arm", SourceState.OFFLINE)
    sources["human_legs"] = Source("human_legs", SourceState.OFFLINE)
    current = initial_selection(4, sources)
    account = BloodAccount(50)
    result = execute_blood_redraw(
        current=current,
        slot=balanced_brain().slots[0],
        expressions=prototype_expressions(),
        sources=sources,
        history=AttentionHistory(),
        rng=SeededRNG(10),
        policy=AttentionPolicy(),
        account=account,
        cost=7,
    )
    assert not result.spent
    assert account.amount == 50
    assert account.events == []
    assert result.reason == "no_legal_alternative_no_spend"


def test_insufficient_blood_keeps_state_and_selection() -> None:
    sources = prototype_sources()
    current = initial_selection(4, sources)
    account = BloodAccount(2)
    result = execute_blood_redraw(
        current=current,
        slot=balanced_brain().slots[0],
        expressions=prototype_expressions(),
        sources=sources,
        history=AttentionHistory(),
        rng=SeededRNG(10),
        policy=AttentionPolicy(),
        account=account,
        cost=7,
    )
    assert not result.spent
    assert result.selection == current
    assert account.amount == 2
    assert account.events == []
    assert result.reason == "insufficient_blood_no_mutation"


def test_committed_redraw_logs_exact_blood_event() -> None:
    sources = prototype_sources()
    current = initial_selection(4, sources)
    account = BloodAccount(50)
    result = execute_blood_redraw(
        current=current,
        slot=balanced_brain().slots[0],
        expressions=prototype_expressions(),
        sources=sources,
        history=AttentionHistory(),
        rng=SeededRNG(10),
        policy=AttentionPolicy(),
        account=account,
        cost=7,
    )
    assert result.spent
    assert result.selection.expression_id != current.expression_id
    assert account.amount == 43
    assert len(account.events) == 1
    event = account.events[0]
    assert (event.before, event.delta, event.after, event.reason) == (50, -7, 43, "attention_redraw")
