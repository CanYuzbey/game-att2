# V3-1 Technical Hardening Report v0.2

Status date: 2026-09-04  
Evidence class: deterministic implementation/fidelity evidence

## Scope

Professional/reversible implementation work only. No owner-dependent creative choice was locked.

## Implemented

1. Body/source legality before Attention probability.
2. Guaranteed Brain duty distinct from guaranteed card.
3. Shaded duty when current body cannot supply a legal expression.
4. Coverage warnings for unfillable guaranteed duties.
5. Seeded weighted selection with inspectable RNG trace.
6. Per-expression factor trace: base, Brain, recency, source-state, Focus, final weight.
7. Soft recency suppression.
8. Source-state weighting without forced illegality where degraded route remains legal.
9. Causal specialization without hidden normalization.
10. Blood redraw no-alternative no-spend invariant.
11. Blood redraw insufficient-Blood no-mutation invariant.
12. Exact Blood ledger event on committed redraw; numeric cost remains injected/configurable.
13. Persistent-hand comparison baseline.
14. Played/dropped/invalid slot refill only on explicit Decision Refresh.
15. Immediate held-card invalidation after physical source loss without mid-exchange replacement.
16. No duplicate expression during partial hand refill.
17. One Preparation + one Main maximum.
18. One voluntary inventory-origin action maximum.
19. Yellow accepts Block/Parry; Red accepts Evade.
20. Structured JSON CLI output with optional debug trace.

## Verification

```text
Python compile: PASS
V3-specific pytest: 26 passed
```

Not claimed:
- Ruff;
- mypy;
- full legacy simulator regression;
- fun;
- comprehension;
- fairness;
- accessibility;
- final balance;
- replay desire.

## Why no more technical decisions were escalated to the owner

Exact fixture weights, slot counts, numeric costs, threshold values, timing windows, test sample sizes, engine/tool choice for research, serialization, CI and optimization are reversible professional decisions. They are intentionally absent from the owner questionnaire unless evidence later shows that one changes product identity.

## Remaining gate

Interactive/human-facing V3-1 validation still requires real participants. No artificial human evidence is produced.
