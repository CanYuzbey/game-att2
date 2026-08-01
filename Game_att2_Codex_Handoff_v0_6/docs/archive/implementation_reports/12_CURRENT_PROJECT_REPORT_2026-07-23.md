# Game att2 — Current Project Report

> **ARCHIVED IMPLEMENTATION SNAPSHOT.** “Current” below means 2026-07-23. Use
> `../../README.md` and `../README.md` for the active documentation map.

Report date: 2026-07-23
Repository branch: `codex/simulator-causal-integrity`
Assessment role: skeptical senior multidisciplinary game-development leadership and hostile technical reviewer
Evidence basis: repository sources, Git history, code inspection, automated verification, simulator output, and recorded paper/self-play evidence

## 1. Executive summary

Game att2 has progressed beyond a paper-only concept into a small, deterministic Python rules simulator. The simulator represents the approved S-001 → Jeff → emergency graft → Anna → Grafting Table loop, structured event logging, seeded randomness, seven required scenarios, strategy batches, non-canonical post-table diagnostics, and owner-approved Downed/Stand/Brace behavior.

The project’s strongest validated result is conceptual coherence: the player desires a missing limb, pays Blood to acquire it cleanly, grafts it, inherits risk, faces a later maintenance decision, and can integrate the body change. The strongest implementation result is reproducibility: the current seed-42 mini-campaign ends at 25 Blood with an Integrated Grafted Human Right Arm, and the event stream explains every configured Blood transaction.

The project is not ready for Unity or Encounter 3 runtime implementation. Simulator output does not prove fun or balance, the available human evidence is contaminated designer self-play, P01–P08 remain pending, and two known action-economy defects weaken the validity of current runtime sequences.

### Gate verdicts

| Gate | Verdict | Confidence | Basis |
|---|---|---:|---|
| Package/build health | Pass | High | Package structure present; current environment runs tests and CLI |
| Automated implementation gate | Pass with known debt | High | 81 tests, Ruff, and strict mypy pass |
| Rules fidelity | Pass for approved simulator scope | High | Main-action ownership and Guard expiry corrected and regression-tested |
| Simulator product signal | Insufficient / non-identifiable | High | Scripted policies, no representative collapse distribution, limited downstream table evidence |
| Encounter 3 paper readiness | Materials ready; evidence pending | High | Bounded v0.2 packet exists; P01–P08 blank |
| Encounter 3 runtime gate | Blocked | Certain | Explicitly prohibited by binding sources |
| Unity gate | Blocked | Certain | Explicitly prohibited pending later review and approval |

### Merge recommendation

For this documentation-only consolidation: **merge**.

For the simulator as a basis for a new development stage: **revise first**. Fix the known action-economy defects, regenerate current evidence, and complete the approved human paper-test gate before any runtime scope expansion.

## 2. Epistemic status

### Confirmed facts

- The repository contains an installable Python package under `src/game_att2_sim/`.
- The package has CLI, YAML configuration, structured events, seeded RNG, scenarios, reports, tests, and non-canonical probes.
- Current verification passes: 81 tests, Ruff, and strict mypy.
- Seed 42 for `mini_campaign` currently completes at 25 Blood.
- Historical 37-Blood paper evidence and current 25-Blood simulation evidence are intentionally unreconciled.
- Encounter 3 runtime implementation and Unity are blocked.
- P01–P08 Encounter 3 human sessions are pending.
- `SELF-S01` and `SELF-S02` are contaminated designer diagnostics.

### Supported inferences

- The body-as-build hook is sufficiently coherent to justify continued rules research.
- The simulator is useful for detecting rule contradictions and implementation drift.
- Current strategy distributions are diagnostics, not reliable player-behavior predictions.
- The present implementation cannot support confident balance or fun conclusions.

### Recommendations

- Correct main-action ownership and Guard expiry before relying on later simulator evidence.
- Publish one regenerated current results artifact after corrections.
- Run the eight valid human sessions before revisiting the Encounter 3 runtime gate.
- Keep Unity blocked.

## 3. Project vision and identity

### One-sentence pitch

Game att2 is a single-player PC hell-loop limb-grafting roguelike/roguelite where the player survives ritualized turn-based duels by cutting useful limbs from other beings, spending Blood as both health and currency, and rebuilding their body into a desperate combat engine.

### Player fantasy

```text
I wake up broken.
I fight other broken things.
I cut away what I need.
I graft it onto myself.
I become something that can survive the loop.
```

