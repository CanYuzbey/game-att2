# Game att2 - Demo Mini-Game AI Working Contract

Status date: 2026-08-25

Status: **BINDING OPERATIONAL CONTRACT FOR AI-ASSISTED DEMO WORK. NOT A DESIGN
AUTHORITY, RUNTIME APPROVAL, OR CLAIM THAT THE MINI-GAME EXISTS.**

## 1. Purpose

Direct one developer and their AI toward a small, genuinely playable sample demo. Its
eventual purpose is owner self-play and informal friend play, producing directional
evidence for whether to begin full-time development or pursue investors. The job is
not to describe the whole game as finished, build generic future systems, or turn
every idea in the documents into content. This sample cannot by itself establish
market demand, retention, broad-audience fun, or investor readiness.

The five living design documents remain the paper-design authority. This file controls
how work is scoped, evidenced, and reported.

## 2. Current existence baseline

As of 2026-08-25:

- the new Underground City mini-game has paper decisions but **no approved or verified
  product runtime**;
- the deterministic Python campaign is frozen legacy rules evidence;
- the H1 runner and visual lab are isolated research instruments;
- the former disposable browser movement demo is not retained in the active tree;
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
-> refuse and remain captive, attack and risk death, or accept one disclosed
   Guard-favorable concession
-> if accepted, buy freedom at a real cost and leave weaker but playable
-> traverse one small playable dungeon/city section
-> complete pre-boss limb fight A using body-sourced cards, target regions, defense,
   Will, surrender, and death
-> kill for Blood and lose limb access, or after living surrender perform the agreed
   limb bargain through a Grafting Table transition with no kill-Blood reward
-> optionally complete pre-boss limb fight B to expose the graft's exact benefit and
   drawback in ordinary combat; keep the Blood/no-graft route viable
