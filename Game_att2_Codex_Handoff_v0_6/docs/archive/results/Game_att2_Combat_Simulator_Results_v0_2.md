# Game att2 Combat Simulator Results v0.2

> **ARCHIVED RESULT SNAPSHOT.** This report remains regression evidence for the
> 2026-07-23 simulator state. It does not override Combat Rules v0.5, the active
> documentation index, or current verification output.

Historical status at publication: **current authoritative simulator implementation evidence**
Correction: Simulator Causal Integrity
Date: 2026-07-23
Scope: S-001 → Jeff → emergency graft → Anna → Grafting Table only

## 1. Executive verdict

The causal-integrity correction passes its implementation gate.

- Exactly one successfully committed Main action is allowed per actor per round.
- Main-action commitment is centralized in rules-owned logic.
- Pre-commit rejection does not consume Main or mutate gameplay state.
- Focus and one Fast item remain non-consuming pre-Main operations.
- Stand consumes Main.
- Guard Flesh is either consumed by eligible damage or expires during rules-owned end-of-round cleanup.
- No balance values, canonical content, Encounter 3 runtime material, Unity work, or production system changed.

The corrected seed-42 mini-campaign still completes at **25 Blood**. Its event count increases from **32 to 39** because six successful Main actions now emit explicit commitment events and Guard use emits one explicit consumption event.

This is implementation evidence. It does not prove fun, balance, accessibility, market demand, Encounter 3 runtime readiness, or Unity readiness.

## 2. Architecture correction

### Main-action ownership

Each Main action follows one transaction boundary:

```text
check current Main availability
→ validate source, item, target, state, and affordability
→ commit Main once through RuleEngine
→ emit main_action_committed
→ apply cost, randomness, and state effects
```

The centralized commit owns `normal_action_consumed`, the commitment event, and action-frequency accounting. Grip Strike, Claim the Cut, Bone Scissors, Hell Saw, Guard Flesh, Stand, and Brace all use it.

Failure before commitment is atomic with respect to gameplay state: the action remains available, resources and inventory remain unchanged, and no target mutation occurs. A committed action may still produce an unfavorable approved outcome, such as a failed Hell Saw or failed Stabilized sever; that is a resolved action and correctly consumes Main.

### Round-lifecycle ownership

`RuleEngine.start_round()` closes the prior round before opening the next one. Rules-owned `end_round()` now:

- expires unused Guard Flesh and emits `guard_expired`;
- expires unused active Brace protection;
- resolves Unstable Surge fallback;
- prevents temporary protection from leaking into the next round.

Guard mitigation also flows through one rules method. A used Guard emits `guard_consumed`; a cancelled or invalid enemy action leaves it active only until end-of-round cleanup.

## 3. Files changed for the correction

| File | Change |
|---|---|
| `src/game_att2_sim/models.py` | Added explicit active-Brace round state |
| `src/game_att2_sim/rules.py` | Central Main commitment, precommit validation, Guard mitigation/expiry, Stand and Brace ownership |
| `src/game_att2_sim/scenarios.py` | One round per successful Jeff no-spend Grip Strike |
| `src/game_att2_sim/probe.py` | Uses rules-owned Guard mitigation |
| `src/game_att2_sim/reporting.py` | Marks newly rendered Markdown evidence as Results v0.2 |
| `tests/unit/test_causal_integrity.py` | Focused causal-integrity regression suite |
| integration reporting/probe tests | Updated rejection-event and results-version expectations |
| `docs/08_DECISIONS_RISKS_OPEN_QUESTIONS.md` | Recorded owner-directed correction |
| `README.md` and current report | Updated project state |
| historical result/review artifacts | Added superseded status banners only |

## 4. Verification results

| Check | Result |
|---|---|
| Full pytest suite | 81 passed |
| Ruff | All checks passed |
| Strict mypy | Success; no issues in 14 source files |
| Seven approved scenarios | All executed successfully |
| Seed-42 mini-campaign | Completed, 25 Blood, 39 events |
| Repeated seed-42 comparison | Byte-for-byte identical JSON output |
| Representative strategy batches | Five strategies × 100 seeds completed |

## 5. Required scenario results: before and after

The “before” column is the verified pre-correction checkout. The “after” column is this correction.

| Scenario, seed 42 | Before result / Blood | After result / Blood | After events / rounds | Explanation |
|---|---:|---:|---:|---|
| Jeff baseline | completed / 47 | completed / 47 | 27 / 5 | Valid driver already used one Main per round; only commitment events were added |
| Jeff no-spend | completed / 85 | completed / 85 | 13 / 4 | Four Grip Strikes now occupy four rounds instead of two; no Blood transaction changed |
| Failed Hell Saw | completed / 29 | completed / 29 | 16 / 3 | Driver already obeyed action economy; commitment events added |
| Anna stabilization | completed / 63 | completed / 63 | 13 / 1 | Focus remains pre-Main; Guard is the single Main action |
| Anna greed | completed / 79 | completed / 79 | 14 / 3 | Existing three Main actions already occupied separate rounds |
| Mini-campaign | completed / 25 | completed / 25 | 39 / 6 | No configured transaction changed; new causal events only |
| Blood Bag balance | completed / 117 | completed / 117 | 11 / 3 | Fast items remain non-Main; no Main action is used |

