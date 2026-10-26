from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import FrozenSet


class SourceState(str, Enum):
    FULL = "full"
    STRAINED = "strained"
    DESPERATE = "desperate"
    OFFLINE = "offline"


class ActionClass(str, Enum):
    ATTACK = "attack"
    DEFENCE = "defence"
    UTILITY = "utility"
    PREPARATION = "preparation"
    RECOVERY = "recovery"


class ThreatClass(str, Enum):
    YELLOW = "yellow"
    RED = "red"


class DefenceResponse(str, Enum):
    BLOCK = "block"
    PARRY = "parry"
    EVADE = "evade"


@dataclass(frozen=True)
class Source:
    id: str
    state: SourceState
    tags: FrozenSet[str] = frozenset()

    @property
    def usable(self) -> bool:
        return self.state is not SourceState.OFFLINE


@dataclass(frozen=True)
class Expression:
    id: str
    action_class: ActionClass
    source_ids: tuple[str, ...]
    tags: FrozenSet[str] = frozenset()
    base_weight: float = 1.0
    min_state: SourceState = SourceState.DESPERATE

    def __post_init__(self) -> None:
        if not self.source_ids:
            raise ValueError("Expression requires at least one source")
        if self.base_weight < 0:
            raise ValueError("base_weight must be non-negative")


@dataclass(frozen=True)
class BrainSlot:
    id: str
    duty: ActionClass | None
    guaranteed_duty: bool
    flexible_weights: dict[ActionClass, float] = field(default_factory=dict)
    tag_biases: dict[str, float] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.guaranteed_duty and self.duty is None:
            raise ValueError("Guaranteed duty slot must declare duty")
        if any(v < 0 for v in self.flexible_weights.values()):
            raise ValueError("Flexible weights must be non-negative")
        if any(v < 0 for v in self.tag_biases.values()):
            raise ValueError("Tag biases must be non-negative")


@dataclass(frozen=True)
class BrainArchitecture:
    id: str
    slots: tuple[BrainSlot, ...]


@dataclass
class AttentionHistory:
    surfaced_count: dict[str, int] = field(default_factory=dict)

    def note(self, expression_id: str) -> None:
        self.surfaced_count[expression_id] = self.surfaced_count.get(expression_id, 0) + 1


@dataclass(frozen=True)
class AttentionSelection:
    slot_id: str
    duty: ActionClass | None
    expression_id: str | None
    shaded: bool
    candidates: tuple[str, ...]
    normalized_weights: tuple[tuple[str, float], ...]
    reason: str


@dataclass
class RoundBudget:
    preparation_used: bool = False
    main_used: bool = False
    inventory_action_used: bool = False

    def spend_preparation(self) -> None:
        if self.preparation_used:
            raise ValueError("Preparation already used")
        self.preparation_used = True

    def spend_main(self) -> None:
        if self.main_used:
            raise ValueError("Main already used")
        self.main_used = True

    def spend_inventory_action(self) -> None:
        if self.inventory_action_used:
            raise ValueError("Inventory-origin action already used")
        self.inventory_action_used = True