-> face a gate boss that combines already-taught combat rules
-> defeat the gate boss and escape, or die
-> on death, return to the start of the same day under the persistence contract
```

`APPROVED DIRECTION`: the mini-game ends after the city-gate boss is defeated and the
player escapes. Approximately 30 minutes is a soft planning reference, not a duration
requirement, content cap, or acceptance criterion. Attempt, first-escape, and total
session duration are observations to report from playable builds.

The approved proof floor contains the Guard concession opening, one or two pre-boss
limb-mechanic fights, and the gate boss. The exact one-versus-two choice and distribution
of the graft tests remain `OPEN`, but D0 must select the initial fixture before runtime
approval; the choice is not deferred to a runtime playtest that does not yet exist.
Fight A must create the limb/Blood choice. A retained Fight B must uniquely show the
graft's gain and drawback in ordinary combat; it may not merely repeat Fight A. If
there is only one pre-boss fight, the boss also exposes the downstream graft delta and
the resulting evidence confound must be reported.

`WORKING HYPOTHESIS`: for a clean combat-appeal test, the gate boss introduces no new
fundamental combat rule. D0 must promote, revise, or reject that isolation rule before
it becomes runtime acceptance.

Without Fight B or an equivalent bounded non-boss rehearsal of the changed body, the
connected chain may verify rule fidelity, but gate-boss combat-appeal evidence must be
reported as tutorial-confounded. It may inform the go/no-go discussion, but cannot
independently support that judgment or be presented as a clean combat-fun result.

This floor is neither a hard encounter cap nor runtime approval. Additional
sample-scale content may be proposed inside D0 only with a named evidence or
presentation purpose; after D0 it requires a separately approved content gate,
normally supported by an observed evidence gap. A Merchant, generic Exit Keeper,
complete roguelite meta, and the full game are not implied.

### Opening contract — paper rule

- Refusing the Guard's offer leaves the player captive and returns to negotiation.
- Attacking while bound is a legible lethal choice; the Guard warns the player before
  commitment, and the result follows the bound body state rather than a hidden script.
- Accepting a Guard-favorable bargain releases the player in a weaker but freely
  controllable state.
- For this sample, the opening's "loss" is that disclosed unfavorable concession. It
  is not a full Guard duel, enforced player-Will-break claim, or approval of the
  still-`OPEN` claim-versus-`Defy` decision.
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
- The known starting concept vocabulary currently includes `Punch`, `Kick`, and
  `Headbutt`; their concrete expressions still require exact compatible sources.
- A card declares an exact source/body requirement, minimum source condition, target
  body region, cost, effect, and important consequence. The previously mentioned
  `2/6 arm` and `4/6 legs` values are examples, not approved thresholds.
- The ordinary round permits zero or one Preparation and zero or one Main. Attention
  capacity and the separate Readied Item Card do not grant extra ordinary plays.
- The player uses a read/calculate/hold/drop/commit rhythm. The card owns its source;
  the player selects a target body region only when the card requires it.
- The selected achievement-earned Concept Deck constructs the Anatomical Deck through
  compatible atomic exchanges. Persistent Brain Parts then shape declared labelled
  Attention access or one execution relationship through a visible paired buff/nerf.
- Offensive cards resolve without an attack-side QTE. Short input occurs when
  defending an incoming attack: Yellow permits `Block` or `Parry`; Red requires
  `Evade`. Red cannot be Blocked or Parried. Color must be reinforced by a distinct
  icon/shape, animation, or audio cue.
- Every card declares whether execution is interceptable. The defender's automatic
  reflex and/or compatible prior Preparation resolves during that action. Enemy
  interception of a player card remains automatic/state-derived, not a player attack
  QTE.
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
- the complete abstract card-concept vocabulary remains known;
- achievement-earned Concept Decks remain;
- boss/progression-earned Brain Parts remain;
- incompatible Concept Deck expressions remain Dormant and produce no replacement;
- run-derived temporary Brain/body instability clears;
- death creates no Memory Card or card reward.

Achievement conditions, boss rewards, equipped Concept Deck/Brain Part counts,
duplicate/storage rules, save boundary, and exact power curve remain `OPEN`.

## 5. What counts as a playable mini-game

A menu, rendered room, dialogue mock-up, combat panel, card animation, or passing unit
test alone does not qualify. Before calling the new artifact a playable mini-game, a
fresh build must allow a player to complete the bounded chain with real input and
observable state:

1. reach Guard refusal and release outcomes, observe the exact concession mutation,
   and continue from the D0-approved accepted concession branch in its declared
   weaker-but-playable state; if D0 approves multiple branches, each must pass; at
   least one accepted branch is required;
2. move through the playable section;
3. enter/leave the contextual interaction without changing scenes;
4. complete the selected one-or-two-fight pre-boss set, with every retained fight
   answering its named limb/graft evidence question;
5. construct one compatible Concept Deck exchange, reject a missing/Dormant sacrifice
   without partial gain, expose Brain-Part buff/nerf and Attention tendency, play a
   legal Preparation/Main card, reject an illegal source/card, choose a target region,
   and observe the resulting capability/state change;
6. observe a redundant Yellow cue, protect the intended target by Block while the
   selected guarding part weakens, then successfully Parry with no incoming damage
   and visible enemy Will loss; observe a redundant Red cue that rejects Block/Parry
   and can be answered by Evade without creating reposition state;
7. reach Broken Will and observe a legal living surrender/limb bargain;
8. across repeatable attempts, reach one kill and observe Blood gain with no limb
   access, then reach one state-derived living surrender and complete the Grafting
   Table transfer with no kill-Blood gain;
9. after D0 promotes an exact graft contract, carry the graft into a later fight and
   observe its legal capability gain, draw-independent change, and physical drawback;
   reproduce source-ruin reversal separately through a deterministic negative test;
10. after D0 promotes the boss isolation and route contract, across repeatable route
    smoke runs reach the gate boss, keep both the disclosed Blood/no-graft and living-
    limb/graft routes viable, defeat the boss, and complete the Underground City
    escape endpoint;
11. after D0 promotes one bounded Concept Deck/Brain Part fixture, earn each through
    its separate achievement/boss path, die, reset day/body/world and temporary
    instability, retain both persistent layers and known concepts, create no death
    card reward, and observe an incompatible expression remain Dormant;
12. continue playing after kill reward, graft, or reset;
13. reproduce the critical state transitions through logs/tests and a manual smoke run.

The duel must also demonstrate that no repeatable sequence can reproduce the same
complete meaningful combat state indefinitely without consuming or mutating a named
finite fact. Every full round must consume or worsen Blood, integrity, wound severity,
a finite item/charge, card lifecycle state, or capability. A temporary status cycle is insufficient. The
exact anti-stall mechanic remains `OPEN`; this is an acceptance constraint, not
permission to invent a hidden timer.

If only part passes, report only that part as verified.

### Evidence classes — do not collapse them

1. **Rule fidelity:** automated checks, state logs, and manual route smoke runs may
   verify legality, exact mutation, completion, and lack of softlocks. A single wrong
   critical mutation or mutually granted kill-and-limb reward is a blocker. This class
   cannot establish fun.
2. **Comprehension:** for each player not previously taught the solution, record
   whether they can identify what they sacrificed to the Guard, why a card is
   Ready/Dormant/Invalid, the kill-versus-surrender reward split, and at least one graft
   gain and drawback. Facilitator interventions and repeated misunderstandings must be
   logged rather than coached away; the protocol defines its pass/revise threshold
   before sessions begin.
3. **Combat appeal:** only human play after the limb/graft rules are understood can
   test the gate-boss hypothesis. Record whether the player can explain why a plan
   worked or failed, names a different next plan, voluntarily retries or explores the
   other route, and identifies the body/limb interaction as a distinctive source of
   interest. Completion rate alone is not a fun metric.

Owner self-play is internal design evidence. Informal friend sessions are a convenience
sample; record prior exposure and relationship as bias. They may support a bounded
go/no-go judgment for further development, but may not be reported as proof of general
fun, retention, market demand, or investor readiness. Exact participant count and
numeric thresholds remain `OPEN` until a playtest protocol is approved.

Before any human-play acceptance gate, the protocol must name a versioned build,
participant consent, prior exposure/relationship, raw observations, facilitator
instructions and deviations, observed duration, and the owner-approved pass/revise
interpretation. Do not run an unlabeled acceptance gate while its sample and thresholds
remain `OPEN`.

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
- exact Anatomical Deck size, Attention count/lifecycle/weights, redraw rule/cost,
  Preparation/Main costs, and Readied-Item readiness boundary;
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
- exact card labels, Concept Deck exchange/content/equipment rules, achievement
  conditions, and deck-edit points;
- exact Brain Part boss/progression sources, equipped count, access/execution limits,
  and visible paired tradeoffs;
- exact surrender evaluation inputs per opponent;
- exact Grafting Table cost/replacement procedure;
- exact one-versus-two pre-boss fight choice, actor roles, and distribution of the
  limb/graft evidence questions;
- exact gate-boss identity/defeat contract, two viable reward routes, and bounded
  human-play question for integrated combat appeal;
- observed clean-attempt, first-escape, and total-session pacing; exact external
  playtest sample and interpretation thresholds;
- theme, tone details, character identities, art direction, and final presentation.
