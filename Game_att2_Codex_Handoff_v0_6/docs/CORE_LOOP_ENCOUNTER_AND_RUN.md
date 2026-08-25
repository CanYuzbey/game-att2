# Game att2 - Core Loop, Encounter, and Run

Status date: 2026-08-25

Status: **CURRENT LIVING GAME-DESIGN AUTHORITY. THE UNDERGROUND-CITY MINI-GAME HAS A
BOUNDED SAME-DAY LOOP AND AN ESCAPE/GATE-BOSS END DIRECTION; DETAILED PACING AND THE
FULL-GAME RUN REMAIN OPEN. NO RUNTIME APPROVAL.**

## What is currently solid

The smallest coherent active-play loop is:

```text
read the concrete pressure and visible hostile intent
-> inspect current body, hand, turn budget, wounds/Blood, and available sources
-> choose an action/card, exact source, target, and disclosed risk
-> lock the commitment
-> resolve outgoing cards without an attack QTE
-> answer incoming Yellow attacks with Block/Parry or Red attacks with Evade
-> apply integrity, wound, Blood, inventory, and capability consequences
-> recompute the next legal decision state
```

The player must be able to see the incoming action family, its physical/tool source,
its target or target category, and the expected consequence if unaltered. Exact UI,
certainty bands, numbers, camera, and animation remain open.

## Active-demo turn contract

For the current one-versus-one strategic model:

```text
start-of-round scheduled effects and forced checks
-> Decision Refresh for Spent/Invalid Attention positions
-> show readable hostile intent, current Attention, and Readied Item Card
-> optionally hold/drop one legal Preparation and exact target
-> hold/drop one legal Main and exact target
-> preview sources, costs, Concept Deck/Brain effects, interception, and consequences
-> lock and revalidate the Preparation, then the Main
-> resolve each started atomic action and recompute later legality
-> during an interceptable action, resolve the defender's automatic reflex and any
   compatible previously played Preparation
-> for an incoming Yellow attack choose Block or attempt Parry; for Red attempt Evade
-> resolve the defense result, final recipient, and body consequences
-> reduce opponent Will on a successful Parry and test for living surrender
-> expiry and next-round refresh
```

Cards declare whether their execution is interceptable. The defender's automatic
reflex and/or previously played compatible Preparation resolves inside that action
and is not another voluntary play. A player attack has no attack-side player QTE; an
enemy interruption is state-derived or previously prepared. For an incoming player-
defence event, Yellow permits Block or Parry and Red requires Evade. Block redirects
the attack from its declared target into a chosen legal guarding part and weakens that
part. Successful Parry prevents the incoming damage and reduces enemy Will;
successful Evade prevents a Red consequence without creating reposition or range
state. Exact inputs, timing windows, source requirements, Block loss, Will values,
and assistance remain `OPEN`.

A started atomic action completes; later source damage changes future capability
rather than retroactively erasing the action. The ordinary budget is zero or one
Preparation and zero or one Main per actor per round. Attention capacity and a Readied
Item never add an ordinary play. The Aug-22 growing-Mana/multi-card sequence is
superseded for the active paper design.

`WORKING HYPOTHESIS`: causal state loss prevents stalling without a growing Mana
clock. A complete round must not reproduce the same meaningful combat state through a
free defence/heal/redraw cycle. Repeated play must consume or worsen a named finite
fact such as Blood, integrity, wound severity, a finite item/charge, a card lifecycle
state, or capability. A temporary status that later expires is insufficient by
itself. Exact recovery limits and any maximum-round fallback remain `OPEN`.

## Encounter meaning

Combat is core interaction, but combat is not automatically the purpose of every
encounter. Keep these layers separate:

| Layer | Question |
|---|---|
| Motivation | Why does this actor enter or continue conflict? |
| Objective | What state are they trying to create? |
| Route | Which reachable state can satisfy that objective? |
| Resolution | Why did active conflict stop? |
| Outcome | How successful was each actor? |

