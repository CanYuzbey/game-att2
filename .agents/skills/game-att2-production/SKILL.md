---
name: game-att2-production
description: Lead, audit, design, implement, test, document, or research Game att2 under V3 authority. Use for V3 system design, the isolated combat sandbox, Body/Concept/Brain/Attention rules, Blood, wounds, grafting, surrender, tests, evidence, human-test preparation, production gates, or legacy-simulator comparison. Enforce V3 source precedence, state-derived causality, deterministic evidence, owner-vs-professional decision separation, and the V3 return contract.
---

# Game att2 Production — V3

Operate as an evidence-led game designer, systems engineer, researcher, QA lead, UX/accessibility reviewer, and producer.

Preserve the V3 experience hierarchy:

1. desperate bodily and Blood sacrifice;
2. body reconstruction changes how combat is played;
3. anatomical targeting and tactical body reading;
4. card/build richness.

Cards are a primary interaction language, but Body remains the physical capability authority.

## Establish authority

1. Locate the Git root and `Game_att2_Codex_Handoff_v0_6/`.
2. Read the applicable `AGENTS.md`.
3. Inspect branch/worktree state and preserve unrelated user changes.
4. For V3 product/rules work, start at `Game_att2_Codex_Handoff_v0_6/docs/v3/README.md`.
5. Use this precedence:

```text
V3 Authority and Supersession Contract
-> dated owner-approved V3 amendments
-> V3 Development Master
-> mechanic-specific V3 specifications
-> validated V3 config/tunables only
-> V3 tests and reproducible evidence
-> V3 comparison/legacy ledgers
-> V2 living documents as provenance only
-> V1 simulator/history as engineering evidence only
-> archive
```

No old runtime behavior, polished prose, numeric fixture, or historical commit silently overrides V3.

## Separate owner decisions from professional decisions

Owner approval is required for identity-defining, creative, expensive-to-reverse, or product-locking choices: protagonist/world identity, core sacrifice meaning, narrative actors, progression philosophy, presentation identity, commercial scope, or other choices explicitly listed in the V3 owner questionnaire.

Resolve reversible professional decisions without escalating them merely because they are OPEN. Examples include temporary fixture values, statistical sample sizes, test architecture, module boundaries, debug formats, CI/lint setup, deterministic RNG implementation, telemetry schema, prototype implementation vehicle, and balance-search methodology. Label temporary values as fixtures/research values and keep them replaceable.

## Apply the causal contract

For every meaningful action or transition:

```text
prior explicit state
-> exact source / ownership / target / timing legality
-> approved rule plus injected randomness
-> atomic explicit mutation
-> recompute physical capability
-> recompute Concept/card legality
-> recompute Brain/Attention eligibility
-> forced consequences
-> motivation-supported legal response
-> state-derived continuation / surrender / death / escape
-> structured evidence
```

Reject script immortality, resource theatre, decorative limb damage, outcome teleportation, invented anatomy/psychology, Attention substitution, Concept compensation, Brain omnipotence, and encounter-specific branches disguised as emergence.

## Preserve V3 Body / Brain / Attention authority

- Body owns physical capability and exact source validity.
- Concept Deck may specialize/filter/bias only source-valid expressions.
- Brain Architecture owns tactical duties/access structure, not physical capability.
- Guaranteed Duty is not a guaranteed card. If Body cannot supply the duty, the slot shades.
- Attention runs only after legality and may use intrinsic expression weight, Brain bias, recency, source-state, Concept bias, and bounded visible context.
- Specialization may legitimately increase consistency; do not secretly normalize it away.
- A no-alternative Blood redraw spends nothing.
- Held legal options may persist; source invalidation removes dependent held cards without inventing a mid-exchange replacement.
- Every meaningful Attention decision must be explainable in debug evidence.

## Preserve action and inventory boundaries

- ordinary round: maximum one Preparation + one Main;
- Attention slots do not add actions;
- inventory is a separate origin/lane, not an ordinary body-card draw;
- maximum one voluntary inventory-origin action per round unless a later explicit V3 rule changes it;
- state-required and automatic opportunities cannot change origin to bypass limits;
- rejected actions do not consume uncommitted resources or gameplay RNG;
- started atomic actions resolve under their declared contract.

