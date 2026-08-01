# Game att2 Simulator Review Gate v0.1

> **Historical review artifact — superseded for current implementation results.** Preserve this review as evidence of the earlier correction. Use `Game_att2_Combat_Simulator_Results_v0_2.md` for the authoritative post-causal-integrity state.

## 1. Executive Verdict

This review found and corrected P1 source-compliance defects in the Jeff baseline and batch outcome labeling. The implementation is now a materially better validation tool, but the current simulator cannot establish table-choice value beyond terminal summaries and does not yet support a product continue signal.

**Implementation gate: PASS WITH NON-BLOCKING DEBT.** All required rules and scenarios execute, with deterministic seeded output and focused automated coverage. Remaining debt is primarily diagnostic completeness and configuration validation breadth.

**Simulator product signal: INSUFFICIENT / NON-IDENTIFIABLE EVIDENCE.** The review distinguishes failed extraction from completion, but the short campaign cannot observe most table effects downstream.

**Unity gate: BLOCKED.** No newer owner-approved source authorizes a change.

## 2. Repository and Branch Integrity

At review start, Git had no project commit and `codex/combat-loop-simulator-v01` was an unborn branch. There was therefore no correct committed base branch and `git diff <base>...HEAD` was not meaningful. The archive manifest and checked-in handoff files were used as the immutable source baseline.

The only project implementation is under this branch's worktree. No secrets, virtual environments, caches, or local-machine paths were added to project reports. `Game_att2_Combat_Simulator_Results_v0_1.md` and this document are intentional generated/review artifacts. The handoff archive at repository root remains an external input and is not part of the project commit.

## 3. Actual Diff Scope

- `config/content_v0_1.yaml`: Jeff Right Arm is now `large`, making only the documented Jeff target valid for the existing large-limb Hell Saw rule.
- `src/game_att2_sim/rules.py`: config-backed Guard Flesh, Bleeding, Unstable, Stabilized, Anna trade, cost, and event ownership.
- `src/game_att2_sim/scenarios.py`: valid S1 Hell Saw sequence, truthful incomplete outcomes, random-legal diagnostics, isolated Blood Bag overlays, and aggregate metrics.
- `src/game_att2_sim/{models,config_loader,cli}.py`: diagnostic metrics, Guard Flesh reduction loading, portable output directories.
- `tests/`: S1 saw regression, graft-cost transaction, overlays, CLI, renderers, deterministic output, and batch metrics.

No content beyond Jeff/Anna/Table, engine integration, UI, save/load, procedural generation, or balance-value change was introduced.

## 4. Findings

| Severity | Finding | Status |
|---|---|---|
| P1 | S1 used Bone Scissors despite the approved Hell Saw baseline. | Fixed: Jeff Right Arm is large; S1 asserts one valid Hell Saw event and no scissors action. |
| P1 | Failed-saw batch paths used an illegal scissors fallback or were treated as completed. | Fixed: no fabricated reward; campaign becomes `incomplete` without a graft. |
| P1 | Blood Hoarder reported completion despite ending with a missing right arm. | Fixed: classified `incomplete` in the campaign. |
| P1 | Blood Bag comparison mutated shared loaded config. | Fixed: isolated deep-copy overlays. |
| P2 | Guard Flesh, trade, and some condition changes lived in scenario code. | Fixed: moved behind `RuleEngine` methods and events. |
| P2 | Existing policies do not use Blood Bag; table effects are mostly terminal. | Reported; not a balance conclusion. |
| P2 | Generic Plead Pressure lacks encounter paths for enemy-low-blood/core/fear because those states are not exercised. | Open diagnostic coverage debt. |
| P3 | Config validation does not exhaustively validate every enemy action/table transformation reference. | Open hardening debt. |

## 5. Requirements Traceability

| ID | Requirement | Implementation / Evidence | Verified Result / Gap |
|---|---|---|---|
| RQ-001 | Six body slots | `models.py`, `factory.py`; unit config test | Pass |
| RQ-002 | Blood health/currency/fuel | `rules.spend_blood/gain_blood`; transaction tests | Pass |
| RQ-003 | Limb states | `rules.apply_damage`; threshold tests | Pass |
| RQ-004 | Source impairment | `effectiveness/action_damage`; unit test | Pass |
| RQ-005 | No free premium harvest | `rules.grip`; S2 | Pass |
| RQ-006 | Committed clean sever | `claim/saw/scissors`; S1 test | Pass |
| RQ-007 | Harvest quality | `harvest/salvage`; distribution tests | Pass |
| RQ-008 | Emergency graft | `emergency_graft`; exact cost test | Pass |
| RQ-009 | Unstable v0.4 | `unstable_checks/limb_action_cost`; branch tests | Pass |
| RQ-010 | Focus pre-action | `focus`; unit/integration tests | Pass |
| RQ-011 | One Fast item | `fast_item`; unit test | Pass |
| RQ-012 | Plead/surrender | `add_plead_pressure`; Jeff scripts | Pass with P2 coverage debt |
| RQ-013 | Table options | `integrate`; legality tests | Pass; downstream value not identifiable |
| RQ-014 | Structured logs | `EventLog`, renderers; CLI tests | Pass |
| RQ-015 | Seeded reproducibility | `SeededRNG`; repeatable CLI test | Pass |
| RQ-016 | Injected RNG only | `rng.py`; source audit | Pass |
| RQ-017 | CLI/scenario batches | `cli.py`; smoke tests | Pass |
| RQ-018 | Text/JSON/Markdown reports | `reporting.py`; renderer tests | Pass |
| RQ-019 | Config validation | `config_loader.py`; loading tests | Pass with P3 breadth debt |
| RQ-020 | Domain systems do not print | source audit; CLI owns printing | Pass |
| RQ-021 | Completion traceability | this review and tests | Pass |

