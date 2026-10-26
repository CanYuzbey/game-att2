# V3 Full-Fidelity Master — sequential chunk 05/12

Death / incapacity / surrender / bargain / mercy / escape / mutual success / objective completion must follow state + motivation.

## 13. Anti-psychology rule

No invented fear/sanity/personality mechanics to force desired ending.

## 14. Historical Plead Pressure

V1 threshold system is legacy.
V3 Will/claim system supersedes generic Plead Pressure as active sample surrender grammar.
Specific future personality pressure may still be authored through explicit Will/motivation rules.

---

# SOURCE DOCUMENT: docs/09_WORLD_NPC_PURPOSE_RUN_AND_PROGRESSION_V3_FULL.md

# World, NPC Purpose, Run, Reset, and Progression V3 — Full

**Status:** ACTIVE DIRECTION + OPEN FULL-GAME STRUCTURE

## 1. NPC purpose contract

Consequential actors should have:
Goal / Need / Want / RedLine / Leverage / Claim / optional counterclaim / Concession / Fallback.

Capability and RiskTolerance separate.

## 2. Four observable purpose moments — inherited V2 working contract

1. Goal-related activity before interaction;
2. readable Want/RedLine during contact;
3. goal-consistent conflict behavior;
4. post-result action advancing/revising Goal.

This is preferred to full off-screen life simulation.

## 3. Faction-role-individual

Faction doctrine
→ current role/duty
→ individual Goal/Need/RedLine/Claim.

Faction does not define morality/aggression/strength.

## 4. Purpose-family research fixtures

Historical V2 examples, not lore canon:
- Blood accumulators/Houses;
- Flesh guilds/grafters;
- Wardens/authorities;
- Hunters/claimants;
- free/unaffiliated.

Keep as authoring test families only.

## 5. G1 Guard comparison

Research fixture, not canon:
- Guard has failing guarding arm before duty inspection;
- wants Full compatible Right Arm or 20 Blood;
- starts comparison from 70 Blood/full body;
- Blood branch → 50 Blood/full body;
- Arm branch → 60 Blood/Missing Right Arm/Controlled stump after provisional 10-Blood procedure consequence.

Retained because it is a useful exact sacrifice/concession fixture.
Not promoted into V3 content without later content approval.

## 6. Underground City

Bounded sample container remains active direction.

World treats bodies/limbs/Blood as practical assets.
One connected section preferred over open world.

## 7. Destination landmark / level-design hypothesis

V2 proposed persistent upward-light/tunnel destination.
Preserve as presentation/level research only.

## 8. Same-day reset

Active:
aware protagonist repeats day;
unaware world resets.

Persistent:
- protagonist knowledge;
- abstract concept vocabulary;
- earned Concept Decks;
- earned Brain Parts.

Reset:
- flesh/grafts/wounds;
- unaware world;
- temporary instability.

No death-generated Memory Card.

## 9. Same-day opportunity consistency

World must not inspect player's current Blood and secretly alter whether desired limb/opportunity exists.

Different outcomes should follow changed choices/routes, not adaptive reward denial.

## 10. Full-game run

OPEN:
- run start/end;
- topology;
- checkpoints;
- failure short of death;
- long-term reset;
- ultimate goal;
- 10–12 hour shape.

## 11. Progression split

Concept Deck:
achievement/non-boss milestone path.

Brain Part:
boss/progression path.

Do not collapse to one generic permanent-power ladder.

## 12. Art-direction hypothesis from V2

Research-only:
- fixed-angle stylized low-poly 3D;
- modular silhouettes/shared attachment grammar;
- 2D card/portrait/UI;
- restrained palette;
- gore as state-readable graphic design;
- pixel art and high-fidelity realism excluded from first slice.

V3 does not promote final art style yet.

## 13. Engine hypothesis from V2

Unity 6 + C# owner-preferred working hypothesis.
Blender/Krita/Audacity pipeline suggestion.
Godot fallback.
Unreal rejected unless fidelity/team context changes.

