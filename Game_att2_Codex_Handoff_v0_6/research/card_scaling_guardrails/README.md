# Card Scaling Guardrails Research Tool

Status: **RESEARCH-ONLY VALIDATOR FOR OWNER-APPROVED DIAGNOSTIC BOUNDARIES. NOT
RUNTIME, CONTENT, FINAL BALANCE, OR PRODUCTION APPROVAL.**

`assessor.py` implements the static and combinatorial portions of the companion
research contract in `CARD_ECOLOGY_SCALING_GUARDRAILS_v0_1.md`.

It checks:

- exact card-source ownership;
- one causal signature property per card;
- provisional label, mechanic, source-card, and exchange-content budgets;
- near-duplicate mechanical fingerprints;
- declared Pareto dominance;
- atomic Concept Deck exchanges;
- deterministic pairwise or higher-strength covering cases.

The defaults are diagnostic starting limits. A clean result means only that the
fixture obeys the declared structural model. It does not establish balance, fun,
creativity, comprehension, accessibility, or replay value.

Run the isolated checks from this directory:

```powershell
python -m unittest -v test_assessor.py
```

No third-party dependency is required.