### Identity that must be preserved

- Limbs are the primary build engine, not cosmetic equipment.
- Blood remains a volatile survival and spending resource.
- Combat is about extraction quality and future body state, not only damage.
- Emergency power creates maintenance consequences.
- Later encounters should test previous body decisions.
- Major actions must be readable and causally traceable.

### Identity failure conditions

The concept should be challenged if:

- limbs become passive stat gear;
- Blood becomes ordinary health or mana;
- premium extraction becomes free;
- grafting becomes consequence-free equipment swapping;
- later encounters ignore prior body changes;
- scripts preserve planned scenes after action sources become invalid.

## 4. Current product scope

### Approved simulator scope

- S-001 Torn but Stable;
- Jeff v0.4;
- emergency harvest and graft;
- Anna v0.4 stabilization/trade and greed paths;
- Grafting Table v0.2;
- six body slots;
- Blood, Panic Pulse, collapse, and tutorial soft collapse;
- limb states, tags, impairment, and harvest quality;
- Focus and Fast timing;
- Plead Pressure and Jeff incapacity surrender;
- Unstable v0.4;
- seeded scenarios, reports, and metrics;
- owner-approved Downed, Stand, and Brace behavior.

### Research-only scope

- non-canonical post-table pressure probes;
- bounded Encounter 3 Warden paper target zones;
- Momentum and Butcher facilitator policies;
- P01–P08 moderated human test materials.

### Prohibited current scope

- Warden runtime/configuration;
- additional runtime enemies or content;
- Warden anatomy, death, harvest, surrender, bargaining, escape, or rewards;
- Unity or another production-engine commitment;
- production UI, graphics, audio, persistence, map, procedural generation, meta progression, multiplayer, or store work.

## 5. Current architecture assessment

### Structure

| Area | Evidence | Assessment |
|---|---|---|
| Domain models | `models.py`, `enums.py` | Appropriate small dataclass/Enum model |
| Configuration | three versioned YAML files and `config_loader.py` | Clear authority for tunables; validation not exhaustive |
| Randomness | `rng.py` with seeded and scripted services | Correct architectural direction |
| Rule ownership | `rules.py` | Centralized and inspectable, but large and carrying unresolved action-economy debt |
| Scenarios | `scenarios.py` | Explicit test drivers; some scripted shortcuts weaken round fidelity |
| Reporting | structured events plus text/JSON/Markdown renderers | Meets traceability intent |
| Non-canonical probes | `probe.py` | Clearly labeled; scope boundary mostly well preserved |
| Tests | unit and integration suites | Good breadth for a small simulator; known behavior gaps remain untested |

### Positive technical qualities

- Domain systems do not print directly.
- Randomness is injected.
- Definitions and runtime state are separated.
- Invalid actions use domain-specific errors.
- YAML values are versioned and checked in.
- CLI supports named scenarios, batches, seeds, formats, and output.
- Reports are machine-readable and human-readable.
- Non-canonical probes are explicitly marked.

### Technical debt

1. `rules.py` is a broad rules engine rather than the narrower module map proposed in the technical specification. This is acceptable at current size but increases ownership coupling.
2. Configuration validation does not exhaustively validate all enemy action and table transformation references.
3. Some scenario scripts modify or force state for test setup. This is legitimate for fixtures only when prominently labeled.
4. Historical reports coexist with superseding reports, making the current state easy to misread.
5. Generated caches and local tooling artifacts exist in the working directory but are ignored; they should remain uncommitted.

## 6. Hostile rules and code review

### Resolved 2026-07-23 — main-action enforcement

Resolution:

- One rules-owned commitment path now consumes Main exactly once.
- Action-specific prerequisites are validated before commitment.
- Grip Strike, Claim the Cut, Bone Scissors, Hell Saw, Guard Flesh, Stand, and Brace use the same mechanism.
- The Jeff no-spend driver now advances one round between successful attacks.
- Focus and Fast remain non-consuming pre-Main operations.
- Focused regression tests cover every required invariant.

### Resolved 2026-07-23 — Guard Flesh round expiry

Resolution:

- Rules-owned end-of-round cleanup clears unused Guard.
- `guard_expired` is emitted for unused protection.
- `guard_consumed` is emitted when damage uses the protection.
- Cancelled, invalid, and absent enemy actions cannot carry Guard into the next round.

