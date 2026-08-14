# Game att2 - Current Development Lead Brief

Status date: 2026-08-14

Status: active cross-discipline production brief. Read with documents 19 through 30.
This file summarizes current authority; it does not replace the Development Master,
Combat Rules, technical specification, or decision ledger.

## 1. Executive position

Game att2 is in late pre-production systems and interaction validation. The narrow
deterministic simulator is technically healthy, but the product does not yet have
valid external evidence for fun, comprehension, accessibility, fairness, balance, or
production readiness.

The current product task is not story production, final UI, engine selection, or a
small content roster. The bounded visual diagnostic is now implemented and
fidelity-verified without changing the approved campaign or declaring final combat
rules. The owner deferred VL-WP4 and broader reflex work on 2026-08-13 before
execution. Space/reach and the strategic card/action-economy architecture are now
approved design directions. The active dependency-ordered gate is the wound-to-Blood,
repair, treatment, and wounded-limb self-risk numeric package. The physical-
consequence meanings were approved on 2026-08-13 without final numeric tuning or
runtime implementation approval.

The owner-approved combat identity guardrail continues to apply: the game must not
become upgraded stat-menu dueling. Body-sourced tactical
cards, reflex execution, and lasting physical consequences define the intended loop;
space is an action-produced supporting state and must not become the primary activity.

## 1A. Latest owner-delegated approval recorded on 2026-08-14

The owner delegated research, optimization, and design-direction approval for the
brain-slot proposal. Codex approved the document 29 paper architecture: three
Attention Slots developing toward five, flexible Commitment/Response/Adaptive duties,
persistent cards with Decision Refresh and one Reconsider per round, body-owned
eligibility, brain-owned selection, and shared physical compatibility instead of
generic action points. More slots add choices only. Individual cards, exact weights,
Fast-item limits, wound/repair values, production Stamina, reflex execution, final UI,
and runtime remain unapproved.

## 1B. Earlier owner decision recorded on 2026-08-13

The owner approved the complete latest action-produced range direction. Clinch,
Engaged, and Distant are shared combat states created by action, defense, reflex, and
other explicit outcomes rather than generic movement. Unmaintained Clinch receives
one complete later playable round and unmaintained Distant receives two before
settling to Engaged. Dedicated range builds may explicitly maintain or re-create their
state. Runtime, individual card profiles, hand rules, and balance remain deferred.

## 1C. Earlier owner decision recorded on 2026-08-13

The owner approved a combat identity guardrail. Strategic play should use a bounded
card-like hand whose opportunities and legality reflect the body and current state;
reflex interaction modifies committed execution; Blood, wounds, extraction, and body
change provide persistence. A repeated select-attack/watch-damage loop is explicitly
rejected. Space may support or be carried by actions/cards but must not dominate the
loop. This is identity authority, not approval for a full deck system, draw rules,
movement implementation, reflex implementation, or new content.

A cognitive capacity/selection role is now approved in document 29. Literal
brain/Head anatomy, progression delivery, and named reflex/offensive effects remain
deferred and may not displace limb-based build identity.

## 1D. Earlier owner decision recorded on 2026-08-13

The owner approved every recommendation and all eight decisions in the aimed-wound
direction. This locks wound families, dominant-wound occupancy, treatment/repair
separation, repeat-Major Ruin for arms/Legs, sever/harvest separation, symmetry,
basic-attack Major pressure without Clean harvest, and conditional-fatal Ruined Torso
with one rescue window. Exact values, exact rescue timing, implementation, and
specific repair content remain deferred.

VL-WP4 and broader reflex-mechanics work remain deferred; no diagnostic evidence was
captured. No external pilot, production integration, content, Encounter 3 runtime, or
engine gate is open.

## 2. Owner decision recorded on 2026-08-12

The owner approved the shared-readiness design method:

- one visible general Stamina/readiness resource replaces a separate standalone
  Block-pressure meter for visual-lab research;
- repeated use of the same physical response family temporarily increases its strain;
- repeated Block receives a stronger family-specific penalty than most actions;
- low Blood visibly amplifies existing strain and consequence pressure but does not
  independently create a hidden control penalty;
- body impairment remains a separate legality/effectiveness fact: an unusable source
  cannot act regardless of remaining readiness;
- this is approval to plan and compare the model, not approval for runtime Stamina,
  final values, campaign integration, or a production mechanic.

The owner approved VL-WP1 through VL-WP3 of
`25_BOUNDED_VISUAL_INTERACTION_LAB_PLAN_v0_1.md` on 2026-08-12. Their verified results
are in `26_VISUAL_INTERACTION_LAB_IMPLEMENTATION_RESULTS_v0_1.md`. VL-WP4 was
separately opened and then deferred before execution by the owner on 2026-08-13.

## 3. Verified repository baseline

Fresh local verification on 2026-08-12:

| Evidence | Result | What it supports |
|---|---|---|
| Automated tests | 261 passed | Current implementation fidelity |
| Coverage | 87% line coverage | Broad automated branch exercise, not product quality |
| Ruff | Passed | Static style/lint health |
| Strict mypy | Passed across 32 source files | Current type-contract health |
| Seven scenarios, seed 42 | Passed; mini-campaign ends at 25 Blood | Deterministic scenario behavior |
| Playable campaign replay, seed 42 | Completed at 36 Blood | Current CLI path remains usable |
| H1 scripted comparisons | Deterministic | H1 fidelity and causal traceability |
| Visual-lab scripted comparisons | 20 variants, byte-identical | VL-WP1 through VL-WP3 fidelity only |
| Local browser inspection | Passed with no console warnings/errors | Visual control and risk-gate fidelity only |

