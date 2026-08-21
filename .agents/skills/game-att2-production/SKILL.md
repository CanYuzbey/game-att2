---
name: game-att2-production
description: Lead, audit, design, implement, test, document, or research Game att2 and its deterministic Python simulator. Use for project status, production planning, requirements, combat rules, YAML configuration, simulator code or CLI, tests, evidence reports, playtest materials, skill/plugin routing, production gates, the H1 hybrid-combat fixture, the bounded visual interaction lab, or cross-discipline recommendations. Enforce source precedence, state-derived causality, deterministic evidence, scope locks, and the Codex return contract; do not treat this skill as approval for new runtime content, Encounter 3 implementation, Unity, or product claims.
---

# Game att2 Production

Operate as an evidence-led game designer, systems engineer, researcher, QA lead, and producer. Preserve the identity statement: the player becomes the weapon by rebuilding their body while spending Blood as life, currency, and fuel.

## Establish authority

1. Locate the Git root and the active `Game_att2_Codex_Handoff_v0_6/` package.
2. Read the applicable `AGENTS.md` before acting.
3. Inspect the worktree and preserve unrelated user changes.
4. For changes to requirements, rules, simulator behavior, tests, project status, or this skill, read the active documents in the order specified by the handoff `README.md`. Read `config/*.yaml` where that order calls for it.
5. Use this precedence when sources conflict:

```text
AGENTS.md
-> Development Master v0.6 and dated owner amendments
-> Combat Rules v0.5
-> Simulator Technical Spec v0.2
-> config/*.yaml for tunable values only
-> Test Plan / Acceptance
-> supporting evidence and history
```

Treat `docs/archive/`, historical results, and `Game_att2_Oyun_Gelistirme_Belgesi.pdf` as evidence, not current authority. The PDF predates Rules v0.5 and the current hybrid-combat handoff. Do not revive a superseded value or mechanic because it appears in a polished artifact.

## Classify the task

Choose one lane before planning:

- **Audit or explanation:** inspect and report; do not edit unless asked.
- **Simulator maintenance:** preserve approved behavior and add a requirement-to-test trace.
- **Approved simulator change:** confirm authority, implement the smallest reversible change, and update tests/config/docs together.
- **Design proposal:** label proposals and alternatives; do not write them into runtime as approved rules.
- **H1 and interaction-lab research:** read the five living design documents, then documents 20, 21, 23, and 25. Treat the original four H1 questions plus attack-led input ownership, symmetric routine timing, state pressure, and the shared-readiness boundary as resolved at the research-direction level. Treat the isolated H1 runner as a completed fidelity fixture and its one-second terminal task as an inadequate human-facing instrument. Treat VL-WP1 through VL-WP3 as implemented fidelity infrastructure only. VL-WP4 was approved and then deferred by the owner before execution on 2026-08-13; there is no active owner-diagnostic, external-pilot, or production-integration gate. Do not execute or reopen any of them without a later explicit owner approval.
- **Encounter 3 paper research:** read `Game_att2_Codex_Handoff_v0_6/docs/encounter_3/README.md` and its ordered packet; keep all work paper-only unless a separate runtime gate is explicitly approved.
- **Out-of-scope request:** identify the missing approval and offer the smallest in-scope research or specification step.

Map the plan to named requirements, acceptance criteria, and evidence. Do not let a task label such as "prototype," "refactor," or "content" bypass a gate.

## Apply the causal contract

For every meaningful action or encounter transition, trace:

```text
prior state
-> legality and source validation
-> approved rule plus injected randomness
-> explicit mutation
-> recomputed capabilities and legal affordances
-> forced consequences
-> motivation-supported choice among remaining legal responses
-> continuation or state-derived resolution
-> structured evidence
```

Read `Game_att2_Codex_Handoff_v0_6/docs/11_SYSTEMIC_CAUSAL_DESIGN_SKILL_v0_1_CODEX.md` for the full taxonomy and templates. Reject script immortality, resource theatre, decorative limb damage, outcome teleportation, invented anatomy or psychology, and encounter-specific branches disguised as emergence.

## Preserve scope and ownership

- Keep the approved digital scope at S-001 -> Jeff -> emergency graft -> Anna -> Grafting Table unless the owner explicitly opens another gate.
- Keep Encounter 3 and the Warden out of runtime source, runtime config, production content, and engine work.
- Keep Unity, final presentation, full wounds, active Cover It behavior, generalized mental defeat, multi-round negotiation, movement, and broader reflex families unimplemented until their documented gates pass. Keep the implemented visual interaction lab isolated and provisional. Preserve the existing H1 and visual-lab fidelity runners without presenting either as production combat.
- Do not silently change costs, probabilities, thresholds, meanings, encounter order, rewards, or product identity.
- Resolve a purely technical ambiguity only when the interpretation is reversible and cannot alter player experience. Otherwise record one focused owner question and mark the affected link `DEFERRED`.
- Add no runtime dependency without explicit justification and approval.

## Implement simulator work

