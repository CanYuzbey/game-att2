# Game att2 - Brain and Anatomical Deck Synthesis Proposal v0.2

> **SUPERSEDED RESEARCH PROPOSAL (2026-08-25):** v0.2 embedded the Readied Item
> Card in Attention and then required a neutral Commitment floor to repair the lost
> action capacity. Player-like and adversarial testing rejected that coupling. The
> replacement proposal is `BRAIN_ANATOMICAL_DECK_SYNTHESIS_PROPOSAL_v0_3.md`.

> **CURRENT DISPOSITION:** the later owner-approved synthesis is consolidated in
> `../../docs/DECK_BRAIN_AND_ACTIONS.md`. This file is retained only as research
> provenance and cannot override the living design set.

Status date: 2026-08-22

Status: **OWNER-REVIEW DESIGN PROPOSAL. NOT CURRENT AUTHORITY. NO RUNTIME,
CONFIGURATION, CONTENT, VALUE, UI, ENGINE, OR PRODUCTION APPROVAL.**

This proposal does not supersede the current simulator or any living paper rule.

## 1. Owner correction

The rejected v0.1 draft made a design mistake: it treated the two existing proposals
as ingredients for a third independent system. That weakened the owner's Brain Part
identity and rewrote the item-card boundary.

This revision starts from the owner's system and adds only the valuable responsibilities
that the later active-deck proposal addressed.

Owner foundation retained:

- permanent Brain Parts provide roguelite progression;
- Brain Parts give visible buffs and nerfs;
- Brain Parts are configured into Attention Slots;
- the body generates physical card capability;
- Attention is a small hand, not an action-point system;
- item opportunities remain actual item cards;
- one item card is deliberately readied rather than randomly remembered;
- automatic reflexes and passives remain outside played cards.

Later proposal responsibilities adopted:

- the player deliberately chooses some compatible technique cards;
- ordinary draw operates on a bounded set the player understands;
- Brain benefits and penalties are previewed rather than hidden;
- wounded, incompatible, or unstable body state can matter to a Brain modifier;
- body changes revalidate the deck and current hand.

## 2. Design thesis

> The body writes the unavoidable core of the deck. The player chooses how to train
> that body. Items remain deliberately readied cards. The Brain is a permanent
> roguelite modifier layer that buffs and nerfs the Attention Slots through which the
> player experiences the deck.

Short form:

```text
body authors capability and mandatory identity
-> player authors compatible technique specialization
-> inventory authors deliberately readied item cards
-> draw creates imperfect Attention
-> permanent Brain Parts buff and nerf Attention Slots
-> physical commitment and consequences rewrite the next deck state
```

This is a synthesis, not a compromise between unrelated systems. The Body, Deck,
Items, Attention, and Brain each retain one separate responsibility.

## 3. Ownership structure

| Layer | Owns | Cannot own |
|---|---|---|
| Body | Exact physical sources, innate Body Cards, technique compatibility, and current execution profiles | Technique knowledge, item ownership, or Brain progression |
| Technique knowledge | Learned technique definitions | Current ability to perform them |
| Anatomical Deck | Mandatory Body Core plus player-selected compatible Technique Cards | Waiving source legality or inventory ownership |
| Inventory | Item Card definitions, exact instances, uses, quantity, expiry, and required sources | Ordinary Body/Technique draw probability |
| Attention Slots | Current persistent hand and slot positions | Additional Preparation/Main actions |
| Brain Parts | Permanent run-configured slot buffs/nerfs, access biases, or lifecycle modifiers | Physical capability, free items, or universal extra actions |
| State affordances | Stand, Pass, approved surrender/rescue, and other state-required opportunities | Random deck access or invented ownership |
| Automatic layer | Reflexive Defence, Intercept, and passive effects | Voluntary cards or bonus actions |
| Resolution | Costs, sources, commitment, effects, wounds, Blood, range, items, and capability mutation | Scripted outcomes detached from state |

## 4. Card origins

