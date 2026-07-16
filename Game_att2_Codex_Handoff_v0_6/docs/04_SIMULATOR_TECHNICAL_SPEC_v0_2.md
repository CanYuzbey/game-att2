# Game att2 — Simulator Technical Specification v0.2

## 1. Purpose

Implement an inspectable rules simulator. It is not a UI prototype and not an engine architecture commitment.

## 2. Quality goals

- deterministic and reproducible;
- easy to modify through config;
- explicit timing and ownership;
- high unit-test coverage for rules;
- readable event logs;
- no unnecessary framework or runtime dependency;
- safe failure on invalid data/state.

## 3. Proposed repository layout

```text
src/game_att2_sim/
  __init__.py
  __main__.py
  cli.py
  enums.py
  errors.py
  definitions.py
  state.py
  config_loader.py
  rng.py
  events.py
  metrics.py
  systems/
    blood.py
    limbs.py
    actions.py
    rounds.py
    harvest.py
    grafts.py
    plead.py
    table.py
  encounters/
    base.py
    jeff.py
    anna.py
  strategies/
    base.py
    balanced.py
    blood_hoarder.py
    limb_greed.py
    survival_first.py
    reckless_sever.py
  scenarios/
    runner.py
    catalog.py
  reporting/
    text.py
    json_report.py
    markdown.py

tests/
  unit/
  integration/
  scenarios/
```

Equivalent grouping is allowed if module boundaries remain clear.

## 4. Definition/runtime separation

### Definitions

Immutable content loaded from config:

- limb definitions;
- action definitions;
- item definitions;
- encounter definitions;
- table option definitions;
- numeric rules.

### Runtime state

Mutable per run/fight:

- limb integrity/state/tags;
- blood;
- inventory uses;
- Plead Pressure;
- unstable queued effects;
- current intent;
- fight-level passives used;
- event stream and metrics.

Never mutate shared definitions.

## 5. Core types

```python
class Slot(Enum):
    HEAD = "head"
    TORSO = "torso"
    LEFT_ARM = "left_arm"
    RIGHT_ARM = "right_arm"
    LEGS = "legs"
    CORE = "core"

class LimbState(Enum):
    INTACT = "intact"
    DAMAGED = "damaged"
    CRITICAL = "critical"
    DISABLED = "disabled"
    SEVERED = "severed"
    MISSING = "missing"
    RUINED = "ruined"

class LimbTag(Enum):
    BLEEDING = "bleeding"
    GRAFTED = "grafted"
    UNSTABLE = "unstable"
    INTEGRATED = "integrated"
    STABILIZED = "stabilized"
    MARKED = "marked"
    HANGING = "hanging"
    PROTECTED = "protected"
```

Other enums should cover timing, damage type, harvest quality, event type, intent clarity, and scenario result.

## 6. Suggested dataclasses

```python
@dataclass(frozen=True)
class LimbDefinition:
    id: str
    name: str
    slot: Slot
    max_integrity: int
    size: str
    action_ids: tuple[str, ...] = ()
    passive_ids: tuple[str, ...] = ()

@dataclass
class LimbRuntime:
    definition: LimbDefinition
    integrity: int
    state: LimbState
    tags: set[LimbTag]
    disabled_rounds: int = 0

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
    plead_pressure: int = 0
    panic_pulse_used: bool = False
    soft_collapse_used: bool = False

@dataclass(frozen=True)
class ActionDefinition:
    id: str
    name: str
    timing: str
    base_cost: int
    source_slot: Slot | None
    source_item: str | None
    damage: int = 0
    damage_type: str | None = None
    can_clean_sever: bool = False

@dataclass(frozen=True)
class EnemyIntent:
    action_id: str
    source_slot: Slot | None
    target_slot: Slot | None
    clarity: str

@dataclass(frozen=True)
class Event:
    sequence: int
    round_number: int
    phase: str
    type: str
    actor_id: str | None
    target_id: str | None
    payload: dict[str, object]
```

Exact names may vary, but equivalent data must be available.

## 7. RNG service

```python
class RNGService(Protocol):
    def randint(self, a: int, b: int) -> int: ...
    def choice(self, values: Sequence[T]) -> T: ...
```

Provide:

- seeded production implementation;
- scripted/fake implementation for tests;
- seed recorded in every scenario report.

No domain module may import and call global random directly.

## 8. Data loading and validation

Load YAML into validated dataclasses. Runtime may use a tiny internal loader or PyYAML if approved; if avoiding runtime dependencies, JSON/TOML conversion is acceptable. The checked-in YAML remains the authoritative handoff data unless Codex documents a format migration.