## 6. Jeff Baseline Compliance Correction

The valid S1 sequence is now Claim Jeff's Right Arm, Grip Strike it from 30 to 20 (Damaged), Hell Saw it, use injected d6, bargain/harvest, then emergency graft. The seed-42 log records `hell_saw_roll` with `valid: true` and roll `6`, followed by a Clean harvest and one emergency-graft transaction of `-12` blood.

The correction changes only Jeff Right Arm's content size to `large`; Hell Saw remains restricted to damaged/critical large targets. Bone Scissors remains small/medium only. Failed Hell Saw still grants Rage and remains exercised by S3.

## 7. Seed-42 Paper Reconciliation

| Step | Paper action/result | Simulator action/result | Paper delta | Simulator delta | Cumulative simulator | Difference reason | Classification |
|---|---|---|---:|---:|---:|---|---|
| Start | S-001 begins at 85 | Starts at 85 | 0 | 0 | 85 | Same start | intended rule clarification |
| Jeff claim | Claim Right Arm | Claim Right Arm | -10 assumed | -10 | 75 | Same configured cost | intended rule clarification |
| Jeff setup | Damage valid target | Grip: 30 to 20, Damaged | 0 | 0 | 75 | Same role | intended rule clarification |
| Jeff extraction | Hell Saw sever | Hell Saw roll 6, Clean sever | -18 assumed | -18 | 57 | Now source-compliant | implementation defect corrected |
| Bargain/sale | Forced bargain and spare-arm sale | Right-arm bargain; left arm is ruined, no sale | undocumented gain | 0 | 57 | Sale value/path is absent from authoritative config/rules | unresolved contradiction |
| Emergency graft | Right Arm grafted, Unstable | Clean graft: -12; roll 1 Unstable | -12 | -12 | 45 | Same source-backed cost | intended rule clarification |
| Unstable | Paper says Unstable | Twitch then Surge fallback | unspecified | +2 | 47 | Seeded result was not specified on paper | random outcome |
| Anna | Focus, Guard, trade | Focus -3, Guard -4, Black Stitch trade | -7 assumed | -7 | 40 | Same modeled actions | scenario-policy difference |
| Table | Integrate arm | Integrate arm | -15 | -15 | 25 | Same table cost | intended rule clarification |
| Final | 37 blood | 25 blood | -48 total implied | -60 total | 25 | Missing/undefined spare-sale value; inferred +12 is not source-backed | paper arithmetic inconsistency / unresolved contradiction |

The simulator was not forced to 37. The paper's spare-arm sale is real historical evidence but lacks a configured price and implementation contract; adding one would be a product decision.

## 8. Existing Strategy Policy Audit

| Strategy | Fixed policy | RNG-sensitive branch | Blood Bag / rescue | Anna / table policy | Why completion was formerly universal |
|---|---|---|---|---|---|
| balanced | Claim, Grip, Saw, graft | Saw success; graft/Unstable rolls | Never uses bag; Panic may occur after low blood | Trade; integrate | Old runner labeled failed saw paths complete |
| blood_hoarder | Free Grip only | None | No bag, Panic, or rescue | No Anna/table | Incapacity surrender was counted as campaign completion |
| limb_greed | Claim/Saw then Anna greed | Saw and Stabilized roll | No bag | Greed; strengthen legs | Same failed-saw label problem |
| survival_first | Claim/Saw then trade | Saw and graft rolls | No bag; Panic may occur | Trade; repair torso | Same failed-saw label problem |
| reckless_sever | Unmarked Saw | Saw/graft rolls | No bag | Trade; integrate | Success creates Stressed, not premium, harvest |
| random_legal | Diagnostic legal choices only | Every choice via injected RNG | 10.6% use, rounds 4-7 | Random legal table option | Newly added; not representative player behavior |

All fixed strategies have no reachable collapse in the current scripted loop. Failed saws now produce `incomplete`, not collapse, because no follow-up enemy action/low-blood loop is run in those policies. Limb for Life remains reachable and unit-tested but was not used in these batches.

## 9. 500-Seed Metrics

`completed` means the campaign reached its scripted terminal table decision. `incomplete` means it did not acquire the graftable right arm. Neither label claims healthy survival or fun.