V3 current position:
engine remains open until V3-1 implementation vehicle is chosen.
The historical one-room spike criteria remain useful:
fixed camera navigation, body swap, card/intent overlay, bounded input, deterministic mutation, Windows build.

## 14. Commercial comparisons

Historical V2:
10–12 hour full-game hypothesis;
USD 8–12 comparison.

Preserve as non-evidence commercial hypotheses.
No pricing/store decision exists.

---

# SOURCE DOCUMENT: docs/10_FIRST_PLAYABLE_AND_CONTENT_CATALOG_V3_FULL.md

# First Playable and Content Catalog V3 — Full

**Status:** ACTIVE CONTENT BOUNDARY; IDENTITIES/VALUES PARTLY OPEN

## Gate V3-1 fixture

Minimum:
- 3 body/source families;
- enough cards to test class guarantees and source weighting;
- 2 Brain architectures;
- one source-degradation chain;
- Yellow/Red attacks;
- Drop/Focus/Blood Redraw candidates;
- deterministic logs.

No story required.

## Source family roles

1. Human baseline — precision/control/readable defense.
2. Heavy abnormal limb — powerful/heavy, distinct intrinsic weights/cost profile.
3. Complementary non-arm source — proves Head/Core/Legs card generation.

Names are placeholders until content choice.

## V3-2
Body A → real loss → graft → Body B → later fight.

## V3-3
Add:
Blood pressure + chosen sacrifice + kill/surrender reward.

## V3-4
One gate-boss-style test actor, multiple body solutions.

## V3-5 sample

Captive Guard
→ Fight A
→ graft
→ Fight B
→ boss
→ escape/reset.

## 3–4 graft families

Need functionally distinct:
- raw power;
- precision/control;
- defense/utility;
- physiology/complementary.

## Multi-source synergy

At least one systemic synergy.
Optional one rare signature pairing.

## Identity sacrifice

At least one explicit choice with persistent record.

## Readied Item

If first sample includes inventory, use only the minimum item(s) needed to prove the lane.
Do not import V1 item roster wholesale.

## Concept Deck

First sample may include one tiny inherited/persistent Concept Deck only if needed to prove the boundary.
Do not create full achievement catalog.

## Brain Part

First sample may include one boss/progression Brain Part only if needed to prove persistence/paired tradeoff.
Do not build tree/collection.

## Legacy V1 content catalog

S-001, Jeff, Anna, Grafting Table v0.2, Blood Bag, Clotting Cream, Bone Scissors, Hell Saw, Claim the Cut, Black Stitch remain fully documented in `legacy/00_LEGACY_MECHANICS_AND_FIXTURES_LEDGER.md`.

They are not active V3 content automatically.

## Warden

Minotaur Warden remains historical paper research.
No automatic V3 boss promotion.

## Content admission rule

Every new room/enemy/item/limb/card must name:
- proof question;
- unique decision;
- systems touched;
- evidence gained;
- why existing content cannot answer it.

Otherwise cut/defer.

---

# SOURCE DOCUMENT: docs/11_TECHNICAL_ARCHITECTURE_DATA_AND_EVENTS_V3_FULL.md

# Technical Architecture, Data, Events, and Determinism V3 — Full

**Status:** BINDING TECHNICAL BOUNDARIES; ENGINE-NEUTRAL

## Quality goals inherited from V1

- deterministic/reproducible evidence mode;
- config-driven tunables;
- explicit timing/ownership;
- high rule-test coverage;
- readable structured events;
- safe invalid-state failure;
- no unnecessary framework;
- definitions immutable;
- runtime state explicit.

## Recommended ownership

### Definition layer
BodySourceDefinition
ExpressionDefinition
ConceptDeckDefinition
BrainArchitectureDefinition
BrainPartDefinition
ItemDefinition
ProcedureDefinition
EncounterActorDefinition

### Runtime
ActorState
BodyState
SourceState
WoundState
BloodState
ConceptState
BrainState
AttentionState
InventoryState
WillState
EncounterState
SacrificeRecord

### Services
RuleEngine
CapabilityResolver
AttentionResolver
BloodSystem
WoundSystem
GraftSystem
DefenseResolver
Will/ClaimResolver
InventoryResolver
RNGService
EventRecorder
Reporting/Telemetry boundary

