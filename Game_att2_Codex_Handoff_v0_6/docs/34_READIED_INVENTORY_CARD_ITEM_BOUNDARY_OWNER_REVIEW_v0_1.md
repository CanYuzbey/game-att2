# Game att2 - Readied Inventory Card/Item Boundary Owner Review v0.1

Status date: 2026-08-16

Status: **Package A2 - Readied Inventory Attention Slot is owner-approved as paper
design authority. Runtime, configuration, individual production cards/items, final
timing values, balance, UI, and human-experience claims remain unapproved.**

## 1. Decision and authority boundary

Package A2 resolves the remaining architecture-level card and item boundary. It
replaces random inventory injection from the earlier Package A recommendation with a
deliberately readied inventory opportunity:

> An owned item or tool is not randomly remembered by the brain and is not freely
> playable from the whole inventory. The actor deliberately readies at most one
> eligible inventory opportunity in one Adaptive or flexible Attention Slot. That
> opportunity uses the existing Preparation/Main budget and the real item's sources,
> uses, expiry, and other access conditions.

This is a bounded amendment to documents 29 through 33. It does not create a new
deck, action point, free Quick Item rail, universal equipment system, runtime item,
or production card catalogue.

The existing simulator continues to use Focus plus at most one Fast item before the
Main action. Package A2 is later paper authority only and does not silently replace
that implemented behavior.

**Runtime remains unchanged.**

## 2. Canonical opportunity origins

Every combat opportunity has exactly one primary origin.

| Origin | Meaning | Attention Slot handling | Existing examples |
|---|---|---|---|
| Body | A body source authors the action or preparation. | Selected from the current source-supported pool. | Focus, Grip Strike, Guard Flesh, Brace |
| Inventory | A real owned item, stack, or tool authors an activated use. | At most one is deliberately readied in an Adaptive/flexible slot. | Blood Bag, Clotting Cream, Claim the Cut, Bone Scissors, Hell Saw |
| State | An approved current state requires or exposes an affordance. | Guaranteed into the appropriate existing slot duty when required; never randomized and never a bonus slot. | Stand, approved Ruined-Torso rescue, Pass, approved surrender |
| Automatic | An incoming event and current build derive a response or passive result. | Never a played card and never occupies an Attention Slot. | Reflexive Defence, automatic Intercept, passive protection |

An opportunity cannot change origin to bypass its restrictions. A carried item does
not become a body card; an activated equipment ability does not become passive; an
automatic event does not become an extra voluntary play.

## 3. Shared timing and voluntary action budget

Each actor retains the approved round budget:

- zero or one Preparation;
- zero or one Main;
- automatic eligible events inside resolution, never additional plays.

Every activated inventory opportunity declares **Preparation** or **Main** timing.
The future paper default for an item previously described as `Fast` is Preparation.
There is no separate free Fast-item window in Package A2.

Individual production items may later request a visible signature exception, but no
exception is approved by this package. Current runtime Fast-item rules remain
unchanged until a separately approved implementation plan reconciles them.

## 4. Readied Inventory Attention Slot

### 4.1 Deliberate readiness

During Decision Refresh, after current ownership and legality inputs are known, the
actor may deliberately assign one eligible owned item or tool to one Adaptive or
otherwise flexible Attention Slot.

- The selection is intentional, not random.
- The item remains inventory-owned; the slot contains only its current opportunity.
- No more than one inventory-origin opportunity may be readied at a time.
- The minimum Commitment-capable body opportunity cannot be replaced accidentally.
- If no item is readied, the slot follows the normal source-supported selection rules.
- Looking at the inventory does not make unready items playable.

"Readied" represents immediate physical and tactical access: held, opened, placed,
gripped, or otherwise prepared for the present exchange. It is not a claim that the
actor forgot every other carried object.

### 4.2 Persistence

An unused readied opportunity persists under document 29's normal lifecycle. It does
not reroll merely because another slot was used.

It leaves the slot when:

- it executes and becomes Spent;
- Reconsider legally replaces it before use;
- the item reaches zero uses, expires, is destroyed, or is permanently lost and the
  opportunity becomes Invalid;
