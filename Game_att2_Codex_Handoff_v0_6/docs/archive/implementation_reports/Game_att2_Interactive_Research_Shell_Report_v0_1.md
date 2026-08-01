# Game att2 Interactive Research Shell Report v0.1

Status date: 2026-07-23

Branch: `research/interactive-shell-v01`

Parent baseline: `9b3f72b33e0c6b27f29e90e72f91841e5f0dbb81`

Evidence status: implementation and owner diagnostic complete; external-player evidence absent

## 1. Scope and purpose

Interactive Research Shell v0.1 is a terminal research interface over the accepted
deterministic Python simulator. Its only playable sequence is:

```text
S-001 -> Jeff -> emergency graft -> Anna -> Grafting Table
```

The shell makes the simulator's existing choices inspectable and selectable without
becoming a second rules engine. It is intended to collect traceable diagnostic and
pilot evidence about comprehension, action selection, consequences, and the current
economy. It is not production UI, a balance claim, or permission to implement Unity or
Encounter 3.

This branch descends directly from provisional accepted causal-integrity commit
`9b3f72b`. That branch has not been described as merged or integrated into the main
research branch. The required later review order remains:

```text
review causal-integrity commit
-> merge causal-integrity branch
-> review interactive-shell branch
-> merge interactive-shell branch
```

## 2. Architecture and authority

`InteractiveResearchSession` owns presentation, session progression, confirmations,
research metadata, transcript capture, and export. `RuleEngine` remains the sole
authority for legality, cost, Main/Fast/Focus timing, action-source usability, state
mutation, Guard lifecycle, grafting, Anna resolution, table resolution, and structured
domain events.

The shell asks rules-owned affordance methods for both legal and disabled actions.
Each affordance contains an action identifier, readable label, timing class, cost,
enabled state, disabled reason, source, target, risk, and confirmation requirement.
Execution then calls the existing rule method; the shell does not waive a failed
validation or directly reproduce the rule mutation.

Decision records capture the state before commitment, including Blood, body state,
statuses, visible enemy intent, Main/Focus/Fast availability, source availability, the
complete offered-action list, the selected action, and its disposition. Invalid,
disabled, and cancelled attempts remain visible as research evidence.

Confirmation is required for irreversible choices. Cancellation is recorded before
commitment and does not call the rule method, consume Main, change gameplay state, or
advance the RNG. This is regression-tested using state and RNG tokens.

The shell's encounter driver uses a small explicit deterministic enemy policy only to
advance the already approved Jeff and Anna encounters. It adds no enemy, action,
reward, dialogue system, or canonical outcome.

## 3. Evidence classification

Every session must be one of:

- `OWNER_DIAGNOSTIC`
- `EXTERNAL_PILOT`
- `AUTOMATED_REGRESSION`

Participant-code prefix validation prevents the interface from labeling owner/self or
automated evidence as external pilot evidence. This is an interface integrity guard,
not an identity-verification system. Strategy intention and information condition are
stored as metadata; the current approved sequence uses `NOT_APPLICABLE` unless a
research protocol supplies a meaningful condition.

## 4. Configuration integrity

Configuration loading now validates all references used by the approved sequence:

- limb-provided action identifiers;
- starting-body limbs and item inventory;
- enemy body slots and action identifiers;
- table transaction identifiers and configured fields;
- scenario starting-body and encounter identifiers.

The content file now defines `cover_it`, `black_stitch`, `calm_guard`, and
`trade_offer`, which were already referenced by the approved Jeff/Anna scripts. This
formalizes existing references for fail-fast validation; it does not add playable
actions or new canonical content.

Generic Plead Pressure is reachable through free choice. A clean major sever applies
the existing pressure rule, and Jeff losing both arms invokes the existing documented
Jeff trigger. The threshold resolution and its structured event are covered by an
integration test.

## 5. Owner-diagnostic session

Session `OWNER-DIAG-SHELL-001` was run through the interactive terminal loop with seed
42 and classified `OWNER_DIAGNOSTIC`. It is diagnostic evidence, not an external
playtest.

Selected path:

```text
Claim the Cut: Jeff right arm
-> Grip Strike: Jeff right arm
-> Hell Saw: Jeff right arm
-> Grip Strike: Jeff left arm
-> Grip Strike: Jeff left arm
-> emergency graft
-> Focus
-> Guard Flesh
-> accept Anna stabilization trade
-> integrate arm at the Grafting Table
```

Result:

| Field | Result |
|---|---|
| Outcome | `COMPLETED` |
| Anna path | `stabilization_trade` |
| Table choice | `integrate_arm` |
| Final Blood | 25 |
| Decision points | 10 |
| Structured events | 49 |
| Right arm | grafted and integrated |
| Torso | critical and bleeding |

Evidence files:

- `research/interactive_shell/OWNER-DIAG-SHELL-001-transcript.txt`
- `research/interactive_shell/OWNER-DIAG-SHELL-001.json`
- `research/interactive_shell/OWNER-DIAG-SHELL-001-summary.md`
- `research/interactive_shell/example_action_sequence.json`

