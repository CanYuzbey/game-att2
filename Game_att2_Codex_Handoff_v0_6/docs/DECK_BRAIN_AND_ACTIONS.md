# Game att2 - Deck, Brain, and Actions

Status date: 2026-08-25

Status: **CURRENT LIVING PAPER-DESIGN AUTHORITY. CONCEPT-DECK, BRAIN-PART,
ATTENTION, READIED-ITEM, AND PREPARATION/MAIN OWNERSHIP ARE APPROVED DIRECTIONS;
DIAGNOSTIC COUNTS, CONTENT, VALUES, ACHIEVEMENTS, SAVE DATA, UI, AND RUNTIME REMAIN
UNAPPROVED.**

## Anatomical deckbuilder thesis

> A card declares what the player is trying to do; the body determines how and at
> what physical cost it can be done.

The player does not discover basic combat concepts one at a time. The complete
abstract card vocabulary is known from the beginning. The current body determines
which physical expressions of those concepts can exist, and an earned Concept Deck
determines which compatible expressions are deliberately carried.

The same limb may support several roles. A crab-like arm is not restricted to one
attack: it may have characteristic Attack, Defence, Control, or Preparation
expressions. Those expressions must still differ causally from another limb through
source requirements, targeting, effect, cost, exposure, reflex profile, commitment,
or downstream body consequence. Label or number changes alone do not create a new
card.

Automatic reflexes, body passives, wounds, Blood transactions, survival checks, and
forced state reactions remain outside the voluntary hand.

## Ownership layers

| Layer | Owns | Does not own |
|---|---|---|
| Card-concept vocabulary | Abstract intents and techniques known from the beginning | Physical capability or current deck membership |
| Body | Exact source-valid physical card expressions and non-card capabilities | Meta progression or Attention access |
| Concept Deck | Achievement-earned playstyle chassis, dedicated special cards, and atomic compatible exchanges | Missing anatomy or hidden draw correction |
| Anatomical Deck | The current bounded set produced from body-compatible expressions and the selected Concept Deck | Inventory, reflexes, passives, or forced actions |
| Attention | Imperfect current access to the Anatomical Deck | Physical capability or extra voluntary actions |
| Brain Parts | Persistent paired buffs/nerfs that affect one declared Attention/access/execution relationship | Deck membership, invented sources, perfect hands, or ordinary extra plays |
| Readied Item Card | One deliberately prepared owned item opportunity with exact uses/source/timing | Random Attention selection or automatic replacement |

This separation is binding. Body compatibility is checked before Concept Deck
construction; Concept Deck exchanges complete before Brain selection/modification;
Brain rules never reintroduce a removed card.

## Card labels

Every card receives a small manually authored set of functional labels based on its
causal effect, such as Attack, Defence, Control, Preparation, or Recovery. Labels are
mechanical metadata used by Concept Deck selection/exchange rules and eligible Brain
Part rules. A label grants no damage, defence, rarity, or class bonus by itself.

Labels are assigned to cards, not chosen dynamically to chase a buff. A multi-label
card remains one card instance and is never duplicated because several rules match.
The exact final label vocabulary remains `OPEN`.

## Achievement-earned Concept Decks

`APPROVED DIRECTION`: earned Concept Decks persist between attempts/runs. They are
unlocked through authored achievements or equivalent non-boss milestones. Boss
progression is reserved for Brain Parts so the two persistent layers do not duplicate
the same reward path.

A Concept Deck is a reusable playstyle chassis, not an exact saved list that
fabricates incompatible anatomy. It contains:

- one declared playstyle promise;
- label/source requirements;
- one or more explicit remove/add exchanges;
- dedicated special cards;
- a visible sacrifice as well as a gain;
- a compatibility and Dormant rule.

At an approved construction boundary, the chassis resolves against the current body.
Compatible exchanges may be applied. Incompatible expressions remain known but
Dormant; they are not deleted, rewritten, or replaced automatically.

