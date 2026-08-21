# Game att2 — Director's Choice Core-Gameplay Working Record

Status date: 2026-08-21

Status: **OWNER-DIRECTED WORKING DESIGN RECORD. READ FOR NEW CORE-GAMEPLAY
CONVERSATIONS. NOT RUNTIME, CONTENT, FINAL-UI, ENGINE, OR PRODUCTION APPROVAL.**

## 1. Purpose and authority boundary

This document preserves the owner's current creative direction from the 2026-08-19
game-director conversation so later collaborators and AI agents do not restart the
same foundational questions or promote examples into rules.

Use the following labels literally:

| Label | Meaning |
|---|---|
| `OWNER DIRECTION` | The owner affirmed the conceptual direction. Details may still change unless a higher-authority document locks them. |
| `OWNER-DELEGATED RESOLUTION` | On 2026-08-21 the owner authorized logical reconciliation of already-discussed collisions; paper-only and subordinate to explicit owner statements. |
| `WORKING HYPOTHESIS` | Coherent enough to prototype or question next, but not proven fun and not approved for runtime. |
| `EXAMPLE ONLY` | Illustrative material; never infer canon, content, or a mechanic from it. |
| `DEFERRED` | Intentionally unresolved because a more foundational decision must come first. |

This record does not supersede `02_DEVELOPMENT_MASTER_v0_6.md`, dated owner
amendments, `03_COMBAT_RULES_v0_5.md`, or the owner-approved paper contracts in
documents 27 through 39. Document 39 is now the current Brain/Attention authority;
document 29 retains only the staged-turn, exact-source, and lifecycle rules that
document 39 preserves. A separate collectible-technique deck, active-deck editor,
draw/discard piles, and technique persistence remain working exploration rather than
approved Brain Module requirements.

If this document conflicts with a later explicit owner statement, record the newer
statement as a dated amendment instead of silently reconciling it. No item below
opens Unity, runtime card-system, Encounter 3, content-production, final-UI, or
external-playtest gates.

## 2. Product and intended memory

### DC-P01 — Bounded weekend game

Status: `OWNER DIRECTION`; commercial details remain hypotheses.

- The intended product is a contained game that a player can finish in roughly one
  weekend, provisionally around 10–12 hours.
- The working price thought is USD 8–12. This is not market evidence, pricing
  approval, or a store commitment.
- The desired outcome is not necessarily “the best game the player has ever played.”
  It should entertain throughout its bounded length and leave a distinctive, pleasant,
  slightly strange aftertaste.

### DC-P02 — Signature player memory

Status: `OWNER DIRECTION`.

Preserve the owner's formulation:

> “Kendimi yeniden inşa ettiğim bir oyundu.”

English working gloss:

> “It was a game in which I rebuilt myself.”

This memory is stronger than “I collected unusual limbs” or “I built a deck.” Body
construction must change what the player can actually do and risk.

## 3. Creative thesis hierarchy

### DC-T01 — Use is the core; construction supports it

Status: `OWNER DIRECTION`.

Building the body is supporting content. The primary playable pleasure must come from
**using the constructed body** to solve pressure. A strong body-building fantasy
without a satisfying use grammar is insufficient.

### DC-T02 — Three-thesis hierarchy

Status: `OWNER DIRECTION`.

1. **Core-play thesis:** the build is a body that can act, be committed, wounded, and
   lose capability. “Build'in taşıdığın şey değil; yaralanabilen bedenindir.”
2. **Controlled-depth thesis:** body parts influence one another and current choices,
   but the system must avoid uncontrolled combinatorial overload.
3. **Emotional-result thesis:** strengthening the body gradually asks what part of the
   former self has been surrendered.

The owner explicitly endorsed this ordering: the first thesis owns core play, the
second adds bounded depth, and the third supplies emotional consequence.

### DC-T03 — Strategy/execution balance

Status: `OWNER DIRECTION` at the experiential level; exact values and interaction
families remain open.

Use approximately **70% problem solving and selection / 30% physical application** as
a design compass, not a numeric balance promise. Strategy should decide what and why;
physical execution should make the committed body feel used without erasing a bad
strategic decision.

### DC-T04 — Transhumanist control tension

Status: `OWNER DIRECTION`; exact meters, failure states, and progression rules are
`DEFERRED`.

Transhumanism should be experienced as more than a visual theme. New body parts may
increase power while making the body less balanced, less compatible, or harder to
control. A recurring player concern should be how much transformation can be accepted
without losing functional control of the assembled self. Do not infer a specific
sanity, corruption, instability, or control meter from this direction.

### DC-T05 — Puzzle-action pressure

Status: `OWNER DIRECTION` at the experiential level; encounter grammar is `DEFERRED`.