Every visible opportunity has one primary origin. Origin remains meaningful even when
all voluntary opportunities share a card presentation.

### 4.1 Body Cards

Body Cards are innate actions or preparations authored by exact current body sources.

- Each action-capable body part contributes a small authored **Body Core**.
- Body Core cards are mandatory while that source remains part of the current body.
- The player cannot remove every expression of a functional body part merely to
  optimize deck probability.
- Source damage changes the card's Full/Strained/Desperate profile.
- Permanent source loss immediately Invalidates its dependent cards.
- Grafting or replacing a source changes the Body Core at the next legal reconstruction
  boundary and may immediately change capability during an encounter.

Body Core size and whether every source supplies a card remain test variables. The
purpose is identity, not automatic deck bloat.

### 4.2 Technique Cards

Technique Cards are learned ways of using a compatible body source.

- The player selects a bounded set from currently known and source-compatible
  techniques.
- Each selected instance retains one exact source or declared source set.
- Two compatible arms may create two separately sourced instances of the same
  technique when the content permits it.
- Removing a Technique Card from the active deck does not erase knowledge.
- Losing its source removes current execution capability but does not necessarily
  erase learned knowledge.
- A technique requiring multiple sources must reserve and revalidate all of them.

This is where deckbuilding enters the owner's design. It adds deliberate specialization
without allowing the deck to replace the body.

### 4.3 Item Cards

Items remain Item Cards as in the owner's initial Readied Inventory direction.

- An Item Card always represents one real owned item, stack, tool, or activated piece
  of equipment.
- During Decision Refresh, the player may deliberately ready at most one eligible
  Item Card in one Adaptive/flexible Attention Slot.
- The Item Card is not randomly shuffled into the ordinary Anatomical Deck.
- Looking at inventory does not make every carried item immediately playable.
- The card displays quantity/uses, expiry, required hands/tools, timing, target, cost,
  and disabled reason.
- A Preparation Item Card may be followed by a Body/Technique Main when compatible.
- At most one voluntary inventory-origin action executes per actor per round.
- After an Item Card executes, its slot is Spent for the round and cannot be swapped
  into a second inventory action.
- Exact item/tool/source reservation, weakest-source resolution, pay-on-execution,
  and no-substitution rules remain binding.

Item Cards participate in the card decision surface and deck/loadout preparation, but
real inventory state—not the draw pile—owns their existence.

### 4.4 State and Automatic opportunities

- State-required opportunities are surfaced when their approved state exists. They
  are not random rewards and never invent an item or source.
- Automatic reflexes and passives are not cards, do not occupy Attention Slots, and
  consume no voluntary play.
- Neither category is inserted into the deck to manipulate draw probability.

## 5. Anatomical Deck construction

The active combat structure has three visible zones:

```text
BODY CORE
mandatory cards from current exact body sources

TECHNIQUE SELECTION
player-chosen learned cards compatible with those sources

READIED ITEM
zero or one deliberate Item Card from real inventory
```

The **Anatomical Deck** is Body Core plus Technique Selection. The Readied Item is a
card in the current decision surface but not part of ordinary random draw.

Construction occurs only at an approved maintenance/reconstruction boundary:

```text
inspect current body and known techniques
-> generate mandatory Body Core
-> validate compatible Technique Cards
-> player selects bounded Technique Cards
-> validate deck contract
-> choose zero or one readied Item Card from owned inventory
-> configure unlocked Brain Parts into Attention Slots
```

Mid-encounter body mutation does not open a deck editor. It changes legality:

- lost sources immediately invalidate dependent cards;
- temporary source/range/commitment blocks make them Dormant;
- a newly grafted source may supply an explicitly immediate innate opportunity only
  if the graft procedure says so;
- ordinary deck reconstruction waits for the next approved boundary.

## 6. Recommended first draw model: Persistent Attention Draw

The owner had not finalized drawing. This proposal recommends one first comparison
baseline without treating it as approved final design.

