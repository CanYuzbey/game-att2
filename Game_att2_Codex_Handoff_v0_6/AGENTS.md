# AGENTS.md — Game att2 V3 Binding Instructions

## Mission

Preserve the legacy `game_att2_sim` package as frozen deterministic evidence while developing V3 in the separate `game_att2_v3` package.

On branch `v3/isolated-combat-sandbox-v01`, V3 is the active design/architecture authority for new work. V1/V2 documents remain provenance, research, and legacy evidence unless V3 explicitly inherits them.

## V3 authority order

1. `docs/v3/README.md`
2. V3 authority / development / mechanic specifications under `docs/v3/`
3. dated owner-approved V3 amendments
4. V3 test and acceptance contracts
5. validated V3 configuration for tunable values only
6. fresh generated evidence
7. V2 and V1 documents as provenance only

No implemented legacy behavior silently overrides V3.

## Identity hierarchy

Protect this order:

1. desperate bodily / Blood sacrifice;
2. body reconstruction changes combat;
3. anatomical targeting and body reading;
4. card/build richness.

Cards remain core, but Body owns physical capability.

## Causal contract

For every meaningful V3 action or access decision:

```text
prior explicit state
-> exact source / ownership / target / timing legality
-> approved rule + injected randomness
-> atomic mutation
-> recompute physical capability
-> recompute card / Concept legality
-> recompute Brain / Attention eligibility
-> forced consequences
-> motivation-supported legal response
-> state-derived continuation / surrender / death / escape
-> structured evidence
```

## V3-1 hardening invariants

- Legality precedes probability.
- Brain guarantees a tactical **duty**, not a fabricated card.
- If the body cannot supply a legal expression for a guaranteed duty, the slot is visibly shaded/empty.
- Brain configuration must expose duty coverage (`available / required`).
- Attention never substitutes an illegal source or wrong action class.
- Recency is soft suppression, not a hidden hard cooldown.
- Source degradation may change legality, effect, and/or access weight only through explicit rules.
- Blood redraw requires a distinct legal alternative; otherwise no redraw and no Blood spend.
- Extreme specialization is not secretly normalized away. Consistency gains and coverage loss remain causal.
- One ordinary Preparation and one ordinary Main maximum per round.
- At most one voluntary inventory-origin action per actor per round.
- Yellow threat permits Block/Parry; Red threat permits Evade. No color-only final UI.

## Package boundary

- `game_att2_sim`: legacy simulator/research evidence. Do not port Jeff/Anna/Table content into V3 by convenience.
- `game_att2_v3`: isolated V3 fidelity/sandbox code.
- V3-1 is not permission to build the full Underground City sample, story, final UI, persistence, meta progression, large Concept catalog, large Brain-Part catalog, or production engine architecture.

## Evidence discipline

Separate:
- CONFIRMED FACT
- IMPLEMENTED
- VERIFIED
- WORKING HYPOTHESIS
- HUMAN EVIDENCE REQUIRED
- LEGACY EVIDENCE
- OPEN

Automated evidence can establish determinism, legality, state transitions, negative cases, distributions, and regressions.
It cannot establish fun, comprehension, fairness, accessibility, market value, or replay desire.
Designer/AI self-play is not external human evidence.

## Required workflow

1. Read V3 authority before changing V3 behavior.
2. Map work to named requirements and acceptance criteria.
3. Keep V3 modules narrow and typed.
4. Route all V3 randomness through injected seeded RNG.
5. Add negative tests with each behavior.
6. Run focused tests, then relevant full suite where the environment permits.
7. Keep exact test/tool limitations explicit.
8. Perform hostile review for source substitution, action inflation, hidden RNG, Attention rubber-banding, Concept/Brain authority creep, scope creep, and overclaim.
9. Do not merge to `main` without explicit owner approval.

## Current product gate

`V3-1 — Isolated Combat Sandbox`

The current implementation may prove Body -> Brain Architecture -> Attention -> Action invariants only. The next human-facing evidence gate remains separate and must not be claimed from automated tests.
