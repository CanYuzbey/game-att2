# Game att2 - Deck, Brain, and Actions

Status date: 2026-08-24

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

### D0 eight-card/four-hand comparison — working hypothesis

On 2026-08-24 the owner asked that the following proposal be retained for later
comparison. It replaces the earlier `6/4` proposal as the current comparison surface;
it does **not** promote deck cadence, card values, or acquisition to paper rules.

The proposed starter package contains five technique types and eight instances:

| Technique | Instances | Proposed role | Proposed minimum contract |
|---|---:|---|---|
| `Punch` | 2 | low-commitment arm attack | approved default; exact values still open |
| `Kick` | 2 | leg-sourced attack | approved default; exact values still open |
| `Headbutt` | 2 | head-sourced attack | approved default; exact values still open |
| `Brace` | 1 | preparation for a stronger next Block | `1 Mana`; reserve one Full/Strained guarding Arm; improve its next legal `GuardFactor` by one comparison step (`1.20 -> 1.00`, `1.00 -> 0.80`, `0.80 -> 0.80`); expire after the enemy action; never automate Block or modify Parry |
| `Feint` | 1 | same-turn setup for a second source | `1 Mana`; commit one Full/Strained attack-capable source and exact enemy region; the next attack from a different source to that region gains `+3 Impact`; expire unused at turn end; never change cue or defense route |

`Brace` and `Feint` are proposed starter additions, not approved default content.
Their values exist only to make a paper hand resolvable and are not balance claims.

The comparison cadence is:

- active deck: exactly eight instances;
- opening hand and hand cap: four;
- round end: retain at most one unplayed card and discard the rest;
- next round: draw to four and reshuffle the discard pile only when required;
- a Dormant card remains visible, occupies a hand position, and receives no automatic
  replacement draw;
- editing is one-for-one at a Grafting Table, so learning never grows the active deck;
- provisional copy limit: two ordinary copies and one copy of a Memory/Unique card;
- provisional validation floor: at least five Attacks, at least two distinct attack-
  source families, and at least two cards costing `1 Mana`.

The proposed starting deck has six Attacks and two preparations; every four-card
opening contains at least two Attacks. That arithmetic does not prove that its choices
are interesting. Before promotion, compare source commitment, Dormant-hand frequency,
draw-order repetition, and whether `8/4` becomes too consistent or still creates
obvious turns.

### Technique acquisition comparison — working hypothesis

The proposed acquisition loop is:

```text
Observe -> Candidate -> Learn -> Slot -> Prove -> Memory
```

- **Observe:** a visible enemy intent can reveal a technique candidate; the player
  need not be hit. An important demo enemy exposes at most two candidates.
- **Candidate:** observation creates an inspectable opportunity, never an automatic
  reward. A graft or implant changes compatibility but does not teach a technique.
- **Learn:** each Grafting Table visit permits at most one `Technique Study` choice
  from observed candidates. It joins the current-attempt known library even if the
  present body cannot yet source it.
- **Slot:** the player may make at most one one-for-one deck swap per table visit.
  Ordinary source-incompatible attempt techniques remain known but cannot be slotted;
  the existing stored-Memory/Dormant rule is the explicit exception. There is no
  universal Blood purchase price; an NPC trainer's authored price must follow that
  actor's Goal, Need, Claim, and Concession.
- **Prove:** Memory eligibility still requires legal source use, voluntary commitment,
  an explicit state mutation, and a later changed decision or outcome.
- **Memory:** attempt-learned techniques are lost on death. Exactly one eligible
  lesson may become the run's Memory Card; otherwise death prints an `Unresolved
  Memory`. A Memory joins the library but is neither auto-slotted nor auto-drawn.

For the bounded demo, Fight A may expose at most two candidates, the next Grafting
Table may teach one and allow one swap, and the player reaches the gate boss with at
most one attempt-learned technique. Random three-card reward screens, card rarity,
and card upgrades are excluded from this comparison; body, graft, implant, source
condition, and deck replacement are expected to supply the variation.

The first authored comparison catalogue is capped at twelve technique types: the five
starter types above plus up to seven learned candidates. The following names are
`EXAMPLE ONLY`, not approved demo content:

| Example | Distinct decision it should test |
|---|---|
| `Hook` | threat/source denial rather than raw damage |
| `Joint Break` | a visible condition breakpoint, such as Full `4` versus Strained `10` |
| `Shoulder Check` | a high-commitment Torso + Legs attack |
| `Tendon Cut` | Cutting/Open Wound pressure that also endangers graft value |
| `Pin` | delay Recovery of an already-Committed source |
| `Blood Lunge` | an exceptional disclosed Mana + Blood technique |
| `Last Nerve` | a Desperate-only technique that Exhausts |

Candidate requirements should use capability tags, not species names. No learned
card should dominate merely through a larger damage number; each must alter target,
source, timing, commitment, wound, Will, or reward-routing decisions.

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

`WORKING HYPOTHESIS`: after draw/refresh and hostile-intent reveal, but before the
player's card sequence, open one `Tool Window`. The player may use zero or one owned
tool per round. A tool spends no Mana, consumes one finite charge, requires its exact
physical source, and leaves that source Committed until cleanup. Tools remain outside
the deck; implants are passive biological modifiers and do not consume the tool use.
No reactive/emergency tool use is included in the demo comparison.

This does not approve any particular tool, charge count, source tag, healing amount,
or UI. Finite charges and the one-use bound must still be tested against healing loops
and anti-stall. The old required Attention Slot readiness rule is historical.

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

### Memory Imprint and one Brain protocol — working hypothesis

The original demo-facing proposition is:

> Death is the printer; an earned causal lesson is the ink.

Death still produces exactly one Memory Card, but a usable payload requires one
authored lesson proof from that attempt:

```text
inspectable prior state
-> legal voluntary technique or preparation
-> explicit state mutation
-> later changed legal affordance or outcome
```

Mere death, manual abandon/reset, observation without player application, repeated
QTE execution, self-harm, and cosmetic target variations create no eligible lesson.
If several eligible attempt-learned techniques exist, the player chooses one through
a disclosed rule; hidden random selection is excluded. If none exists, death still
prints one visible `Unresolved Memory` with zero gameplay payload. It does not occupy
the active deck or mint permanent power.

`WORKING HYPOTHESIS`: the demo stores one usable source-bound Memory Card. A new one
requires a visible replace/archive choice; duplicates keyed to the same authored
lesson do not stack. A stored Memory joins the known library but is not auto-slotted,
auto-drawn, or guaranteed in the opening hand. Normal body-source legality applies,
including Dormant state after reset.

One bounded persistent Brain comparison is `Mnemonic Grip`: once per encounter, the
first already-drawn, source-legal Memory Card that would be discarded at round end is
retained without consuming the ordinary one-card retain allowance. The trigger,
affected card, one-use limit, and result are visible. It does not change draw order,
card source, cost, target, enemy state, or QTE timing. Its acquisition must be tied to
one named first-time causal proof/milestone, not death count; the exact proof remains
`OPEN`.

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