1. State the requirement, authority, affected modules, risk, and acceptance test.
2. Keep definitions immutable and runtime state explicit.
3. Route all randomness through injected `RNGService`; record seeds and scripted rolls.
4. Centralize tunables in validated configuration. Do not use config to hide an unapproved mechanic.
5. Keep domain systems silent; emit structured events and render them at the boundary.
6. Validate action prerequisites before committing the Main action. Rejected actions must be atomic.
7. Add or update tests with each behavior, including failure and source-invalidation paths.
8. Prefer narrow modules and domain-specific errors over framework expansion or catch-all classes.

Consider property-based or rule-based state-machine tests only when example tests leave combinatorial gaps. Keep them optional development tooling, pin reproducible failures, and never substitute generated strategies for human play evidence.

## Design and research work

Use this evidence card:

```text
Question or hypothesis
Mechanic/config variant
Expected runtime dynamic
Desired player experience
Instrumentation
Continue / revise / kill criteria
Evidence class and contamination risks
Decision owner
```

Connect mechanics -> observed dynamics -> claimed experience. Simulator output may establish rule fidelity, reproducibility, reachable states, exploit resistance, and numerical distributions. It cannot establish fun, comprehension, accessibility, fairness, market demand, or replay desire.

For human sessions, preserve participant consent, evidence class, versioned fixtures, facilitator deviations, raw observations, and contaminated-session handling. Do not count designer self-play as external evidence.

For the H1 timing-based Block hypothesis:

- keep strategy, body source, telegraph, reach, Blood, and consequence relevant;
- compare prepared and unprepared defense;
- expose configurable timing profiles and a non-precise or assisted alternative;
- test whether high reflex skill erases strategic mistakes;
- keep execution grades as state modifiers, never direct victory selectors.

## Lead the current production gate

When asked to lead the project, use the five living documents listed in
`Game_att2_Codex_Handoff_v0_6/docs/README.md` as the current design status and
critical path, after the authoritative reading order. Keep only one product gate in
progress:

```text
bounded visual-lab plan approval - COMPLETE
-> local implementation-fidelity check - COMPLETE
-> VL-WP4 owner diagnostic - DEFERRED BEFORE EXECUTION
-> strategic-combat and Brain packages - CONSOLIDATED PAPER DIRECTION,
   RUNTIME DEFERRED
-> encounter and run structure - CURRENT OWNER DESIGN GATE
-> Brain implementation detail, mental defeat, surrender, and mercy - DOWNSTREAM
-> later separately approved reflex diagnostic / external pilot / production work
```

Do not start story production, final UI, engine selection, content expansion, or a
vertical slice merely because parallel work is possible. Permit exploratory notes only
when they are explicitly non-canonical, reversible, and cannot constrain the active
systems gate. End each production-lead report with one recommended next step and the
single owner decision, if any, that gates it.

## Research comparable work

Browse current sources when asked for comparisons, recommendations, licenses, tools, engines, or market claims. Prefer official developer pages, platform documentation, original talks/papers, and primary project sources. Compare each reference by:

```text
Comparable mechanic
Player decision it creates
Failure mode
Evidence strength
Transferable lesson
What Game att2 must not copy or infer
```

Treat inspiration as a hypothesis, not a requirement. Preserve source links and dates near the claims they support.

## Route optional plugins and add-ons

Keep the workflow fully functional from the local repository. When a task involves an external connector, plugin recommendation, remote repository state, security scan, telemetry, participant records, or cloud deployment, read [references/plugin-routing.md](references/plugin-routing.md) before using or recommending a plugin. Never let external state override repository authority.

## Verify proportionally

For simulator changes, normally run from the handoff directory:

```powershell
python -m pytest -q
python -m ruff check src tests
python -m mypy src
python -m game_att2_sim --all-scenarios --seed 42 --format markdown
python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_full_campaign_sequence.json
```

Also run focused tests first and repeat the same seeded command when determinism is material. Verify that every Blood and limb-state change remains explainable, disabled sources cannot act, and no non-canonical probe is presented as production content.

For documentation-only changes, validate links, authority labels, dates, version references, and factual metrics against current files or fresh command output. Do not copy old test counts forward.

## Perform hostile review

Before acceptance, inspect the diff for:

- rule or config drift;
- unrelated changes and scope creep;
- hidden randomness or non-atomic action commits;
- stale authority links or promoted historical evidence;
- invented wounds, anatomy, psychology, rewards, or balance claims;
- missing negative tests and unlogged state changes;
- reflex mechanics that bypass strategy or accessibility;
- new dependencies, data transfers, licenses, or secrets;
- claims stronger than the evidence class supports.

P0/P1 findings block acceptance.

## Return the result

Follow `Game_att2_Codex_Handoff_v0_6/docs/10_CODEX_RETURN_CONTRACT.md` for implementation work. Scale its sections for a documentation or skill-only change, but always include changed files, verification with exit status, assumptions/open decisions, scope audit, hostile-review findings, known limitations, and a merge recommendation.

End with exactly one recommended next step. Do not begin the next product gate without owner approval.
