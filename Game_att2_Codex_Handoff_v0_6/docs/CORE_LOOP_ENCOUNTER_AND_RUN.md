# Game att2 - Core Loop, Encounter, and Run

Status date: 2026-08-21

Status: **CURRENT LIVING GAME-DESIGN AUTHORITY. THE COMBAT DECISION LOOP IS A PAPER
DIRECTION; ENCOUNTER AND RUN STRUCTURE REMAIN OPEN. NO RUNTIME APPROVAL.**

## What is currently solid

The smallest coherent active-play loop is:

```text
read the concrete pressure and visible hostile intent
-> inspect current body, hand, Blood, wounds, range, and available sources
-> choose an action/card, exact source, target, and disclosed risk
-> lock the commitment
-> perform a short physical/reflex application when the action calls for it
-> apply integrity, wound, Blood, range, inventory, and capability consequences
-> recompute the next legal decision state
```

The player must be able to see the incoming action family, its physical/tool source,
its target or target category, and the expected consequence if unaltered. Exact UI,
certainty bands, numbers, camera, and animation remain open.

## Paper round contract

For the current one-versus-one strategic model:

```text
start-of-round scheduled effects and forced checks
-> decision refresh
-> show deterministic public Lead
-> Lead takes zero/one Preparation and locks zero/one Main
-> show permitted Lead intent
-> Reply takes zero/one Preparation and locks zero/one Main
-> activate explicit on-lock states and reservations
-> revalidate and resolve Lead
-> settle all consequences and recompute state
-> revalidate the Reply's unchanged commitment
-> resolve it if still legal; otherwise cancel without substitution
-> expiry and neutral range settling
```

Automatic reflex-defense events occur inside incoming-action resolution. They are not
extra voluntary plays. A started atomic action completes; later source damage changes
future capability rather than retroactively erasing the action.

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
-> claim/extract/salvage only where state grants legal access
-> treat, restore Blood, repair, graft, integrate, sell, preserve, or refuse
-> carry the changed body into the next pressure
```

Treatment, Blood restoration, structural repair, extraction, grafting, and
integration are separate effects. An option performs only what it declares.

## Run structure: OPEN

The project does **not** yet have an approved definition of a run. The current Python
mini-campaign and the phrase "hell loop" do not decide the production structure.

Still open:

- what starts and ends a run;
- how encounters, hazards, rooms, or authored scenes connect;
- whether the world is a map, sequence, hub, branching path, or another structure;
- checkpoint and restart behavior;
- what body, cards, techniques, Brain progression, and narrative knowledge survive
  death;
- what failure short of death means;
- what the player is ultimately trying to accomplish in a run and in the full game;
- how a 10-12 hour complete arc differs from replay or post-completion structure.

No detailed Brain value, card count, encounter roster, UI, or level-layout decision
should masquerade as an answer to this missing structure.

## Current design focus

The foundational focus is to make encounter and run structure coherent with the
active-play loop. Brain implementation detail, mental defeat, negotiation depth,
content expansion, story production, final UI, engine selection, and a vertical slice
remain downstream until this macro structure can be stated plainly.
