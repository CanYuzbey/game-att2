# Game att2 — V3 Codex Handoff

This package now has three deliberately separated surfaces:

1. **V3 active product/design authority** under `docs/v3/`;
2. **V3 deterministic isolated-combat sandbox** under `src/game_att2_v3/` and `tests/v3/`;
3. **V1/V2 legacy and research evidence** retained elsewhere in the package.

The V3 sandbox is implemented as deterministic fidelity infrastructure. It is not yet evidence that the game is fun, comprehensible, fair, accessible, or production-ready. Those claims require real human testing.

## Read in this order for V3 work

1. `AGENTS.md` — repository/evidence rules.
2. `docs/v3/README.md` — active V3 front door.
3. `docs/v3/full_fidelity/README.md` — then read `MASTER_CHUNK_01.md` through `MASTER_CHUNK_12.md` in sequence. These contain the complete V3 full-fidelity authority/specification mirror with source-document banners.
4. `docs/v3/V3_1_ISOLATED_COMBAT_SANDBOX_ACCEPTANCE.md` and `docs/v3/V3_1_TECHNICAL_HARDENING_REPORT.md` — current implementation/fidelity evidence.
5. `docs/v3/V3_1_HUMAN_VALIDATION_PROTOCOL.md` — next evidence gate.
6. `docs/v3/21_OWNER_DECISION_QUESTIONNAIRE_V3.md` — only when owner-dependent decisions are needed.

Do not start new V3 work from old numbered simulator documents or V2 living documents. They remain provenance/evidence and are explicitly reconciled in the V3 full-fidelity comparison/legacy sections.

## Current V3 product chain

```text
V3-0 authority/documentation consolidation — COMPLETE
→ V3-1 isolated deterministic combat/Attention sandbox — IMPLEMENTED / HARDENED
→ V3-1 real human comprehension and agency validation — NEXT EVIDENCE GATE
→ V3-2 body transition / graft consequence
→ V3-3 sacrifice / Blood economy
→ V3-4 same-boss alternate-body replay
→ V3-5 bounded Underground City connected sample
```

The bounded product-facing sample remains:

```text
captivity
→ disclosed sacrifice/concession
→ weaker-but-free release
→ Fight A
→ kill for Blood OR living surrender for a legal limb
→ graft
→ Fight B demonstrating benefit + drawback
→ gate boss with multiple body solutions
→ escape or same-day reset
```

Exact actors, sacrifice fiction, progression boundaries, presentation identity, long-form world structure, and other owner-dependent choices are intentionally collected in the ordered owner questionnaire rather than silently invented.

## V3 implementation surface

| Path | Responsibility |
|---|---|
| `src/game_att2_v3/` | V3 Body/Brain/Attention/action fidelity sandbox |
| `tests/v3/` | V3 deterministic and negative tests |
| `docs/v3/` | V3 authority, evidence, questionnaire, full-fidelity comparison and legacy mirror |
| `src/game_att2_sim/` | frozen/legacy simulator and research tooling |
| `config/` | legacy/research config unless a future explicit V3 config surface supersedes it |
| `research/` | V2/V1 research fixtures and provenance |
| `docs/archive/` | historical evidence |

## V3 sandbox behavior currently implemented

- exact body/source legality before probability;
- Full/Strained/Desperate/Offline source states;
- guaranteed and flexible Brain duties;
- intrinsic expression weights + Brain tag bias + soft recency + source-state + Focus factors;
- seeded deterministic weighted Attention;
- visible duty-coverage shortfall warnings;
- shaded duty rather than illegal class/source substitution;
- per-slot candidate rejection, factor, RNG roll, and selection traces;
- persistent held-card comparison lifecycle;
- no mid-exchange replacement after source invalidation;
- no duplicate physical expression during partial hand refill;
- causal specialization without hidden normalization;
- Blood redraw no-alternative/no-spend and insufficient-Blood/no-mutation behavior;
- exact committed-redraw Blood ledger event;
- one Preparation + one Main;
- one voluntary inventory-origin action;
- Yellow Block/Parry and Red Evade legality.

## Verification

Latest professional hardening verified locally:

```text
Python compile: PASS
V3-specific pytest: 26 passed
Ruff: NOT VERIFIED in latest environment
mypy: NOT VERIFIED in latest environment
full legacy regression suite: NOT VERIFIED in latest environment
```

Never convert unavailable checks into assumed passes.

## Legacy evidence

The old deterministic simulator, Jeff/Anna/Table campaign, H1, visual lab, Warden paper work, numeric comparisons, and historical results remain valuable evidence. They do not regain design authority merely because they are more implemented or more detailed.