The five required 100-seed strategy batches remain diagnostic only. Four scripted
strategies completed 44% of runs and Blood Hoarder completed 0%, with no deaths. This
supports the no-free-premium-harvest control but demonstrates that strategies are test
drivers, not models of player behavior or balance.

The `blood_bag_balance` scenario applies its comparison values sequentially and ends
at 117 Blood. That number is a diagnostic trace, not a campaign balance result. Use
isolated counterfactual overlays for actual comparison work.

## 4. Cross-discipline readiness

| Discipline | Current state | Gate |
|---|---|---|
| Core identity | Locked strongly enough to protect | Preserve Body as Build and Blood as volatile bankroll |
| Simulator engineering | Fidelity gate passed with maintenance debt | Change only for an approved research requirement |
| Hybrid combat | Strategic direction approved; reflex research preserved but deferred | Complete strategic-combat packages in dependency order |
| Human evidence | No VL-WP4 evidence and no valid external pilot | Defer until the strategic loop is coherent |
| Combat systems | Wounds, movement, defense balance, recovery, and resolution incomplete | Make packages timely from lab evidence |
| Story and characters | Theme and encounter functions exist; canon remains thin | Wait until combat and information grammar stabilize |
| UI/UX | Research lab implements the narrow information contract | Diagnose it; do not treat it as final UI |
| Art/audio | Directional inspiration only | No production asset gate |
| Content | S-001, Jeff, Anna, and Table only in runtime | No roster or item expansion |
| Encounter 3 | Moderated paper packet prepared; P01-P08 pending | Runtime remains blocked |
| Engine/vertical slice | Not selected or approved | Revisit only after external evidence and system packages |

## 5. Critical path

```text
reflex diagnostics and broader reflex mechanics - DEFERRED
-> physical-consequence meanings - APPROVED, VALUES DEFERRED
-> action-produced range and settling cadence - APPROVED, RUNTIME DEFERRED
-> strategic card/action economy and cadence - APPROVED PAPER DIRECTION, RUNTIME DEFERRED
-> wound-to-Blood values and stabilization tuning - PROVISIONAL PAPER DIRECTION APPROVED
-> strategic defense roles and stacking - NEXT DESIGN GATE
-> extraction and maintenance rules
-> encounter resolution rules
-> information and interaction grammar
-> later reflex-mechanics gate
-> minimum complete game-design paper
-> paper content set for a few characters, items, and encounters
-> engine and production proposal
```

Only one product gate may be active. Documentation cleanup, test maintenance, and
archive hygiene may occur in parallel when they do not make product decisions.

## 6. Design route after the lab

If the diagnostic produces a continue signal, resolve the following as bounded system
packages rather than a long list of disconnected questions:

1. **Physical consequence package:** minimum wound classes, repeated-Major collapse,
   integrity-repair boundaries, Blood mappings, stabilization, worsening, and Ruined
   Torso handling.
2. **Space and tempo package:** action-produced range profiles, neutral settling,
   action/card cost, preparation, Main action, and triggered response timing.
3. **Defense and readiness package:** Guard Flesh, Block, Brace, Braced Legs, Cover It,
   shared readiness, repetition, recovery, stacking, and source exposure.
4. **Extraction and maintenance package:** preservation quality, emergency graft,
   integration, repair, item timing, and downstream body consequences.
5. **Encounter resolution package:** offensive incapacity, surrender, one bounded
   asset bargain, escape, mutual outcomes, and unresolved states.
6. **Information and interaction grammar:** public state, telegraphs, legal/disabled
   actions, cost/risk previews, feedback, and assisted input equivalence.

Only after those packages form one coherent combat loop should the project finalize a
small paper content set. That later set should prove system breadth with the fewest
characters, limbs, items, and encounter pressures possible; it must not be used to
design around unresolved rules.

## 7. Scope locks

- Do not integrate Stamina, Block pressure, or broader reflex families into the
  approved campaign yet.
- Do not add Warden or Encounter 3 runtime content.
- Do not start story production, final UI, final art/audio, engine work, a vertical
  slice, or a larger character/item roster.
- Do not convert provisional lab values into Combat Rules or production configuration.
- Exploratory notes are permitted only when clearly non-canonical and reversible.

## 8. Repository and workflow notes

- `docs/` is current authority and working documentation.
- `docs/archive/` and the Turkish PDF are historical evidence.
- Generated render/cache material belongs under ignored `tmp/` and must not be
  committed.
- Local deterministic development must remain functional without plugins.
- The isolated local visualization is implemented; no external participant or project
  data is transferred.

## 9. Current owner gate

The owner-approved action-produced range direction remains binding: Clinch, Engaged,
and Distant are outcomes rather than movement controls. Document 29 resolves the
strategic hand/action architecture as an approved paper baseline. The owner approved
document 30's WNR-0.1 numeric wound/Blood/repair package as a provisional paper
baseline on 2026-08-14, while keeping exact values tunable after connected systems are
defined. Runtime and configuration remain unchanged. The next dependency-safe design
gate is strategic defense roles, physical sources, effects, and stacking. Reflex work,
runtime card/wound implementation, an external pilot, content expansion, and
production integration remain deferred.
