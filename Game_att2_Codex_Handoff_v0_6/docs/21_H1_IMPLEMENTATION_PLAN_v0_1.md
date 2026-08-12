# Game att2 — H1 Implementation Plan v0.1

Status date: 2026-08-12

Status: owner-approved for execution on 2026-08-11 against
`20_H1_HYBRID_COMBAT_SPEC_v0_1.md`. This approval opens only the bounded H1 research
implementation described here. Exact H1 comparison values remain provisional research
data. The bounded implementation passed its automated fidelity gate on 2026-08-12;
see `22_H1_IMPLEMENTATION_RESULTS_v0_1.md`.

## 1. Planned outcome

Implement one isolated, deterministic H1 research slice that can:

- construct the controlled post-Jeff versus Anna fixture;
- compare prepared and unprepared Block;
- reject Block when its body source is illegal;
- distinguish ordinary and disclosed high-risk failure;
- grade scripted and human timing input through the same resolver;
- apply only approved limb-integrity consequences;
- recompute the grafted Right Arm's defensive capability;
- export inspectable JSON and Markdown evidence;
- leave all seven current simulator scenarios and the playable campaign unchanged by
  default.

The implementation is a research instrument, not a production combat system.

## 2. Binding constraints

The implementation must preserve:

- Combat Rules v0.5 behavior outside an explicitly invoked H1 run;
- exactly one committed Main action per actor per round;
- Guard Flesh's existing Blood cost, Right-Arm source, one-round lifetime, and single
  current damage reduction;
- source revalidation before consequence resolution;
- ordinary limb damage producing no invented Blood loss;
- injected RNG for existing random branches and recorded timing input for H1 grades;
- silent domain systems with structured events rendered at the boundary;
- zero new runtime dependencies;
- the approved digital content scope: S-001 → Jeff → emergency graft → Anna → Table.

H1 must not enter `scenarios_v0_1.yaml` as an eighth approved scenario. It is a
separate research runner and evidence class.

## 3. Current seams to reuse

| Existing surface | Current ownership | Planned H1 use |
|---|---|---|
| `models.py` | Immutable definitions and mutable combat state | Reuse `CombatantRuntime`, `EnemyIntent`, `LimbRuntime`, and `Event` without adding H1 flags to general combatants. |
| `rules.py` | Action legality, costs, damage, Guard, limb state, enemy attacks | Preserve default behavior; accept one optional resolved attack modifier at the existing enemy-attack boundary. |
| `events.py` | Structured ordered event log | Record opportunity, validation, timing, grade, modifier, exposure, and capability recomputation. |
| `config_loader.py` | Current v0.5/content/scenario configuration | Leave current loader contract unchanged; H1 uses a separate validated loader. |
| `factory.py` | Player/enemy construction from current content | Build S-001, Jeff's Right Arm, and Anna from existing definitions. |
| `rng.py` | Seeded/scripted randomness | Script the emergency-graft/Anna branches used by the fixture; timing grades do not use RNG. |
| `research_shell.py` | Current evidence/session conventions | Reuse evidence-class and export principles, not its full campaign state machine. |
| `reporting.py` | Text/JSON/Markdown boundary patterns | Reuse serialization conventions where practical; do not add printing to H1 domain modules. |

## 4. Planned file surface

### New authored files