- a later approved rule explicitly removes it.

Temporary source, grip, posture, or range failure makes the opportunity Dormant when
future restoration remains possible. Permanent loss of the item or every required
source makes it Invalid.

### 4.3 One voluntary inventory action per round

When an inventory-origin action begins execution, its slot becomes Spent for the
remainder of the round. It cannot be restored, exchanged, or refilled until the next
Decision Refresh.

Therefore:

- a Preparation item may be followed by a body-sourced Main;
- a body Preparation such as Focus may be followed by a readied Main tool;
- a Preparation item cannot normally be followed by a second inventory-origin Main;
- increasing Attention Slot capacity never increases the one-inventory-action limit.

This preserves reliable item access without creating item chains or a third action
economy.

## 5. Reconsider and inventory switching

The existing once-per-round Reconsider may replace the currently readied inventory
opportunity with another eligible owned item or tool when all of the following hold:

1. no inventory-origin action has begun execution this round;
2. the destination is the same Adaptive/flexible slot;
3. the replacement item is currently owned and eligible to be readied;
4. no locked commitment reserves either item or its required sources;
5. Reconsider has not already been used this round.

Reconsider does not:

- generate an item;
- restore a consumed use;
- refresh a Spent inventory slot;
- provide a second inventory action;
- waive source, range, posture, target, or cost rules;
- alter a locked Main after its result is known.

If Reconsider is routinely spent only to access inventory, that is evidence to revise
the readiness rule rather than proof that the tax is desirable.

## 6. Ownership, stacks, uses, expiry, and cost timing

Inventory state owns:

- definition and instance identity;
- current quantity or remaining uses;
- expiry or disappearance state;
- required tools, hands, and other sources;
- equip/readiness restrictions;
- legal targets and range;
- costs and effect payloads.

One stack or multi-use item produces one visible opportunity showing its current
quantity/uses. The system does not create one duplicate card per unit unless a later
content definition explicitly requires separate instances.

Ordinary item uses and execution-time costs are deducted only when legal execution
begins, following document 32. A locked Main canceled before execution loses its Main
tempo but preserves unpaid execution resources and item uses. An explicit protective
state activated on lock may retain its declared on-lock cost even if later execution
is canceled.

After an item action executes:

- zero remaining uses makes it Invalid and removes it from the future eligible pool;
- remaining uses allow it to re-enter the eligible inventory pool at the next
  Decision Refresh;
- expiry or destruction is applied from the real inventory state, not card text
  alone.

## 7. Tools, equipment, and multiple sources

Every activated tool or equipment action declares:

- the exact item or tool instance;
- required body sources;
- occupied or reserved sources;
- Full/Strained/Desperate profiles where applicable;
- Clinch/Engaged/Distant profiles;
- timing and commitment type;
- Blood, integrity, wound, item-use, or other approved costs;
- effect payload and delivery conditions;
- current uses/expiry;
- one Integrity Echo sensitivity and optional collision-only fallback under document
  33.

The weakest required source governs a multi-source tool action. The locked action
reserves its exact tool, sources, target, and current authored profile. It cannot
silently regrip, change hands, substitute another copy, or choose a different tool
after seeing the earlier result.

A passive item or equipment effect does not need an Attention Slot and is not a
played card. If the same equipment also has an activated ability, that activated use
must be readied through the inventory slot. Passive ownership never grants free use
of the activated component.

## 8. State-required and automatic boundaries

Approved state-required actions are contextual affordances, not random hand offers.
This package recognizes only already approved categories such as Stand, Ruined-Torso
rescue, Pass, and approved surrender. It creates no new survival, anatomy, treatment,
or encounter-resolution rule.

A required affordance occupies the appropriate existing Attention Slot duty and its
declared Preparation/Main timing. It displaces an ordinary offer where necessary; it
does not create a bonus slot or play.

When a state-required rescue accepts an item input:

- only actually owned qualifying items are shown;
- remaining uses, costs, source requirements, and timing still apply;
- absence of a legal item remains a real failure state;
- the rescue never creates a bonus voluntary action;
- activating or consuming an item still counts as the round's inventory-origin action
  even though the current state guaranteed that rescue opportunity was surfaced.

