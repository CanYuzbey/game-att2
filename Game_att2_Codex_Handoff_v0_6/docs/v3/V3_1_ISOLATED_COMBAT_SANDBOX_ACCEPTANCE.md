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
