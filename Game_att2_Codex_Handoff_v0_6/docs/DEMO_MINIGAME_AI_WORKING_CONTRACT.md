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
-> after a living surrender, perform the limb bargain through a Grafting Table transition
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
- A player may play as many legal cards, including a combo, as the current turn budget
  permits. A combo resolves within that turn. The resource name, amount, refresh rule,
  and exact sequencing are `OPEN`.
- Card faces show only decision-critical facts; inspect/hover may reveal layered detail.

### Surrender, limb transfer, and death — paper rule

- Parts are not extracted from corpses in the active demo.
- A desired limb can be received only from a living actor after a state-derived
  surrender/bargain grants access.
- A surrendered opponent accepts the agreed limb transfer because resuming the lost
  fight is understood to mean likely death. This is coerced survival bargaining, not
  freely offered consent; presentation must not disguise it.
- An opponent who has not surrendered still believes survival, victory, escape, or
  meaningful resistance is possible. Surrender cannot be a decorative HP threshold.
- Accepting surrender enters a visible Grafting Table transition and completes the
  agreed transfer. Exact animation, timing, attachment cost, and replacement rules
  remain `OPEN`.
- Killing the opponent resolves the immediate threat but permanently loses that limb
  reward for the current day.

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
   turn cost, and observe the resulting capability/state change;
5. reach at least one state-derived living surrender and complete the Grafting Table
   transfer;
6. reach death, reset the day/body/world, lose learned cards, retain defaults, create
   one Memory Card, reset instability, and retain a visible Brain buff if one exists;
7. continue playing after either graft or reset;
8. reproduce the critical state transitions through logs/tests and a manual smoke run.

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

- exact Guard payment and released weaker state;
- exact starting-body generation/reset rule;
- turn resource name, budget, refresh, and combo resolution order;
- exact body-condition scale and card thresholds;
- target-region effects, defense timing, and death rules beyond the decisions above;
- draw, hand, deck size, acquisition cadence, deck-edit points, and learned-card sources;
- Memory Card generation/content/storage rules;
- persistent Brain buff sources, limits, and visible tradeoffs;
- exact surrender evaluation inputs per opponent;
- exact Grafting Table cost/replacement procedure;
- mini-game end condition, target playtime, and replay objective;
- theme, tone details, character identities, art direction, and final presentation.