### 6.1 Opening and refill

1. Shuffle or deterministically script the Anatomical Deck using injected RNG.
2. Draw into the ordinary Attention Slots without replacement.
3. Deliberately assign the Readied Item Card to its flexible slot after ordinary draw.
4. Unused Ready or Dormant cards persist.
5. A played card becomes Spent.
6. Spent and Invalid slots refill only at Decision Refresh after all consequences.
7. Permanently invalid cards leave the active draw cycle immediately.
8. No card play, source loss, or item use creates a mid-resolution draw.
9. When the draw pile is empty, a later-approved discard/recycle rule applies; the
   first paper fixture may use a scripted finite sequence instead.
10. **Commitment floor:** if at least one legal Main card exists in the Anatomical
    Deck, opening draw and Decision Refresh must expose at least one legal Main card
    in an ordinary Attention Slot. This is neutral draw safety, not a Brain Part buff,
    and it does not promise a counter, preferred category, or strong card.

This retains the owner's planning-oriented Attention hand while giving the player
ownership of the optional technique portion of the draw pool.

### 6.2 Baseline Reconsider

Restore the owner's earlier delayed Reconsider as the neutral baseline:

- once per round, mark one unused Body/Technique card to leave at the next Decision
  Refresh;
- no immediate replacement;
- no Preparation/Main cost;
- no guarantee of a better card;
- it cannot refresh a Spent slot or create a second Item Card use.

Blood-paid immediate redraw is not a universal baseline. It may return as one explicit
Brain Part buff/nerf or another separately tested rule. This prevents Blood from
becoming a routine charge for repairing an ordinary draw.

### 6.3 Required draw alternatives

Compare Persistent Attention Draw against:

- full-hand redraw at each Decision Refresh;
- strict replace-only-the-card-used;
- the owner's original weighted body-pool selection without active deck construction.

The final drawing system remains open until distribution and human-choice evidence
selects it.

## 7. Brain Parts remain the roguelite system

Brain Parts are rare permanent unlocks. They are configured into Attention Slots at
run start, locked for that run, and survive ordinary death/body loss. They are not
ordinary anatomy, ordinary enemy harvest, or inventory items.

Each Attention Slot may hold at most one Brain Part rule. Every Brain Part has:

```text
trigger and affected Attention Slot
-> eligible card origin/category/source relationship
-> one primary buff
-> one explicit nerf, cost, restriction, or exposure
-> duration and expiry
-> visible pre-commit preview
-> post-resolution evidence
```

The buff/nerf is the Brain Part's identity. Progression gives different ways to shape
play, not merely more slots or removal of early-game inconvenience.

### 7.1 Brain Part families

#### Access Parts

Change one slot's draw likelihood, source/category preference, repetition, retention,
or refresh behavior.

- Their access effect is explicit and inspectable.
- They may bias but do not fabricate or guarantee a perfect counter.
- Their nerf must affect access, coverage, persistence, or another visible tradeoff.
- Hard filters that frequently shade a slot fail review.

#### Execution Parts

Buff a card played from their slot and apply one visible nerf/cost.

- The modifier belongs to the slot, not permanently to the card.
- It cannot bypass source, target, range, commitment, item use, or action budget.
- The nerf may affect Blood, integrity, wound risk, exposure, range consequence,
  future access, or another approved axis.
- Pure generic percentages are allowed only as diagnostic fixtures; production Brain
  Parts should express body/card relationships.

#### Coordination Parts

Use the later proposal's strongest idea as one Brain Part family rather than the new
definition of the entire Brain system.

- They inspect a named visible fact such as a Damaged source, provisional Unstable
  graft, multi-source demand, or incompatible reservation.
- They may Stabilize that relationship or Exploit it for greater benefit and greater
  persistent risk.
- They cannot create a new global instability meter by implication.
- They cannot restore an unusable source or turn hidden randomness into control loss.

#### Inventory Parts

Rare Brain Parts may explicitly modify a Readied Item Card slot.