### P1 — current human evidence is contaminated

Evidence:

- SELF-S01 omitted body information, incorrectly treated Focus as consuming the main action, and inferred a medical item selection.
- SELF-S02 did not receive the required verbatim rules introduction and lacked requested responses.
- Both are explicitly classified as contaminated designer diagnostics.

Impact:

- They cannot support aggregate claims about fairness, clarity, agency, balance, or onboarding.

### P1 — historical reports can be mistaken for current results

Evidence:

- `Game_att2_Combat_Simulator_Results_v0_1.md` preserves superseded numbers.
- `Game_att2_Simulator_Review_Gate_v0_1.md` corrects them.
- Current CLI seed 42 produces 25 Blood.

Impact:

- Readers can cite 32, 37, or 25 without understanding their evidence class.

Control added by this documentation:

- README points to this report and states the current regression explicitly.

### P2 — product evidence remains thin

- Fixed strategies are scripted.
- Fixed strategies did not reach representative collapse behavior in the reviewed batches.
- Blood Bag use is absent from fixed policies.
- Table effects are often terminal or evaluated through synthetic pressure.
- Random-legal results are fuzz evidence, not human decision evidence.

## 7. Verification performed on 2026-07-23

Environment:

- bundled Python runtime;
- repository working directory;
- current checked-out branch;
- no gameplay values changed.

| Check | Result |
|---|---|
| `python -m pytest -q` | 81 passed |
| `python -m ruff check src tests` | All checks passed |
| `python -m mypy src` | Success; no issues in 14 source files |
| all seven scenarios, seed 42, Markdown | Executed successfully |
| mini-campaign, seed 42, JSON | Completed at 25 Blood with 32 structured events |

### Current seed-42 scenario snapshot

| Scenario | Result | Final Blood | Clean / Stressed / Ruined |
|---|---|---:|---:|
| Jeff baseline | Completed | 47 | 1 / 0 / 0 |
| Jeff no-spend | Completed | 85 | 0 / 0 / 0 |
| Failed Hell Saw | Completed | 29 | 0 / 0 / 0 |
| Anna stabilization | Completed | 63 | 0 / 0 / 0 |
| Anna greed | Completed | 79 | 1 / 0 / 0 |
| Mini-campaign | Completed | 25 | 1 / 0 / 0 |
| Blood Bag balance | Completed | 117 | 0 / 0 / 0 |

Interpretation caution:

- “Completed” is scenario-runner terminology and does not prove a healthy product outcome.
- The Blood Bag balance scenario applies documented variants sequentially as a diagnostic; its final Blood is not a campaign balance target.

## 8. Requirements traceability summary

| ID | Requirement | Current evidence | Status |
|---|---|---|---|
| RQ-001 | Six body slots | models, factory, config tests | Pass |
| RQ-002 | Blood health/currency/fuel | transactions and threshold tests | Pass |
| RQ-003 | Limb state transitions | damage/state tests | Pass |
| RQ-004 | Acting-limb impairment | effectiveness tests | Pass |
| RQ-005 | No free premium harvest | unit test and Jeff no-spend | Pass |
| RQ-006 | Committed clean sever | Claim/Saw/Scissors tests | Pass |
| RQ-007 | Harvest quality affects grafting | stability and salvage tests | Pass |
| RQ-008 | Emergency graft | cost, slot, and action tests | Pass |
| RQ-009 | Unstable v0.4 | branch and cost tests | Pass |
| RQ-010 | Focus before main | timing tests | Pass, but global main-action defect weakens full round assurance |
| RQ-011 | Fast item limit | timing/limit tests | Pass |
| RQ-012 | Plead and surrender | Jeff paths and generic threshold test | Pass with coverage debt |
| RQ-013 | Grafting Table choices | legality and probe tests | Mechanically pass; strategic value incomplete |
| RQ-014 | Structured logs | event and renderer tests | Pass |
| RQ-015 | Seeded reproducibility | repeated CLI/scenario tests | Pass |
| RQ-016 | Injected RNG | source architecture and tests | Pass |
| RQ-017 | CLI and batches | integration tests | Pass |
| RQ-018 | Text/JSON/Markdown | renderer tests and CLI run | Pass |
| RQ-019 | Config validation | load/invalid-value tests | Pass with breadth debt |
| RQ-020 | No domain printing | source inspection | Pass |
| RQ-021 | Completion traceability | review gate and this report | Pass |