### Atomic exchange contract

Every exchange follows:

```text
current compatible Anatomical Deck and usable sources
-> validate every sacrificed card and its source
-> validate every gained card and its source
-> validate deck-size and other declared constraints
-> remove and add in one mutation, or apply nothing
-> construct complete deck
-> only then apply Brain/Attention behavior
```

A missing, Dormant, Invalid, disabled, or otherwise unusable sacrifice cannot buy a
live gain. A gained card with a missing source cannot enter as compensation. If a
source is lost during combat, dependent cards become Dormant/Invalid immediately;
the sacrificed cards do not return mid-encounter. Reconstruction waits for the next
approved safe boundary.

`EXAMPLE ONLY`: an aggressive chassis might remove one defensive Legs expression and
one defensive Left-Arm expression, then add one brutal Left-Arm attack and one brutal
Right-Arm attack. This specializes the body-card relationship; it does not physically
remove those limbs. A future exceptional deck that sacrifices anatomy would require
its own explicit paper rule.

Count parity does not prove balance. Every powerful special card still needs an
experienced Blood, exposure, recovery, interception, commitment, capability, or lost-
future-option burden.

## Attention and Brain Parts

The current research direction combines imperfect Attention with deliberate deck
construction:

```text
known concepts + current body
-> selected Concept Deck and atomic exchanges
-> current Anatomical Deck
-> Brain-Part-configured weighted Attention selection
-> persistent visible hand
-> Preparation/Main commitment
-> source/reflex/consequence resolution
```

`APPROVED DIRECTION`: Brain Parts are rare persistent roguelite rewards, normally on
the boss/progression path. They are configured at the run/attempt boundary and remain
locked for that interval. Each ordinary Part owns one primary lever and exposes both
a buff and a nerf, restriction, risk, or cost.

An ordinary Brain Part may:

- change the visible selection weight of matching labelled/source-bound cards for one
  declared Attention relationship; or
- deterministically modify execution of a card reached through one declared slot or
  relationship.

Ordinary Parts do not combine access and execution power on the same Part. They may
not create a card absent from the Anatomical Deck, restore a missing source, waive a
cost, select a target, guarantee Attack/Defence/Main, grant an ordinary extra action,
or hide random punishment.

`WORKING HYPOTHESIS`: four ordinary persistent Attention positions, weighted
selection without replacement, refill of Spent/Invalid positions at Decision Refresh,
and no category guarantee are the bounded diagnostic baseline. A once-per-round,
pre-lock Blood-paid redraw may be compared only when no identical no-alternative
redraw is possible. Counts, weights, redraw cost, repetition handling, and final hand
lifecycle remain evidence-bound rather than final values.

## Hold-drop-play and action budget

The intended interaction character is Balatro-like in rhythm, not poker rules:

```text
read visible state and intent
-> inspect persistent Attention cards
-> hold/drag a card
-> choose a target limb only when required
-> preview source, cost, risk, Brain effect, and interception
-> drop/commit
-> resolve and wait for the counter/interception boundary
```

The card already declares its exact source or source set. The player does not choose a
different source unless the card explicitly supports a source choice.

`PAPER RULE`: an actor may commit zero or one Preparation and zero or one Main per
round. Preparation resolves before Main and may establish a later automatic response.
Attention capacity never creates another ordinary action. The Aug-22 growing-Mana,
multi-card-sequence, and combo cadence is superseded by this owner decision for the
active paper design. Blood remains life, economy, and selected ability fuel; it is not
renamed into generic card energy.

A started atomic action completes. Later source damage changes future capability
rather than retroactively erasing the action. A now-illegal unstarted commitment is
canceled without fabricating a substitute source, card, or target. Exact spent-cost
handling before execution remains `OPEN`.

## Reflex and previously prepared responses

Cards declare whether and how their execution can be intercepted. During an
interceptable action, the defender receives the authored automatic reflex opportunity
and any compatible previously played Preparation may trigger.

