# Game att2 - Strategic Card and Action Economy Direction

Status date: 2026-08-16

Status: **OWNER-DELEGATED, CODEX-APPROVED DESIGN DIRECTION - PAPER BASELINE ONLY; RUNTIME, CONTENT, AND FINAL BALANCE NOT APPROVED**

This document is the current design authority for brain/attention slots, the tactical
hand lifecycle, voluntary card plays, body-sourced card eligibility, and physical
compatibility. It develops the owner's recommendations using the existing body,
wound, dynamic-range, staged-turn, and deferred-reflex decisions.

Approval here means the architecture is coherent enough to guide the next paper
specification. It does not authorize production code, a full deckbuilder, individual
character or item cards, production Stamina, exact draw weights, final UI, or claims
that the system is fun, balanced, accessible, or scientifically optimal.

Owner amendment, 2026-08-14: document 31 clarifies that reflex-defense events are
automatically surfaced from the incoming action and current build. They are not cards
the player manually plays and do not occupy Attention Slots. The selection duty below
is therefore read as Response-supporting strategic preparation, not a reflex-response
card guarantee.

## 1. Plain-language summary

The body decides what the fighter is physically capable of. The brain decides which
of those possibilities are currently in attention. The turn rules decide how many of
those possibilities may actually be used.

```text
current body + equipment + combat state
-> eligible tactical opportunities
-> a small persistent brain/attention hand
-> at most one Preparation and one Main commitment
-> automatically surfaced eligible reflex events from the attack and current build
-> physical consequences change the next opportunity pool
```

More brain slots therefore mean **more choices, not more actions**. This preserves the
value of cognitive progression without letting it replace limbs, equipment, wounds,
or the approved turn structure.

## 2. Owner requirements preserved

- Body-part cards are generated only from existing, currently valid physical sources.
- The brain-selection system influences which eligible cards reach the hand.
- Items are usually single-use, charge-limited, time-limited, or condition-limited.
- A wounded but usable limb may still act, and an exertive action may worsen its wound
  or bleeding when the card says so.
- Ordinary limb use normally has no extra resource cost.
- Special moves may explicitly spend Blood, a later-approved Stamina resource, item
  uses, integrity, or wound safety.
- The normal system must prevent impossible combinations, such as an ordinary Dodge
  during a whole-body Charge or four independent limb attacks in one Main action.
- Rare exceptions are allowed only when written on the card and previewed before the
  player commits.

## 3. Approved architecture

### 3.1 Brain slots are Attention Slots

The formal system name is **Attention Slot**. "Brain slot" may remain player-facing
language if it fits the final fiction.

An Attention Slot holds one currently considered tactical opportunity. It does not
represent a separate physical limb, a guaranteed action, or an action point.

The approved paper baseline is:

| Progress state | Active slots | Meaning |
|---|---:|---|
| Starting | 3 | Small readable hand with basic tactical coverage |
| Developed normal range | 4-5 | Greater consistency and specialization, not extra plays |
| Sixth slot | Deferred | Rare or late possibility only if testing shows five is insufficient |

Three and five are test baselines, not claims about universal human limits. A normal
sixth slot is withheld because every extra persistent option increases consistency,
coverage, comparison work, and cognitive progression power at the same time.

### 3.2 Slot roles are guarantees, not locked card classes

The starting three slots use flexible guarantees:

1. **Commitment-capable:** at least one currently executable Main opportunity when
   the actor has any legal Main opportunity.
2. **Response-supporting:** one legal proactive guard, stance, intent-reading action,
   or other strategic preparation when the current body and state support one.
3. **Adaptive:** a Preparation, utility, treatment, item, control, alternative Main,
   or build-specific opportunity.

These are selection duties, not permanent Attack/Dodge/Utility compartments. A card
may satisfy more than one intent. A Response-supporting offer is not the reflex event
itself and does not guarantee the expected or best answer to the enemy's exact attack.
If no Response-supporting strategic opportunity exists, that selection duty becomes
Adaptive; the automatic reflex system must not fabricate a Dodge unsupported by the
body.

Later slots are flexible or specialized by an approved cognitive progression effect.
The selection system must not guarantee an ideal answer to every enemy intention.

### 3.3 Slots provide options, not plays

The staged turn remains:

```text
zero or one Preparation
-> zero or one Main commitment
-> automatically surfaced eligible reflex events during resolution
```

Preparation and Main may be voluntarily skipped. Skipping does not bank an extra play
for a later round. Reflex responses are opened automatically by the incoming event,
build legality, and physical compatibility. They are not spent from the hand or from a
general pool of extra Main actions.

