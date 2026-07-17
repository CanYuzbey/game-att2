"""Definitions are immutable; run and combat state is deliberately mutable."""

from __future__ import annotations

from dataclasses import dataclass, field

from .enums import HarvestQuality, IntentClarity, LimbState, LimbTag, Slot


@dataclass(frozen=True)
class LimbDefinition:
    id: str
    name: str
    slot: Slot
    max_integrity: int
    size: str
    actions: tuple[str, ...] = ()
    passives: tuple[str, ...] = ()
    initial_state: LimbState = LimbState.INTACT


@dataclass(frozen=True)
class ActionDefinition:
    id: str
    name: str
    timing: str
    cost: int
    source_slot: Slot | None = None
    damage: int = 0
    damage_type: str | None = None
    reduction: float = 0.0
    can_clean_sever: bool = False


@dataclass
class LimbRuntime:
    definition: LimbDefinition
    integrity: int
    state: LimbState
    tags: set[LimbTag] = field(default_factory=set)
    disabled_rounds: int = 0
    focused_round: int = -1
    unstable_result: str | None = None
    surge_unused: bool = False

    @property
    def slot(self) -> Slot:
        return self.definition.slot

    @property
    def name(self) -> str:
        return self.definition.name


@dataclass
class BodyRuntime:
    slots: dict[Slot, LimbRuntime]


@dataclass
class CombatantRuntime:
    id: str
    name: str
    body: BodyRuntime
    blood: int
    inventory: dict[str, int]
    role: str
    plead_pressure: int = 0
    panic_pulse_used: bool = False
    soft_collapse_used: bool = False
    collapsed: bool = False
    debt: int = 0
    rage: bool = False
    guard_active: bool = False
    brace_used: bool = False
    brace_charges: int = 0
    downed: bool = False
    normal_action_consumed: bool = False


@dataclass(frozen=True)
class EnemyIntent:
    action_id: str
    source_slot: Slot | None
    target_slot: Slot | None
    clarity: IntentClarity


@dataclass(frozen=True)
class HarvestedLimb:
    limb: LimbRuntime
    quality: HarvestQuality
    force_unstable: bool = False


@dataclass(frozen=True)
class Event:
    sequence: int
    round_number: int
    phase: str
    event_type: str
    actor_id: str | None
    target_id: str | None
    payload: dict[str, object]


@dataclass
class ScenarioMetrics:
    scenario: str
    seed: int
    strategy: str
    result: str = "completed"
    final_blood: int = 0
    blood_spent: int = 0
    blood_gained: int = 0
    rounds: int = 0
    focus_used: int = 0
    fast_items_used: int = 0
    clean_harvests: int = 0
    stressed_harvests: int = 0
    ruined_harvests: int = 0
    panic_pulse_used: bool = False
    soft_collapse_used: bool = False
    plea_triggered: bool = False
    grafts_attempted: int = 0
    stable_grafts: int = 0
    unstable_grafts: int = 0
    unstable_results: int = 0
    trade_accepted: bool = False
    anna_greed_attempted: bool = False
    anna_greed_succeeded: bool = False
    blood_bag_uses: int = 0
    critical_rounds: int = 0
    table_choice: str = ""
    actions: dict[str, int] = field(default_factory=dict)
    body_changes: list[str] = field(default_factory=list)
    final_body_summary: str = ""
    probe_metrics: dict[str, object] = field(default_factory=dict)


@dataclass
class ScenarioResult:
    metrics: ScenarioMetrics
    events: list[Event]
    body_summary: dict[str, str]
    notes: list[str] = field(default_factory=list)
