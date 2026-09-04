# V3 Full-Fidelity Master — sequential chunk 06/12

## Research overlays

Numeric comparisons such as DWF-0.1 or WNR-0.1 live as explicitly labelled overlays and cannot become baseline accidentally.

---

# SOURCE DOCUMENT: docs/13_METRICS_REPORTING_AND_DIAGNOSTICS_V3.md

# Metrics, Reporting, and Diagnostics V3

**Status:** ACTIVE EVIDENCE CONTRACT

## Per action/round

- action source;
- target;
- Preparation/Main usage;
- Blood cost/gain;
- source-state change;
- wound change;
- Will change;
- Attention slots before/after;
- cancellations;
- defense route;
- item use;
- procedure state.

## Attention metrics

- category guarantee satisfaction;
- exact-expression distribution;
- repetition rate;
- source-family exposure;
- damaged-source shift;
- empty/shaded slot rate;
- Focus steering effect;
- Blood redraw usage and result;
- specialization consistency.

## Body metrics

- source degradation count;
- capability gained/lost;
- cards invalidated;
- graft deltas;
- multi-source action availability.

## Economy metrics

- Blood spent/gained by reason;
- collapse/death;
- kill vs surrender selection;
- redraw expenditure;
- maintenance;
- procedure costs.

## Replay metrics

At V3-4/V3-5:
- immediate replay chosen?
- body plan changed?
- why?
- same boss outcome under different bodies;
- strategy diversity.

## V1 historical metrics retained

final Blood, spent/gained, rounds,
Focus/Fast use, Clean/Stressed/Ruined,
Panic/soft collapse, plea, grafts, table choice,
final body, scenario result.

Useful legacy comparison, not complete V3 metrics.

## Body Change Summary

Retain V1 requirement after every meaningful transition:

```text
What changed about the body?
What capability/action/passive became available or unavailable?
What new cost/risk/problem exists?
```

## Intent clarity

Retain V1 measurable information concept:
vague / partial / exact (or equivalent).

V3 hostile intent UI may use a different taxonomy,
but information clarity must be instrumentable.

## Batch interpretation

Statistical strategies/policies are diagnostics only.
Do not infer human choice frequencies/fun from them.

---

# SOURCE DOCUMENT: docs/14_RESEARCH_HUMAN_TEST_AND_CONTAMINATION_V3.md

# Research, Human Test, and Contamination V3

**Status:** BINDING EVIDENCE OPERATIONS

## Evidence classes

- DEV-DIAG
- SELF
- PILOT
- VALID HUMAN
- TARGETED HUMAN
- AUTOMATED DETERMINISTIC
- STATISTICAL DIAGNOSTIC
- EXPERT REVIEW

## Designer self-play

Never counted as blind/external comprehension.

## Raw records

participant anonymous ID,
build/config/seed,
condition,
session timing,
actions,
state,
Attention,
Blood,
facilitator interventions,
deviations,
debrief,
replay behavior.

## V1 P01–P08 legacy

Retain lessons:
- balanced conditions;
- fixed scripts/materials;
- individually moderated;
- raw records;
- contamination separation;
- no mid-batch rule changes.

Completion of old P01–P08 is not automatically a V3 gate.

## V3-1 human questions

- What determines the actions you can physically do?
- What determines which of those you can access now?
- Why was this option unavailable?
- What changed when source degraded?
- Did you have a reasonable response?
- What body/Brain change would you make?

## V3-4 replay

Offer restart before asking leading replay questions.
Record if body plan changes spontaneously.

## Evidence card

Question
→ hypothesis
→ variant
→ expected dynamic
→ desired experience
→ instrumentation
→ continue/revise/kill
→ contamination
→ owner.

## Prohibition

No hallucinated participants, quotes, results, or telemetry.

---

# SOURCE DOCUMENT: docs/15_TEST_PLAN_AND_ACCEPTANCE_V3.md

