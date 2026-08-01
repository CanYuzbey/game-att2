"""Typed motivation, victory-route, and multi-actor outcome contracts."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from enum import Enum

from .enums import Slot


class MotivationKind(str, Enum):
    RESTORATION = "restoration"
    SURVIVAL = "survival"
    CONTROL = "control"
    ELIMINATION = "elimination"


class VictoryRouteKind(str, Enum):
    BLOOD_DEATH = "blood_death"
    CAPABILITY_BREAK = "capability_break"
    SURRENDER = "surrender"
    OBJECTIVE_COMPLETION = "objective_completion"
    BOSS_SPECIFIC = "boss_specific"


class ResolutionKind(str, Enum):
    BARGAIN = "bargain"
    COLLAPSE = "collapse"
    DEATH = "death"
    INCAPACITY = "incapacity"
    SURRENDER = "surrender"
    ESCAPE = "escape"
    OBJECTIVE = "objective"


class OutcomeLevel(str, Enum):
    COMPLETE = "complete"
    PARTIAL = "partial"
    FAILED = "failed"
    UNRESOLVED = "unresolved"


@dataclass(frozen=True)
class MotivationProfile:
    id: str
    kind: MotivationKind
    summary: str
    desired_assets: tuple[str, ...]
    preserve_slots: tuple[Slot, ...]
    acceptable_resolutions: tuple[ResolutionKind, ...]
    lethality: str
    escalation_triggers: tuple[str, ...]


@dataclass(frozen=True)
class VictoryRouteDefinition:
    id: str
    actor: str
    kind: VictoryRouteKind
    predicate: str
    success_level: OutcomeLevel


@dataclass(frozen=True)
class EncounterDesignDefinition:
    id: str
    actor_motivations: Mapping[str, str]
    victory_routes: tuple[VictoryRouteDefinition, ...]
    parameters: Mapping[str, object]


@dataclass(frozen=True)
class ActorOutcome:
    actor: str
    level: OutcomeLevel
    achieved_routes: tuple[str, ...]


@dataclass(frozen=True)
class EncounterOutcome:
    encounter_id: str
    resolution: ResolutionKind
    actors: tuple[ActorOutcome, ...]


def evaluate_encounter_outcome(
    definition: EncounterDesignDefinition,
    facts: Mapping[str, bool],
    resolution: ResolutionKind,
) -> EncounterOutcome:
    """Evaluate configured predicates after state mutation for every actor."""
    actors: list[ActorOutcome] = []
    for actor in definition.actor_motivations:
        achieved = tuple(
            route
            for route in definition.victory_routes
            if route.actor == actor and facts.get(route.predicate, False)
        )
        if any(route.success_level is OutcomeLevel.COMPLETE for route in achieved):
            level = OutcomeLevel.COMPLETE
        elif achieved:
            level = OutcomeLevel.PARTIAL
        else:
            level = OutcomeLevel.FAILED
        actors.append(
            ActorOutcome(
                actor=actor,
                level=level,
                achieved_routes=tuple(route.id for route in achieved),
            )
        )
    return EncounterOutcome(definition.id, resolution, tuple(actors))