## RuleEngine authority

Own:
legality, costs, action budget, atomic commitment, state mutation, procedure chain.

Presentation does not mutate gameplay.

## RNG

No domain global random.
Provide:
- seeded;
- scripted/fake;
- production random behind interface.

Record seed/roll for evidence.

## Definition/runtime separation

Never mutate shared definitions.

## Error families

Recommended:
ConfigValidationError
IllegalActionError
InvalidTargetError
InsufficientBloodError
InvalidStateTransitionError
ScenarioDefinitionError
EmptyAttentionPoolError where appropriate.

No broad silent catch.

## Data validation

Validate:
unique IDs;
body slots;
nonnegative weights/costs unless signed transaction;
references;
source-slot compatibility;
Brain distribution constraints;
Concept exchange references;
item/source references;
no impossible exact source;
no illegal duplicate instance rules.

## Action transaction

```text
preview
→ lock
→ revalidate
→ apply lock costs if any
→ execution starts
→ apply execution costs/uses
→ atomic effect chain
→ derived recomputation
→ event record
```

Rejected pre-commit attempts:
- no action-budget mutation;
- no gameplay RNG mutation;
- no cost.

## Event contract

Minimum:
sequence, round/phase, actor, event_type,
source(s), target(s), rule_id,
before/after relevant state,
Blood delta,
action-budget delta,
RNG metadata,
invalid/cancel reason.

## Attention trace

slot, role, candidate expressions,
rejection reasons,
base weight,
Brain factor,
recency factor,
source-state factor,
Concept factor,
context factor,
normalized probability,
RNG roll,
selection.

## Reporting

Human-readable + machine-readable.
V1 supported text/JSON/Markdown; V3 should preserve equivalent inspectability even if format changes.

## Metrics boundary

Domain systems emit state/events.
Reporting renders.
No direct domain printing.

## Enemy AI

AI can rank/select only legal available opportunities.
No behavior tree/framework required until complexity demands it.

## Performance

Correctness/inspectability first.
Avoid accidental quadratic event processing.
Statistical Attention testing should support thousands of seeded refreshes pragmatically.

## Persistence architecture

Separate:
same-day reset state;
persistent protagonist knowledge;
persistent Concept Deck ownership;
persistent Brain Part ownership;
temporary instability;
sacrifice/provenance records according to authored persistence.

Exact save format OPEN.

---

# SOURCE DOCUMENT: docs/12_CONFIG_SCHEMA_AND_TUNABLE_AUTHORITY_V3.md

# Config Schema and Tunable Authority V3

**Status:** BINDING CONFIG GOVERNANCE

## Rule

Config may vary a mechanic; it cannot invent or redefine one.

## Config groups

### body_sources
IDs, slot, capability tags, expressions, intrinsic Attention weights, composition/maintenance values.

### expressions
concept, class/labels, sources, min state, target, cost, effect, degraded profile, interceptability.

### concepts
abstract concept metadata only.

### concept_decks
requirements, exchanges, biases, dedicated special expressions, persistence metadata.

### brains
slot architecture, hard guarantees, flexible distributions, allowed bias dimensions.

### brain_parts
one primary lever, buff, nerf/risk, allowed attachment/config boundary.

### attention
recency profile, refresh lifecycle, selection method, evidence logging.

### inventory
item instance definition, uses, expiry, sources, timing, cost timing.

### wounds
family, escalation, periodic pressure, treatment requirements.

### procedures
graft/treatment/repair definitions.

### defense
cue timing, response windows, eligibility, research profiles.

### will
explicit mutation values and thresholds when approved.

### encounter
actor definitions/goals/claims/content fixtures.

## OPEN handling

Do not place fake numbers in production config merely to satisfy schema.

Use:
- null/disabled;
- explicit research overlay;
- test fixture value;
with status metadata.

## Versioning

Every evidence report records:
- rules/spec version;
- config version/hash;
- seed;
- build/commit.

## Migration

Changing semantic meaning requires rules/doc migration, not config-only edit.