| File | Contract |
|---|---|
| `config/h1_reflex_v0_1.yaml` | H1-only timing profiles, tier labels, grade bands, mitigation modifiers, high-risk exposure, schema/version/status markers. |
| `src/game_att2_sim/h1_config.py` | Strict loader and validation for the H1-only configuration. |
| `src/game_att2_sim/reflex.py` | Frozen H1 definition/input/result types plus pure legality and grade resolution. No printing and no direct narrative/outcome selection. |
| `src/game_att2_sim/h1_research.py` | Controlled fixture builder, comparison runner, consequence orchestration, metrics, and exports. |
| `src/game_att2_sim/h1_cli.py` | Thin standard-library CLI for scripted replay and optional diagnostic timing input. |
| `tests/unit/test_h1_config.py` | H1 schema, range, ordering, reference, and status validation. |
| `tests/unit/test_reflex.py` | Pure legality, grading, risk, assisted-profile, and source-invalidation tests. |
| `tests/integration/test_h1_research.py` | H1-C1 through H1-C6, causal events, replay, and current-scenario isolation. |
| `tests/integration/test_h1_cli.py` | CLI argument, script, output, failure, and deterministic replay tests. |
| `examples/h1_scripted_comparisons.json` | Versioned scripted timing inputs covering required grades and negative paths. |
| `research/h1/README.md` | Evidence classes, output schema, contamination rules, and operator instructions. |

### Narrow modifications to existing files

| File | Maximum planned change |
|---|---|
| `rules.py` | Add an optional, default-neutral resolved attack modifier to `enemy_attack`; apply it through existing damage/state functions and emit structured events. |
| `tests/unit/test_causal_integrity.py` | Prove the default enemy-attack path is unchanged and an invalid reflex source cannot mutate or consume state. |
| `tests/README.md` | Document the separate H1 test layer and commands. |
| `README.md` | Document H1 research invocation and repeat the non-production evidence boundary. |
| `docs/20_H1_HYBRID_COMBAT_SPEC_v0_1.md` | Add the implementation result link only after work passes. |
| `docs/08_DECISIONS_RISKS_OPEN_QUESTIONS.md` | Record implementation status only after the gate is executed and verified. |

No initial H1 implementation should modify `content_v0_1.yaml`,
`scenarios_v0_1.yaml`, Encounter 3 files, or the playable campaign controller.

## 5. Planned domain contracts

Names are reversible technical choices. Their separation is binding.

### H1 configuration

```text
H1Config
  schema_version
  spec_version
  implementation_status = research_only
  timing_profiles
  grade_order
  mitigation_by_grade
  high_risk_exposure_by_grade
  fixture_parameters
```

Validation must reject:

- missing or duplicate profile IDs;
- negative timing bounds, damage, or exposure;
- overlapping or unordered grade bands;
- mitigation outside the configured neutral-to-full range;
- a routine miss that adds exposure;
- a high-risk exposure without an affected source;
- unknown tier, grade, intent, slot, action, or fixture IDs;
- any status other than `research_only` for v0.1;
- wound-to-Blood, Ruined Torso lethality, Warden, or production-content keys.

Use integer timing units and integer mitigation basis points in configuration. Human
clock input is converted at the boundary; the resolver does not depend on operating
system time or floating-point thresholds.

### Pure reflex types

```text
ReflexTier          ROUTINE / SIGNIFICANT / CRITICAL
ExecutionGrade      MISS / LIMITED / STRONG / EXCEPTIONAL
RiskClass           ORDINARY / HIGH_RISK
TimingProfile       immutable grade bands and assisted marker
ReflexContext       action/source/target/telegraph/commitment/body facts
ReflexAttempt       selected source, risk class, profile, recorded input
ReflexAvailability legal flag plus one disabled reason
AttackModifier      damage modifier, declared source exposure, grade metadata
ReflexResolution    availability, grade, modifier, and evidence fields
```

`reflex.py` may inspect supplied state facts, but must not mutate combatants, spend
Blood, apply damage, print, use RNG, or resolve encounter outcomes.

### Shared attack bridge

The planned `RuleEngine.enemy_attack` change is:

```text
current arguments
+ optional resolved AttackModifier = neutral
```

Resolution order:

```text
revalidate enemy source
→ calculate source-impaired base damage
→ apply existing Guard Flesh reduction at most once
→ apply the H1 modifier to the remaining damage
→ apply final target integrity damage through existing apply_damage
→ apply only declared Right-Arm exposure through existing apply_damage
→ resolve existing Surgical Jab Bleeding rule without inventing Blood loss
→ recompute and log Block/Guard capability
```