The player should face concrete problems with multiple body-dependent approaches and
look for the best available solution under current constraints. Problem solving and
choice should lead; physical application should confirm the chosen solution. Breaking
a barrier with an animal-derived arm, crossing height with an imperfect winged body,
or surviving an oxygen hazard through plant/robotic anatomy were `EXAMPLE ONLY`, not
approved content or universal solution classes.

## 4. Combat-form working direction

### DC-C01 — Phase-based hybrid control model

Status: `OWNER DIRECTION`, consistent with document 19; exact cadence remains governed
by the approved paper contracts.

The current high-level combat hypothesis is:

```text
read the state and visible intent
-> choose an action/card, physical source, target, and disclosed risk
-> lock the commitment
-> perform a short bounded physical/reflex application when the action calls for it
-> apply body, wound, Blood, position, and capability consequences
-> rebuild the next legal decision state
```

This chooses the time/control relationship only. It does not decide camera, world
structure, map structure, level design, or final UI.

### DC-C02 — Minimum readable hostile intent

Status: `OWNER DIRECTION`.

The player must be able to see:

- the incoming action type;
- the body part or tool sourcing it;
- its declared target or target category; and
- the consequence that is expected if it is not prevented or altered.

Exact visual grammar, iconography, animation, numbers, certainty bands, and Focus
presentation are `DEFERRED`. Earlier layered-UI examples were presentation hypotheses,
not owner decisions.

### DC-C03 — Contextual execution layer

Status: `WORKING HYPOTHESIS`.

The strongest current presentation candidate is a short real-time application layer
that appears over or within the tactical scene rather than a wholly disconnected
combat screen. It may temporarily dim, crop, zoom, or bound the scene. The chosen
card, physical source, target, and current state must remain causally continuous.

Do not infer an *Undertale* bullet-hell clone, a universal minigame, an isometric
camera, or a final interface. The transferable idea is a bounded application space,
not a copied control scheme. Only contested or meaningfully risky physical actions
need such a window; this frequency remains testable.

## 5. Deckbuilder role

### DC-D01 — Anatomical deckbuilder

Status: `WORKING HYPOTHESIS`, explicitly judged by the owner as solid enough to try;
fun and detailed rules remain unproven.

The current candidate identity is:

> **A card declares what the player is trying to do; the body determines how and at
> what physical cost it can be done.**

Operational boundary:

- voluntary primary combat commitments normally use cards;
- the current body, equipment, wounds, range, and commitments generate eligibility
  and execution profiles;
- cards should usually represent physical techniques or preparations, not detached
  `+N%` buff filler;
- trade-offs, buffs, and debuffs should normally be embedded in a physical action and
  its source commitment;
- automatic reflex opportunities, body passives, wound consequences, Blood changes,
  death-prevention checks, and other forced state reactions remain outside the hand;
- a compatible body and a suitable card must both matter, so neither layer becomes
  decorative.

The shorthand identity is:

> “Desteni toplamıyorsun; bedenini değiştirerek desteni ameliyat ediyorsun.”

English working gloss:

> “You do not merely collect a deck; you operate on it by changing your body.”

This is not approval of individual cards, hand size, total deck size, draw/discard,
energy, card rarity, deck rewards, or a runtime card system.

## 6. Card acquisition, deck construction, and persistence

### DC-D02 — Keep four responsibilities separate

Status: `OWNER DIRECTION` for the separation; implementations are `WORKING
HYPOTHESES`.

Future design must not collapse these into one automatic rule:

| Responsibility | Question |
|---|---|
| Discovery/ownership | Has the character/player learned this technique? |
| Physical compatibility | Can the current body perform it? |
| Active-deck construction | Which compatible techniques does the player deliberately carry? |
| Hand/Attention access | Which carried techniques are currently available to consider? |

If grafting a part automatically inserts every related card and removing it deletes
all of them without player choice, the result may be a dynamic ability loadout rather
than meaningful deckbuilding. Active inclusion/exclusion choices are therefore
required somewhere in the loop if “deckbuilder” remains a product claim.

### DC-D03 — Current acquisition-loop candidate

Status: `WORKING HYPOTHESIS`; the owner explicitly stated that all details are open to
discussion, revision, and fun testing.

The current candidate is:

```text
discover a technique through embodied experience
-> acquire or fit a compatible physical source
-> make the technique eligible
-> deliberately place a bounded compatible selection in the active deck at a
   maintenance/reconstruction point
-> access it through the hand/Attention layer
-> use and possibly master it
-> preserve bounded knowledge across death without making death itself fabricate
   arbitrary cards
```

Useful current rationale:

- embodied discovery supports the transhumanist fantasy better than generic card
  packs alone;
- deliberate active-deck construction preserves player authorship and prevents every
  graft from causing automatic deck bloat;
- removing a source may remove current access without necessarily erasing learned
  knowledge;
- death may preserve knowledge rather than flesh, but death-only rewards must not
  encourage intentional failure farming.

None of the following is decided:

- whether techniques are learned by observation, experimentation, combat use,
  extraction, grafting, rewards, or a mixture;
- whether a graft supplies one innate action, candidate cards, signature cards, or no
  automatic cards;
- where and how often the active deck may be edited;
- whether an incompatible learned card leaves the deck, becomes dormant, or waits in
  an archive;
- how many techniques can persist across death;
- whether death chooses, scores, imprints, degrades, or merely reveals remembered
  techniques;
- whether any card is permanently lost;
- total deck size, copy limits, draw pile, discard pile, exhaustion, reshuffle, rarity,
  upgrades, and reward frequency.

The owner endorsed the general layered structure, not these details. Prototype results
may revise or replace the entire candidate loop.

## 7. Narrative direction and examples

### DC-N01 — Late ontological recontextualization

Status: `OWNER DIRECTION` at the structural level; exact truth is `DEFERRED`.

The story may begin as a relatively ordinary escape, freedom, or survival story and
gradually reveal a larger mystical or ontological reason behind the repeated bodily
experience. The late discovery should materially recontextualize what the player has
been doing.

Simulation, discovering that the world is a server, and attempting to pull its plug
were `EXAMPLE ONLY`. They are not canon, a finale, or an approved explanation.

## 8. Explicitly unresolved foundations

Do not ask for detailed balance or final presentation as if these foundations were
already closed:

- the exact definition, objective, and end conditions of a combat encounter;
- the exact definition of a run and the structure between runs;
- failure, death, retention, and restart rules;
- world topology, camera, traversal, map, rooms, and level-design grammar;
- exact deck ownership, construction, draw, discard, and reward rules;
- exact relationship between environmental problem solving and combat cards;
- exact real-time interaction families and their frequency;
- final narrative truth, theme expression, and ending;
- production scope, engine, final UI, art, audio, pricing, and market positioning.

Examples previously discussed—wolf arms breaking barriers, eagle-derived parts
crossing height, plant replacements surviving oxygen loss, robotic torsos, Kinect,
AR, an open isometric world, *Inscryption*-like revelation, and a simulation/server
ending—remain `EXAMPLE ONLY` unless separately approved.

## 9. Design method for future collaborators

Work from macro to micro, but use small reversible prototypes once a macro hypothesis
is coherent:

```text
identity and intended memory
-> primary control/combat grammar
-> cards/body responsibility boundary
-> encounter objective and resolution
-> run/failure/persistence structure
-> presentation, tuning, content, and polish
```

Do not treat every predicted future dependency as a reason to stop. Choose the
smallest upstream hypothesis that collapses several downstream questions, mark it as
reversible, and test it. Do not prematurely ask the owner to define exact UI,
milliseconds, percentages, card counts, or content lists.

For the anatomical-deckbuilder hypothesis, continue only if a player can explain:

1. why a card was available;
2. which body source executes it;
3. what choosing it prevents or risks;
4. how the resulting wound/body change alters later decisions; and
5. which body and Brain choices authored the pool and slot behavior rather than being
   automatically assigned.

Revise or kill the hypothesis if cards become generic stat modifiers, the body becomes
cosmetic eligibility, automatic graft changes erase deck authorship, dead hands are
routine, or the real-time layer becomes an unrelated minigame.

## 10. Current discussion frontier

Document 39 resolves the current card-access architecture without adding a
conventional active deck: usable body sources generate the eligible card-instance
pool and run-configured Brain Parts shape which instances reach Attention. Exact
counts, weights, and content remain evidence-bound tuning questions rather than the
next macro interview.

The dependency-ordered product frontier is now mental defeat, surrender, and mercy.
A separate collectible-technique or active-deck layer may be proposed later only if
body configuration plus Brain configuration fails to provide enough player authorship.

## 11. Brain Module reconciliation (2026-08-21)

Status: `OWNER-DELEGATED RESOLUTION`.

The simplest non-colliding model is:

```text
body construction decides which physical card instances can exist
-> Brain Part configuration shapes weighted Attention access
-> the persistent hand exposes imperfect current choices
-> staged commitments, reflexes, wounds, and consequences resolve
```

Accordingly:

- the current approved baseline has no separate collectible technique inventory,
  draw pile, discard pile, or active-deck construction screen;
- changing the body and configuring Brain Parts are the two current authorship layers;
- only Brain Parts are confirmed permanent Brain progression; technique knowledge,
  card mastery, and body retention across death remain unapproved;
- `run` means only the interval during which a chosen Brain configuration is locked;
  it does not decide map, room, restart, checkpoint, or world structure;
- the anatomical-deckbuilder phrase remains a working product description, not proof
  that a conventional deckbuilder subsystem is required;
- future technique discovery must justify itself against complexity, deck bloat, and
  duplication of Brain progression before it can reopen this baseline.

This resolution removes overlap without changing runtime or making a market/fun
claim. It may be revised after bounded probability tests and human comprehension
evidence.