When the player attacks, there is no attack-side player QTE; an enemy interception is
automatic/state-derived or comes from that enemy's prior Preparation. When an enemy
attack is incoming, the player's bounded reflex input follows the Yellow/Red defence
contract. This preserves the intended sequence without turning offensive cards into
an action minigame.

Prepared defence plus its reflex is one causal defence, not two unrelated reductions.
Reflex performance may alter the physical result but may not routinely erase a bad
strategic commitment.

## Readied Item Card lane

One owned Item Card may be deliberately readied before the encounter or at another
later-approved readiness boundary.

- It remains visibly an Item Card.
- It occupies a separate lane and never reduces ordinary Attention capacity.
- It retains exact ownership, quantity, uses, expiry, source, target, timing, and cost.
- Playing it consumes its authored Preparation or Main opportunity.
- At most one voluntary inventory-origin action executes per round.
- Once used, lost, expired, or source-invalid, the lane remains empty.
- Another item is never readied automatically.

In-encounter re-readiness remains `OPEN`. If later allowed, it requires an explicit
authored action and cannot become unrestricted inventory access by another name.

## Persistence

At same-day death or a full run end:

- earned Brain Parts persist;
- earned Concept Decks persist;
- the abstract card-concept vocabulary remains known because it was available from
  the beginning;
- a Concept Deck blueprint remains owned even when its current expressions are
  Dormant under the reset body;
- current body, wounds, grafts, encounter state, and unaware-world state follow the
  same-day/full-run reset contract rather than becoming permanent card capability;
- run-derived temporary Brain/body instability clears unless a later explicit rule
  says otherwise.

The Aug-22 attempt-learned-card loss and death-generated Memory Card system is
superseded. Death does not fabricate a new card reward. Exact achievement conditions,
Brain-Part boss rewards, equipped loadout count, save boundary, duplicate handling,
and full-game reset scope remain `OPEN`.

## Scaling and individuality guardrails

`OWNER-APPROVED DIAGNOSTIC BOUNDARY`: the first bounded catalogue uses the following
provisional limits. These are research gates, not final production counts:

- at most five cards referencing one exact source;
- at most three functional labels per card;
- at most six causal mechanic atoms including timing, target, and reflex grammar;
- exactly one causal signature creativity atom per card;
- at most two special cards added by one ordinary Concept Deck exchange;
- at most one novel engine primitive in a card, requiring separate system review.

Authorship is factorized across limb expressions, Concept Deck exchanges, Brain rules,
and shared execution grammar. Full combinations are tested rather than handcrafted.
Static source/atomicity checks, near-duplicate fingerprints, Pareto-dominance review,
exhaustive exchange/source-loss cases, ordinary pairwise coverage, named high-risk
three-way coverage, seeded transparent policies, and human comprehension tests form
the evidence path. The complete method and research-only validator live in
`../research/card_scaling_guardrails/`.

Passing automation establishes structural consistency only. It cannot establish
creativity, comprehension, balance, accessibility, fun, or long-term replay value.

## Poker boundary

Pair, straight, flush, fixed hand ranking, and score-multiplier grammar are not part
of the design. The Balatro comparison describes hold/read/commit rhythm and
achievement-earned deck identities only.

## Minimum information contract

Before commitment the player can inspect:

- action, labels, and Preparation/Main timing;
- exact physical/tool source and current condition;
- target body region and target legality;
- Concept Deck exchange/sacrifice that made the card available;
- expected effect if unaltered;
- Brain-Part selection tendency or execution buff and paired nerf;
- Blood, integrity, wound, item-use, exposure, and other costs with timing;
- interception/reflex route and any previously prepared response;
- important capability or route loss caused by the result;
- Dormant/Invalid reason without an automatic replacement promise.

Final layout, exact card/deck/hand counts, iconography, animation, accessibility,
achievement list, Brain content, values, save data, and runtime implementation remain
`OPEN`.
