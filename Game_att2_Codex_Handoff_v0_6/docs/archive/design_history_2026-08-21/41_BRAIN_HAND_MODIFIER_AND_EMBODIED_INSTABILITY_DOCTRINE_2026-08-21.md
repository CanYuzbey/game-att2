# Game att2 - Brain Hand Modifier and Embodied Instability Doctrine

Status date: 2026-08-21

Status: **OWNER-APPROVED PRODUCT DOCTRINE; PAPER IMPLEMENTATION MODEL PROPOSED;
NUMBERS, CONTENT, PROGRESSION DELIVERY, HUMAN EVIDENCE, RUNTIME, CONFIGURATION,
PERSISTENCE, AND FINAL UI NOT APPROVED**

## 1. Decision and supersession

The Brain is not the system that chooses which body cards the player receives. The
player must retain meaningful authorship over a bounded active deck. The Brain acts
on the current hand and converts embodied compatibility or instability into a
visible power-versus-control tradeoff.

This later owner decision supersedes these parts of document 39 and their document
40 reconciliation:

- weighted or hard-filtered Brain selection as the ordinary source of the hand;
- Brain configuration as the second author of card access;
- the statement that the approved baseline excludes an active deck;
- permanent collectible Brain Parts as the only approved delivery/progression form;
- Brain-paid redraw as the defining expression of the Brain system.

Document 39 remains decision history. Its source-validity, body ownership, inventory
boundary, automatic-reflex boundary, action-budget, preview, and consequence
safeguards survive unless this document explicitly changes them. No runtime was
changed by either document.

## 2. Doctrine

> The Brain does not select or distribute the player's body actions. It interprets
> and modifies the hand the player built, turning transhumanist bodily imbalance
> into an inspectable power-versus-control tradeoff.

Short form:

```text
does not choose -> interprets
does not deal -> modifies
does not secretly punish -> exposes a tradeoff
does not replace the body -> processes relationships within the body
```

The thematic responsibility is deliberate: the body answers **what can I physically
do?**; deck authorship answers **which possibilities did I prepare?**; the Brain
answers **how does this current self process those possibilities together?**

## 3. Approved ownership model

```text
current body and learned/discovered technique state
-> source-valid card library
-> player-authored bounded active deck
-> ordinary draw produces the current hand
-> current body + current hand produce inspectable compatibility facts
-> Brain rule deterministically modifies the hand or its consequences
-> player previews action, source, target, benefit, and instability risk
-> commitment, physical/reflex execution, and causal resolution
-> wounds, source loss, card lifecycle, and body state are recomputed
```

The layers have separate authority:

| Layer | Owns | Must not own |
|---|---|---|
| Body | Physical capability, exact source, source state, and card eligibility | Hidden hand weighting or fabricated techniques |
| Active deck | Player-authored inclusion and exclusion among currently legal/known techniques | Waiving source requirements |
| Draw/hand | Imperfect access to the deck the player authored | Undisclosed Brain steering |
| Brain | Deterministic interpretation or modification of the current hand and visible instability tradeoffs | Ordinary card selection, physical capability, or extra Main actions by implication |
| Resolution | Costs, execution grade, wounds, position/range, and state-derived consequences | Teleporting to authored outcomes |

An exact card may become invalid, degraded, or dormant when its physical source is no
longer usable. Brain rules cannot restore the missing source, fabricate a substitute,
or hide the invalidation.

## 4. Embodied instability contract

Instability is not approved as a new global meter. The first implementation should
derive it from facts the player can inspect, such as:

- whether cards in the current hand depend on mutually strained or poorly integrated
  sources;
- whether one wounded source is being committed repeatedly or simultaneously;
- whether a graft's current integration state conflicts with the demanded action;
- whether a Brain rule deliberately converts an existing incompatibility into more
  power and more risk.

Those are input families, not approved tags, thresholds, or content. The exact
compatibility model remains the current owner-design question.

Every instability effect must be:

1. derived from named current state;
2. recomputed after relevant body or hand changes;
3. visible before commitment;
4. deterministic once the visible state and chosen action are fixed, except for
   separately declared injected randomness already owned by an action;
5. expressed as a consequence or constraint rather than unexplained control theft;
6. usable by the player as a risk they can intentionally accept, avoid, or build
   around.

The doctrine does not approve involuntary random card removal, hidden misplays,
unpreviewed input reversal, arbitrary skipped turns, or a generic insanity meter.

## 5. Brain modifier contract

Every future Brain rule, regardless of whether it comes from a tree, a collectible
part, or another delivery wrapper, must declare:

```text
trigger
-> state-derived condition
-> affected hand, card, source, or relationship
-> deterministic benefit
-> visible instability cost, risk, or limitation
-> duration and expiry
-> pre-commit preview
-> post-resolution evidence
```

