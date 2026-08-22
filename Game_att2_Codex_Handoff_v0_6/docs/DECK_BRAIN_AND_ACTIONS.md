# Game att2 - Deck, Brain, and Actions

Status date: 2026-08-22

Status: **CURRENT LIVING PAPER-DESIGN AUTHORITY. OWNERSHIP, DEFAULT/LEARNED DEATH
PERSISTENCE, MEMORY CARD, AND BRAIN RESET DIRECTION ARE APPROVED; VALUES, CONTENT,
DELIVERY, AND RUNTIME REMAIN OPEN.**

## Anatomical deckbuilder thesis

> A card declares what the player is trying to do; the body determines how and at
> what physical cost it can be done.

Voluntary primary commitments normally use cards. Cards should represent physical
techniques or preparations rather than detached percentage filler. Automatic reflex
events, passives, wounds, Blood transactions, survival checks, and forced state
reactions remain outside the hand.

The body and card must both matter:

- a card without a legal physical source cannot execute;
- a source does not automatically force every related technique into the deck;
- changing or damaging the body changes card legality and execution profile;
- active inclusion/exclusion remains a real player decision.

## Ownership layers

| Layer | Owns |
|---|---|
| Discovery/knowledge | Which techniques have been learned or made available |
| Body | Which techniques are physically possible and through which exact source |
| Active deck | Which compatible techniques the player deliberately carries |
| Draw/hand | Imperfect access to the player-authored deck |
| Brain | How the current hand/body relationship is interpreted or modified |

The player authors a bounded active deck from currently known and source-compatible
possibilities. Ordinary draw randomness acts on that deck and is not secretly
weighted by the Brain.

Exact acquisition, deck size, copy limits, edit locations, draw, discard, retention,
exhaustion, reshuffle, rarity, upgrades, and ordinary rewards remain open. Death
persistence is bounded below.

## Default technique cards

The active-demo starting library currently includes:

| Card | Required source | Target | Status |
|---|---|---|---|
| `Punch` | a qualifying arm | selected opponent body region | Default card; exact cost/effect/threshold open |
| `Kick` | qualifying Legs | selected opponent body region | Default card; exact cost/effect/threshold open |
| `Headbutt` | qualifying Head | selected opponent body region | Default card; exact cost/effect/threshold open |

These are persistent default techniques, not rewards selected by the Brain. A card
whose source requirement is not met remains visible but Dormant/unusable. Starting
body compatibility is not guaranteed.

## Turn budget, combo, and lifecycle

- The active demo's visible per-turn card/action resource is named `Mana`; Mana is
  separate from Blood and replaces the previously unnamed budget.
- Available Mana increases as rounds pass, exposing larger sequences and combos later
  in the duel. Starting Mana, the per-round increase, cap, refill, and carryover remain
  `OPEN`.
- The player may play as many legal cards as that budget permits.
- Two or more declared compatible cards may form a combo and complete within the same
  turn. Exact combo links and resolution order remain open.
- Each card pays a disclosed Mana cost. Mana's maximum, refresh rule, carryover, and
  relationship to Blood remain open; do not silently make Blood pay ordinary card
  costs or generate Mana.
- Automatic reflex-defense consumes neither card nor voluntary play.
- Committing and resolving an offensive technique card does not start an attack-side
  QTE. The active demo's short execution input belongs to incoming defense: Yellow
  allows Block/Parry and Red requires Evade.
- `Ready`, `Dormant`, `Invalid`, and `Spent` remain useful lifecycle meanings.
- Temporary source/commitment/turn-budget failure may make a card Dormant; permanent loss
  of every required source makes it Invalid.
- A locked card canceled before execution pays no unpaid execution cost and receives
  no substitute card/source/target. Whether spent budget is restored remains `OPEN`.