Actions mutate ordinary state. They do not directly select a designer-authored
ending. Death, capability break, objective completion, surrender, bargain, mercy,
escape, mutual success, partial success, or unresolved continuation must follow from
state, motivation, and remaining legal affordances.

For the active-demo duel, `Will (İrade)` is the visible combat-surrender state.
Successful Parry reduces it. Reaching Broken Will triggers the living surrender/limb
bargain only while the opponent lives, the limb remains transferable, and the player
remains a credible threat. Exact values, recovery, other mutation sources, and actor
exceptions remain `OPEN`.

### Goal-driven actors and reciprocal claims

`APPROVED DIRECTION`: consequential NPCs are actors with a purpose, not idle body-part
containers. Their reason to seek Blood, protect/refuse a limb, negotiate, fight,
surrender, or exploit a player defeat must exist before the player selects a route.
An NPC may aim to break player Will and obtain a disclosed useful asset when that
result advances its own goal.

`WORKING HYPOTHESIS`: each bounded actor declares one `Goal`, `Need`, `Want`,
`RedLine`, `Leverage`, primary `Claim`, optional counterclaim, `Concession`, and
`Fallback`. Legal demands come only from that authored claim list and are ordered by
Need closure, Goal progress, Want fit, survival benefit, lower Concession cost, then an
authored tie-break. The system never scans the player's body or wallet for the most
valuable punishment.

Faction doctrine supplies shared long-horizon priorities and relationships; current
role/duty supplies immediate obligations; the individual actor card supplies the
actual Goal, Need, RedLine, and Claim. Combat strength and risk tolerance are separate
from all three. An actor may validly trade, flee, ignore the player, or carry
`NoClaim` when confrontation would not advance its purpose.

Broken Will opens the same legal-claim check for player and NPC. It does not erase
personality or transfer property automatically. A living-result claim must have been
disclosed before commitment, remain useful and transferable, be supported by real
leverage, and leave the released player with the minimum required attack and defense
routes. Exact player `Defy` versus enforced-claim behavior remains an owner decision.
The complete research contract is in
`../research/defense_will_npc_balance_v0_1.md`.

Jeff's reciprocal-repair behavior is an implemented survey prototype, not final
canon or a universal encounter template.

## Between-pressure loop

The current supported fantasy is:

```text
survive or resolve a pressure
-> assess wounds, Blood, body loss, and available parts
-> kill for Blood or accept a living surrender bargain for the agreed part
-> treat, restore Blood, repair, graft, integrate, sell, preserve, or refuse
-> carry the changed body into the next pressure
```

Treatment, Blood restoration, structural repair, extraction, grafting, and
integration are separate effects. An option performs only what it declares. Corpse
limb extraction is excluded from the active demo. Killing the opponent instead grants
a positive Blood reward sourced from that opponent; surrender grants no kill-Blood
reward. Exact yield and collection presentation remain `OPEN`.

## Underground City demo container

`APPROVED DIRECTION`: the next product target is a short playable sample demo proving
one complete same-day loop. It is not an expansion of the Python mini-campaign. Its
proof floor is the Guard concession opening, one or two pre-boss limb-mechanic fights,
and the gate boss; that floor is neither a summary of the full game nor a fixed
encounter ceiling.

`WORKING HYPOTHESIS`: the player is a captive in an Underground City/dungeon economy
that treats living bodies as stock. The old fixed Missing Right Arm/Damaged Torso start
is not the active-demo default. `G1` now supplies one exact comparison rather than a
canon answer: the player begins with `70 Blood` and Full Head `25`, Torso `45`, both
Arms `30`, Legs `35`, and Core `35`. Random generation and the final starting body
remain `OPEN` until the owner promotes, revises, or rejects that comparison.

This container gives the demo a provisional run:

```text
captive and bound
-> Guard negotiation: refuse and remain captive, attack and likely die, or trade
-> if accepted, pay one disclosed Guard-favorable concession and become weaker but free
-> traverse one small Underground City/dungeon section
-> face pre-boss limb fight A
-> use card sources, body targets, defense, and Will to kill or force surrender
-> kill for Blood and lose limb access, or accept a living limb bargain through the
   Grafting Table transition
-> optionally face pre-boss limb fight B to expose the graft's gain and drawback in
   ordinary combat; the Blood/no-graft route remains viable
-> face the gate boss using the already-taught integrated combat language
-> defeat the gate boss and escape, or die and return to the same day's beginning
```

`APPROVED DIRECTION`: defeating the boss at the Underground City gate and escaping is
the mini-game success endpoint. Approximately 30 minutes is a soft planning reference,
not a duration requirement, content cap, or acceptance criterion. Clean-attempt,
first-escape, and total-session durations are evidence to record from real play.

`WORKING HYPOTHESIS`: the Grafting Table consequence must occur before the gate boss
and must change at least one inspectable legal option in a later pre-boss fight or in
the gate-boss confrontation. A limb received only after the final boss cannot prove
the requested graft-result loop. The exact choice of one versus two pre-boss fights,
their actors, the limb, the boss, and the changed option remain `OPEN`; this ordering
is not approval for extra runtime content. With only one pre-boss fight, the boss must
also expose the graft consequence, which contaminates its separate combat-fun test and
must be reported as such rather than hidden.

### G1 Guard comparison — working hypothesis

The Guard is not a generic collector. Its own guarding arm is visibly failing before
an imminent duty inspection. It needs a compatible Full `CanGuard` Right Arm, or
exactly `20 Blood` to fund replacement/treatment, so that it remains fit for duty.
It refuses Strained, Desperate, incompatible, or vital substitutes. Its leverage is
the bound player and controlled exit; its Concession is controlled removal if needed,
stump control, release, an opened exit, and no same-day pursuit.

Two test branches leave the player weaker but playable:

| Payment | Exact released state |
|---|---|
| `20 Blood` | `50 Blood`; complete Full body and every starting route retained. |
| Full Right Arm | `60 Blood` after the provisional `10 Blood` Clean-Stump consequence; Right Arm Missing; stump Controlled for two wound ticks; Left-Arm Punch/Block/Parry, Kick/Evade, and Headbutt retained. |

Every nonlethal release must retain at least `35 Blood`, two Ready attack families,
one legal Block source, one Parry source, one Evade source, and all mandatory traversal
sources. The Guard releases because payment closes its Need and continued custody adds
cost without Goal progress. Refusal leaves captivity; hostile resistance makes the
same disclosed claim its Will objective rather than authorizing a new inventory scan.
This is `G1 WORKING HYPOTHESIS`, not final content or runtime behavior.

For this sample, "losing at the Guard" means accepting one disclosed unfavorable
concession while bound so the player can leave captivity weaker but playable. It does
not promote a full Guard combat, a player-Will-break claim outcome, or the still-open
claim-versus-`Defy` rule.

The success endpoint is decided at direction level; duration is observed rather than
accepted against a fixed target. The failure contract is decided: death resets the
body and unaware world to the same day's start;
the protagonist remembers; earned Concept Decks and Brain Parts remain; the known
concept vocabulary remains; body/world state and temporary instability reset.

### Minimum interaction responsibilities

