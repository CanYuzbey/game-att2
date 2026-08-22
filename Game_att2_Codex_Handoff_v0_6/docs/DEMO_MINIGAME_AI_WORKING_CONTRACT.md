# Game att2 - Demo Mini-Game AI Working Contract

Status date: 2026-08-22

Status: **BINDING OPERATIONAL CONTRACT FOR AI-ASSISTED DEMO WORK. NOT A DESIGN
AUTHORITY, RUNTIME APPROVAL, OR CLAIM THAT THE MINI-GAME EXISTS.**

## 1. Purpose

Direct one developer and their AI toward a small, genuinely playable mini-game. The
job is not to describe the whole game as finished, build generic future systems, or
turn every idea in the documents into content.

The five living design documents remain the paper-design authority. This file controls
how work is scoped, evidenced, and reported.

## 2. Current existence baseline

As of 2026-08-22:

- the new Underground City mini-game has paper decisions but **no approved or verified
  product runtime**;
- the deterministic Python campaign is frozen legacy rules evidence;
- the H1 runner and visual lab are isolated research instruments;
- `demo/` is a disposable movement demo, not the Underground City mini-game;
- no engine choice, engine project, production content pipeline, complete UI, save
  system, or playable new-demo build is established by these documents.

An AI must verify this baseline again from the repository before each implementation
task. Documentation is evidence of intent, never evidence that gameplay exists.

## 3. Required status vocabulary

| Label | Use |
|---|---|
| `PAPER RULE` | Owner chose the player-facing direction; it is not code. |
| `WORKING HYPOTHESIS` | Worth testing; may change after play. |
| `OPEN` | Owner has not decided; do not fill it by plausibility. |
| `IMPLEMENTED — NOT VERIFIED` | Relevant code/assets exist but the required check has not passed. |
| `VERIFIED IN <artifact>` | Fresh evidence passed for one named artifact and scope. |
| `BLOCKED` | A named gate or owner decision prevents the next action. |

Never use an unlabeled `done`, `ready`, `complete`, `working`, `playable`, or a project
completion percentage. A valid claim has this shape:

```text
VERIFIED IN <exact artifact>: <observable behavior>
Evidence: <command/build>, exit <status>, <manual or automated observation>
Does not prove: <adjacent untested/product claims>
```

## 4. Bounded mini-game contract

The intended playable proof is one compact same-day loop:

```text
captive in the Underground City
-> negotiate/trade with the Guard while bound
-> become free but leave the bargain weaker
-> traverse one small playable dungeon/city section
-> enter one paused, in-world, one-versus-one interaction
-> use dialogue as a route into bargain, refusal, surrender, or card combat
-> play body-sourced cards against target body regions
-> produce causal injury, capability, surrender, or death consequences
-> kill for Blood and lose limb access, or after living surrender perform the limb
   bargain through a Grafting Table transition with no kill-Blood reward
-> continue with the changed body or die
-> on death, return to the start of the same day under the persistence contract
```

The exact mini-game ending and duration are `OPEN`. Three encounters, a Merchant, an
Exit Keeper, a complete roguelite meta, and the full game are not implied minimum
scope. Add content only when it is required to prove the chain above.

### Opening contract — paper rule

- Refusing the Guard's offer leaves the player captive and returns to negotiation.
- Attacking while bound is a legible lethal choice; the Guard warns the player before
  commitment, and the result follows the bound body state rather than a hidden script.
- Accepting a Guard-favorable bargain releases the player in a weaker but freely
  controllable state.
- The exact payment—Blood, time/day pressure, body condition, item, or another cost—is
  `OPEN` and requires an owner decision.

### Current Guard comparison — not an implementation default

`G1 WORKING HYPOTHESIS` is the current exact paper comparison. The Guard's own guarding
arm is failing before a duty inspection; it seeks a compatible Full Right Arm or
`20 Blood` for replacement/treatment. The captive comparison starts at `70 Blood` with
a complete Full body. Blood payment releases at `50 Blood` with the body intact. Arm
payment releases at `60 Blood` after the provisional `10 Blood` Clean-Stump result,
with Right Arm Missing and the stump Controlled for two wound ticks. Left-Arm Punch/
Block/Parry, Kick/Evade, and Headbutt remain.

Do not implement these numbers until the owner promotes the package. If promoted, the
release must retain at least `35 Blood`, two Ready attack families, one Block source,
one Parry source, one Evade source, and every mandatory traversal source.

### Interaction and combat contract — paper rule

- Exploration remains visible. Entering interaction pauses world time and opens one
  contextual panel; it does not teleport to a detached battle screen.
- Dialogue, combat routes, current body, hand/cards, items, and relevant state share
  the interaction surface. Dialogue is a delivery mechanism for choices and character,
  not a requirement for a deep general dialogue tree.