- They do not invent ownership or uses.
- They do not create a second voluntary inventory action.
- They must name the exact item-card rule affected.

### 7.2 One-primary-lever rule

An ordinary Brain Part modifies exactly one primary lever:

- access;
- execution;
- coordination; or
- item-card behavior.

It does not simultaneously improve draw odds, card power, slot retention, and action
economy. A rare exception requires a separately reviewed compound drawback and must
still grant no ordinary extra action by implication.

### 7.3 Capacity boundary

More Attention Slots mean more options and consistency, not more actions. Slot-capacity
growth remains a dangerous progression lever because it may dominate every body,
technique, item, and Brain Part choice. The first comparison holds capacity fixed.

## 8. Body, deck, Brain, and item interaction

The complete player-authorship chain is:

```text
BODY CHOICE
What can this assembled body physically do?

TECHNIQUE CHOICE
Which compatible learned methods do I deliberately prepare?

ITEM CHOICE
Which real owned tool or consumable do I ready as a card?

BRAIN CHOICE
Which permanent slot buffs/nerfs shape access or execution this run?

ATTENTION DRAW
Which prepared Body/Technique opportunities are available now?

COMMITMENT
Which source, target, cost, item, and risk do I lock?

CONSEQUENCE
How does using or losing the body rewrite later cards and choices?
```

No two layers answer the same question. If testing shows that two layers collapse into
the same decision, one must be removed rather than defended through more explanation.

## 9. Causal resolution

```text
current body, knowledge, deck, inventory, Brain configuration, and state
-> generate mandatory Body Core and validate selected Technique Cards
-> create the current source-valid draw pool
-> draw Body/Technique Cards into Attention Slots
-> deliberately ready zero or one owned Item Card
-> apply each slot's one Brain Part buff/nerf contract
-> expose origin, exact source, target, timing, effect, cost, uses, buff, and nerf
-> take zero/one Preparation and lock zero/one Main
-> revalidate card, exact source/item, target, range, cost, and commitment
-> pay when execution begins and mark the slot lifecycle
-> resolve automatic defence and physical/reflex execution
-> mutate integrity, wound, Blood, range, posture, inventory, and card state
-> recompute source capability, deck legality, Brain conditions, and affordances
-> evaluate forced and motivation-supported encounter consequences
-> refill only at Decision Refresh
-> emit structured evidence
```

## 10. Roguelite progression contract

The Brain remains the primary confirmed permanent roguelite progression layer.

| Progression | Proposed role | Guardrail |
|---|---|---|
| Brain Part unlock | Add a new paired buff/nerf configuration option | Must change playstyle, not merely erase frustration |
| Brain configuration | Assign unlocked Parts to Attention Slots before a run | Locked during the run; no perfect-hand guarantee |
| Attention capacity | Rare consistency progression | Fixed during first tests; reject if universally dominant |
| Technique knowledge | Possible learned repertoire | Persistence and acquisition remain deferred |
| Body | Main within-run physical build | Must continue to change capability more than Brain percentages |
| Items | Consumable/tool decisions inside a run | Ownership, uses, and loss remain real |

Permanent Brain Parts may be obtained from later-authored boss, side-mission, or other
non-ordinary-enemy rewards, but exact content and acquisition remain deferred. The
system does not imply that ordinary brains are harvested as Brain Parts.

## 11. Example-only Brain Part grammar

These demonstrate structure, not approved content or values.

| Family | Example buff | Example nerf |
|---|---|---|
| Access | Slot favours exact Arm-source cards | Other source families appear less often in that slot |
| Execution | Card from this slot gains stronger authored effect | Its exact source gains declared wound/exposure pressure |
| Coordination | Contested graft action retains its normal control profile | It loses the possible exploit bonus or pays a future-access cost |
| Exploit | Contested graft action gains a stronger effect | Previewed Blood, wound, integration, or future-card consequence increases |
| Retention | One matching unused card persists through a refresh | The slot refills more slowly after that card is spent |
| Inventory | Readied tool gains one authored handling benefit | It occupies/reserves an additional exact source or raises its cost |

