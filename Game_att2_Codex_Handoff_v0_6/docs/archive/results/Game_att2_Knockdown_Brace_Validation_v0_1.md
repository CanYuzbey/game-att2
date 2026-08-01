# Game att2 Knockdown and Brace Validation v0.1

## Executive verdict

**LEG VALUE SHOWS SITUATIONAL EVIDENCE.** Owner-approved Tempo Loss is deterministic, logged, and bounded: unresolved Knockdown applies Downed, the next normal action must Stand, and Braced legs cancel one successful Knockdown per encounter. Unity remains blocked.

## Implemented rule

- Downed blocks Focus, attacks, Guard Flesh, tools, and other normal actions.
- One Fast medical item may resolve before Stand; it does not clear Downed.
- Stand clears Downed and consumes the normal action; another normal action that turn is rejected.
- Braced legs reset to one automatic Brace charge at encounter start.
- Brace cancels only the first otherwise-successful Knockdown, never failed attempts, already-Downed attempts, or attempts with unusable legs.

## Architecture and events

`CombatantRuntime` owns explicit `downed`, `brace_charges`, and normal-action consumption state. `RuleEngine` owns encounter reset, Knockdown, Brace, Stand, Downed legality, and involuntary Bleeding loss. Events distinguish `knockdown_attempted`, `knockdown_failed`, `knockdown_prevented_by_brace`, `downed_applied`, `action_rejected_while_downed`, `stand_performed`, and `brace_reset`.

## Verification

- `ruff check src tests`: pass.
- `mypy src`: pass.
- `pytest --cov=game_att2_sim --cov-report=term-missing -q`: 63 passed.
- Seed-42 mini-campaign: unchanged, completed at 25 Blood.
- Required probe CLI cases: Strengthen Legs and Leave both complete under Knockdown Pressure.

## Paired-seed result

Natural pre-table state, 1,000 paired seeds, Knockdown Pressure:

| Choice | Completion | Mean Blood | Brace prevention | Mean Stand actions |
|---|---:|---:|---:|---:|
| Strengthen Legs | 100% | 45.775 | 93.7% | 1.098 |
| Leave Unchanged | 100% | 63.425 | 0.0% | 2.035 |

Strengthen Legs prevents meaningful tempo loss but pays its 12-Blood opportunity cost. It is therefore situational, not universally dominant. The full multi-fixture 1,000-row expansion was reduced after two 120-second command-limit attempts caused by repeatedly loading configuration; the validated rows reuse a single loaded config and complete in 1.14 seconds.

## Exploit audit

Fast-before-Stand is legal but still limited to one Fast item per round. Downed cannot be cleared by scenarios or strategies because rules methods own the state. Stand cannot be repeated, cannot be followed by a normal action, and Brace neither refreshes mid-encounter nor consumes on a failed Knockdown. Event tests distinguish prevention from failure.

## Bleeding P1

**IMPLEMENTATION DEFECT WITH AUTHORITATIVE RESOLUTION.** Combat Rules define Blood 0 as collapse. Involuntary Bleeding now uses rules-layer loss that reaches zero and triggers existing collapse/soft-collapse handling; voluntary actions remain affordability-checked.

## Hostile review and next gate

- P0: none.
- P1: broader multi-fixture batch reporting still needs a CLI/batch API that reuses loaded config.
- P2: Brace prevalence is synthetic probe pressure, not encounter balance evidence.
- P3: no human-player or fun claim follows from this result.

**Encounter 3 readiness: READY TO DESIGN PAPER ENCOUNTER 3.** This permits paper design/testing only, not implementation, Unity, enemies, rewards, or production content.

Remaining owner decisions: Knockdown prevalence, future special-limb charge counts, and all encounter identity, presentation, and narrative choices.