| Interaction | Actor motivation | What the mini-game must prove | Non-goal |
|---|---|---|---|
| Bound Guard opening | `G1` candidate: preserve duty by replacing/treating its failing guarding arm | Refusal loops to captivity; warned bound attack can kill; the player can identify the disclosed loss accepted to buy freedom; the D0-approved concession releases its declared weaker-but-playable body; if D0 approves multiple branches, each has a later consequence | A fake choice, a disguised Guard duel, a universal limb price, or inventory-scanning punishment |
| Pre-boss limb fight A | `OPEN`, but must explain why it still expects to survive or win and why the desired limb matters to it | In-world body-sourced combat, source/target consequences, state-derived surrender/death, and the kill-for-Blood versus surrender-for-limb choice produce the graft decision | A detached battle scene, corpse-limb loot, or acquisition without a causal body decision |
| Optional pre-boss limb fight B | `OPEN`; include only if it owns the distinct post-graft proof | In ordinary combat, the graft changes one legal capability and one drawback before the boss; the no-graft/Blood route also remains viable | Repeating Fight A, adding content for length, or making the graft a pure stat upgrade |
| Gate boss | `OPEN`, but must guard the city exit for a goal/duty that exists without the player | `WORKING HYPOTHESIS`: without teaching a new fundamental combat rule, it combines a predeclared multi-layer subset of the already-taught card/body/defense/resource pressures; omitted systems are recorded; defeat opens escape; human observation tests whether the understood loop is engaging and worth another plan | A bespoke graft lock, a tutorial checklist, or a boss disconnected from body/Brain decisions |
| Death/reset | World has no loop awareness | Same day/world/body reset plus asymmetric card/Brain/memory persistence | A generic roguelite results screen with unexplained reset |

The pre-boss actors' and gate boss's motivations remain identity-level content
decisions. Until chosen, none may be filled by a generic desire to kill or a scripted
final twist.

## Demo presentation hypothesis

`APPROVED DIRECTION`: exploration and confrontation share the visible world. Entering
an interaction pauses world time and opens the hand/body/item/dialogue interface over
the scene rather than teleporting to a separate combat screen. Cards select intent,
source, target region, cost, and disclosed risk. Short physical input belongs to
defending incoming attacks: Yellow announces Block/Parry and Red announces Evade.
Exact camera and layout remain `OPEN`.

The active demo has no combat range state, range profile, neutral settling, or
reposition action. Traversal outside interaction remains ordinary world movement.

## Same-day run contract

`PAPER RULE`: the player character knows the day is repeating; the world and NPCs do
not. Death returns the body to that day's original starting configuration and returns
world state to the day's beginning.

The same day restores the same underlying Blood and limb opportunities unless the
player's new choices causally change access. The game does not inspect the player's
current Blood and secretly remove or spawn a desired limb. A failed attempt may end
with Blood but no desired-limb access, or desired-limb access without enough Blood for
the intended downstream use; remembered route knowledge should let the next attempt
sequence the same opportunities better.

Persistence is asymmetric:

- protagonist/narrative knowledge persists;
- the complete abstract card-concept vocabulary remains known;
- earned achievement-based Concept Decks persist;
- earned boss/progression Brain Parts persist;
- a retained Concept Deck expression remains Dormant if the reset body cannot source
  it and produces no replacement reward;
- run-derived temporary Brain/body instability resets;
- current flesh, grafts, wounds, encounter state, and unaware-world state reset under
  the same-day contract.

Death creates no Memory Card. Exact achievement conditions, Brain-Part rewards,
equipped persistent loadouts, starting-body rule, save boundary, and full-game reset
scope remain `OPEN`.

## Full-game run structure: OPEN

The demo now has the same-day reset contract above. The full game still does **not**
have an approved complete definition of a run. The current Python mini-campaign does
not decide it.

Still open:

- what starts and ends a run;
- how encounters, hazards, rooms, or authored scenes connect;
- whether the world is a map, sequence, hub, branching path, or another structure;
- checkpoint behavior beyond the same-day death reset;
- how the approved demo persistence contract expands across the full game;
- what failure short of death means;
- what the player is ultimately trying to accomplish in a run and in the full game;
- how a 10-12 hour complete arc differs from replay or post-completion structure.

No detailed Brain value, card count, encounter roster, UI, or level-layout decision
should masquerade as an answer to this missing structure.

## Current design focus

The current gate is to close the remaining `OPEN` choices needed for the smallest
Guard-concession, one-or-two-fight limb/graft proof, integrated gate-boss escape, and
same-day reset contract. The bounded Concept Deck/Brain diagnostic must use the
approved scaling guardrails; full card/Brain content, a broad dialogue system, content
that does not answer one of those proof questions, final content, and polish must not
be built first.
