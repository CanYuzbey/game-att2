# Game att2 — H1 Implementation Record v0.1

Status date: 2026-08-12

Status: completed implementation-fidelity record. This document consolidates the
executed H1 implementation plan and its verified result. It does not establish fun,
balance, comprehension, accessibility, market value, or production readiness.

Authority: `20_H1_HYBRID_COMBAT_SPEC_v0_1.md` and the owner approval recorded on
2026-08-11. Combat Rules v0.5 remains unchanged outside an explicitly invoked H1 run.

## 1. Delivered outcome

The completed slice is an isolated deterministic research runner that:

- constructs the controlled post-Jeff versus Anna fixture from existing definitions;
- compares prepared/unprepared Block, usable/unusable source, ordinary/high-risk
  failure, intent clarity, precise/assisted input, and normal/threshold pressure;
- validates the Block source before grading and again before consequence resolution;
- routes Torso damage and disclosed Right-Arm exposure through the existing rule
  engine;
- records structured, replayable JSON and Markdown evidence;
- leaves the seven approved scenarios and playable campaign unchanged by default.

H1 is a research instrument, not production combat and not an eighth campaign
scenario.

## 2. Binding implementation boundary

The implementation preserves:

- one committed Main action per actor per round;
- Guard Flesh's existing cost, Right-Arm source, duration, and single reduction;
- source revalidation before mutation;
- no invented Blood loss from ordinary limb damage;
- injected randomness and explicit recorded timing input;
- silent domain systems with structured events rendered at the boundary;
- no new runtime dependency or production content;
- the digital scope S-001 -> Jeff -> emergency graft -> Anna -> Grafting Table.

The only shared runtime seam is an optional default-neutral `AttackModifier` at
`RuleEngine.enemy_attack`. Existing callers omit it and retain their prior behavior.

## 3. Implementation surface

| Area | Files | Role |
|---|---|---|
| Research configuration | `config/h1_reflex_v0_1.yaml` | Provisional timing, mitigation, exposure, and fixture values |
| Strict loading | `src/game_att2_sim/h1_config.py` | Schema, range, reference, status, duplicate-key, and prohibited-key validation |
| Pure contracts | `src/game_att2_sim/reflex.py` | Immutable contexts, attempts, grades, risks, availability, and modifiers |
| Fixture/evidence | `src/game_att2_sim/h1_research.py` | Fixture construction, paired comparisons, events, metrics, and exports |
| Operator boundary | `src/game_att2_sim/h1_cli.py` | Scripted replay and local owner-diagnostic input |
| Scripted input | `examples/h1_scripted_comparisons.json` | Versioned deterministic comparison data |
| Verification | H1 unit/integration tests and `test_causal_integrity.py` | Contracts, negative paths, replay, CLI, and default-path isolation |

## 4. Deterministic comparison result

All values are `PROVISIONAL_H1_RESEARCH_ONLY`.

| Comparison | Variant A | Variant B | Fidelity observation |
|---|---|---|---|
| H1-C1 | Unprepared: Limited, 7 Torso damage | Guard-prepared: Strong, 2 Torso damage | Preparation changes context and consequence; Guard is consumed once. |
| H1-C2 | Usable arm: Exceptional, 4 damage | Disabled arm: denied, original 8 damage | Timing cannot bypass an unusable source. |
| H1-C3 | Ordinary miss: 8 Torso, 0 arm | High-risk miss: 8 Torso, 30 arm | Ordinary failure adds nothing; disclosed risk can expose the source. |
| H1-C4 | Vague intent: Miss, 8 damage | Exact intent: Limited, 7 damage | Information changes grade without changing legality. |
| H1-C5 | Precise: Limited, 7 damage | Assisted: Strong, 6 damage | Both profiles share one legality/consequence pipeline. |
| H1-C6 | Normal: 4 Torso, 4 arm | Threshold: 0 Torso, 4 arm | Legal exceptional input may preserve a known threshold; downstream meaning remains deferred. |

## 5. Requirement result

H1-RQ-001 through H1-RQ-012 passed their traceable fidelity checks. The decisive
controls were:

- preparation and intent remain measurable state facts;
- missing, disabled, incompatible, or invalidated sources reject/cancel Block;
- ordinary misses add no exposure;
- high-risk exposure is previewed, selected, source-specific, and logged;
- execution grades modify state and never write victory or narrative outcomes;
- precise and assisted profiles share legality and consequence ownership;
- no wound-to-Blood, Ruined Torso, content, Encounter 3, or Unity rule entered runtime.

The detailed requirement definitions remain in
`20_H1_HYBRID_COMBAT_SPEC_v0_1.md`; executable traceability remains in the H1 tests.

## 6. Historical verification record

The bounded implementation passed on 2026-08-12:

| Check | Recorded result |
|---|---|
| Full tests at the H1 merge point | 242 passed |
| Source line coverage | 87% |
| Ruff | Passed |
| Strict mypy | Passed across 28 source files |
| Seven scenarios, seed 42 | Unchanged; mini-campaign ended at 25 Blood |
| Playable campaign replay, seed 42 | Completed at 36 Blood with 38 events |
| H1 replay | Byte-identical repeated output |

These are historical merge-point results, not a substitute for fresh verification.
The current game-design baseline is the five living-document set in `docs/README.md`.
The former lead brief is preserved under `archive/design_history_2026-08-21/`.

## 7. Owner diagnostic and disposition

`OWNER-H1-DIAG-004` completed H1-C1, H1-C3, and H1-C5 with six consented local
timing captures. Structural validation passed, but the fixed one-second terminal task
did not isolate preparation and provided no useful fairness, risk, clarity, or control
evidence. Precise and assisted profiles both graded Miss.

Disposition: `REVISE INSTRUMENT BEFORE EXPERIENCE CLAIMS`. The raw record and
contamination status remain under `research/h1/`. The corrected taxonomy and research
direction are in
`23_REFLEX_INTERACTION_TAXONOMY_AND_DIAGNOSTIC_REVISION_v0_1.md`.

## 8. Current gate

The H1 runner remains a valid deterministic fidelity fixture. It is not an adequate
human-facing instrument and does not approve broader reflex families, final timing,
wounds, movement, active Cover It, new content, Encounter 3 runtime, or Unity.
Broader reflex work remains deferred.