Mana escalation must not become permission for an infinite defensive loop. Repeated
defense, restoration, redraw, retention, or setup must consume or mutate a finite
state and may not reproduce the same complete combat position at no cost. Before the
Mana cap, round growth advances the clock. At or beyond the cap, temporary card/status
cycling is insufficient: a full round must consume or worsen Blood, integrity, wound
severity, a finite item/charge, or capability. Exact anti-stall card rules remain a
`WORKING HYPOTHESIS` until a bounded comparison closes them.

Block supports that constraint directly: its chosen legal guarding part becomes the
recipient and loses Integrity/capability rather than creating free total-state
restoration. Parry and Evade remain reflex routes, not cards, and do not pay Mana.
Their timing, source, and assistance rules remain separate from deck cadence.

## Inventory boundary

Inventory is not part of ordinary Brain hand selection. Owned items and tools remain
directly inspectable and subject to real ownership, uses, expiry, source, timing,
target, cost, and commitment rules.

Whether inventory spends the same turn budget or retains one separate bounded use is
`OPEN`. It must not create an unlimited item/card chain. The exact production
presentation remains open; the old required Attention Slot readiness rule is
historical.

## Brain doctrine

> The Brain does not select or distribute the player's body actions. It interprets
> and modifies the hand the player built, turning bodily imbalance into an
> inspectable power-versus-control tradeoff.

```text
body/knowledge -> source-valid library
-> player-authored active deck
-> ordinary draw -> current hand
-> body + hand -> inspectable compatibility facts
-> deterministic Brain modifier
-> complete benefit/risk preview
-> player commitment and physical resolution
-> body/card legality and compatibility recomputed
```

The Brain may stabilize, exploit, retain, transform, or redirect an already-declared
hand/body relationship. Every rule must declare:

```text
trigger
-> state-derived condition
-> affected hand/card/source/relationship
-> deterministic benefit
-> visible instability cost, risk, or limitation
-> duration/expiry
-> pre-commit preview
-> post-resolution evidence
```

The Brain may not normally choose, weight, filter, draw, remove, or guarantee cards;
fabricate capability; restore an invalid source; waive costs or legality; create a
card absent from the library/deck contract; add an ordinary Main; or produce hidden
random punishment.

## Same-day death persistence

On death:

- persistent default cards remain;
- technique cards learned during that attempt are removed;
- exactly one Memory Card is generated;
- an incompatible Memory Card remains Dormant until the reset body or a later graft
  supplies its required source; incompatibility produces no replacement reward;
- run-derived embodied instability clears;
- already-earned persistent Brain buffs/bonuses remain.

A persistent Brain buff must expose its trigger, legal affected relationship,
deterministic benefit, limitation, and evidence. It should make later opponents easier
to pass through an inspectable player advantage, not by secretly lowering enemy state,
selecting favorable cards, restoring absent sources, or waiving card legality.

Memory Card generation recipe, whether it records a used/learned/death-context card,
copy/storage rules, deck placement, duplicates, caps, Brain buff catalogue, acquisition,
and numerical power curve remain `OPEN`.

## Embodied instability

Instability is not approved as a new global meter. It must derive from inspectable
current facts such as source state, wound, integration, incompatible commitments, or
another explicitly authored body relationship. It is recomputed after relevant state
changes and previewed before commitment.

Exact compatibility inputs, thresholds, representation, Brain content, number of
active rules, and whether progression uses a tree, collectible parts, a hybrid, or
another wrapper remain open.

## Poker boundary

Pair, straight, flush, fixed hand ranking, and score-multiplier grammar are not part
of the doctrine. Hand composition matters only through anatomical and causal facts.

## Minimum information contract

Before commitment the player can inspect:

- action and timing;
- exact physical/tool source;
- target body region and target legality;
- minimum source condition and current source condition;
- turn cost, remaining budget, and any declared combo relationship;
- expected effect if unaltered;
- occupied or reserved sources;
- Blood, integrity, wound, item-use, and other costs with timing;
- Full/Strained/Desperate/Dormant/Invalid state and reason;
- Brain benefit and instability consequence;
- important capability or route loss caused by the result.

Final layout, iconography, animation, certainty bands, and accessibility presentation
remain open.