Reject an example if it could be moved unchanged into a generic deckbuilder without
reference to a body source, item, wound, graft, commitment, or Attention Slot.

## 12. Requirements

| ID | Proposal requirement |
|---|---|
| BAD-001 | Every voluntary card has exactly one origin: Body, Technique, or Inventory. |
| BAD-002 | Every Body or Technique Card declares one exact physical source or source set. |
| BAD-003 | The current body generates a mandatory bounded Body Core. |
| BAD-004 | The player selects a bounded active Technique set only from known and source-compatible cards. |
| BAD-005 | Body Core plus selected Technique Cards form the Anatomical Deck. |
| BAD-006 | Item Cards remain inventory-owned and are deliberately readied rather than randomly drawn. |
| BAD-007 | At most one Item Card occupies one flexible Attention Slot and at most one voluntary inventory action executes per round. |
| BAD-008 | Item Card uses, expiry, sources, costs, and loss come from the exact inventory state. |
| BAD-009 | Attention Slots provide persistent options, not additional Preparation/Main actions. |
| BAD-010 | Persistent Attention Draw is the first comparison baseline, not final approval. |
| BAD-011 | Unused valid cards persist; Spent and Invalid slots refill only at Decision Refresh. |
| BAD-012 | Reconsider is delayed and free in the neutral baseline; immediate Blood redraw requires a specific tested rule. |
| BAD-013 | Brain Parts are permanent unlocks configured into Attention Slots and locked for the run. |
| BAD-014 | Every Brain Part declares one buff and one visible nerf/cost/restriction. |
| BAD-015 | An ordinary Brain Part modifies only one primary lever. |
| BAD-016 | Brain Parts never fabricate capability, ownership, item uses, reflexes, or extra ordinary actions. |
| BAD-017 | Slot-local modifiers remain with the slot and do not permanently alter card instances. |
| BAD-018 | Coordination Parts derive from named current body/source facts and add no hidden global instability meter. |
| BAD-019 | Automatic defence and passives remain outside the deck, Attention Slots, and voluntary play budget. |
| BAD-020 | State-required actions surface only from approved state and never invent sources/items. |
| BAD-021 | Source loss immediately removes dependent capability and revalidates deck/hand state. |
| BAD-022 | Player and enemy implementations share source, item, commitment, and lifecycle legality without requiring identical UI. |
| BAD-023 | No proposal rule changes simulator source, configuration, scenarios, values, or current runtime behavior. |
| BAD-024 | Human evidence is required for fun, comprehension, balance, fairness, accessibility, and replay claims. |
| BAD-025 | Opening draw and Decision Refresh enforce the neutral Commitment floor whenever at least one legal Main card remains in the Anatomical Deck. |

## 13. Brutal three-system comparison

The comparison uses these definitions:

- **Owner original:** body-generated pool; Brain-weighted Attention; permanent Brain
  Parts with buffs/nerfs; deliberately readied Item Card; no active Technique deck.
- **Later active-deck model:** player-authored compatible active deck; ordinary draw;
  Brain interprets/modifies hand/body relationships; items outside ordinary hand.
- **v0.2 synthesis:** mandatory Body Core plus chosen Technique Cards; persistent draw;
  deliberately readied Item Card; permanent Brain Parts with paired buffs/nerfs.