Allowed responsibility families include stabilizing a strained relationship,
exploiting an unstable relationship for upside, retaining or transforming a card
under a declared condition, or redirecting a visible cost. These are mechanic
families, not approved Brain Parts, skill-tree nodes, card text, or balance values.

The Brain may not, by default:

- choose, weight, filter, draw, remove, or guarantee ordinary cards;
- make an unusable body source usable;
- waive Blood, action, item, range, or exact-source legality;
- manufacture a card absent from the player's body/library/deck contract;
- add an ordinary extra play or Main action;
- convert instability into hidden random punishment.

## 6. Poker boundary

This doctrine does not make Game att2 a poker game. Pair, straight, flush, score-
multiplier, and fixed hand-ranking rules are neither required nor approved. Hand
composition may matter only where the relationship is anatomical and causal: source,
integration, wound, demand, commitment, or another explicit body fact.

The transferable lesson from modifier-driven deckbuilders is structural, not
thematic: a player-authored deck creates the raw situation while a separate build
layer changes how the same situation is valued. Game att2's distinct content for that
relationship is embodied compatibility and loss of control, not poker scoring.

## 7. Implementation-neutral architecture

The paper model should expose five narrow records before choosing progression form:

| Record | Minimum responsibility |
|---|---|
| `TechniqueCard` | Exact body source, action profile, lifecycle state, and current legality |
| `ActiveDeck` | Player-authored included card instances and reconstruction-point legality |
| `HandState` | Current drawn instances, invalid/dormant facts, and commitments |
| `CompatibilitySnapshot` | Derived, inspectable relationships among hand, source state, and integration |
| `BrainModifier` | Trigger, condition, benefit, tradeoff, duration, preview, and evidence |

Recommended evaluation order:

```text
draw from the player-authored deck
-> validate exact sources
-> derive compatibility snapshot
-> apply deterministic Brain modifiers
-> render complete benefit/risk preview
-> accept one legal commitment
-> resolve execution and consequences
-> mutate body/card state atomically
-> recompute legality and compatibility
```

This is a paper architecture, not permission to add these classes to the simulator.

## 8. First bounded comparison proposal

Before choosing an RPG tree, collectible Brain Parts, or a hybrid, compare the same
scripted body, active deck, draw order, and hand under three paper configurations:

1. no Brain modifier as a control;
2. one stabilizing rule that lowers a declared instability consequence but gives no
   extra card or action;
3. one exploiting rule that increases the value of the same unstable relationship
   while previewing a larger physical/control consequence.

The hand and draw order remain identical across all three. The comparison therefore
tests whether the Brain changes decision quality through hand interpretation rather
than secretly improving card access.

Continue if players can explain:

- why the current hand exists;
- which body facts make it coherent or unstable;
- what the Brain changes without fabricating capability;
- why accepting the stronger option risks a specific part or future action;
- how the resulting body change alters the next hand.

Revise if the Brain is only a passive percentage bonus, if the strongest modifier is
always obvious, or if instability needs hidden randomness to feel relevant. Kill this
form if the Brain becomes detached equipment whose choices could be moved unchanged
to any generic fantasy deckbuilder.

## 9. Deferred decisions

- exact technique acquisition and discovery;
- active-deck size, duplicate rules, edit locations, draw/discard/retention cadence;
- the first compatibility inputs and qualitative or numeric representation;
- whether Brain progression is a tree, collectible parts, a hybrid, or non-persistent;
- the number of Brain rules active at once;
- concrete benefits, costs, status effects, control consequences, and balance values;
- death, run, checkpoint, body retention, and card-knowledge persistence;
- enemy use of the hand/Brain model;
- runtime, config, save data, telemetry, UI, animation, audio, and accessibility.

## 10. Requirements

| ID | Requirement |
|---|---|
| BRH-001 | The player authors a bounded active deck from currently known and source-compatible possibilities. |
| BRH-002 | Ordinary draw randomness operates on the player-authored deck and is not secretly weighted by the Brain. |
| BRH-003 | The Brain deterministically modifies the current hand, its relationships, or their consequences. |
| BRH-004 | Instability derives from inspectable body/hand state and is previewed before commitment. |
| BRH-005 | The Brain cannot fabricate capability, restore an invalid source, waive legality, or imply an extra ordinary action. |
| BRH-006 | Body changes revalidate cards and recompute compatibility before the next legal decision. |
| BRH-007 | Progression delivery remains replaceable behind the shared Brain modifier contract. |
| BRH-008 | Poker hands and scoring patterns are not part of the doctrine. |
| BRH-009 | This approval changes paper authority only; runtime, configuration, content, and UI remain unchanged. |

## 11. Current gate

The current owner-design gate is the paper implementation of this Brain hand-
modifier and embodied-instability doctrine. Mental defeat, surrender, and mercy
remains the next dependency gate after this implementation model is coherent. No
runtime or production gate is open.
