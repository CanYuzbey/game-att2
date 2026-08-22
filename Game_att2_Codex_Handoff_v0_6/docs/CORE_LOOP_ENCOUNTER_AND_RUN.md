# Game att2 - Core Loop, Encounter, and Run

Status date: 2026-08-22

Status: **CURRENT LIVING GAME-DESIGN AUTHORITY. THE UNDERGROUND-CITY MINI-GAME HAS A
BOUNDED SAME-DAY LOOP; ITS ENDING AND THE FULL-GAME RUN REMAIN OPEN. NO RUNTIME
APPROVAL.**

## What is currently solid

The smallest coherent active-play loop is:

```text
read the concrete pressure and visible hostile intent
-> inspect current body, hand, turn budget, wounds/Blood, and available sources
-> choose an action/card, exact source, target, and disclosed risk
-> lock the commitment
-> perform a short physical/reflex application when the action calls for it
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
-> decision refresh
-> show readable hostile intent and current turn budget
-> player selects an ordered sequence of legal cards and exact targets
-> preview total cost, source requirements, combo relationship, and consequences
-> commit one card at a time or the disclosed sequence
-> revalidate and resolve in declared order
-> after each resolved card, mutate state and recompute later-card legality
-> cancel a now-illegal later card without fabricating a substitute
-> resolve the opponent's legal response under the same causal rules
-> expiry and next-turn refresh
```

Automatic reflex-defense events occur inside incoming-action resolution. They are not
extra voluntary plays. A started atomic action completes; later source damage changes
future capability rather than retroactively erasing the action. The player may use as
many cards as the budget permits, and a combo completes within the same turn. The
resource name, budget, refresh, whether a sequence locks all at once, and exact enemy
cadence are `OPEN`.

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

Jeff's reciprocal-repair behavior is an implemented survey prototype, not final
canon or a universal encounter template.

## Between-pressure loop

The current supported fantasy is:

```text
survive or resolve a pressure
-> assess wounds, Blood, body loss, and available parts
-> receive a part only through a living surrender bargain that grants legal access
-> treat, restore Blood, repair, graft, integrate, sell, preserve, or refuse
-> carry the changed body into the next pressure
```

Treatment, Blood restoration, structural repair, extraction, grafting, and
integration are separate effects. An option performs only what it declares. Corpse
extraction is excluded from the active demo.

## Underground City demo container

`APPROVED DIRECTION`: the next product target is a short playable mini-game proving
one complete same-day loop. It is not an expansion of the Python mini-campaign and is
not required to summarize the whole game through three encounters.

`WORKING HYPOTHESIS`: the player is a captive in an Underground City/dungeon economy
that treats living bodies as stock. The exact original starting body and whether it
is selected randomly remain `OPEN`; the old fixed Missing Right Arm/Damaged Torso
start is not the active-demo default.

This container gives the demo a provisional run:

```text
captive and bound
-> Guard negotiation: refuse and remain captive, attack and likely die, or trade
-> accept a Guard-favorable payment and become weaker but free
-> traverse one small Underground City/dungeon section
-> meet one actor who blocks escape/progress
-> use dialogue, card combat, targeting, and body state to bargain or force surrender
-> accept a living limb bargain through the Grafting Table transition
-> continue with the changed body, or die and return to the same day's beginning
```

The exact mini-game victory endpoint and target duration remain `OPEN`. The failure
contract is decided: death resets the body and unaware world to the same day's start;
the protagonist remembers; default cards remain; attempt-learned cards are lost; one
Memory Card is created; run instability clears; persistent Brain buffs remain.

### Minimum interaction responsibilities

| Interaction | Actor motivation | What the mini-game must prove | Non-goal |
|---|---|---|---|
| Bound Guard opening | Benefits from captivity and demands an advantageous price | Refusal loops to captivity; warned bound attack can kill; a costly bargain releases the player | A fake choice where every option releases the player |
| Escape/progress blocker | `OPEN`, but must explain why it still expects to survive or win | In-world interaction, body-sourced multi-card turn, target regions, state-derived surrender/death, living bargain, and graft consequence | A detached battle scene or corpse loot |
| Death/reset | World has no loop awareness | Same day/world/body reset plus asymmetric card/Brain/memory persistence | A generic roguelite results screen with unexplained reset |

The blocking actor's motivation and the mini-game's success endpoint are identity-level
content decisions. Until chosen, neither may be filled by a generic desire to kill or
a scripted final twist.

## Demo presentation hypothesis

`APPROVED DIRECTION`: exploration and confrontation share the visible world. Entering
an interaction pauses world time and opens the hand/body/item/dialogue interface over
the scene rather than teleporting to a separate combat screen. Cards select intent,
source, target region, cost, and disclosed risk; bounded physical execution resolves
against that same interaction. Exact camera and layout remain `OPEN`.

The active demo has no combat range state, range profile, neutral settling, or
reposition action. Traversal outside interaction remains ordinary world movement.

## Same-day run contract

`PAPER RULE`: the player character knows the day is repeating; the world and NPCs do
not. Death returns the body to that day's original starting configuration and returns
world state to the day's beginning.

Persistence is asymmetric:

- protagonist/narrative knowledge persists;
- default cards persist;
- cards learned during the failed attempt do not persist;
- death generates exactly one Memory Card;
- a Memory Card remains Dormant if the reset body cannot source it;
- run-derived Brain instability resets;
- already-earned persistent Brain buffs/bonuses remain and make later attempts easier
  through a visible legal advantage.

Memory Card generation/content, Brain buff catalogue, starting-body rule, storage,
save boundary, and exact numerical advantage remain `OPEN`.

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
Guard-opening plus one-duel same-day mini-game contract. Full Brain content, a broad
dialogue system, additional encounters, final content, and polish must not be built
first.