Automatic Reflexive Defence, Intercept, and compatible passives remain derived inside
incoming-action resolution. They consume no Attention Slot, Preparation, Main, or
inventory action. An active preparation may improve or enable their route, but the
automatic event itself is never played.

## 9. Shared card/opportunity definition and signature overrides

The paper definition schema is:

```text
opportunity_id
origin: body | inventory | state | automatic
timing: preparation | main | contextual | automatic
definition_source
required_sources
occupied_sources
item_instance_or_stack
uses_and_expiry
full_profile
strained_profile
desperate_profile_or_none
range_profiles
cost_timing: on_lock | on_execution
costs
effect_package_declarations
source_payloads
integrity_echo_sensitivity
collision_fallback_or_none
lifecycle_result
disabled_reason
signature_override_or_none
```

A card/action may name at most one signature override. The override must state:

1. the exact shared rule being overridden;
2. the authored reason;
3. the visible pre-commitment preview;
4. the dedicated paper case and eventual deterministic negative test.

An override cannot waive ownership, source legality, timing budget, commitment,
effect delivery, causal order, evidence, or the distinction between voluntary and
automatic actions.

## 10. Information contract

The immediate preview shows only current and decision-relevant information:

1. name and origin;
2. Preparation, Main, contextual, or automatic timing;
3. physical/item source;
4. current Full/Strained/Desperate profile;
5. current range profile and target;
6. occupied/reserved sources;
7. Blood, integrity, wound, and item-use costs with their timing;
8. remaining uses/quantity and expiry;
9. delivered effect package/payload;
10. relevant Integrity Echo consequence;
11. why Dormant or Invalid;
12. any signature override.

The interface must distinguish **owned**, **readied**, **Dormant**, **Invalid**, and
**Spent**. It must not imply that every inspected item is currently actionable.

## 11. Complete causal order

```text
prior body, inventory, state, range, Lead, and slot facts
-> enumerate body-, inventory-, state-, and automatic-origin opportunities
-> derive required sources and Full/Strained/Desperate/Dormant/Invalid profiles
-> run ordinary Attention Slot selection
-> deliberately assign zero or one eligible inventory opportunity to a flexible slot
-> expose current timing, target, cost, uses, effect, and disabled reasons
-> optionally use Reconsider before inventory execution or incompatible lock
-> take Preparation and lock Main under documents 29 and 32
-> revalidate exact item, sources, target, range, costs, and opportunity
-> if legal, pay execution-time cost/use and mark inventory slot Spent
-> resolve the atomic action and any compatible automatic response
-> apply effect, body, Blood, wound, range, posture, and inventory mutations
-> recompute source capability, ownership, uses, lifecycle, and state affordances
-> record structured evidence
-> refill Spent/Invalid slots only at the next Decision Refresh
```

No stage may invent ownership, restore a used item, substitute a locked source, or
promote an automatic event into a voluntary play.

## 12. Minimum bounded paper fixture

The first paper fixture uses existing approved content names only.

| Boundary exercised | Existing content or neutral fixture | Content status |
|---|---|---|
| Body Preparation | Focus | Existing simulator content; paper timing remains future authority. |
| Body Main | Grip Strike | Existing simulator content. |
| Prepared defense Main | Guard Flesh | Existing simulator content; document 31 paper behavior remains runtime-gated. |
| Posture/state Main | Brace and Stand | Existing simulator content. |
| Inventory Preparation | Blood Bag and Clotting Cream | Existing simulator items; A2 timing is paper-only. |
| Inventory Main | Claim the Cut | Existing simulator item. |
| Main tools | Bone Scissors and Hell Saw | Existing simulator tools. |
| Automatic boundary | Cover It and automatic Intercept | Paper fixture only; active production behavior remains gated. |
| Treatment/repair vocabulary | Control, Stabilize, Field Repair | Neutral WNR paper fixtures only; not production content. |

A neutral multi-source tool or three-range profile may be added only as a diagnostic
record, not as a named production card/item. Poison and Burn remain document 33
architecture fixtures and are not admitted into this card set.