| Strategy | Complete | Incomplete | Collapse / Soft | Premium / Emergency graft | Final blood min / median / mean / max | Panic | Table paths |
|---|---:|---:|---:|---:|---|---:|---|
| balanced | 46.0% | 54.0% | 0 / 0 | 46.0% / 46.0% | 25 / 57 / 44.9 / 57 | 35.4% | 230 integrate; 270 none |
| blood_hoarder | 0.0% | 100.0% | 0 / 0 | 0.0% / 0.0% | 85 / 85 / 85.0 / 85 | 0.0% | 500 none |
| limb_greed | 46.0% | 54.0% | 0 / 0 | 46.0% / 46.0% | 27 / 57 / 43.3 / 57 | 0.0% | 230 strengthen; 270 none |
| survival_first | 46.0% | 54.0% | 0 / 0 | 46.0% / 46.0% | 27 / 57 / 44.6 / 57 | 46.0% | 230 repair; 270 none |
| reckless_sever | 46.0% | 54.0% | 0 / 0 | 0.0% / 46.0% | 30 / 67 / 51.4 / 67 | 0.0% | 230 integrate; 270 none |
| random_legal | 33.4% | 66.6% | 0 / 0 | 23.6% / 33.4% | 26 / 63 / 61.0 / 86 | 5.2% | 167 terminal choices; 333 none |

`random_legal` reached 17.6% Anna trade acceptance, 15.8% greed attempts, 7.8% greed successes, 10.6% Blood Bag use, 22.8% identical-body rate, and an average 5.45 actions / 5.85 rounds. Its most common bailout is `diagnostic_incomplete`. This is fuzz evidence only, not player behavior evidence.

## 10. Blood Bag Counterfactuals

All variants use the same 500 random-legal seeds and isolated in-memory config overlays. Baseline files were not changed.

| Variant | Completion | Soft rescue | Bag use | Mean final blood | Median | Panic | Interpretation |
|---|---:|---:|---:|---:|---:|---:|---|
| A baseline 25 / 15 bleeding | 33.4% | 0.0% | 10.6% | 61.0 | 63.0 | 5.2% | Reference |
| B 20 / 12 bleeding | 33.4% | 0.0% | 10.6% | 60.5 | 59.0 | 5.2% | Small blood reduction only |
| C 25 / 15, cap 60 | 33.4% | 0.0% | 10.6% | 59.9 | 57.5 | 5.2% | Cap changes terminal blood only |
| D unavailable | 33.4% | 0.0% | 0.0% | 59.4 | 59.0 | 7.2% | No completion change |

Blood Bag use occurs only in diagnostic rounds 4-7. It does not erase meaningful risk in this model, but that conclusion is weak because fixed strategies never use it and no collapse occurred. No variant is selected.

## 11. Table Identifiability Audit

| Option | Observable inside v0.1 | Verdict |
|---|---|---|
| Integrate arm | Removes Unstable checks and changes final body tag | Observable, but only terminally after Anna |
| Repair torso | Restores integrity/removes existing Bleeding tag | No future encounter tests the benefit | NOT IDENTIFIABLE IN SIMULATOR v0.1 |
| Strengthen legs | Changes limb definition/name | No knockdown/leg-pressure encounter follows | NOT IDENTIFIABLE IN SIMULATOR v0.1 |
| Table loan | Adds blood and records debt | No next fight resolves debt | NOT IDENTIFIABLE IN SIMULATOR v0.1 |
| Leave | Preserves state | Terminal summary only | NOT IDENTIFIABLE IN SIMULATOR v0.1 |

Fixed table choices are caused by strategy scripting and the campaign ending immediately after the table, not by demonstrated dominance. The random-legal spread proves legality, not strategic value.

## 12. Known Limitations and Product Gate

- Jeff/Anna scripts are intentionally narrow and do not create enough blood-loss pressure to evaluate collapse rates.
- Enemy blood remains separate from limb integrity as required, but the current scripts do not reduce enemy blood.
- The spare-arm sale in paper evidence has no authoritative value or rule path.
- No external player evidence exists; simulations do not prove fun.

### Verdict Evidence

**Implementation: PASS WITH NON-BLOCKING DEBT.** Supporting evidence: 44 automated tests, seeded reproducibility, valid S1 saw, exact graft cost, CLI/reporting coverage, and no global RNG. Contrary evidence: partial generic Plead/config-validation coverage. Confidence: high. Smallest next test: add explicit enemy-low-blood/core-exposed Plead cases.

**Product: INSUFFICIENT / NON-IDENTIFIABLE EVIDENCE.** Supporting evidence: no-spend premium exploit remains blocked; random legal choices reveal incomplete extraction and varied terminal bodies. Contrary evidence: no downstream table test, no collapse in 3,000 reviewed runs, and policies do not use most medical/escape branches. Confidence: high. Smallest next test: owner-approved rule/config clarification for spare sale plus a non-content diagnostic continuation only if approved.

**Unity: BLOCKED.** Supporting evidence: source gate remains explicit. Confidence: certain. Smallest next test: none until the simulator product signal is adequate.

## 13. Recommendation

Do not begin another development stage. Obtain owner decisions on the spare-arm sale/bargain transaction and on what evidence is required to evaluate table choices. Then revise rules/config and rerun the review diagnostics; no baseline rebalance is recommended from this evidence alone.