# Test Plan and Acceptance V3 — Full

**Status:** BINDING VERIFICATION PLAN

## Unit / invariant families

### Config
duplicate IDs, broken refs, impossible source, invalid distribution, negative unsupported values.

### Body
state transitions, source legality, missing/offline behavior, local degradation.

### Action economy
1 Prep / 1 Main, inventory-origin limit, invalid action no mutation.

### Atomicity
commit chain complete, cancellation correct, no half-pay.

### Blood
ledger exact, collapse/fatality order, kill/surrender reward, redraw cost.

### Concept
atomic exchange; incompatible sacrifice fails entire exchange.

### Brain
slot architecture valid; guaranteed/flexible role resolution.

### Attention
legality before probability;
seed determinism;
without-replacement/instance rules if used;
recency;
state weighting;
Focus;
Drop;
redraw;
empty pool.

### Defense
Yellow/Red legality;
Block recipient;
Parry/Evade result;
no fallback route;
expiry.

### Will/claim
named mutations only;
dead actor no surrender;
illegal claim no transfer;
Defy variant if later chosen.

### Inventory
ownership, uses/expiry, source reservation, one inventory-origin action, no substitution.

### Graft
part/slot/cost/quality/provenance/capability update.

### Sacrifice
exact source, preview, persistent record, replacement does not erase record.

## Statistical diagnostics

Attention distributions across:
- seeds;
- Brain architectures;
- source-state changes;
- specialization;
- Concept bias;
- recency;
- redraw.

Economy:
- Blood pressure;
- kill/surrender;
- maintenance.

Do not call these human balance.

## V3-1 pass

- body vs card mental model clear;
- physical capability vs Attention access distinction clear;
- class guarantees prevent "no type of move" frustration;
- source degradation matters;
- defense readable;
- at least two body/Brain configurations yield meaningfully different decision sets.

## V3-2 pass

- graft changes exact legal capability;
- downside visible;
- later fight uses consequence.

## V3-3 pass

- chosen sacrifice remembered;
- replacement not perceived as undo;
- kill/surrender has state-dependent choice;
- Blood creates real cost.

## V3-4 pass

Strong signal:
player wants same boss again to try a different body.

## Historical V1 regression knowledge

Keep tests against:
- free/basic attack creating premium harvest;
- hidden extra Main;
- Guard persistence;
- unlogged Blood;
- disabled source action;
- seed non-reproducibility;
- scenario script overriding source;
- config invalid refs.

## Historical V1 scenario status

Seven old scenarios remain LEGACY EVIDENCE, not mandatory V3 acceptance.

## Evidence result vocabulary

PASS
PASS WITH DEBT
REVISE
REJECT
ARCHIVE/RESEARCH ONLY.

## V3-1 Hardening regression set V3-RQ-053..056

Automated acceptance must include:

- same state + same seed → identical Attention selection;
- an Offline source contributes zero selected expressions over large seeded batches;
- a guaranteed duty never fills with a wrong action class;
- a guaranteed duty shades when no legal expression exists;
- architecture coverage reports insufficient available expressions;
- recency soft-suppresses without becoming a hard cooldown;
- degraded source weighting can reduce access without necessarily invalidating the expression;
- deliberate specialization may raise consistency;
- additional duplicate duties shade when specialization leaves too few distinct legal expressions;
- redraw with no legal alternative returns a no-spend result;
- redraw with alternatives never returns the current expression as the “alternative”;
- Yellow/Red defence legality and one-Preparation/one-Main remain regression-tested.

---

# SOURCE DOCUMENT: docs/16_ACCESSIBILITY_PRESENTATION_ART_AUDIO_V3.md

# Accessibility, Presentation, Art, and Audio V3

**Status:** ACTIVE REQUIREMENTS + WORKING PRESENTATION HYPOTHESES

## Core readability