- Combat is primarily one-versus-one duel play.
- Active-demo combat has no distance/range state or reposition system.
- Default technique cards currently include `Punch`, `Kick`, and `Headbutt`.
- A card declares an exact source/body requirement, minimum source condition, target
  body region, cost, effect, and important consequence. The previously mentioned
  `2/6 arm` and `4/6 legs` values are examples, not approved thresholds.
- A player may play as many legal cards, including a combo, as the current `Mana`
  budget permits. A combo resolves within that turn. Mana's amount, refresh rule,
  carryover, relationship to Blood, and exact sequencing are `OPEN`. Mana capacity
  increases as rounds pass; starting Mana, increment, cap, and refill remain `OPEN`.
- Offensive cards resolve without an attack-side QTE. Short input occurs when
  defending an incoming attack: Yellow permits `Block` or `Parry`; Red requires
  `Evade`. Red cannot be Blocked or Parried. Color must be reinforced by a distinct
  icon/shape, animation, or audio cue.
- Block protects the declared target by making another player-chosen legal usable
  body part the final structural recipient. That guarding part loses Integrity and may
  lose dependent capability; it is not a free damage cancel.
- Successful Parry uses a deliberately difficult precision window, prevents all
  incoming Integrity/wound/Blood consequence, and reduces enemy `Will (İrade)`.
  A miss applies the original attack without an extra hidden penalty.
- Successful Evade prevents a Red attack's consequence and creates no range,
  distance, or reposition state.
- Card faces show only decision-critical facts; inspect/hover may reveal layered detail.

`DWF-0.1 WORKING HYPOTHESIS` provides one bounded comparison only: ordinary
Full/Strained Arms Block/Parry, Full/Strained Legs Evade; Block loss
`ceil(D * 0.75 * GuardFactor)` with factors `0.80/1.00/1.20`; a `900 ms` cue; Block
held by `250 ms` before contact; Parry `±90 ms`; Evade `±180 ms`; independent
`100/140/200%` timing scale, `100/75/50%` defense speed, and per-route automation.
Body, Blood, and Will may not shrink timing windows. The source research and reject
criteria are in `../research/defense_will_npc_balance_v0_1.md`.

### Surrender, limb transfer, and death — paper rule

- Parts are not extracted from corpses in the active demo.
- A desired limb can be received only from a living actor after a state-derived
  surrender/bargain grants access.
- A surrendered opponent accepts the agreed limb transfer because resuming the lost
  fight is understood to mean likely death. This is coerced survival bargaining, not
  freely offered consent; presentation must not disguise it.
- An opponent who has not surrendered still believes survival, victory, escape, or
  meaningful resistance is possible. Surrender cannot be a decorative HP threshold.
- The active-demo duel exposes visible `Will (İrade)`. Successful Parry reduces it;
  Broken Will triggers living surrender only while the opponent lives, the agreed
  limb remains transferable, and the player remains a credible threat. Will break
  does not itself damage or transfer the limb.
- Accepting surrender enters a visible Grafting Table transition and completes the
  agreed transfer. Exact animation, timing, attachment cost, and replacement rules
  remain `OPEN`.
- Killing the opponent resolves the immediate threat but permanently loses that limb
  reward for the current day. It instead grants a positive Blood reward sourced from
  the killed opponent. Accepting surrender grants no kill-Blood reward. Exact Blood
  yield, collection timing/presentation, wound/yield relationship, and cap remain
  `OPEN`.

`APPROVED DIRECTION`: consequential NPCs need an independent Goal, Need, Want, Red
Line, and world-facing behavior. They may pursue player Will and a disclosed claim;
they may not generate a demand by scanning the player's most valuable asset at the
moment of defeat. `DWF-0.1` tests bilateral `90 Will`, no passive encounter recovery,
and `24/30/36` Will loss when a Routine/Committed/Critical attack is successfully
Parried. Ordinary damage changes Will by zero. These values remain a working
hypothesis, and whether Broken player Will enforces the claim or permits one final
lethal Defy remains `OPEN`.

### Same-day death persistence — paper rule

On player death:

- the same aware protagonist returns to the start of the same day;
- the body returns to that day's original starting body;
- the world and NPCs reset and do not remember prior attempts;
- the protagonist/narrative knowledge remembers;
- default cards remain;
- technique cards learned during that attempt are lost;
- exactly one `Memory Card` is generated at death;
- a Memory Card whose source requirements are not met by the starting body remains
  Dormant/unusable until a compatible source exists; it is not rewritten into a legal
  card or compensated with another reward;
- run-derived Brain instability clears;
- already-earned persistent Brain buffs/bonuses remain and must provide a visible,
  inspectable advantage that makes later attempts easier without selecting cards or
  fabricating missing body capability.

The Memory Card's generation recipe, content limits, duplicates, storage/copy rules,
Brain buff catalogue, and exact power curve remain `OPEN`.

