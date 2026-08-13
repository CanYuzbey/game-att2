# Game att2 - Current Development Lead Brief

Status date: 2026-08-12

Status: active cross-discipline production brief. Read after documents 19 through 23.
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
rules. The active gate is whether to open its counterbalanced owner diagnostic.

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
are in `26_VISUAL_INTERACTION_LAB_IMPLEMENTATION_RESULTS_v0_1.md`. VL-WP4 was not
opened by that approval.

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
| Hybrid combat | Direction approved; H1 fixture and visual-lab fidelity complete | Owner diagnostic approval |
| Human evidence | Owner diagnostics only; no valid external pilot | Separate consented pilot after owner diagnostic |
| Combat systems | Wounds, movement, defense balance, recovery, and resolution incomplete | Make packages timely from lab evidence |
| Story and characters | Theme and encounter functions exist; canon remains thin | Wait until combat and information grammar stabilize |
| UI/UX | Research lab implements the narrow information contract | Diagnose it; do not treat it as final UI |
| Art/audio | Directional inspiration only | No production asset gate |
| Content | S-001, Jeff, Anna, and Table only in runtime | No roster or item expansion |
| Encounter 3 | Moderated paper packet prepared; P01-P08 pending | Runtime remains blocked |
| Engine/vertical slice | Not selected or approved | Revisit only after external evidence and system packages |

## 5. Critical path

```text
shared-readiness boundary - RESOLVED FOR RESEARCH PLANNING
-> bounded visual-lab plan approval - COMPLETE
-> isolated local implementation-fidelity check - COMPLETE
-> repeated, counterbalanced owner diagnostic
-> separately approved external pilot
-> evidence-led wound / movement / defense / recovery packages
-> minimum complete game-design paper
-> later paper content set for a few characters, items, and encounters
-> engine and production proposal
```

Only one product gate may be active. Documentation cleanup, test maintenance, and
archive hygiene may occur in parallel when they do not make product decisions.

## 6. Design route after the lab

If the diagnostic produces a continue signal, resolve the following as bounded system
packages rather than a long list of disconnected questions:

1. **Physical consequence package:** minimum wound classes, Blood mappings,
   stabilization, worsening, and Ruined Torso handling.
2. **Space and tempo package:** abstract position/reach, movement cost, preparation,
   Main action, and triggered response timing.
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

Review `26_VISUAL_INTERACTION_LAB_IMPLEMENTATION_RESULTS_v0_1.md` and approve, revise,
or reject VL-WP4. Approval would open only the local counterbalanced owner diagnostic;
it would not approve an external pilot or production integration.