Prepared Guard improves the timing profile/result floor in H1; it does not apply a
second hidden Guard Flesh reduction. Existing non-H1 callers omit the modifier and
must produce byte-for-byte equivalent event meaning and identical seeded outcomes.

## 6. Controlled fixture plan

`h1_research.py` builds `H1-F0` from current definitions:

1. Create S-001 with `player_from_start`.
2. Create Jeff only to source the existing Right Arm definition.
3. Use existing harvest/emergency-graft rules with scripted RNG to create a controlled
   usable graft; do not hard-code a duplicate arm definition.
4. Create Anna with `enemy_from_config`.
5. Set the research-shell fixture intent: Surgical Jab, Anna Right Arm, player Torso.
6. Apply only the named comparison override.
7. Run one Preparation/Main/Block/consequence slice.
8. Export prior state, legality, timing, grade, mutations, and recomputed capability.

The Torso target remains a fixture-only choice and is not added to Anna's general
content definition.

### Comparison execution

| Comparison | Implementation mechanism | Required assertion |
|---|---|---|
| H1-C1 prepared/unprepared | Guard Flesh Main action versus another legal/non-Guard commitment | Guard changes a declared timing/outcome dimension and applies its current reduction once. |
| H1-C2 usable/unusable arm | Paired snapshot override before Block validation | Exceptional input cannot bypass missing/disabled source. |
| H1-C3 ordinary/high-risk | Paired `RiskClass` with identical input | Ordinary miss adds nothing; high-risk miss applies only previewed arm exposure. |
| H1-C4 intent clarity | Broad/partial/exact context with identical state | Availability/profile differences match configuration and are logged. |
| H1-C5 precise/assisted | Same context/input through two timing profiles | Same legality and consequence pipeline; only profile-derived grade may differ. |
| H1-C6 threshold pressure | Controlled Torso integrity near an approved state threshold | Exceptional legal Block may preserve the threshold; no downstream wound/death claim. |

## 7. Work packages and gates

### WP0 — Baseline and branch

Planned actions:

- create `codex/h1-hybrid-combat` from the reviewed documentation baseline;
- run and record the full current verification suite and seeded outputs;
- save no generated caches or local feedback records.

Gate: the current suite, Ruff, strict mypy, seven-scenario report, and scripted playable
campaign pass before any H1 code change.

### WP1 — Configuration and immutable contracts

Implement `h1_reflex_v0_1.yaml`, `h1_config.py`, and the frozen types in `reflex.py`.

Requirements: H1-RQ-002, H1-RQ-010, H1-RQ-012.

Gate: invalid values and prohibited categories fail loudly; current `load_config()`
loads exactly as before without requiring the H1 file.

### WP2 — Pure opportunity and grade resolver

Implement:

- source, telegraph, target, commitment, affordability, and condition validation;
- deterministic timing-grade calculation;
- ordinary versus high-risk result construction;
- precise and assisted timing profiles through one resolver.

Requirements: H1-RQ-001, H1-RQ-002, H1-RQ-003, H1-RQ-005, H1-RQ-006,
H1-RQ-007, H1-RQ-009, H1-RQ-010.

Gate: pure unit tests cover every grade boundary, invalid source, incompatible
commitment, ordinary miss, high-risk preview/exposure, and exceptional illegal input.

### WP3 — Shared consequence bridge

Add the default-neutral attack modifier seam to `RuleEngine.enemy_attack` and apply
the resolved modifier through existing damage/event functions.

Requirements: H1-RQ-003, H1-RQ-004, H1-RQ-005, H1-RQ-006, H1-RQ-007,
H1-RQ-008, H1-RQ-009, H1-RQ-012.

Gate:

- all existing enemy-attack and Guard tests pass unchanged;
- default non-H1 calls retain identical event sequences for pinned seeds;
- Guard reduction occurs once;
- exposure changes only the declared Right Arm integrity/state;
- no limb damage creates Blood loss.

### WP4 — H1 fixture, comparisons, and evidence