| Aspect | Owner original | Later active-deck model | v0.2 synthesis | Brutal result |
|---|---|---|---|---|
| Body-as-build purity | Excellent | Good but vulnerable to eligibility-key drift | Very good | Original remains purest. |
| Player deck authorship | Weak/indirect | Excellent | Very good | Synthesis adds agency without full detachment. |
| Brain identity | Excellent: attention plus progression | Unclear: may become generic hand interpreter | Excellent: permanent paired slot modifiers | Synthesis preserves the owner's strongest differentiator. |
| Roguelite progression | Clear and strong | Delivery form unresolved | Clear and strong | Original and synthesis win. |
| Item-card identity | Strong under initial A2 | Weak: items sit outside the hand | Strong | Synthesis restores the owner's item design. |
| Draw fairness | Risky weighted droughts | Understandable deck-owned variance | Understandable but still imperfect | Later model is cleanest; synthesis is acceptable only with bounded Body Core. |
| Readability | Weight/filter heavy | Clearest conventional model | Harder: body, technique, item, Brain, slot | Later model wins. Synthesis has a real teaching burden. |
| Originality | Highest systemic purity | Lowest; closer to familiar deckbuilders | High | Synthesis is more original than later model, less elegant than original. |
| Build expression | Body plus Brain | Body plus deck plus modifiers | Body plus technique choice plus Brain plus item readiness | Synthesis has highest potential and highest menu-risk. |
| Blood integration | Strong but redraw can become a tax | Underdefined | Optional Brain-specific tradeoff | Synthesis improves intent but is not yet proven. |
| Balance burden | High probability tuning | High card/modifier tuning | Very high: mandatory cards, selected cards, items, draw, slot buffs/nerfs | Synthesis is hardest to balance. |
| Content burden | Moderate/high | High | Highest | Synthesis can collapse under content production cost. |
| Prototype readiness | Most specified | Doctrine is underspecified | Structurally specified, numerically open | Original is still fastest to test. |
| Long-term play potential | Variance may frustrate | Strong agency but generic-deck risk | Highest potential if layers remain distinct | Synthesis is not automatically best; it must earn its complexity. |

### 13.1 Where the owner original is still better

- It is more elegant: body plus Brain, with fewer overlapping build layers.
- It expresses the Brain-as-attention fantasy more directly.
- It is cheaper to prototype and explain internally.
- Every graft automatically matters to the opportunity pool.

It loses when weighted access repeatedly withholds useful options or when permanent
progression mainly buys relief from unreliable early hands.

### 13.2 Where the later active-deck model is still better

- Players understand why cards are present because they chose the deck.
- It gives the cleanest ownership of tactical identity.
- It avoids hidden Brain steering and makes balance easier to discuss.
- It is familiar enough that onboarding may be easier.

It loses when the active deck becomes the real build, items become menu buttons, and
the Brain becomes a generic modifier layer that could belong to another deckbuilder.

### 13.3 Where v0.2 may be better

- Body changes remain unavoidable because Body Core cannot be optimized away.
- Technique selection adds authorship without deleting anatomical identity.
- Item Cards remain visible tactical commitments rather than free inventory access.
- Brain Parts retain permanent roguelite meaning, buff/nerf identity, and slot logic.
- Coordination/instability becomes one possible Brain family rather than replacing
  the entire system.
- The player authors body, techniques, item readiness, and Brain configuration through
  clearly different decisions.

### 13.4 Where v0.2 may be worse than both

This is the crucial risk: v0.2 can become **system soup**.

The player may need to understand:

1. mandatory Body Core cards;
2. selected Technique Cards;
3. draw/discard/persistence;
4. Readied Item Cards;
5. Brain Part slot buffs/nerfs;
6. body-source profiles and commitments;
7. Preparation/Main/reflex timing.

If all seven demand attention simultaneously, the synthesis is worse than both
parents. It will be original but exhausting. More systems do not equal more depth.

The other major danger is Brain double-dipping. A Brain Part that improves draw odds
and execution power makes Brain progression more important than grafting. The
one-primary-lever rule is therefore an acceptance requirement, not polish.

## 14. Verdict

### Design-potential verdict

v0.2 has the best **potential fit** for Game att2 because it preserves:

- the owner's distinctive Brain Parts;
- the owner's item-card contract;
- body-authored physical identity;
- the later model's player deck authorship and visible modifier consequences.

### Current-maturity verdict

v0.2 is **not currently proven to be the best system**.