## 13. Paper acceptance cases

| Case | Required result |
|---:|---|
| 01 | Decision Refresh deliberately reads one eligible owned item; no random item injection occurs. |
| 02 | Reading an item never removes the minimum Commitment-capable body opportunity. |
| 03 | Declining to read an item returns the flexible slot to normal selection. |
| 04 | A Preparation item executes, spends the inventory slot, and permits a body Main. |
| 05 | The same round cannot produce a second voluntary inventory-origin Main. |
| 06 | Focus may precede a readied Main tool when all sources remain legal. |
| 07 | Reconsider swaps the readied item before inventory execution. |
| 08 | Reconsider cannot refill a Spent inventory slot or produce a second inventory action. |
| 09 | Inspecting an unready owned item does not make it playable. |
| 10 | Temporary grip/source/range loss makes the readied opportunity Dormant with reason. |
| 11 | Zero uses, expiry, destruction, or permanent item loss makes it Invalid. |
| 12 | A locked inventory Main canceled before execution preserves its unpaid use. |
| 13 | An explicitly activated on-lock protective state retains its declared on-lock cost. |
| 14 | Passive equipment applies without a card; its activated use still requires readiness. |
| 15 | A multi-source tool uses its weakest required source profile. |
| 16 | Source or tool loss before execution cancels the same locked action without substitution. |
| 17 | A contextual rescue occupies the appropriate existing slot duty and shows only legal qualifying owned item inputs. |
| 18 | Missing ownership or legal sources can make rescue unavailable; the system invents nothing. |
| 19 | Reflexive Defence appears automatically and consumes no slot or voluntary play. |
| 20 | Player and enemy inventory opportunities follow the same ownership/readiness contract. |
| 21 | Seeded or scripted randomness, if later used, explains every selection and result. |
| 22 | Neutral diagnostics cannot enter the production catalogue through fixture use. |

## 14. Requirements and future traceability

| Requirement | Paper contract | Future verification |
|---|---|---|
| CIB-A2-001 | Every opportunity has one declared origin. | Reject missing or multiple primary origins. |
| CIB-A2-002 | One item/tool may be deliberately readied in one flexible slot. | Refresh fixture and selection trace. |
| CIB-A2-003 | Inventory injection is never random. | Seeded negative selection tests. |
| CIB-A2-004 | Minimum Commitment-capable body access is protected. | Body/inventory competition cases. |
| CIB-A2-005 | Inventory uses Preparation or Main; no free Fast rail exists. | Timing-budget assertions. |
| CIB-A2-006 | At most one voluntary inventory action executes per round. | Preparation-to-Main chain negative tests. |
| CIB-A2-007 | Reconsider swaps before use but never refreshes Spent inventory. | Lifecycle/state-machine tests. |
| CIB-A2-008 | Inventory owns uses, expiry, and item legality. | Depletion/expiry/destruction tests. |
| CIB-A2-009 | Execution-time uses are paid only when execution begins. | Canceled-lock tests. |
| CIB-A2-010 | On-lock costs require an explicit activated state. | Retained-cost and rejection tests. |
| CIB-A2-011 | Temporary blocks are Dormant; permanent loss is Invalid. | Source/range/item-loss matrix. |
| CIB-A2-012 | Multi-source tools use the weakest required source. | Mixed-source profile cases. |
| CIB-A2-013 | Locked tools/sources cannot be substituted. | Pre-execution loss tests. |
| CIB-A2-014 | Passive equipment is automatic; activated use requires readiness. | Passive/active boundary tests. |
| CIB-A2-015 | State-required actions are guaranteed into an existing duty, owned, and not random or bonus slots. | Stand/rescue/pass fixtures. |
| CIB-A2-016 | Automatic defense consumes no slot or voluntary play. | Incoming-action defense cases. |
| CIB-A2-017 | A definition may contain at most one governed signature override. | Schema validation and dedicated negative test. |
| CIB-A2-018 | Current preview exposes origin, readiness, timing, sources, uses, costs, and disabled reason. | Information-contract review. |
| CIB-A2-019 | Player and enemy use the same readiness/ownership rules. | Symmetric actor fixtures. |
| CIB-A2-020 | Current simulator Fast-item behavior remains unchanged until implementation approval. | Diff/scope audit. |
| CIB-A2-021 | Paper fixtures do not approve production content. | Catalogue and runtime negative audit. |