Validate at startup:

- unique IDs;
- all six starting slots present;
- max integrity > 0 for non-Missing parts;
- integrity in range;
- costs and gains nonnegative unless explicitly a signed transaction;
- actions reference existing sources/items;
- enemy body/action references exist;
- table options reference valid transformations;
- no Clean-sever flag on Grip Strike.

## 9. System contracts

### BloodSystem

Owns blood transactions and threshold triggers. It does not select actions or print.

```python
spend(actor, amount, reason, context) -> list[Event]
gain(actor, amount, reason, context) -> list[Event]
check_panic_pulse(actor, context) -> list[Event]
resolve_collapse(actor, context) -> list[Event]
```

### LimbSystem

Owns integrity, primary state, tags, and usability.

```python
apply_damage(limb, amount, damage_type, extraction_context) -> DamageResult
recalculate_state(limb, zero_outcome) -> LimbState
is_usable_source(limb) -> bool
effectiveness_multiplier(limb) -> Decimal
```

### ActionSystem

Validates phase, source, cost, target, and applies effect through systems.

```python
validate_action(...)
resolve_focus(...)
resolve_fast_item(...)
resolve_main_action(...)
resolve_enemy_action(...)
```

### RoundResolver

Owns phase order only. It delegates effects.

### HarvestSystem

Owns extraction quality and salvage. It does not graft.

### GraftSystem

Owns slot replacement, emergency stability, Unstable checks, and integration.

### PleadSystem

Owns generic Plead Pressure and encounter-specific surrender queries.

### TableSystem

Owns table affordability and transformations.

### Event/Reporting

Systems return structured events. Renderers create console text, JSON, and Markdown.

## 10. Encounter scripts

Use a small explicit interface:

```python
class EncounterScript(Protocol):
    def choose_intent(self, state, rng) -> EnemyIntent: ...
    def post_player_action(self, state, events, rng) -> None: ...
    def check_special_resolution(self, state) -> Resolution | None: ...
```

Jeff and Anna may use straightforward conditionals. Do not build behavior trees, planners, or generalized dialogue engines.

## 11. Player strategies

Strategies select legal actions from current state. They are deterministic given state and RNG.

- Balanced: value survival and desired limb.
- Blood Hoarder: avoid blood costs; verifies exploit gates.
- Limb Greed: maximize harvest value.
- Survival First: use medical/trade options early.
- Reckless Sever: prioritize expensive sever attempts.

Strategies must not bypass action validation.

## 12. Scenario runner

A scenario defines:

- start state;
- encounter sequence;
- player strategy or scripted decisions;
- seed/scripted rolls;
- expected invariants;
- report outputs.

The runner should support a single detailed event log and batches with aggregate metrics.

## 13. CLI

Required flags:

```text
--scenario NAME
--all-scenarios
--seed INTEGER
--strategy NAME
--batch INTEGER
--format text|json|markdown
--output PATH (optional)
--verbose (detailed events)
```

Invalid combinations should produce useful errors and nonzero exit status.

## 14. Metrics

Per run:

- final blood;
- blood spent/gained by reason;
- rounds per encounter;
- Focus and Fast item uses;
- action-frequency counts;
- limb-state transitions;
- Clean/Stressed/Ruined counts;
- emergency graft/stability result;
- Panic Pulse and soft-collapse use;
- plea/trade decisions;
- table choice;
- final body summary;
- run result.

Batch:

- success/collapse rates;
- distributions/means/medians where useful;
- dominant action frequencies;
- path selection rates;
- identical-body outcome rate.

Do not interpret these as player-fun evidence.

## 15. Error handling

Define domain errors such as:

- `ConfigValidationError`;
- `IllegalActionError`;
- `InvalidTargetError`;
- `InsufficientBloodError`;
- `InvalidStateTransitionError`;
- `ScenarioDefinitionError`.

CLI catches and renders them; tests may assert them. Avoid broad silent exception handling.

## 16. Testing and tooling

- `pytest` for tests;
- `ruff` for formatting/linting;
- `mypy` for type checks if feasible;
- coverage report recommended, with emphasis on rule branches rather than arbitrary percentage.

## 17. Performance

No optimization is required beyond avoiding obvious accidental quadratic event processing. A few thousand simulator runs should be practical. Correctness and inspectability dominate.

## 18. Extensibility boundary

Design data-driven definitions so later content can be added, but do not implement future systems. The architecture should make a third encounter possible without requiring one now.