Implement the fixture and all H1-C1 through H1-C6 paired runs. Emit separate events
for opportunity, validation, input, grade, modifier, exposure, and capability view.

Requirements: all H1-RQ-001 through H1-RQ-012.

Gate: paired runs differ only by the named comparison condition; scripted reruns are
identical; every requirement has a direct test and evidence field.

### WP5 — Scripted and diagnostic input boundary

Implement `h1_cli.py` with:

- `--script PATH` deterministic replay;
- `--comparison ID` and `--all-comparisons`;
- `--profile precise|assisted`;
- JSON and Markdown output;
- optional terminal timing capture using only the Python standard library;
- explicit `AUTOMATED_REGRESSION` or `OWNER_DIAGNOSTIC` evidence labels.

Do not collect participant identity, upload data, or call external services.

Requirements: H1-RQ-010, H1-RQ-011.

Gate: scripted CLI replay is deterministic; human timing records raw input separately
from derived grade; malformed scripts fail without partial evidence output.

### WP6 — Full verification and evidence report

Run focused tests first, then the complete repository gate. Produce a documentation
report that separates rule fidelity from experience claims.

Gate: all H1 acceptance items in the specification pass; all prior scenarios and CLI
replays remain unchanged; hostile review has no P0/P1 finding.

## 8. Requirement-to-implementation trace

| Requirement | Primary implementation | Primary tests/evidence |
|---|---|---|
| H1-RQ-001 | `reflex.py`, `h1_research.py` | prepared/unprepared and intent paired tests |
| H1-RQ-002 | `h1_reflex_v0_1.yaml`, `h1_config.py`, `reflex.py` | tier/profile validation and grade tests |
| H1-RQ-003 | `reflex.py`, optional `rules.py` bridge | missing/disabled/committed-source negative tests |
| H1-RQ-004 | existing Guard plus prepared profile | H1-C1 and single-reduction regression |
| H1-RQ-005 | ordinary miss resolution | exact original-consequence comparison |
| H1-RQ-006 | high-risk attempt and modifier | preview, consent, source exposure, no-unrelated-effect tests |
| H1-RQ-007 | pure `AttackModifier`/`ReflexResolution` | assert no resolution/outcome field or event is written |
| H1-RQ-008 | fixture consequence plus capability recomputation | H1-C2 and post-exposure availability tests |
| H1-RQ-009 | validation before grading/application | exceptional input with illegal source test |
| H1-RQ-010 | two timing profiles, one resolver | precise/assisted parity tests |
| H1-RQ-011 | `h1_research.py`, `h1_cli.py`, structured events | identical scripted replay and export-schema tests |
| H1-RQ-012 | isolated config and existing damage functions | prohibited-key validation and zero Blood-transaction assertion |

## 9. Planned event vocabulary

The implementation may add these structured event types:

```text
h1_fixture_started
reflex_opportunity_offered
reflex_opportunity_denied
reflex_opportunity_cancelled
reflex_risk_previewed
reflex_input_recorded
reflex_grade_resolved
reflex_modifier_applied
reflex_source_exposed
reflex_capability_recomputed
h1_comparison_completed
```

Every event includes the fixture/comparison ID and spec/config versions. Events record
facts; renderers create prose.

## 10. Planned tests

### Unit

- H1 configuration schema, ordering, bounds, and prohibited keys;
- every exact grade boundary for precise and assisted profiles;
- ordinary miss neutrality;
- explicit high-risk exposure only;
- unusable, missing, incompatible, Downed, unaffordable, and insufficient-telegraph
  rejection;
- exceptional input cannot change illegality;
- resolver purity and immutability;
- Guard single-application and default attack equivalence.

### Integration

- all six paired comparisons;
- source invalidation between offer and resolution causes cancellation;
- Right-Arm exposure crosses an approved integrity threshold and removes capability;
- threshold-pressure Torso comparison stops before an unapproved downstream rule;
- scripted input produces identical events and exports twice;
- precise/assisted use the same legality and consequence route;
- current seven scenarios retain pinned seed-42 outputs;
- current playable and research scripted replays remain valid.