No generic movement points or action points are added to the baseline. Dynamic range
continues to be produced by action, defense, and reflex outcomes.

Approved Preparation roles include:

- **Read/Check Intent:** improves the declared public information layer before the
  Main choice; it does not reveal unexplained internal scores or guarantee a counter;
- **Power Up/Prepare:** modifies the next compatible Main or Response and declares
  any reserved source, cost, expiry, and blocked alternative before commitment;
- **Utility/Treatment:** performs its authored non-Main effect within the same source,
  cost, and consequence rules.

A Preparation cannot secretly contain a second full Main action. Unless its card says
otherwise, an unused one-round preparation expires after the round and never banks an
extra play.

### 3.4 Persistent-hand lifecycle

Cards are persistent so the player can form and retain a short plan.

At each **Decision Refresh**, after the previous consequences are complete and before
the next choice window:

1. used or consumed cards leave their slots;
2. cards with permanently lost sources or expired items leave automatically;
3. empty slots refill from the newly eligible pool;
4. unused, still-valid cards remain;
5. temporary usability and risk are recalculated and shown.

Refill never occurs immediately after a play. This prevents draw-play chains and
ensures wounds, range, items, and source commitments settle before the next offer.

Card states are distinct:

| State | Meaning | Slot treatment |
|---|---|---|
| Ready | Currently executable | Remains until used, released, or invalidated |
| Dormant | Temporarily unusable because of range, posture, timing, or a short-lived commitment | Remains, visibly explains why, may be released |
| Invalid | Source is gone/unusable for the action, item expired/empty, or the opportunity no longer exists | Clears automatically at Decision Refresh |
| Spent | Played or consumed this round | Clears and refills at Decision Refresh |

Range alone normally changes a card's current profile or makes it Dormant; it does not
erase a planned card. A destroyed source or exhausted item makes the card Invalid.

### 3.5 One Reconsider per round

Once per round, the player may mark one unused Ready or Dormant card for
**Reconsider**. It leaves at the next Decision Refresh and is replaced normally.

Reconsider:

- does not count as Preparation or Main;
- cannot refill immediately;
- cannot be repeated through another effect unless that effect explicitly says so;
- does not guarantee a different or better card;
- exists to prevent a persistent hand from becoming a trap after the plan changes.

The player must be shown that the replacement still comes from the current eligible
pool. A small repetition dampener may reduce an immediate identical redraw when other
eligible options exist; its exact weight is a tuning variable, not an approved value.

## 4. Body and brain responsibilities

### 4.1 Body eligibility

The body owns whether an opportunity exists and whether its sources can execute it.

An eligible body card must declare:

- one or more required physical sources;
- timing: Preparation, Main, or Response;
- intent tags used by selection and presentation;
- legal range profiles;
- physical commitments it creates;
- costs and self-risks;
- target requirements;
- explicit compatibility override, if any.

A Disabled, Ruined, Severed, or Missing source cannot generate or execute an action
that requires its use. A card already in hand becomes Invalid if its required source
crosses that boundary.

A wounded but usable source remains eligible unless its wound rule explicitly removes
the capability. Its current card must show reduced performance or self-risk rather
than hiding the consequence in a separate menu.

### 4.2 Brain selection

The brain/attention selector may:

- satisfy the current slot guarantees;
- weight opportunities toward learned tendencies or a build identity;
- reduce excessive immediate repetition;
- consider current range, visible intent, body state, and item validity;
- use deterministic seeded randomness when the specification calls for variation.

It may not:

- create an action without a valid body, equipment, item, or universal-rule source;
- make an unusable limb act;
- guarantee the perfect counter to a telegraph;
- grant extra Preparation, Main, or reflex plays merely because slot capacity grew;
- silently alter consequences after a card is shown.

The selector pipeline for the paper specification is:

```text
enumerate source-supported opportunities
-> remove permanently impossible opportunities
-> calculate current profiles, costs, and risk
-> satisfy Commitment/Response-supporting/Adaptive duties where possible
-> fill flexible slots using declared weights
-> produce a seeded, inspectable selection record
```

The exact probabilities remain open. Testing must be able to reproduce why each card
was eligible, why it was selected, and why another was not.

## 5. Physical compatibility instead of action points

Pair-by-pair bans do not scale. All cards instead use the same physical commitment
contract.

Minimum shared facts:

```text
timing
required_sources
occupied_sources
posture_or_commitment
response_compatibility
explicit_override (rare)
```

Approved general rules:

1. One physical source cannot perform incompatible roles in the same exchange.
2. A whole-body or Legs-heavy Charge blocks an ordinary Evade/Dodge response unless
   an explicit exception allows both.