The 49-event shell trace is not numerically comparable to the 39-event automated
`mini_campaign` trace. The shell records UI decisions and uses actual per-round enemy
responses, while the approved automated scenario remains a compact deterministic
regression driver. The shared final 25 Blood is an observed result, not a target the
shell forced.

## 6. Regression and verification

Verification run on 2026-07-23:

| Check | Result |
|---|---|
| Full pytest suite | 91 passed |
| Ruff | all checks passed |
| Strict mypy | success; 16 source files |
| Seven approved scenarios, seed 42 | all completed |
| `mini_campaign`, seed 42 | completed; 25 Blood |
| Representative batches | five strategies x 100 seeds completed |
| Repeated replay | byte-identical for identical metadata, seed, and action sequence |
| Manual owner diagnostic | completed; export, summary, transcript retained |

Approved seed-42 scenario results remain:

| Scenario | Result | Final Blood | Clean/Stressed/Ruined |
|---|---|---:|---|
| `jeff_baseline` | completed | 47 | 1/0/0 |
| `jeff_no_spend` | completed | 85 | 0/0/0 |
| `failed_hell_saw` | completed | 29 | 0/0/0 |
| `anna_stabilization` | completed | 63 | 0/0/0 |
| `anna_greed` | completed | 79 | 1/0/0 |
| `mini_campaign` | completed | 25 | 1/0/0 |
| `blood_bag_balance` | completed | 117 | 0/0/0 |

Representative batch metrics are unchanged from
`Game_att2_Combat_Simulator_Results_v0_2.md`: balanced, limb-greed, survival-first,
and reckless-sever each complete 44%; Blood Hoarder completes 0%. No shell change
modifies a balance value or accepted scenario policy.

Focused shell tests cover state-derived legal/disabled affordances and reasons,
disabled/rejected attempts, cancellation integrity, Main consumption, Focus + Main,
Fast + Main, source destruction, Guard use and expiry, generic Plead, evidence
classification, complete structured export, divergent free-choice trajectories,
deterministic replay, broken configuration references, and continued approved-scenario
execution.

## 7. Run instructions

Interactive session:

```powershell
python -m game_att2_sim.research_cli `
  --session-id OWNER-DIAG-002 `
  --evidence-class OWNER_DIAGNOSTIC `
  --participant-code OWNER-002 `
  --seed 42 `
  --json-output research/interactive_shell/OWNER-DIAG-002.json `
  --summary-output research/interactive_shell/OWNER-DIAG-002-summary.md `
  --transcript-output research/interactive_shell/OWNER-DIAG-002-transcript.txt
```

Deterministic scripted replay:

```powershell
python -m game_att2_sim.research_cli `
  --session-id AUTO-SHELL-002 `
  --evidence-class AUTOMATED_REGRESSION `
  --participant-code AUTO-002 `
  --seed 42 `
  --script research/interactive_shell/example_action_sequence.json `
  --json-output research/interactive_shell/AUTO-SHELL-002.json `
  --summary-output research/interactive_shell/AUTO-SHELL-002-summary.md
```

For byte comparison, replay with identical complete metadata, including the same
timestamp. The timestamp is research metadata and is therefore part of the exported
input identity.

## 8. Scope confirmation

No balance values, Blood costs, damage values, probabilities, limb thresholds, table
prices, approved scenario outcomes, or economy systems changed. No Encounter 3,
Minotaur Warden, Unity, production UI, art, audio, persistence, procedural generation,
meta-progression, new enemy, or new canonical content was implemented.

Historical simulator result files remain unchanged. The authoritative causal-integrity
simulator artifact is still `Game_att2_Combat_Simulator_Results_v0_2.md`. This report
is the new authoritative artifact for Interactive Research Shell v0.1 and does not
supersede historical simulator evidence.

## 9. Remaining defects, limitations, and contradictions

- No valid external-pilot session exists. The shell proves execution and auditability,
  not comprehension, fun, accessibility, preference, or balance.
- The terminal presentation is intentionally minimal and is not production UI.
- Affordance construction and action execution are separate methods inside the same
  `RuleEngine`; tests guard their agreement, but future rule changes must update both
  contracts together.
- The deterministic enemy policy is a research driver, not a claim about final enemy
  AI or encounter pacing.
- The owner diagnostic reached the table with a critical bleeding torso. This is a
  valid trace under existing rules and should be evaluated as research evidence, not
  silently repaired by the interface.
- Generic Plead and Jeff's special both-arms-lost surrender share a documented
  boundary. The shell invokes existing triggers and records their order; an owner may
  later decide whether the presentation should distinguish them more explicitly.
- Evidence-class prefix validation prevents obvious mislabeling but cannot establish
  participant independence by itself; research operations must still control that.
- The historical paper 37-Blood result and deterministic 25-Blood result remain
  unreconciled because the spare-arm sale has no approved configured rule or value.
- Encounter 3 runtime work and Unity remain blocked by the existing evidence gates.
