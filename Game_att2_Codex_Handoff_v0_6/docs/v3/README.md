# Game att2 — V3 Sandbox Authority

Status: ACTIVE on `v3/isolated-combat-sandbox-v01`

This directory is the active documentation front door for V3 implementation work on this branch.

## Current gate

**V3-1 — Isolated Combat Sandbox**

The purpose of this gate is to validate the Body → Brain Architecture → Attention → Action relationship before the wider Underground City sample is implemented.

## Current implemented V3 package

`src/game_att2_v3/`

It is intentionally separate from legacy `src/game_att2_sim/`.

Implemented fidelity surface:
- exact source states;
- source-valid body expressions;
- guaranteed/flexible Brain duties;
- weighted Attention;
- intrinsic expression weights;
- Brain tag bias;
- recency suppression;
- source-state weighting;
- Focus source-family bias;
- seeded selection;
- no-replacement inside one refresh;
- architecture coverage reporting;
- shaded unfillable duties;
- redraw no-alternative protection;
- Preparation/Main budget;
- inventory-origin action limit;
- Yellow/Red defense legality.

## Binding hardening rules

### V3-RQ-053 — Guaranteed Duty != Guaranteed Card
Brain guarantees the tactical duty. The body must provide a legal physical expression. If none exists, the slot shades. No substitution.

### V3-RQ-054 — Architecture Feasibility Warning
At Brain configuration boundaries, expose `available / required` coverage for guaranteed duties. Insufficient coverage may be deliberately accepted; it must not be hidden.

### V3-RQ-055 — Redraw Alternative Invariant
Blood redraw requires a distinct legal alternative. If none exists, redraw is disabled and no Blood is spent.

### V3-RQ-056 — Causal Specialization
Do not secretly normalize specialization. A single remaining Attack expression may become perfectly consistent while additional Attack duties shade because real body coverage was lost.

## Evidence boundary

Automated V3-1 evidence can establish deterministic causal fidelity. It does not establish fun, comprehension, fairness, accessibility, final balance, or replay desire.

Read next:
- `V3_1_ISOLATED_COMBAT_SANDBOX_ACCEPTANCE.md`
- `V3_1_HUMAN_VALIDATION_PROTOCOL.md`

The complete full-fidelity V3 design package remains the design source used to derive this branch; V1/V2 files outside this directory are provenance unless explicitly inherited by V3.
