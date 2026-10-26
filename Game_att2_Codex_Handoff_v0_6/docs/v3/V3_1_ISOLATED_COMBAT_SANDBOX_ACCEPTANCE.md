# V3-1 Isolated Combat Sandbox Acceptance Contract

Status: IMPLEMENTED RESEARCH/FIDELITY FIXTURE

## Question

Can V3's Body → Brain Architecture → Attention model preserve body authority while
providing tactical-class access and bounded imperfect exact-expression access?

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
Brain guarantees the tactical duty. Body must supply a legal expression.
If none exists, the slot shades; no substitution.

### V3-RQ-054 — Architecture Feasibility Warning
Configuration can expose available/required expression counts for guaranteed duties.
Insufficient coverage is visible but need not be forbidden.

### V3-RQ-055 — Redraw Alternative Invariant
Blood redraw requires a distinct legal alternative.
If none exists, redraw is disabled and no Blood should be spent.

### V3-RQ-056 — Causal Specialization
The system does not normalize away extreme specialization.
If only one legal Attack remains, it may become perfectly consistent while additional
Attack duties shade. The downside emerges from actual lost coverage.

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

Those remain human-evidence gates.

## Technical hardening pass — 2026-09-04

The non-owner-dependent hardening pass additionally implemented:

- full per-slot Attention explanation traces (candidate rejection reason, base weight, Brain factor, recency factor, source-state factor, Focus factor, final weight, seeded roll, selected expression);
- explicit architecture coverage warnings when guaranteed duties exceed current legal expression coverage;
- atomic Blood redraw transactions with injected cost and exact ledger events;
- insufficient-Blood redraw rejection with zero mutation;
- persistent Attention hand baseline: unused legal cards persist, played/dropped/invalid positions wait for explicit Decision Refresh;
- immediate source-invalidation of held cards without mid-exchange replacement;
- reserved-expression exclusion during partial hand refill so one physical expression cannot duplicate across held/refilled slots.

Current local verification for the V3-specific suite after this pass:

```text
Python compile: PASS
pytest: 26 passed
```

Ruff/mypy/full legacy suite still require a normal repository execution environment before their status can be upgraded from NOT VERIFIED.