### Numerical changes

Only one approved-scenario numeric metric changes:

- Jeff no-spend `rounds`: **2 → 4**, because four successful Grip Strikes can no longer be compressed into two rounds.

Final Blood, harvest counts, body outcomes, and scenario result labels are unchanged for all seven seed-42 scenarios. The correction does not preserve invalid timing; it preserves only outcomes that still follow from legal sequencing.

## 6. Seed-42 mini-campaign reconciliation

### Before

- Final Blood: 25
- Events: 32
- Rounds: 6

### After

- Final Blood: 25
- Events: 39
- Rounds: 6

### Seven added events

- six `main_action_committed` events:
  - Claim the Cut;
  - three Grip Strikes;
  - Hell Saw;
  - Guard Flesh;
- one `guard_consumed` event when Anna’s Surgical Jab uses Guard.

No Blood delta, RNG result, harvest quality, graft outcome, Anna trade, table cost, or final body state changed.

## 7. Representative 100-seed strategy batches

All batches use `mini_campaign`, seeds beginning at 42, and the existing strategies.

| Strategy | Completion | Collapse | Mean / median Blood | Mean rounds | Premium graft | Table paths |
|---|---:|---:|---:|---:|---:|---|
| balanced | 44% | 0% | 45.59 / 57 | 4.32 | 44% | 44 integrate; 56 incomplete |
| blood_hoarder | 0% | 0% | 85 / 85 | 4.00 | 0% | 100 incomplete |
| limb_greed | 44% | 0% | 43.92 / 57 | 5.20 | 44% | 44 strengthen; 56 incomplete |
| survival_first | 44% | 0% | 45.07 / 57 | 4.32 | 44% | 44 repair; 56 incomplete |
| reckless_sever | 44% | 0% | 52.14 / 67 | 4.32 | 0% | 44 integrate; 56 incomplete |

Compared with the captured pre-correction 100-seed baseline, all listed rates and Blood statistics are unchanged. Blood Hoarder mean rounds changes from **2.00 to 4.00** because its four successful attacks now use four legal rounds.

These fixed policies still produce no collapse and are not representative human-play evidence.

## 8. Regression coverage

Focused tests prove:

- every implemented Main action commits exactly once on success;
- a second Main action in the same round is rejected;
- invalid target, unavailable resource, and destroyed source failures do not commit;
- rejected actions do not change Blood, inventory, target integrity/state/tags, or Main availability;
- Focus + Main remains legal;
- Fast + Main remains legal;
- Fast remains legal while Downed before Stand;
- Stand consumes Main and blocks a follow-up Main;
- Guard clears and emits an event when used;
- unused Guard expires and emits an event at round end;
- Guard cannot survive cancelled or absent enemy action into the next round;
- approved seed-42 scenarios contain at most one Main commitment for each actor-round;
- unusable action sources cannot resolve.

## 9. Determinism

Two independent CLI executions of:

```text
python -m game_att2_sim --scenario mini_campaign --seed 42 --format json
```

produced byte-for-byte identical output. Existing seeded and scripted RNG ownership is unchanged; no module-global domain randomness was introduced.

## 10. Scope audit

Confirmed unchanged:

- all costs, gains, thresholds, probabilities, and configured content;
- S-001, Jeff, Anna, and Grafting Table definitions;
- historical 37-Blood paper evidence and its unresolved spare-arm sale contradiction;
- Encounter 3 paper materials;
- Encounter 3 runtime block;
- Unity block;
- production-system exclusions.

Not added:

- enemies, items, limbs, rewards, economy systems, UI, art, audio, persistence, procedural generation, meta progression, engine integration, or new canonical content.

## 11. Remaining defects and contradictions

### Implementation/diagnostic debt

- Generic Plead Pressure triggers for enemy-low-Blood, core exposure, and personality fear remain lightly exercised.
- Configuration validation still does not exhaustively validate every enemy action and table transformation reference.
- Fixed strategy policies under-exercise Blood Bag, collapse, and soft-collapse behavior.
- `rules.py` remains a broad module; further splitting is not justified until scope or complexity grows.

### Product/evidence gaps

- Historical paper 37 Blood and deterministic seed-42 25 Blood remain unreconciled because the spare-arm sale has no approved configured rule or value.
- Simulator batches do not prove fun, balance, accessibility, or player behavior.
- P01–P08 human Encounter 3 paper sessions remain pending.
- SELF-S01 and SELF-S02 remain contaminated diagnostics.
- Encounter 3 runtime implementation and Unity remain blocked.

## 12. Recommendation

Accept the causal-integrity correction as the current simulator implementation baseline. Do not rebalance from these results. Proceed next to owner review and the already-approved moderated human paper-test gate; do not implement Encounter 3 or begin Unity without a separate approval.