3. A coordinated multi-limb technique is **one Main card** that lists all required
   sources. It is not several free attacks.
4. A Preparation may reserve or commit a source; the preview must show which later
   Main and Response routes it disables.
5. A card that is illegal before commitment cannot be paid or consumed.
6. Document 32 now supplies the default: a locked card canceled before execution loses
   Main tempo, preserves unpaid execution resources, and recomputes Ready, Dormant, or
   Invalid. A card whose atomic execution began pays its costs, becomes Spent, and
   completes. An authored special checkpoint may override only when explicit.
7. An exception must be visible before commitment and pass through the same source,
   cost, consequence, and logging rules.

This creates logical combinations without a growing blacklist such as "Card A cannot
be used with Cards B, C, D...".

## 6. Items in the slot system

Items remain inventory-owned; the brain does not invent them.

For the first paper baseline:

- a usable item opportunity may occupy an Adaptive or flexible Attention Slot;
- an item may not replace the minimum Commitment-capable opportunity by accident;
- inventory state owns remaining uses, disappearance timer, required arms/tools, and
  every other access condition;
- using the card spends its declared Preparation or Main timing unless a later rule
  explicitly marks it Fast;
- item use is deducted only after legal commitment;
- zero uses, expiry, or permanent loss makes the card Invalid;
- inspecting inventory does not make every carried item a freely playable hand card.

A separate quick-item rail is **not approved yet**. It may be compared later if item
cards make the hand unreadable, but it must not bypass the staged turn.

Fast-item limits and which items qualify remain a later item-timing decision.

## 7. Wounded-limb use and special costs

Ordinary limb cards have no generic resource fee. Their main limits are the staged
turn, source legality, current profile, and physical compatibility.

Special cards may explicitly declare one or more of:

- Blood payment;
- item use;
- integrity damage to a named source;
- worsening of the source's dominant wound;
- increased bleeding or a new wound consequence;
- Stamina only after a separate production Stamina decision is approved.

Using a wounded limb does **not** automatically worsen every wound. Self-worsening is
reserved for exertive, desperate, or otherwise authored moves so the system creates a
meaningful risk choice rather than punishing all play from an injured build.

All costs and plausible self-worsening must be previewed before commitment. Exact
Blood loss, wound transitions, integrity values, and Stamina behavior remain blocked
by the wound/Blood/treatment numeric gate.

## 8. Range and reflex integration

- Each card shows its current Clinch, Engaged, or Distant profile first.
- A single card may remain legal at multiple ranges with different accuracy, damage,
  timing, defense pressure, or consequences.
- Range changes are results written into action, defense, and later reflex profiles;
  there is no universal Walk card or freely editable range control.
- Dormant cards explain which state prevents use.
- Reflex events are automatically surfaced only when they are event-eligible and
  physically compatible with the committed sources and posture; they never require a
  persistent Response card.
- The exact reflex interaction families remain deferred as previously ordered.

## 9. Information shown to the player

Every visible card must make the immediate decision readable without requiring the
player to remember hidden rules. Show, in this order:

1. current effect;
2. timing and intent;
3. physical source or item;
4. current range profile;
5. cost and self-risk;
6. uses/expiry for an item;
7. commitments and important blocked responses;
8. why the card is Dormant or Invalid.

Alternate range profiles and rare exception detail may sit behind inspection. The
player should be able to answer: "Why is this card here, what body part performs it,
what will it cost, and what will it stop me from doing?"

## 10. Cognitive progression boundary

This approval activates a **cognitive capacity and selection role**, not a detailed
brain-anatomy feature.

Approved now:

- Attention Slot capacity may progress from three toward five;
- later cognitive effects may bias declared intent categories or selection weights;
- capacity and selection never replace body eligibility or grant extra normal plays.

Still deferred:

- whether the system is literally located in the Head;
- named brain regions;
- replaceable brain anatomy;
- shop, graft, skill, spell, or other upgrade delivery;
- adrenaline, reflex, or offensive brain upgrades;
- exact weights and progression costs.

This preserves the owner's future brain concept without forcing fictional anatomy or
progression content into the current rules gate.

## 11. Enemy symmetry

Players and enemies follow the same source, wound, cost, commitment, item, and range
legality rules. Enemy decision-making may rank opportunities through AI rather than a
player-visible hand, but it may not bypass the physical contract.

Any asymmetric exception must be authored, visible when relevant, and justified by
state or content rather than by the need to preserve a planned scene.

## 12. Evidence and transferable lessons

### Cognitive and motivational research