Before commitment:
action, labels/class, source, source condition,
target, timing, Blood/cost, risk,
interception/reflex route,
capability loss,
Dormant/Invalid reason.

## Physical illegality vs Attention absence

UI must clearly distinguish:
- body cannot do it;
- body can do it but it is not currently surfaced.

## Probability presentation

No exact Attention equation by default.
Qualitative tendency communication.

## Threat cue accessibility

No color-only Yellow/Red.
Add shape/icon/motion/audio/text redundancy.

## Timing assists

Independent timing/speed/automation options are valid design families.
Do not reduce strategic reward merely for accessibility.

## Input

Remapping, tap/hold alternatives, latency calibration/practice are retained V2 accessibility recommendations.

## Text

Readable/scalable text.

## Audio

No critical audio-only information.
Captions/subtitles where dialogue/critical sound conveys state.

## Motion

Reduced-motion alternative where cut-ins/camera movement are intense.

## Historical presentation directions

### V1
Hybrid table decisions + side/body action cut-ins was locked for prototype at one stage.

### V2
Paused in-world interaction over visible exploration became active paper direction.
Fixed-angle stylized low-poly 3D became art working hypothesis.

### V3
No final camera/UI/art style locked.
Both historical directions are inputs to later interaction testing.
The stronger current requirement is uninterrupted causal/readable body state.

## Art/audio production gate

Final assets only after direction/prototype proves interaction.
AI-generated art/audio stays concept/placeholder until consistency, cleanup, licensing, and commercial review.

---

# SOURCE DOCUMENT: docs/17_PRODUCTION_OPERATIONS_LEGAL_RELEASE_AND_AI_GOVERNANCE_V3.md

# Production Operations, Legal/Release, and AI Governance V3

**Status:** BINDING PROCESS

## Role

Operate as skeptical senior game-design, engineering, QA, UX, research and production leadership.

## User authority

Owner controls identity/creative/irreversible decisions.
Reversible experience-neutral implementation may be delegated.

## Evidence labels

Fact / assumption / inference / recommendation / approved / open / risk.

## Maturity

Idea → concept → prototype → first playable → vertical slice → production → alpha → beta → release candidate.

Do not cross by document confidence.

## Irreversibility

Reversible / semi-reversible / expensive / identity-locking.

Higher irreversibility requires stronger evidence.

## Scope classes

Core MVP / prototype-only / later / nice-to-have / expansion / cut.

## Module contract

Purpose / owns / does not own / input / output / dependencies / API / data / errors / debug / tests / integration.

## AI output quarantine

Before acceptance:
diff/changes, unrelated changes, dependency, architecture, edge cases, tests, docs, controlled commit.

## Repository discipline

Meaningful work should use isolated branch/worktree when repo implementation resumes.
No direct main unless explicitly approved.

## QA evidence levels

self-test → structured internal → expert → blind player → repeated players → telemetry.

## Balance

baseline → simulation → play → one variable group → document → retest.

## Accessibility

motor/cognitive/hearing/vision/general constraints considered before final interaction lock.

## External dependencies/assets

Track source, version, license, commercial use, attribution, modification, redistribution, AI restrictions.

## Release preparedness — downstream

Build reproducibility,
store requirements,
privacy,
license inventory,
known issues,
rollback,
patch workflow.

## Current gate protection

Do not use release/marketing/legal future work to justify broad sample scope now.

## Hostile review

Search for:
authority drift, hidden source substitution, RNG, action inflation, unlogged mutations,
Attention rubber-banding, Concept/Brain authority creep,
content explosion, accessibility bypass, licensing risk,
human-evidence overclaim.

P0/P1 blocks adoption.

---

# SOURCE DOCUMENT: docs/18_DECISIONS_RISKS_OPEN_QUESTIONS_V3_FULL.md

# Decisions, Risks, and Open Questions V3 — Full

**Status:** ACTIVE LEDGER

## Closed V3 owner decisions