## 9. Evidence and balance evaluation

### What the simulator supports

- Free blunt attacks do not independently create premium parts.
- Seeded success/failure paths are reproducible.
- A graft changes the available action set.
- Unstable grafts create inspectable outcomes.
- Anna can end through stabilization rather than death.
- Table options perform distinct state transformations.
- Downed/Stand/Brace can create measurable tempo differences.

### What it does not support

- a claim that Blood costs are balanced;
- a claim that Blood Bag is healthy in representative play;
- a claim that Anna paths are equally attractive;
- a claim that table options are generally competitive;
- a claim that the loop is fun, fair, readable, or replayable for outside players;
- a claim that Unity work should begin.

### 500-seed review evidence

The repository’s reviewed 500-seed batches found approximately 46% completion for several fixed extraction strategies because Hell Saw succeeds on half the seeded rolls. Blood Hoarder completed 0% under corrected campaign labeling and gained no premium limb. No reviewed fixed strategy collapsed, showing that the scripted policies did not exercise the intended death-pressure distribution.

This supports exploit protection and deterministic branching. It does not establish balance.

## 10. Paper and human-test state

### Completed internal evidence

- Jeff baseline paper test;
- no-spend exploit test;
- failed Hell Saw/death-spiral test;
- Anna medical test;
- forced Unstable test;
- mini-campaign paper test;
- non-canonical post-table probe;
- Knockdown/Brace validation;
- two contaminated designer Encounter 3 diagnostics.

### Pending evidence

- eight valid, free-choice, individually moderated P01–P08 Encounter 3 sessions;
- at least six participants explaining source damage → lost/weakened action;
- evidence that at least two strategic families avoid collapse;
- evidence that Known Threat affects planning without forcing one table choice;
- evidence that at least two table options remain defensible;
- zero facilitator invention of anatomy or hidden weak points;
- traceable state explaining failures.

### Encounter 3 boundary

The paper Warden has only three mechanical target zones and two action sources for the bounded test. These are not approval for complete anatomy, runtime enemy content, rewards, death, surrender, escape, or general AI.

## 11. Risks

| Risk | Probability | Impact | Current control | Status |
|---|---:|---:|---|---|
| Blood hoarding returns | Medium | Very high | clean-sever gate and no-spend scenario | Controlled but keep testing |
| Main-action drift | Confirmed | Very high | documented only | Open P0 |
| Guard persists across rounds | Confirmed | High | documented only | Open P1 |
| Blood Bag dominance | High | Medium | counterfactual diagnostics | Unresolved |
| Death spiral | Medium | Very high | Panic, Fast items, soft valve | Under-exercised |
| Limb system becomes stat gear | Medium | Very high | actions/passives and body summaries | Watch |
| Table has one answer | High | Medium | non-canonical probes | Not identified conclusively |
| Unstable becomes hated/ignored | Medium | High | branch metrics and Anna treatment | Unresolved |
| Facilitator overrides state | Medium | Very high | causal loop and cancellation policy | Must audit in P01–P08 |
| Paper zones imply anatomy | Medium | High | explicit boundary and contamination rule | Controlled on paper |
| Historical evidence is overclaimed | High | High | evidence labels and consolidated report | Reduced |
| Premature Unity | High | Very high | explicit blocked gate | Controlled |

## 12. Project timeline and time logs

The repository contains commit timestamps, not authoritative labor-hour tracking. The following is therefore a development-event log, not a timesheet.

| Timestamp (Europe/Istanbul) | Recorded event | Evidence class |
|---|---|---|
| 2026-07-16 19:07:17 | Combat-loop simulator review gate | Git commit |
| 2026-07-16 19:41:15 | Post-table consequence probe | Git commit |
| 2026-07-17 12:17:57 | Knockdown and Brace validation | Git commit |
| 2026-07-17 12:28:28 | Minotaur Warden paper encounter | Git commit |
| 2026-07-17 12:35:32 | Minotaur human-test operations | Git commit |
| 2026-07-18 14:59:27 | Designer self-play protocol | Git commit |
| 2026-07-18 16:24:27 | Interim self-play closeout | Git commit |
| 2026-07-18 19:37:52 | Systemic causal design skill | Git commit |
| 2026-07-18 20:11:02 | Encounter 3 paper reconciliation | Git commit |
| 2026-07-23 | Current repository audit, verification, report, and README | Current work session |