## 5. What counts as a playable mini-game

A menu, rendered room, dialogue mock-up, combat panel, card animation, or passing unit
test alone does not qualify. Before calling the new artifact a playable mini-game, a
fresh build must allow a player to complete the bounded chain with real input and
observable state:

1. make the Guard negotiation choice and reach both refusal and release outcomes;
2. move through the playable section;
3. enter/leave the contextual interaction without changing scenes;
4. play a legal card, reject an illegal source/card, choose a target region, pay the
   turn cost, observe Mana capacity increase across rounds, and observe the resulting
   capability/state change;
5. observe a redundant Yellow cue, protect the intended target by Block while the
   selected guarding part weakens, then successfully Parry with no incoming damage
   and visible enemy Will loss; observe a redundant Red cue that rejects Block/Parry
   and can be answered by Evade without creating reposition state;
6. reach Broken Will and observe a legal living surrender/limb bargain;
7. across repeatable attempts, reach one kill and observe Blood gain with no limb
   access, then reach one state-derived living surrender and complete the Grafting
   Table transfer with no kill-Blood gain;
8. reach death, reset the day/body/world, lose learned cards, retain defaults, create
   one Memory Card, reset instability, and retain a visible Brain buff if one exists;
9. continue playing after kill reward, graft, or reset;
10. reproduce the critical state transitions through logs/tests and a manual smoke run.

The duel must also demonstrate that no repeatable sequence can reproduce the same
complete meaningful combat state indefinitely without consuming or mutating a named
finite fact. Mana growth supplies that monotonic fact before its cap; at or beyond the
cap, every full round must consume or worsen Blood, integrity, wound severity, a
finite item/charge, or capability. A temporary status cycle is insufficient. The
exact anti-stall mechanic remains `OPEN`; this is an acceptance constraint, not
permission to invent a hidden timer.

If only part passes, report only that part as verified.

## 6. AI work order

For every task:

1. Read root `AGENTS.md`, package `AGENTS.md`, `docs/README.md`, the five living design
   documents, and this contract.
2. Inspect the repository and state what actually exists before proposing work.
3. Name one player-observable capability and its acceptance evidence.
4. List every `OPEN` choice it touches. Ask the owner only about identity-changing
   choices; use no invented default for them.
5. Confirm the implementation gate. Documentation/planning does not authorize an
   engine project or runtime.
6. Change the smallest coherent slice. Do not scaffold future systems merely because
   they may be useful later.
7. Test causal legality, mutation, lost/gained capability, and end/reset state.
8. Run a fresh verification and report exact commands and exit statuses.
9. Perform a hostile review for scope creep, hidden assumptions, false completion
   language, and confusion with legacy/research artifacts.

## 7. Required AI return format

```text
Outcome for this task
- VERIFIED / IMPLEMENTED — NOT VERIFIED / PAPER ONLY / BLOCKED

What existed before
- exact files/artifacts and evidence

What changed
- exact files and player-observable behavior

Verification
- command/build, exit status, observed result

Still absent or open
- missing behaviors, owner decisions, and untested claims

Scope audit
- legacy simulator changed? engine/runtime gate exceeded? unrelated systems added?

Hostile review
- likely false claim, hidden assumption, or weakest untested link

One recommended next gate
- exactly one bounded next step; do not begin it without approval
```

## 8. Current open owner decisions

- owner promotion, revision, or rejection of the exact `G1` Guard payment and released
  states;
- exact starting-body generation/reset rule;
- starting Mana, per-round increase, cap, refresh, carryover, relationship to Blood,
  and combo resolution order;
- kill-Blood yield, collection timing/presentation, wound/yield relationship, and cap;
- exact downstream Blood requirement that makes kill-versus-limb routing meaningful;
- exact anti-stall rule and any maximum-round fallback;
- exact body-condition scale and card thresholds;
- target-region effects and death rules beyond the decisions above;
- Yellow/Red cue duration and redundant presentation language;
- promotion/revision of the `DWF-0.1` Block/Parry/Evade sources and input bindings;
- promotion/revision of the `DWF-0.1` Block loss and wound/Blood boundary;
- promotion/revision of the `DWF-0.1` timing and accessibility grid;
- promotion/revision of bilateral `90 Will`, `24/30/36` Parry loss, recovery, named
  GoalCritical mutations, actor exceptions, and the player Broken-Will consequence;
- draw, hand, deck size, acquisition cadence, deck-edit points, and learned-card sources;
- Memory Card generation/content/storage rules;
- persistent Brain buff sources, limits, and visible tradeoffs;
- exact surrender evaluation inputs per opponent;
- exact Grafting Table cost/replacement procedure;
- mini-game end condition, target playtime, and replay objective;
- theme, tone details, character identities, art direction, and final presentation.
