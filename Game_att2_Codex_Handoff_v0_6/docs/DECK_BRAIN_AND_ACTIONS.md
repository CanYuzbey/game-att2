# Game att2 - Deck, Brain, and Actions

Status date: 2026-08-21

Status: **CURRENT LIVING PAPER-DESIGN AUTHORITY. OWNERSHIP DOCTRINE IS APPROVED;
ACQUISITION, COUNTS, CADENCE, CONTENT, PROGRESSION DELIVERY, AND RUNTIME ARE OPEN.**

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
exhaustion, reshuffle, rarity, upgrades, rewards, and death persistence remain open.

## Action budget and lifecycle

- Each actor has zero/one Preparation and zero/one Main in the paper round model.
- A card supplies an option, not an extra play.
- Automatic reflex-defense consumes neither card nor voluntary play.
- `Ready`, `Dormant`, `Invalid`, and `Spent` remain useful lifecycle meanings.
- Temporary source/range/commitment failure may make a card Dormant; permanent loss
  of every required source makes it Invalid.
- A locked action canceled before execution loses its Main tempo but pays no unpaid
  execution cost and receives no substitute card/source/target.

## Inventory boundary

Inventory is not part of ordinary Brain hand selection. Owned items and tools remain
directly inspectable and subject to real ownership, uses, expiry, source, timing,
target, cost, and commitment rules.

The surviving paper safeguard is at most one voluntary inventory-origin action per
round. An inventory Preparation may be followed by a body Main, but ordinary item
chains do not create a third action economy. The exact production presentation of
inventory access remains open; the old required Attention Slot readiness rule is
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
- target and current range profile;
- expected effect if unaltered;
- occupied or reserved sources;
- Blood, integrity, wound, item-use, and other costs with timing;
- Full/Strained/Desperate/Dormant/Invalid state and reason;
- Brain benefit and instability consequence;
- important capability or route loss caused by the result.

Final layout, iconography, animation, certainty bands, and accessibility presentation
remain open.