- The owner original is simpler, purer, and more prototype-ready.
- The later model is clearer and easier for conventional deckbuilder players.
- v0.2 is the most complex, most expensive, and easiest to overdesign.

It becomes the best only if one bounded fixture proves that players can explain all
four authorship decisions—Body, Technique, Item, Brain—without treating any as
redundant administration.

### Automated structural evidence, 2026-08-22

An isolated deterministic research fixture ran 5,000 six-round sessions per
configuration across 18 configurations (540,000 observed rounds total). It used
neutral diagnostic records, not production cards or balance values.

- Without the Commitment floor, balanced v0.2 produced Main droughts in 26.03% of
  rounds at three total Attention Slots and 10.34% at four. After Right Arm source
  loss, those rates rose to 39.15% and 18.27%. That version is rejected.
- With the Commitment floor, Main drought, dead-hand, illegal-action, and action-budget
  violation rates were all 0% in the tested three-, four-, and five-slot fixtures.
- The guarantee did not prove rich choice. At four slots, v0.2 exposed both a
  Preparation and Main card in only 46.38% of rounds, versus 83.02% for the owner
  original and 100% for the balanced later active-deck fixture.
- Mandatory Body Core prevented a defensive Technique package from becoming inert:
  the later defensive active deck had 64.38% Main drought, while v0.2 with the floor
  had 0%. The later system therefore also needs deck-composition constraints.
- The Readied Item Card remained separate from random draw, obeyed its exact source,
  and produced no action-budget violation in the fixture.
- A +60%/-35% Access weighting fixture changed actual synthesis draw share modestly:
  attack 35.58% to 36.34%, defence 32.11% to 29.76%. The draw cycle and Commitment
  floor correctly damped Brain dominance, but human perception is unknown.
- A symmetric +0.25/-0.25 Execution fixture was net +0.25 when the nerf was ignored,
  +0.125 when half-valued, and neutral only when fully valued. A written paired nerf
  is therefore not balance evidence; its consequence must be unavoidable or
  decision-changing.

The evidence changes the recommendation from “test Commitment” to “Commitment is a
required neutral baseline.” It does **not** approve slot count, production values,
fun, comprehension, long-term playfulness, or implementation. Four total slots are
the strongest next human-test candidate: three is tactically narrow, while five may
buy consistency through raw capacity.

## 15. Bounded comparison fixture

Use identical content/state across all three systems:

- the same body with at least two usable action sources;
- one Damaged or provisionally Unstable source;
- the same six Body Cards;
- the same four optional Technique Cards;
- the same two owned Item Cards, with one readied;
- the same two Brain Part buff/nerf fixtures;
- the same enemy intent sequence;
- the same source-loss event;
- the same six Decision Refreshes;
- one normal and one dangerous Blood state.

Test these conditions:

| Condition | Owner original | Later model | v0.2 |
|---|---|---|---|
| Authorship | Body/Brain configuration | Active-deck construction | Body Core + Technique + Item + Brain configuration |
| Draw | Weighted Attention | Ordinary deck draw | Persistent Attention Draw |
| Brain | Access weights plus slot modifier | Deterministic hand/body modifier | Paired slot buff/nerf; one primary lever |
| Items | Readied Item Card | Direct inventory | Readied Item Card |

Record:

- explanation accuracy for why each card exists, appeared, and changed;
- meaningful choices per refresh versus administrative operations;
- non-functional/drought hand frequency;
- Body Core share of the hand and whether it crowds out technique authorship;
- Technique selection impact versus graft/body impact;
- Item Card use, readiness errors, and action stacking attempts;
- Brain Part influence versus body influence;
- cases where the Brain buff is automatic and the nerf irrelevant;
- source invalidation and capability-recomputation accuracy;
- which system players describe as body-building, deck-building, or menu management;
- decision time and unaided recall of the action budget.

## 16. Continue, revise, and kill criteria

### Continue v0.2 if

- players can explain Body, Technique, Item, and Brain ownership after one short
  teaching pass;