- Cowan's review argues that working-memory capacity under constrained conditions is
  closer to about four chunks than the older seven-item rule. This supports beginning
  with a small hand and testing expansion; it does **not** prove that three or five
  cards is an optimal game interface. [Cowan 2001, PubMed](https://pubmed.ncbi.nlm.nih.gov/11515286/)
- Hick's choice-reaction experiments connected response time with uncertainty across
  alternative stimuli. The careful transfer is to limit simultaneous comparison and
  clarify card categories, not to predict exact turn time from card count.
  [Hick 1952, Quarterly Journal of Experimental Psychology](https://journals.sagepub.com/doi/10.1080/17470215208416600)
- A meta-analysis of 99 observations found that choice overload depends on choice-set
  complexity, task difficulty, preference uncertainty, and the chooser's goal. More
  options are not automatically harmful; growing the hand is safer when options are
  relevant, categorized, and understandable.
  [Chernev, Bockenholt, and Goodman 2015](https://myscp.onlinelibrary.wiley.com/doi/abs/10.1016/j.jcps.2014.08.002)
- Four studies of video-game play associated perceived autonomy and competence with
  enjoyment and preference. The transferable design target is meaningful, legible
  choice and understandable mastery; the paper does not validate this specific card
  system.
  [Ryan, Rigby, and Przybylski 2006](https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf)
- Kirsh and Maglio showed in *Tetris* that visible actions in the world can simplify
  mental work. The inference for Game att2 is that persistent visible cards, source
  labels, and previews can externalize part of planning; it is not evidence for the
  exact refill rule.
  [Kirsh and Maglio 1994](https://onlinelibrary.wiley.com/doi/abs/10.1207/s15516709cog1804_1)

### Shipped-system lessons

- *Dicey Dungeons* separates six active battle-equipment slots from a larger carried
  inventory. The transferable lesson is a bounded active decision surface, not its
  dice economy or exact count.
  [Official equipment reference](https://wiki.diceydungeons.com/doku.php?id=equipment)
- Mega Crit described a card that returns to the next hand as providing surprisingly
  strong consistency. Persistent cards and additional slots must therefore be treated
  as power and reliability levers, not harmless interface upgrades.
  [Official developer update](https://www.megacrit.com/news/2025-7-16-neowsletter-issue-12/)
- *Into the Breach* publicly frames play around telegraphed enemy attacks that the
  player analyzes and counters. The transferable lesson is to make intent and the
  consequences of a counter legible; Game att2 keeps its own body, wound, reflex, and
  extraction identity.
  [Official game page](https://subsetgames.com/itb.html)
- The developers of *Fights in Tight Spaces* reported that movement risked becoming
  overpowered and used physical-board prototyping. The transferable lesson is to
  paper-test positional value before adding generic movement economy; Game att2 has
  already chosen action-produced range instead.
  [Official Xbox developer article](https://news.xbox.com/en-us/2020/11/12/fights-in-tight-spaces-packs-a-punch/)

These sources provide design ground, not proof of product success. Game att2's final
experience must be established through its own human tests.

## 13. Paper-test requirements before runtime consideration

The first paper model must compare starting three-slot play with developed five-slot
play while keeping the number of voluntary plays unchanged.

Record at minimum:

- whether a legal Main existed in the body pool but was absent from the hand;
- Ready, Dormant, Invalid, Spent, and Reconsidered slot counts;
- time to choose Preparation and Main, without declaring a universal pass/fail time;
- immediate repeated offers and use of Reconsider;
- whether players can explain card source, cost, range profile, and incompatibility;
- whether extra capacity dominates body, item, or repair upgrade choices;
- illegal-combination attempts and the reason for each;
- wounded-limb risk choices;
- deterministic selection trace and seed.

Continue toward a runtime specification only if:

- the hand never lacks a Commitment-capable card when a legal one exists in the
  eligible pool;
- extra slots improve planning without increasing ordinary play count;
- cards never execute from invalid physical sources;
- multi-limb and Charge/Response conflicts resolve through shared tags;
- item expiry and source destruction clear cards predictably;
- players can explain the important decision facts without relying on the designer;
- cognitive capacity is not an obviously universal best upgrade in the tested set.

Revise or stop if the system repeatedly produces dead hands, hidden incompatibilities,
perfect-counter guarantees, dominant capacity progression, immediate refill chains,
or a generic card menu detached from body condition.

## 14. Approval record and remaining decisions

On 2026-08-14 the owner asked Codex to research, optimize, edit, develop, and approve
the system under the owner's recommendations. Codex approves the following as design
direction:

- three starting Attention Slots and five as the normal developed paper baseline;
- sixth slot deferred;
- flexible Commitment/Response-supporting/Adaptive selection duties;
- slot growth expands choice only;
- zero-or-one Preparation, zero-or-one Main, then automatically surfaced eligible
  reflex events;
- persistent unused cards, Decision Refresh, and one Reconsider per round;
- Ready/Dormant/Invalid/Spent lifecycle;
- body-owned eligibility and brain-owned selection;
- shared timing/source/commitment compatibility instead of generic action points;
- one-card treatment of coordinated multi-limb techniques;
- bounded Adaptive/flexible inventory opportunity, with its exact access rule then
  resolved by document 34;
- authored, previewed wounded-limb self-risk;
- player/enemy physical-rule symmetry.

Not approved yet:

- individual cards, characters, items, skills, or spells;
- exact selection weights and repetition damping;
- final slot cap or progression cost after human evidence;
- individual item timing/content and any exception to document 34's default;
- wound-to-Blood, integrity, repair, treatment, and self-risk numbers;
- production Stamina;
- detailed reflex execution;
- final UI or runtime implementation.

The owner approved document 30's WNR-0.1 as the provisional wound-to-Blood, repair,
treatment, and wounded-limb self-risk paper baseline. It uses this approved turn and
hand cadence without rewriting them; exact numbers remain tunable and runtime-gated.

Document 31 later clarifies the response boundary: Attention Slots may surface
strategic preparations that support defense, but the reflex-defense event itself is a
transient build-derived affordance and never a played card.

## 15. Later Package D reconciliation (2026-08-16)

Document 33 formalizes body-owned card capability as Full, Strained, optional
Desperate, Dormant, or Invalid source profiles. The weakest required source governs a
multi-source action; occupied/reserved sources create Dormancy; offline sources create
Invalidity. Decision Refresh and Reconsider select only from the resulting current
eligible pool.

Cards may reference centralized effect packages through sparse apply/resist/cleanse
declarations and may deliver compatible source-owned payloads. They do not own private
effect timing, stacking, or cap rules. Each card also declares one Integrity Echo
sensitivity and may name one collision-only fallback, but at most one Echo modifier
can apply. Echo cannot change slot count, draw duties, Preparation/Main budget, card
legality, or automatic-response availability.

Individual profiles, item timing classes, Fast-item limits, signature overrides, and
the minimum complete paper card set remain the next design gate.

## 16. Later Package A2 reconciliation (2026-08-16)

Document 34 resolves the architecture-level item boundary with Package A2. A usable
owned item or tool is deliberately readied in at most one Adaptive/flexible Attention
Slot during Decision Refresh; it is not randomly injected and the whole inventory is
not freely playable. Reconsider may replace the readied item before inventory
execution, but cannot refresh a Spent inventory slot or create a second item action.

Every activated item uses Preparation or Main timing. At most one voluntary
inventory-origin action executes per actor per round, while approved state-required
actions remain contextual and automatic Reflexive Defence remains outside the hand.
Inventory continues to own uses, expiry, sources, and loss. Multi-source tools use
their weakest required source and cannot substitute tool or grip after lock.

This supersedes the earlier open Fast-item/access boundary at architecture level.
Individual production items, signature timing exceptions, values, runtime, and the
simulator's existing Fast-item sequence remain deferred.

## 17. Later Package C reconciliation (2026-08-17)

Document 35 fixes execution-bound range maintenance within this action budget.
Preparation may enable or improve a later range result but never refreshes Clinch or
Distant by itself. A resolved Main or the final authored spatial result of an
incoming-action/automatic-defense chain may maintain, shift, or release range.
Maintenance grants no extra slot, Preparation, Main, reflex event, or refill. Runtime
and individual production profiles remain deferred.

## 18. Later Package B reconciliation (2026-08-17)

Document 36 assigns authored Control and Blood restoration to Preparation while
repair, Claim, extraction, and default Stabilize use Main. Contextual salvage, graft,
and table procedures create no combat play. The one voluntary inventory-origin action
per round remains binding: an inventory Preparation may be followed by a body Main,
but not by a second inventory Main. Claim and an inventory extraction tool therefore
normally require separate rounds. Runtime remains unchanged.

## 19. Later Package A catastrophic-survival reconciliation (2026-08-19)

Document 37 defines Limb for Life as a forced consequence window, not a card, item,
body-source opportunity, Attention Slot, Preparation, Main, inventory-origin action,
Reply, or Lead effect. The current atomic action completes before the choice. After
sacrifice, later commitments revalidate and may cancel without replacement. Runtime
and card/item content remain unchanged.