## Current code boundaries

- `src/game_att2_v3/` is the V3 isolated deterministic sandbox and active implementation/fidelity surface.
- `tests/v3/` is the V3 automated evidence surface.
- `src/game_att2_sim/`, its config, scenarios, H1/visual-lab runners, and old campaign are legacy/research evidence. Preserve them unless an isolated maintenance task explicitly targets them.
- Do not port Jeff/Anna/Table content into V3 merely because implementation exists.

## Design and research work

Use:

```text
Question / hypothesis
Authority constraints
Mechanic or fixture variant
Expected state dynamic
Desired player experience
Instrumentation
Continue / revise / kill criteria
Evidence class
Contamination risks
Decision owner
```

Automation may establish fidelity, reproducibility, reachable states, exploit resistance, and distributions. It cannot establish fun, comprehension, accessibility, fairness, market demand, or replay desire.

Human sessions must preserve anonymous participant identity, build/config/seed, facilitator deviations, raw observations, debrief, replay behavior, and contamination labels. Designer/AI self-play is diagnostic only.

## Current production gate

```text
V3-0 authority/documentation consolidation — COMPLETE
-> V3-1 deterministic isolated-combat fidelity sandbox — IMPLEMENTED / HARDENED
-> V3-1 human-facing comprehension/agency validation — REQUIRES REAL HUMAN EVIDENCE
-> V3-2 body transition/graft consequence — DOWNSTREAM
-> V3-3 sacrifice/economy — DOWNSTREAM
-> V3-4 same-boss alternate-body replay — DOWNSTREAM
-> V3-5 Underground City connected sample — DOWNSTREAM
-> vertical slice / production — NOT AUTHORIZED BY EARLIER EVIDENCE
```

Do not fabricate human evidence or use automation to skip V3-1 human validation.

## Technical standards

Every module should define purpose, ownership, inputs, outputs/events, dependencies, public API, data format, errors, debug visibility, tests, and integration points.

Definitions are immutable where practical; runtime state is explicit. Route all meaningful randomness through injected RNG. Domain state changes are structured rather than hidden in presentation. Config changes tunables only and cannot introduce an undocumented mechanic.

## AI governance

Treat AI output as untrusted until:

1. authority/diff review;
2. unrelated-change check;
3. architecture-fit review;
4. edge-case and negative-test review;
5. deterministic verification where material;
6. build/test/lint/type checks as available;
7. documentation/config alignment;
8. controlled commit/merge.

Do not expose secrets. External dependencies/assets require source, license, maintenance, integration risk, and alternatives.

## Verify proportionally

For V3 changes, normally run:

```powershell
python -m pytest -q tests/v3
python -m ruff check src/game_att2_v3 tests/v3
python -m mypy src/game_att2_v3
python -m game_att2_v3.cli --seed 42 --brain balanced --debug-trace
```

When a normal repository environment is available, also run the relevant legacy/full suite before merging changes that could affect shared packaging or infrastructure. Never copy old test counts forward as current evidence.

## Hostile review

Before acceptance search for:
- Body losing capability authority;
- illegal-source leakage;
- hidden source/target substitution;
- action-economy inflation;
- hidden RNG or incomplete RNG trace;
- no-op Blood charges;
- mid-exchange card fabrication;
- Concept/Brain authority creep;
- specialization anti-cheat compensation;
- temporary effects without expiry;
- Will becoming second HP;
- transformation becoming generic corruption;
- bespoke boss keys;
- human-evidence overclaim;
- stale V1/V2 authority links;
- new dependencies/licenses/secrets.

P0/P1 findings block adoption.

## Return contract

For substantive work report:
- branch/commit/worktree or connector state;
- requested gate;
- files changed;
- authority references;
- exact behavior changed;
- verification and unavailable checks;
- fact/inference/hypothesis/unknown;
- hostile-review findings;
- scope audit;
- known limitations;
- adoption verdict;
- exactly one recommended next gate.

Do not say implemented/playable/validated without naming the exact artifact and evidence class.
