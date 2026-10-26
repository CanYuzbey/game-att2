from __future__ import annotations

from game_att2_v3.attention import coverage_report
from game_att2_v3.fixtures import balanced_brain, prototype_expressions, prototype_sources
from game_att2_v3.model import ActionClass


def test_balanced_brain_fixture_has_required_coverage() -> None:
    report = coverage_report(balanced_brain(), prototype_expressions(), prototype_sources())
    assert report[ActionClass.ATTACK][0] >= report[ActionClass.ATTACK][1]
    assert report[ActionClass.DEFENCE][0] >= report[ActionClass.DEFENCE][1]