## 15. Comparable-system evidence and limits

Sources below were checked on 2026-08-16.

- *Slay the Spire* separates cards, relics, and potions. The transferable lesson is
  clear origin and presentation; Package A2 does not copy a free potion rail.
  [Mega Crit press kit](https://www.megacrit.com/press-kits/slay-the-spire/)
- *Wildfrost* places elemental items in its card economy while Counters/Reactions
  trigger automatically. The transferable lesson is shared play pressure plus an
  explicit automatic layer; Package A2 avoids random access to essential owned items.
  [Wildfrost press kit](https://www.wildfrostgame.com/presskit/)
  [Wildfrost Counter reference](https://wildfrostwiki.com/Counter)
- *Griftlands* uses limited-use item cards inside its decks. The transferable lesson
  is that ownership can produce a finite action; Package A2 avoids using deck dilution
  as the main price of access.
  [Klei item-card balance notes](https://forums.kleientertainment.com/forums/topic/127196-griftlands-new-update-available/)
- *Darkest Dungeon II* gives each hero one equipped combat-item slot and treats use as
  a free action. The transferable lesson is reliable preparation and strict capacity;
  Package A2 explicitly rejects the free-action part.
  [Official Darkest Dungeon Wiki](https://darkestdungeon.wiki.gg/wiki/Combat_Items)
- *Balatro* uses bounded Joker slots and separate consumables. The transferable lesson
  is that capacity may expand build choice without granting another hand; Game att2's
  slots remain actionable, source-derived opportunities rather than a modifier shelf.
  [Official Balatro FAQ](https://www.playbalatro.com/faq)

These references establish shipped alternatives, not proof that Package A2 is fun,
balanced, accessible, unique in the market, or commercially viable. The positive
Game att2 hypothesis is narrower: deliberate physical readiness may combine reliable
item access with body-first opportunity pressure.

## 16. Evidence card

| Field | Record |
|---|---|
| Question | Can one deliberately readied inventory opportunity provide dependable item access without weakening body-first combat? |
| Mechanic package | Package A2: one selected flexible inventory slot, one voluntary inventory action per round, existing timing budget, contextual state actions, automatic defense outside cards. |
| Expected dynamic | Actors prepare one accessible item/tool, retain body commitments, and spend Reconsider when circumstances invalidate that preparation. |
| Desired experience | "I readied the wrong tool" rather than "the game forgot I owned it." |
| Instrumentation | Readied item identity, slot occupancy, item use, item-focused Reconsider use, unavailable-item attempts, stranded rescue cases, body/item Main choices, lifecycle reason, and explanation accuracy. |
| Continue criteria | Players explain access and cost; legal rescue is never randomly stranded; items supplement rather than replace body actions. |
| Revise criteria | Players repeatedly expect the whole inventory, Reconsider becomes primarily an inventory tax, or the same treatment is always readied. |
| Kill criteria | Optimal play consistently suppresses body commitments, readiness cannot be explained physically, or the rule requires a hidden/free item rail. |
| Evidence class | Owner-approved paper architecture informed by comparable shipped systems; no runtime or valid human evidence. |
| Contamination risks | Designer familiarity, explanatory prompting, existing simulator Fast-item expectations, and fixtures mistaken for content. |
| Decision owner | Can Yuzbey. |

## 17. Hostile review

| Risk | Severity | Required safeguard |
|---|---|---|
| Readiness feels like forgetting owned inventory | High | Present it as physical access/readiness; record explanation failures. |
| One healing item dominates every loadout | High | Instrument repeated readiness; revise if body/item choice collapses. |
| Reconsider becomes mandatory inventory tax | High | Track item-specific use; do not assume frequent use is healthy. |
| Item use creates Preparation + item + Main stacking | Critical | Inventory action consumes Preparation or Main; no free rail. |
| Reconsider enables a second item | Critical | Spent inventory slot cannot be swapped or refreshed this round. |
| State rescue invents unavailable treatment | Critical | Actual ownership, uses, sources, costs, and state legality remain mandatory. |
| Passive equipment grants free activated use | High | Passive/active definition boundary and readiness requirement. |
| Tool silently changes hands after lock | High | Reserve exact instance and sources; no substitution. |
| Inventory removes body identity | Critical | Protect Commitment body access and cap voluntary inventory use at one. |
| Reflex defense returns as a card | Critical | Automatic origin never occupies a slot or play. |
| Runtime behavior silently changes | Critical | Documentation-only diff; existing Fast rules remain authoritative in runtime. |
| Neutral fixtures become production items/cards | High | Explicit fixture labels and catalogue/runtime negative audit. |
| Comparison becomes a product-success claim | High | Treat references as hypotheses; require human evidence for experience claims. |

No P0 or P1 contradiction remains after preventing Reconsider from refreshing a
Spent inventory slot and keeping state rescue tied to actual ownership. The principal
human-evidence risk is whether one readied item feels like meaningful preparation or
an artificial restriction.

## 18. Approval record and explicit deferrals

On 2026-08-16 the owner directed continuation with Package A2 after reviewing the
comparable-system analysis and recalibrated recommendation.

Approved paper direction:

- the four-origin body/inventory/state/automatic taxonomy;
- one deliberately selected Readied Inventory opportunity in a flexible slot;
- no random item injection and no whole-inventory free access;
- one voluntary inventory action per round;
- Preparation/Main item timing and no paper Fast-item rail;
- Reconsider swapping before use but never refreshing Spent inventory;
- inventory-owned uses, expiry, and legality;
- weakest-source multi-source tools and no post-lock substitution;
- passive/activated equipment separation;
- contextual approved state actions and automatic defense outside cards;
- one governed signature override maximum;
- the bounded existing-content paper fixture and evidence contract.

Deferred:

- runtime, configuration, production tests, and implementation planning;
- changes to the simulator's current Focus/Fast-item sequence;
- individual production card/item profiles, values, timing exceptions, and balance;
- production Stamina, full equipment/loadout systems, and inventory capacity;
- detailed Ruined-Torso rescue implementation beyond WNR-0.1 paper authority;
- detailed reflex success/input/readiness/repetition rules;
- new cards, items, tools, effects, characters, or encounters;
- final UI, accessibility implementation, Unity, and product claims.

## 19. Recommended next decision at Package A2 approval

Resolve the range-maintenance action grammar: which existing action profiles can
maintain, release, or exploit Clinch/Engaged/Distant without creating a universal
movement command, new content, or runtime implementation.

## 20. Later Package C resolution (2026-08-17)

Document 35 resolves that decision with execution-bound, non-stacking maintenance.
Readied inventory Preparation cannot refresh exceptional range by itself. A readied
Main tool may produce only the range result declared by its exact current source and
range profile; cancellation preserves unpaid use but provides no maintenance. The
neutral `RANGE_DIAGNOSTIC_MAIN` record is paper evidence only and cannot enter the
inventory or content catalogue. Runtime remains unchanged. The next dependency-safe
gate was treatment, repair, extraction, and graft commitment flow; section 21 records
its later resolution.

## 21. Later Package B resolution (2026-08-17)

Document 36 resolves that gate with Tiered Atomic Commitments. Authored treatment and
Blood-restoration items may use Preparation; Claim and extraction tools use Main;
ordinary uses pay on execution; exact items/tools/sources cannot substitute after
lock; and pre-execution cancellation preserves unpaid uses. One inventory Preparation
cannot be followed by a second voluntary inventory Main in the same round. Contextual
salvage/graft never invents ownership or a bonus slot/play. Runtime and production
content remain unchanged.

## 22. Later Package A catastrophic-survival resolution (2026-08-19)

Document 37 makes the Limb for Life charge a visible run-level affordance rather than
an item, tool, card, inventory object, ready-slot occupant, or state-required action.
It needs no readiness and consumes no inventory action. Its severed limb creates no
harvested object or owned inventory record. Runtime and production content remain
unchanged.
