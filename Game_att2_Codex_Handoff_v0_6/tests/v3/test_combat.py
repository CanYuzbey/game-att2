from __future__ import annotations

import pytest

from game_att2_v3.combat import commit_main, commit_preparation, resolve_defence
from game_att2_v3.model import DefenceResponse, RoundBudget, ThreatClass


def test_yellow_rejects_evade() -> None:
    assert not resolve_defence(ThreatClass.YELLOW, DefenceResponse.EVADE, True).legal


def test_red_rejects_block_and_parry() -> None:
    assert not resolve_defence(ThreatClass.RED, DefenceResponse.BLOCK, True).legal
    assert not resolve_defence(ThreatClass.RED, DefenceResponse.PARRY, True).legal


def test_yellow_parry_success_prevents_consequence() -> None:
    result = resolve_defence(ThreatClass.YELLOW, DefenceResponse.PARRY, True)
    assert result.legal and result.consequence_prevented


def test_red_evade_failure_applies_original_consequence() -> None:
    result = resolve_defence(ThreatClass.RED, DefenceResponse.EVADE, False)
    assert result.legal and not result.consequence_prevented


def test_one_preparation_one_main() -> None:
    budget = RoundBudget()
    commit_preparation(budget)
    commit_main(budget)
    with pytest.raises(ValueError):
        commit_preparation(budget)
    with pytest.raises(ValueError):
        commit_main(budget)


def test_one_inventory_origin_action_per_round() -> None:
    budget = RoundBudget()
    commit_preparation(budget, inventory_origin=True)
    with pytest.raises(ValueError):
        budget.spend_inventory_action()
