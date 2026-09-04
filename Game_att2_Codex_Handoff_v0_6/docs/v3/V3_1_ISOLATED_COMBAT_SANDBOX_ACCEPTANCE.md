# V3-1 Isolated Combat Sandbox Acceptance Contract

Status: IMPLEMENTED RESEARCH/FIDELITY FIXTURE

## Question

Can V3's Body → Brain Architecture → Attention model preserve body authority while providing tactical-class access and bounded imperfect exact-expression access?

## Implemented proof surface

- exact physical sources;
- source states Full / Strained / Desperate / Offline;
- source-valid body expressions;
- Brain guaranteed duties and flexible slots;
- tag biases;
- intrinsic expression weight;
- soft recency suppression;
- source-state weighting;
- Focus source-family bias;
- seeded weighted selection;
- no-replacement within one refresh;
- coverage report for unfillable Brain duties;
- shaded guaranteed duty when body cannot provide legal expression;
- redraw with no-alternative protection;
- Preparation/Main action budget;
- one voluntary inventory-origin action per round;
- Yellow Block/Parry and Red Evade legality.

## Hardening rules

### V3-RQ-053 — Guaranteed Duty != Guaranteed Card
Brain guarantees the tactical duty. Body must supply a legal expression. If none exists, the slot shades; no substitution.

### V3-RQ-054 — Architecture Feasibility Warning
Configuration exposes available/required expression counts for guaranteed duties. Insufficient coverage is visible but need not be forbidden.

### V3-RQ-055 — Redraw Alternative Invariant
Blood redraw requires a distinct legal alternative. If none exists, redraw is disabled and no Blood should be spent.

### V3-RQ-056 — Causal Specialization
The system does not normalize away extreme specialization. If only one legal Attack remains, it may become perfectly consistent while additional Attack duties shade. The downside emerges from actual lost coverage.

## Required automated acceptance

- same state + same seed → identical Attention selection;
- an Offline source never leaks into Attention;
- a guaranteed duty never fills with the wrong action class;
- a guaranteed duty shades when no legal expression exists;
- architecture coverage reports insufficient available expressions;
- recency soft-suppresses without becoming a hard cooldown;
- degraded source weighting can reduce access without necessarily invalidating the expression;
- deliberate specialization may raise consistency;
- additional duplicate duties shade when specialization leaves too few distinct legal expressions;
- redraw with no legal alternative returns a no-spend result;
- redraw with alternatives never returns the current expression as the alternative;
- Yellow/Red defence legality is enforced;
- one Preparation and one Main maximum;
- one voluntary inventory-origin action maximum.

## Current verification — 2026-09-04

Verified on the prepared V3 sandbox source in this work session:

```text
Python compile: PASS
pytest V3-specific suite: 17 passed
```

A first test invocation failed during collection because the isolated test subprocess did not receive the `src/` package path. After correcting the test harness environment, the unchanged V3 source/test suite completed with 17/17 passing tests. This was a test-environment import problem, not a gameplay-rule failure.

Not freshly verified here:
- Ruff;
- mypy;
- full legacy `game_att2_sim` suite.

Reason: this execution environment did not provide the repository through the normal local worktree/network path needed to run the complete branch checkout. These checks remain explicitly **NOT VERIFIED**, not assumed pass/fail.

## Evidence boundaries

This fixture can establish:
- deterministic selection;
- causal legality;
- architecture consistency;
- negative-case behavior;
- statistical selection dynamics.

It cannot establish:
- fun;
- comprehension;
- fairness;
- accessibility;
- final balance;
- replay desire.

Those remain human-evidence gates and must not be fabricated from automated output.