- changing the body alters more legal capability than changing one Brain Part;
- selected Technique Cards materially change play without making Body Core feel like
  deck tax;
- Item Cards feel deliberately prepared rather than forgotten inventory;
- Brain buffs create attractive builds and Brain nerfs change real decisions;
- persistent draw produces adaptation without routine dead hands;
- the synthesis produces more meaningful decisions, not merely more setup actions.

### Revise v0.2 if

- players repeatedly confuse Body Cards and Technique Cards;
- the same Technique package is optimal for every compatible body;
- Brain Parts are chosen only for their buff while the nerf is ignored;
- Item Card readiness always selects the same healing option;
- mandatory Body Core exceeds a healthy share of the deck;
- Reconsider is required every round;
- deck editing after body changes becomes repetitive administration.

### Kill v0.2 if

- the deck determines identity more than the body;
- Brain progression dominates body progression;
- the system needs separate tutorials for every layer before one encounter is
  playable;
- removing any one of Body Core, Technique selection, Item readiness, or Brain Parts
  changes little;
- item cards require free inventory access to remain usable;
- the only way to balance Brain buffs is through invisible or irrelevant nerfs;
- players describe the core experience primarily as maintaining menus.

## 17. Hostile review

| Risk | Severity | Required safeguard |
|---|---|---|
| Synthesis becomes system soup | P1 | Count player-facing decisions and remove any layer that does not change the fixture. |
| Brain double-dips into access and power | P1 | Enforce one primary lever per ordinary Brain Part. |
| Body Core becomes mandatory deck garbage | P1 | Keep it bounded; test card share and usefulness after damage. |
| Technique selection makes the body an eligibility key | P1 | Compare capability change from grafting versus deck edits. |
| Brain nerfs become cosmetic | P1 | Require a decision-changing cost/restriction and record ignored nerfs. |
| Weighted Access Parts recreate original frustration | P1 | Make their bias explicit; measure droughts and shaded slots; reject hard filters that strand play. |
| Item Card readiness feels like artificial forgetting | P1 | Preserve deliberate physical-readiness fiction and test explanation. |
| Readied items create action stacking | P0 | One voluntary inventory-origin action per round; no Spent refresh. |
| Persistent draw traps obsolete plans | P1 | Delayed Reconsider plus lifecycle comparison; no automatic Blood tax. |
| Raw slot growth dominates all progression | P1 | Hold capacity fixed until other progression is tested. |
| Coordination family becomes a universal instability system | P1 | Require named body facts and keep it one optional Brain family. |
| Source loss leaves illegal cards executable | P0 | Immediate capability invalidation and pre-lock/pre-execution revalidation. |
| Automatic reflex returns as a card | P0 | Keep automatic origin outside deck, Attention, and voluntary play. |
| Proposal silently changes runtime | P0 | Documentation-only owner-review status; no source/config/test/value changes. |

No implementation or production gate is opened by this proposal.

## 18. Explicit deferrals

- exact Body Core contribution per source;
- Technique selection size, duplicates, acquisition, mastery, and persistence;
- Attention Slot count and capacity progression;
- shuffle, discard, recycle, exhaustion, and encounter-to-encounter draw state;
- final selection between Persistent Attention, full redraw, and strict used-card
  replacement;
- Reconsider cadence and any Brain-specific Blood redraw;
- Brain Part content, values, rarity, acquisition, Head relationship, and compound
  exceptions;
- Item Card capacity, content, timing exceptions, and final readiness presentation;
- enemy deck/Attention implementation and special Brain behavior;
- run, death, checkpoint, body, knowledge, deck, and item persistence;
- UI, accessibility, animation, audio, telemetry, runtime, configuration, save data,
  engine, market, and product claims.

## 19. Owner decision gate

The proposal recommends v0.2 as the third fixture, not as current authority. The next
owner decision is whether this structure correctly preserves the original Brain and
Item Card identity before exact counts, values, content, or runtime work begins.
