from __future__ import annotations

import shutil
from pathlib import Path

import pytest
import yaml

from game_att2_sim.config_loader import load_config
from game_att2_sim.encounter_goals import (
    OutcomeLevel,
    ResolutionKind,
    evaluate_encounter_outcome,
)
from game_att2_sim.enemy_behavior import IntentCandidate, select_intent
from game_att2_sim.enums import Slot
from game_att2_sim.errors import ConfigValidationError


def test_config_loads_general_motivations_and_victory_routes() -> None:
    config = load_config()
    design = config.encounter_designs["jeff"]
    assert design.actor_motivations == {
        "player": "player_body_reconstruction",
        "enemy": "jeff_reciprocal_repair",
    }
    assert config.motivation_profiles["jeff_reciprocal_repair"].desired_assets == (
        "clotting_cream",
    )
    assert design.parameters["repetition_penalty"] == 20
    assert {route.actor for route in design.victory_routes} == {"player", "enemy"}
    assert config.actions["cover_it"].duration_rounds == 1
    assert config.actions["cover_it"].implementation_status.startswith("deferred_")
    assert config.actions["brace"].name == "Brace — Manual Stance"


def test_config_rejects_unknown_motivation_reference(tmp_path: Path) -> None:
    source = Path(__file__).resolve().parents[2] / "config"
    destination = tmp_path / "config"
    shutil.copytree(source, destination)
    content_path = destination / "content_v0_1.yaml"
    content = yaml.safe_load(content_path.read_text(encoding="utf-8"))
    content["encounter_designs"]["jeff"]["actor_motivations"]["enemy"] = "missing"
    content_path.write_text(yaml.safe_dump(content, sort_keys=False), encoding="utf-8")

    with pytest.raises(ConfigValidationError, match="unknown motivation"):
        load_config(destination)


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        (lambda content: content["encounter_designs"]["jeff"]["actor_motivations"].pop("enemy"), "exactly player and enemy"),
        (lambda content: content["motivation_profiles"]["jeff_reciprocal_repair"].update(escalation_triggers=[]), "bargain_rejected"),
        (lambda content: content["encounter_designs"]["jeff"]["parameters"].update(bargain_quality="stressed"), "must be clean"),
        (lambda content: content["encounter_designs"]["jeff"]["victory_routes"][0].update(predicate="typo_fact"), "unsupported"),
        (lambda content: content["actions"]["cover_it"].update(duration_rounds=2), "exactly one round"),
        (lambda content: content["actions"]["cover_it"].update(implementation_status="implemented"), "remain deferred"),
    ),
)
def test_config_rejects_broken_approved_jeff_contract(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
    source = Path(__file__).resolve().parents[2] / "config"
    destination = tmp_path / "config"
    shutil.copytree(source, destination)
    content_path = destination / "content_v0_1.yaml"
    content = yaml.safe_load(content_path.read_text(encoding="utf-8"))
    assert callable(mutation)
    mutation(content)
    content_path.write_text(yaml.safe_dump(content, sort_keys=False), encoding="utf-8")

    with pytest.raises(ConfigValidationError, match=message):
        load_config(destination)


def test_multi_actor_outcome_allows_mutual_success() -> None:
    design = load_config().encounter_designs["jeff"]
    outcome = evaluate_encounter_outcome(
        design,
        {
            "player_has_graftable_jeff_right_arm": True,
            "jeff_has_clotting_cream": True,
            "jeff_survived_resolution": True,
        },
        ResolutionKind.BARGAIN,
    )
    actor_results = {actor.actor: actor for actor in outcome.actors}
    assert actor_results["player"].level is OutcomeLevel.COMPLETE
    assert actor_results["enemy"].level is OutcomeLevel.COMPLETE
    assert outcome.resolution is ResolutionKind.BARGAIN


def test_capability_break_can_be_partial_instead_of_a_universal_ending() -> None:
    design = load_config().encounter_designs["jeff"]
    outcome = evaluate_encounter_outcome(
        design,
        {"jeff_offensive_sources_unusable": True},
        ResolutionKind.INCAPACITY,
    )
    actor_results = {actor.actor: actor for actor in outcome.actors}
    assert actor_results["player"].level is OutcomeLevel.PARTIAL
    assert actor_results["enemy"].level is OutcomeLevel.FAILED


def test_intent_selector_penalizes_exact_repetition_with_stable_ties() -> None:
    candidates = (
        IntentCandidate(
            "swing",
            Slot.LEFT_ARM,
            Slot.LEFT_ARM,
            55,
            ("deny offense",),
            "vague",
            "left",
        ),
        IntentCandidate(
            "swing",
            Slot.LEFT_ARM,
            Slot.TORSO,
            50,
            ("pressure",),
            "vague",
            "torso",
        ),
    )
    first = select_intent(
        candidates,
        last_action_id=None,
        last_target_slot=None,
        repetition_penalty=20,
    )
    assert first is not None and first.candidate.target_slot is Slot.LEFT_ARM
    second = select_intent(
        candidates,
        last_action_id="swing",
        last_target_slot=Slot.LEFT_ARM,
        repetition_penalty=20,
    )
    assert second is not None and second.candidate.target_slot is Slot.TORSO
    assert second.final_score == 50