### Human evidence boundary

Automated tests may establish correctness, reachability, determinism, and causal
traceability. Owner diagnostics may find comprehension or control problems but do not
establish fun or accessibility. External human claims require a separately approved
protocol and consent record.

## 11. Planned verification commands

From `Game_att2_Codex_Handoff_v0_6/`:

```powershell
python -m pytest -q tests/unit/test_h1_config.py tests/unit/test_reflex.py
python -m pytest -q tests/integration/test_h1_research.py tests/integration/test_h1_cli.py
python -m pytest -q
python -m pytest --cov=game_att2_sim --cov-report=term-missing -q
python -m ruff check src tests
python -m mypy src
python -m game_att2_sim --all-scenarios --seed 42 --format markdown
python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_full_campaign_sequence.json
python -m game_att2_sim.h1_cli --all-comparisons --script examples/h1_scripted_comparisons.json --format json
```

Repeat the final H1 command and compare event/export content byte-for-byte after
removing only explicitly nondeterministic file metadata, if any. Prefer emitting no
nondeterministic metadata.

## 12. Provisional-value protocol

Exact timing bands, mitigation basis points, and exposure damage are not owner-level
decisions. During implementation:

1. place them only in `h1_reflex_v0_1.yaml`;
2. label them `PROVISIONAL_H1_RESEARCH_ONLY`;
3. choose the smallest internally coherent baseline plus comparison profile;
4. never change Combat Rules v0.5 or existing Guard values to make H1 pass;
5. report sensitivity rather than declaring a winner;
6. escalate only if every reasonable value range contradicts an owner-level decision.

## 13. Risks and controls

| Risk | Severity | Control |
|---|---:|---|
| Parallel combat engine | P1 | Pure resolver returns a modifier; shared RuleEngine remains mutation authority. |
| Guard reduction applied twice | P1 | Fixed resolution order and dedicated regression test. |
| Reflex bypasses source/body state | P1 | Revalidate before grade application and test exceptional illegal input. |
| Timing creates nondeterministic regression | P1 | Scripted integer input is authoritative for tests; raw human input is recorded/replayable. |
| H1 values leak into v0.5 | P1 | Separate research-only config and loader; no content/scenario YAML edits. |
| Source exposure invents wounds/Blood | P1 | Apply integrity damage only; assert zero Blood transactions. |
| Assisted profile uses different rules | P1 | Same resolver/context; timing profile is the only changed condition. |
| H1 expands into movement/counters/UI | P1 | One Block family, one fixture, thin terminal boundary, stop condition. |
| Current campaign changes accidentally | P1 | Default-neutral bridge plus pinned scenarios and scripted CLI regression. |
| Diagnostic evidence becomes product claim | P1 | Evidence-class labels and explicit claim boundary in every report. |

## 14. Stop and rollback conditions

Stop implementation and return for owner review if:

- H1 requires a new wound/Blood or Ruined Torso rule;
- prepared Block cannot be represented without changing Guard Flesh's current default
  behavior outside H1;
- the optional attack seam changes current seeded outputs;
- a legal Block requires movement, Stamina, Cover It, Counter, or another deferred
  subsystem;
- exceptional execution can only matter by bypassing source legality;
- the H1 fixture requires new Anna content or personality;
- a P0/P1 hostile-review finding cannot be removed narrowly.

Rollback is straightforward because H1 remains isolated: remove the H1 modules,
config, tests, examples, and optional neutral modifier seam. Existing scenarios and
campaign data are not migrated.

## 15. Execution approval gate — passed 2026-08-11

The owner approved this plan for execution on 2026-08-11. Approval opens only the H1
research implementation described here. It does not approve:

- final timing or balance values;
- broader reflex response families;
- active Cover It, wounds, movement, negotiation, or new content;
- Encounter 3 runtime work;
- Unity or production-game work;
- claims of fun, balance, comprehension, or accessibility.
