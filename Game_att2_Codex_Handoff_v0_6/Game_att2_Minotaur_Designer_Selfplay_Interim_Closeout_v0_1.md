# Minotaur Designer Self-Play Interim Closeout v0.1

## Status

This is a user-directed interim closeout after two of four planned designer self-play sessions. `SELF-S03` and `SELF-S04` were not started. The session protocol normally defers analysis until all four sessions; this document is therefore a diagnostic handoff, not a completed study or a production gate.

Evidence classification remains `N=1` project-owner/designer self-play, same sitting, with high prior knowledge and unavoidable learning contamination. It cannot support population, accessibility, fun, fairness, balance, or general onboarding claims.

## Verified State

- Branch: `research/minotaur-designer-selfplay-v01` at `f306dd6` before the uncommitted session records and this closeout.
- Simulator verification on the current checkout:
  - `python -m ruff check src tests`: passed.
  - `python -m mypy src`: passed.
  - `python -m pytest -q`: `63 passed`.
  - `python -m game_att2_sim --all-scenarios --seed 42 --format text`: completed all seven scenarios.
- No Unity, graphics, enemies in runtime, new mechanics, persistence, procedural generation, or progression were added.
- Encounter 3 production implementation and Unity remain blocked.

## Session Evidence

Both sessions used the same four-round Script B and ended with active torso Bleeding and Downed after the final Charge. Each used one Blood Bag, lost one normal action to Stand, and did not collapse.

| Session | Condition | Table choice | Fairness | Clarity | Agency | Table usefulness | Validity |
|---|---|---|---:|---:|---:|---:|---|
| `SELF-S01` | Unknown | Integrate Arm | 1/5 | 3/5 | 1/5 | 3/5 | Contaminated by incomplete body presentation, incorrect Focus facilitation, and an inferred Fast-item selection. |
| `SELF-S02` | Known | Repair Torso | 2/5 | 4/5 | 1/5 | 1/5 | Diagnostic only; the required rules introduction was not delivered verbatim and multiple requested responses were unavailable. |

Participant statements worth preserving, without generalization:

- The table and each action felt forced or unimpactful.
- Focus appeared to reveal an outcome without a usable follow-up.
- The Warden's actions came to feel indistinguishable.
- The participant repeatedly sought offensive, evade, escape, or stun responses.

The raw transcripts and structured data are in `research/designer_selfplay/`.

## Facilitation Deviations

1. `SELF-S01` initially omitted the existing Human Left Arm from the compact body state. This plausibly affected the arm-integration rationale.
2. `SELF-S01` incorrectly treated Focus as consuming the main action. The authoritative rules state that Focus occurs before Fast and main actions and does not consume the main action. The round cannot be used as evidence about intended Focus counterplay.
3. `SELF-S01` inferred Blood Bag from an unspecified request to use a medical item. Blood Bag was the only legal item then, but the selection was not explicitly named.
4. The required facilitator rules introduction was not read verbatim in either session.
5. Grip Strike was offered and resolved as a no-effect action despite the encounter packet intentionally providing no Warden target, health, limbs, loot, or defeat path.

The raw logs and `sessions.csv` include retrospective validity flags. Do not repair the historical outcomes or treat alternative actions as having happened.

## Blocking Findings

### P0: Encounter 3 is not a combat loop with offensive agency

The paper packet explicitly excludes a Warden health, limb, loot, or defeat model. A player attack cannot affect the four-round action sequence. The packet is therefore a defensive survival-pressure probe, while the participant reasonably approached it as a combat encounter.

Owner decision required: either define the packet explicitly as a defensive endurance test with only meaningful legal responses, or approve a separate bounded target/response model. Do not silently add a Warden implementation or a new mechanic.

### P0: Repair Torso is mechanically inert in the chosen baseline

`damaged_human_torso` starts at full integrity and runtime state `intact`. Repair restores that same state. With the fixed first Cleave, both recorded paths went from `45` to `37` integrity and received Bleeding on the public `d6=5`.

Owner decision required: decide whether the post-Anna baseline torso should begin mechanically Damaged, or narrow/remove the table's claimed immediate repair value for this packet.

### P0: Integrate Arm is mechanically inert in the chosen baseline

Anna's trade removes `UNSTABLE`; arm integration principally removes `UNSTABLE` and adds `INTEGRATED`. The paper packet claims integration is valuable against an Unstable graft, but its supplied post-Anna baseline does not expose that condition.

Owner decision required: lock a single intended pre-table baseline before any future table test. Do not use the current sessions to compare Integration with Repair.

### P0: Main-action enforcement is incomplete in the runtime

Focus correctly does not consume the main action, but Grip Strike and Guard Flesh do not consistently mark the main action as consumed. The baseline scenario uses Grip Strike twice in one round. This contradicts the authoritative sequence of one main action after optional Focus and Fast actions.

Required future work, only with approval: enforce consumption for every main action and add regression coverage before treating runtime action economy as validated.

### P1: Guard duration can persist beyond its intended round

Guard is intended for the current round, but runtime state clears it only when an enemy attack lands. A cancelled or invalid enemy action can carry protection into a later round.

Required future work, only with approval: expire Guard at round end and add a regression test.

### P1: Source-precedence conflict blocks Encounter 3 runtime work

`AGENTS.md` forbids new enemies, while lower-precedence supporting material calls the Warden canonical for paper testing. The paper and self-play documents already block production implementation. No Warden runtime code is authorized until the higher-precedence sources are reconciled by the owner.

### P1: Existing simulator report is historically useful but stale as a standalone decision artifact

`Game_att2_Combat_Simulator_Results_v0_1.md` retains an earlier seed-42 mini-campaign total of `32` while later corrections and the current CLI report `25`. A future gate review should publish a consolidated current report rather than relying on the older file alone.

## Next-Chat Entry Point

1. Read this closeout, `AGENTS.md`, and the source-precedence order in `README.md`.
2. Decide the Encounter 3 action-model scope and the intended post-Anna table baseline.
3. Decide whether to discard/replace the two contaminated sessions or end designer self-play.
4. Do not start `SELF-S03`, `SELF-S04`, directed coverage, Encounter 3 implementation, or Unity work without explicit owner approval.
5. If implementation is approved later, first fix the action-economy and Guard-expiry defects with tests, then rerun the unified verification set and produce an updated simulator results artifact.