Known execution-duration records:

- Current automated tests: 2.87 seconds.
- Current full lint/type/test sequence: approximately 9 seconds.
- Historical post-table matrix: 1,000 paired seeds × 5 options × 4 profiles × 8 fixtures, reported as 60.18 seconds.
- Historical large sensitivity runs hit 120-second command limits.
- Optimized natural-state Knockdown rows reused one config and reported 1.14 seconds.

Missing:

- no authoritative hours-by-person record;
- no session start/stop log for early design and implementation;
- no cost or budget ledger.

## 13. Documentation health

### Strong

- binding authority and source precedence are explicit;
- rules, technical specification, test plan, evidence, risks, and return contract exist;
- paper/runtime boundaries are unusually clear;
- systemic causal governance is documented;
- contaminated evidence is preserved rather than repaired.

### Weak

- historical and current statements coexist without a single prior front door;
- some files still say “simulator pending” although implementation exists;
- original results are preserved beside superseding review results;
- the manifest describes the original handoff package rather than every later artifact;
- several old Minotaur documents are superseded but still prominent by filename.

### Documentation recommendation

Keep historical evidence immutable, but add a status banner to superseded documents in a future documentation pass. Do not rewrite old evidence as though later decisions existed at the time.

## 14. Consolidated owner questions

No answer is inferred for these.

### Resolved by the 2026-07-23 owner directive

- Main-action consumption is centralized and enforced.
- Unused Guard expires at end of round with a structured event.
- Affected scenario drivers obey corrected action economy.
- A new versioned authoritative results artifact supersedes historical results without deleting them.

### Product and evidence questions

1. Is the spare Jeff arm still intended to be saleable? If yes, what exact eligibility, value, timing, and persistence rule is approved?
2. What evidence threshold should the simulator meet before you would consider a tiny interactive text prototype?
3. Do you want the eight P01–P08 sessions to proceed now that the simulator action-economy correction is complete?

### Encounter 3 questions

4. Are the current v0.2 bounded causal paper materials approved exactly as the next human-test packet?
5. Should SELF-S01 and SELF-S02 remain permanently separate diagnostics, with replacement human participants still labeled P01–P08?
6. What minimum positive/negative human evidence would authorize revisiting—not automatically approving—Encounter 3 runtime implementation?

### Future identity questions, not needed now

7. Is “Game att2” still only a working title?
8. Is Unity still the leading engine candidate, or should engine choice remain completely open?
9. Is the table/action-cut-in hybrid still the intended presentation hypothesis for a later graybox?
10. Which accessibility goals should become requirements before any interactive prototype?
11. Do you want formal person-hour logging from the next session onward, and if so, by task, discipline, or calendar session?

## 15. Recommended next plan

### Phase A — owner decisions

Answer questions 1–6 as a single decision batch. Questions 7–11 can remain open.

### Phase B — simulator integrity correction

Completed on 2026-07-23. The authoritative evidence is `Game_att2_Combat_Simulator_Results_v0_2.md`.

### Phase C — human paper evidence

- run P01–P08 individually;
- apply contamination rules strictly;
- preserve raw records;
- aggregate only eight valid sessions;
- evaluate all ten paper-gate criteria;
- return a paper-test decision report.

### Phase D — gate review

Choose one:

- revise rules/config and rerun;
- improve simulator coverage;
- build a tiny interactive text prototype;
- prepare a Unity graybox proposal;
- stop or pivot.

Current recommendation: **review the corrected simulator evidence, then run the human paper gate. Keep Encounter 3 runtime and Unity blocked.**

## 16. Scope audit

This reporting task changed documentation only:

- replaced the handoff-only README with a complete project README;
- added this current project report;
- did not change gameplay code, tests, configuration, numeric balance, content, runtime enemies, or research records;
- did not add dependencies, Unity, UI, persistence, or production systems;
- did not reinterpret Encounter 3 paper approval as runtime approval.

## 17. Final conclusion

Game att2 has a distinctive, testable core and a healthy culture of evidence labeling, scope control, and causal traceability. The deterministic simulator is a useful research instrument and currently passes its automated suite. However, the project should not confuse tool health with product validation. Known action-economy defects, contaminated human evidence, pending P01–P08 sessions, and weak balance identifiability block a production-stage recommendation.

The project should continue cautiously at the simulator and moderated-paper-test level. It should not enter Unity or expand runtime content yet.
