# Game att2 - Chosen Irrevocable Sacrifice and Catastrophic Survival v0.1

Status date: **2026-08-19**

Status: **Package A - Chosen Irrevocable Sacrifice is owner-approved as paper
design authority. Runtime, configuration, production values, final UI, fiction,
and human-experience claims remain unapproved.**

## 1. Decision and authority boundary

The owner selected Package A on 2026-08-19 as the paper answer to Limb for Life and
its interaction with catastrophic survival.

The contract is:

> After an atomic consequence and Panic Pulse finish, an actor with one available
> Limb for Life charge may answer Blood-0 death by choosing one eligible attached
> arm or Legs as an irrevocable sacrifice, or may accept death. The sacrifice creates
> an untreated severed stump, produces no harvested object, and finishes the survival
> chain at provisional Blood 12. It never prevents catastrophic Torso failure.

This document consumes rather than replaces the wound and Blood model in documents
27 and 30, the staged action economy in document 29, sequential resolution in
document 32, source-first capability mapping in document 33, the inventory boundary
in document 34, range tenure in document 35, and procedure atomicity in document 36.

Approval here does **not**:

- turn Limb for Life into a card, item, action, reflex, body source, or Attention Slot;
- add a character, enemy, card, item, wound type, encounter, or victory route;
- make the tutorial player package universal to all future actors;
- allow Head, Torso, Core, Disabled, Ruined, Severed, or Missing sacrifice;
- prevent `CATASTROPHIC_TORSO_FAILURE` or extend the Ruined-Torso deadline;
- create a harvested-part object, ownership, access, or harvest quality;
- change the current simulator, YAML configuration, tests, or provisional value 12;
- prove that the package is fun, fair, balanced, comprehensible, or accessible.

Current runtime rules remain authoritative for the existing simulator until a later
implementation plan is separately approved. Where runtime differs from this paper
contract, the difference is an explicit future migration obligation.

## 2. Death-source boundary

Limb for Life prevents exactly one consequence: final death caused by Blood reaching
0 or less after the current atomic chain and Panic Pulse have resolved.

| Consequence source | May present Limb for Life? | Result |
|---|---:|---|
| Action cost, wound loss, periodic pressure, or other legal Blood mutation reaches 0 | Yes, if the actor has a charge and an eligible sacrifice | Choice prompt follows Panic Pulse |
| Ruined Torso is created and its immediate Blood loss reaches 0 | Yes | Blood may recover, but `TORSO_FATALITY_PENDING` remains |
| A legal Stabilize procedure pays a cost that reaches 0 after execution begins | Yes, after the atomic Stabilize chain completes | Stabilization may clear pending fatality; then Blood survival resolves |
| Ruined-Torso deadline expires | No | `CATASTROPHIC_TORSO_FAILURE` is final |
| Actor takes the permitted final non-rescue Main and the deadline then expires | No | The refusal is honored; catastrophic failure is final |
| Any future explicit non-Blood fatality | No by default | Requires its own approved prevention rule |

The system must record the fatality source before offering prevention. A positive
Blood value must never erase an already-triggered non-Blood catastrophic fatality.

## 3. Availability and charge

For the current minimum tutorial package, the player has one visible Limb for Life
charge per run.

- The charge is a run-level affordance, not an owned object or usable body source.
- It requires no card draw, readiness slot, inventory slot, grip, or item use.
- It cannot be stolen, dropped, harvested, grafted, repaired, or traded.
- It cannot be refreshed by Reconsider, treatment, repair, integration, or encounter
  transition.
- It is marked used only when the actor accepts an eligible sacrifice.
- Refusing the offer ends in death and does not create a reusable post-death charge.
- Future actors receive the affordance only when content explicitly grants it.
- An explicitly granted actor uses this same timing, eligibility, choice, mutation,
  and logging contract; enemies do not receive it by default.

The exact fiction that explains the affordance is deferred. The mechanical state must
remain visible even before that fiction is approved.

## 4. Eligible sacrifices

An eligible sacrifice must satisfy every rule below at presentation and again at
acceptance:

1. The slot is `Left Arm`, `Right Arm`, or `Legs`.
2. The structure is attached.
3. Its structure state is usable: `Intact`, `Damaged`, or `Critical`.
4. The structure is not `Disabled`, `Ruined`, `Severed`, or `Missing`.
5. The exact slot still belongs to the actor at mutation time.

Additional rulings:

- A grafted or integrated arm is eligible when it satisfies the same structural
  predicates.
- A Critical arm or Legs is eligible. Low remaining Integrity is not immunity.
- An objective-critical limb is eligible. Narrative or route importance grants no
  hidden plot protection.
- Head, Torso, and Core are never eligible, even when their structure is otherwise
  usable.
- Occupation or reservation does not immunize a limb. A started atomic action finishes
  first; later commitments using the sacrificed source may become invalid.
- Eligibility is state-derived and contains no random selection step.

Any future rule that makes a named part unsacrificable is separate authored content
and requires explicit approval. It is not the default architecture.

## 5. Choice, refusal, and preview

The prompt presents:

- the remaining charge and why Blood-0 death is pending;
- every currently eligible exact slot, with attachment, structure, graft, wound, and
  source state;
- the exact capabilities, Attention Slots, legal cards/actions, grip routes, range
  options, commitments, and known encounter/victory routes lost by each choice;
- the untreated stump and its future periodic Blood pressure;
- commitments that will cancel after recomputation, with no replacement action;
- `TORSO_FATALITY_PENDING` and its deadline when present;
- an explicit `Accept Death` option.

The player chooses the exact eligible limb. Seeded randomness may order display rows
only if it has no semantic effect; it may not choose the sacrifice. The prompt cannot
hide a route loss merely because the route is inconvenient or objective-critical.

If no eligible limb exists, or the charge is already used, no false choice prompt is
shown. Blood-0 death finalizes and the reason is logged.

## 6. Atomic sacrifice chain

Once an eligible sacrifice is accepted, resolve this chain without interruption:

```text
revalidate Blood-0 fatality source, charge, actor, and chosen exact slot
-> mark Limb for Life used
-> sever/consume the chosen attached structure
-> create and log one Untreated Severed Stump on that slot
-> create no harvested-part object, access, ownership, or quality
-> set Blood to provisional final net 12 for this survival chain
-> recompute body-source profiles and local capability
-> recompute Attention Slots and Integrity Echo
-> recompute range legality and all still-locked commitments
-> cancel invalid later commitments with no substitute or replacement action
-> retain any unresolved Ruined-Torso fatality state and deadline
-> evaluate whether the actor and encounter can legally continue
-> log the complete before/after evidence record
```

The current implementation's `SEVERED` structure vocabulary remains the expected
structural result. A future evidence-only marker such as `LIFE_SACRIFICED` may record
cause, but it must not become a new usable anatomy state or content object.

## 7. Stump and Blood reconciliation

The new Stump is real and untreated. Its existence, treatment state, and later
periodic pressure follow WNR-0.1.

For the survival event itself, the provisional value `restore_blood: 12` means the
**final net Blood after the complete Limb for Life chain is 12**. Implementations must
not set Blood to 12 and then immediately deduct the same sacrifice's stump-creation
loss a second time.

The required order is therefore:

1. Create and log the physical severance and untreated stump consequence.
2. Record the stump's normal immediate pressure as consumed by the exceptional
   survival resolution rather than applying it again after the reset.
3. Finish this chain at Blood 12.
4. Apply the stump's ordinary future periodic pressure at later legal wound ticks.

This is a narrow causal reconciliation, not free treatment. Control, Stabilize,
Resolution, repair, grafting, and Blood restoration remain separate later effects.
The value 12 is inherited provisional authority, not a final balance claim.

## 8. Action economy, locks, and resolution

The prompt and accepted sacrifice consume no Preparation, Main, inventory-origin
action, Attention Slot, automatic-defense event, Reply, or Lead.

- Limb for Life is a forced consequence window after the current atomic chain.
- It cannot interrupt or roll back a started atomic action or procedure.
- If an action's execution cost reaches Blood 0, that action still finishes its
  declared atomic chain before Panic Pulse and Limb for Life.
- The chosen limb may have participated in that just-finished action.
- After sacrifice, all derived legality is recomputed from the new body state.
- A later locked action or Reply with an invalid source cancels under document 32.
- Cancellation grants no replacement limb, source, card, target, Main, or Reply.
- Unpaid execution-time costs and item uses remain unspent under the existing
  cancellation contract.
- A genuine same-timing batch finishes before the Blood-0 consequence window unless
  its authored authority explicitly defines an internal fatality checkpoint.

## 9. Ruined-Torso interaction

Ruined Torso remains an independent catastrophic clock.

When Ruined Torso creation also reaches Blood 0:

```text
finish the Ruined-Torso creation chain and its immediate Blood mutation
-> set/retain TORSO_FATALITY_PENDING and its existing deadline
-> resolve Panic Pulse
-> if still at Blood 0, offer legal Limb for Life
-> if accepted, finish at Blood 12 but keep TORSO_FATALITY_PENDING
-> continue only through the existing rescue/refusal window
```

When a legal Stabilize procedure begins before the deadline and its execution cost
reaches Blood 0, the procedure's atomic chain completes first. If that chain legally
Stabilizes the Torso, the pending catastrophic state may clear under document 30;
Panic Pulse and Limb for Life then resolve the remaining Blood-0 consequence.

When the deadline expires—because the actor refuses rescue, uses the allowed final
non-rescue Main, lacks a legal source, or fails to Stabilize in time—the system emits
`CATASTROPHIC_TORSO_FAILURE`. Limb for Life is not offered for that fatality and cannot
extend, reset, or reopen the deadline.

## 10. Capability and encounter consequences

The sacrifice is not an abstract life token. Losing its exact body source may:

- remove or strain cards/actions whose minimum source is no longer available;
- reduce Attention Slots and suppress later prepared options;
- change grip, tool, inventory, defense, movement, and range capability;
- cancel a later locked Reply or procedure after state revalidation;
- close an encounter or victory route that required the source;
- expose new stump pressure and treatment needs.

No generic victory route requires Limb for Life. A future route may react to
`limb_for_life_used`, but it cannot pre-author the sacrifice as mandatory without a
separate owner-approved content decision. The sacrifice is not victory, surrender,
escape, encounter ending, or legal access to an opponent.

## 11. Symmetry and content boundary

Mechanic causality is symmetric; availability is authored.

- The current tutorial player has one charge.
- Current enemies do not receive a charge by default.
- A future player, ally, or enemy with an explicitly granted charge follows the same
  eligible-slot, exact-choice, refusal, atomicity, stump, Blood, Torso, recomputation,
  and evidence rules.
- AI policy for choosing or refusing a sacrifice is content/implementation work and
  must not alter eligibility or causality.

This is affordance symmetry, not universal distribution.

## 12. Complete causal order

The authoritative consequence order for this package is:

```text
finish current atomic action/procedure/batch
-> apply its ordered structure, wound, Blood, and encounter mutations
-> record pending fatality sources
-> resolve Panic Pulse when legally available
-> if Blood remains 0 and its fatality source is Blood-0, inspect Limb for Life
-> if no charge or eligible limb: finalize Blood-0 death
-> otherwise present exact sacrifices plus Accept Death
-> on refusal: finalize Blood-0 death
-> on acceptance: execute the atomic sacrifice chain
-> recompute all derived state and locked commitments
-> preserve independent catastrophic clocks
-> evaluate death, incapacity, surrender, victory, and encounter continuation
```

No step may infer success from an intended action that did not execute.

## 13. Existing runtime and content disposition

The current configuration and simulator intentionally remain unchanged in this paper
gate. They currently use:

- one tutorial-scope use;
- provisional restore value 12;
- seeded-random selection from usable non-Core limbs;
- direct severance without the complete stump/choice/refusal contract.

The current usable predicate also permits states broader than this document's exact
slot restriction. Existing tests demonstrate current runtime behavior, not compliance
with this later paper authority.

A future implementation plan must explicitly migrate:

1. seeded random selection to exact player choice plus refusal;
2. broad non-Core eligibility to attached usable Left Arm/Right Arm/Legs;
3. direct severance to the full stump/no-harvest/net-12 chain;
4. generic Blood-0 handling to fatality-source-aware Torso separation;
5. post-sacrifice state to full source/capability/lock recomputation;
6. traces and tests to the requirements below.

No production character, card, item, or Encounter 3 content is approved here.

## 14. Minimum bounded paper fixture

These are acceptance fixtures, not production content.

| Case | Setup | Required result |
|---|---|---|
| CIS-A-01 | Atomic action ends at Blood 0; Panic cannot restore; eligible arm/Legs exists | Exact choices and Accept Death appear after the action |
| CIS-A-02 | Player chooses an eligible arm | Charge used; arm Severed; untreated stump; no harvested object; final Blood 12; capabilities recomputed |
| CIS-A-03 | Player chooses eligible Legs | Same chain; locomotion/range consequences recompute from Legs loss |
| CIS-A-04 | Player selects Accept Death | Blood-0 death finalizes; no sacrifice mutation |
| CIS-A-05 | No eligible arm/Legs exists | No false prompt; Blood-0 death finalizes |
| CIS-A-06 | Limb for Life was already used | No second use; Blood-0 death finalizes |
| CIS-A-07 | Only Head, Torso, or Core is usable | No eligible sacrifice exists |
| CIS-A-08 | A grafted or integrated arm is attached and usable | It is presented and may be sacrificed under the same chain |
| CIS-A-09 | A Critical arm is otherwise eligible | It remains selectable; exact loss is previewed |
| CIS-A-10 | An objective-critical limb is eligible | No plot immunity; route loss is previewed before choice |
| CIS-A-11 | Sacrificed source supports a later locked Reply | Reply revalidates and cancels if illegal; no replacement action |
| CIS-A-12 | Ruined Torso creation reaches Blood 0 | Limb for Life may restore Blood; pending fatality and deadline remain |
| CIS-A-13 | Legal Stabilize execution cost reaches Blood 0 | Stabilize chain completes; pending state may clear; then Blood survival resolves |
| CIS-A-14 | Ruined-Torso deadline emits catastrophic failure | Limb for Life is not offered |
| CIS-A-15 | Enemy lacks the affordance; mirrored future actor explicitly has it | First dies at Blood 0; second follows the same granted-use contract |
| CIS-A-16 | Surviving actor reaches a later periodic wound tick | Untreated stump applies its normal later pressure; no second immediate creation loss |

## 15. Future acceptance requirements

| Requirement | Binding paper rule | Minimum future evidence |
|---|---|---|
| CIS-A-001 | Blood-0 rescue is checked only after the current atomic chain and Panic Pulse. | Ordered Blood-0 traces |
| CIS-A-002 | The current tutorial actor has one visible run-level charge; no implicit universal grant exists. | Availability and second-use cases |
| CIS-A-003 | The actor chooses an exact eligible limb or Accept Death. | Choice/refusal state diffs |
| CIS-A-004 | Eligibility is limited to attached usable Left Arm, Right Arm, or Legs. | Positive and excluded-slot matrix |
| CIS-A-005 | Grafted, integrated, Critical, and objective-critical limbs receive no hidden immunity. | CIS-A-08 through 10 |
| CIS-A-006 | Randomness never selects the sacrificed limb. | Seed-invariant choice evidence |
| CIS-A-007 | Accepted sacrifice resolves one uninterruptible ordered chain. | Full event trace |
| CIS-A-008 | Sacrifice creates an untreated severed stump and no harvested object, access, ownership, or quality. | Object/wound negative assertions |
| CIS-A-009 | The survival chain finishes at provisional net Blood 12; later stump pressure remains active. | CIS-A-02 and 16 arithmetic |
| CIS-A-010 | The prompt and sacrifice consume no action, readiness, defense, Reply, or Lead budget. | Before/after budget diff |
| CIS-A-011 | Body sources, capabilities, Attention Slots, Integrity Echo, range, and locks recompute after sacrifice. | CIS-A-03 and 11 traces |
| CIS-A-012 | Limb for Life never prevents or delays `CATASTROPHIC_TORSO_FAILURE`. | CIS-A-12 through 14 |
| CIS-A-013 | No generic victory route requires sacrifice; route reactions require separate authored content. | Route-definition validation |
| CIS-A-014 | Explicitly granted actors use symmetric rules; enemies have no default charge. | CIS-A-15 mirrored evidence |
| CIS-A-015 | Preview and logs expose eligibility, refusal, losses, stump, cancellations, and pending fatality. | Presentation and trace inspection |
| CIS-A-016 | Runtime/configuration remain unchanged until a separately approved implementation gate. | Clean paper-only diff |

These are obligations for a future implementation or paper harness. They are not a
claim that the current runtime already passes them.

## 16. Comparable evidence

Comparable systems supply design evidence, not authority.

### Wildermyth Mortal Choice

Wildermyth presents a player-facing choice at zero health that can include death or
persistent maiming: <https://wildermyth.com/wiki/Mortal_Choice>.

Transferable lesson: agency at catastrophe can make persistent capability loss feel
owned. Do not copy roster withdrawal, story-event variety, or random exact-limb logic.

### Gloomhaven damage prevention

Gloomhaven permits a player to lose persistent hand/deck capability to prevent a
damage event: <https://cephalofairgames.github.io/gloomhaven2e-faq/>.

Transferable lesson: survival can demand a visible future-capability cost. Do not copy
card exhaustion, routine damage negation, or a pre-zero mitigation window.

### Battle Brothers permanent injuries

Battle Brothers links survival after being struck down to persistent injury:
<https://battlebrothersgame.com/dev-blog-79-progress-update-injury-mechanics/>.

Transferable lesson: survival must leave a durable consequence. Do not copy random
roster maiming; Game att2's single-avatar Body-as-Build structure needs exact agency.

## 17. Evidence card

| Field | Package A record |
|---|---|
| Question | Can one catastrophic Blood-0 reprieve preserve player agency, body causality, and genuine permanent cost without becoming a generic extra life? |
| Mechanic/config variant | One visible run-level charge; exact eligible arm/Legs choice or death; untreated stump; no harvest; final net Blood 12; Torso catastrophe excluded |
| Expected runtime dynamic | A player may preserve the run by destroying a chosen capability and accepting ongoing wound pressure, while independent fatality clocks remain binding |
| Desired player experience | The reprieve feels desperate, informed, physical, and owned rather than arbitrary or free |
| Instrumentation | Fatality source, charge, eligible set, previewed losses, choice/refusal, severance, stump, Blood reconciliation, recomputed capability, canceled locks, Torso pending state |
| Continue criteria | Choices differ by build and state; consequences are legible; refusal is meaningful; no generic route or universal enemy use emerges |
| Revise criteria | Players always sacrifice the same lowest-value Critical/grafted limb, route loss is unreadable, or final Blood 12 makes later stump pressure irrelevant |
| Kill criteria | The package requires random sacrifice, hidden plot immunity, harvested rewards, action-budget payment, or Torso-catastrophe prevention |
| Evidence class | Owner-approved paper architecture plus deterministic future-fixture obligations; no human evidence |
| Contamination risks | Current seeded-random runtime, prototype value 12, designer familiarity, and comparable-game conventions |
| Decision owner | Can Yuzbey |

## 18. Hostile review

| Finding tested | Severity if present | Safeguard/result |
|---|---:|---|
| Sacrifice becomes a generic extra life with no body cost | Critical | Exact attached structure is permanently severed and an untreated stump remains |
| Random selection destroys the player's build arbitrarily | Critical | Player chooses exact eligible limb; no semantic RNG |
| Player is forced to sacrifice when death is preferable | High | `Accept Death` is mandatory |
| Head/Torso sacrifice creates nonsense or self-defeating loops | Critical | Only Left Arm, Right Arm, or Legs is eligible |
| Sacrifice creates valuable harvest and becomes a farming action | Critical | No harvested object, quality, access, or ownership |
| Blood reset double-charges immediate stump loss | Critical | Final net 12 after creation; future periodic pressure remains |
| Limb for Life erases Ruined-Torso catastrophe | Critical | Pending state persists; catastrophic failure is never prevented |
| Objective route quietly protects a limb | High | No plot immunity; exact route loss is previewed |
| Source reservation protects a limb from sacrifice | High | Atomic action completes, sacrifice proceeds, later locks revalidate/cancel |
| Grafted or Critical limbs become cheap dominant fuel | High | Whole source and capability are lost; repetition is an explicit revision trigger |
| Enemies gain universal extra lives | High | Availability must be explicitly authored; current enemies have none by default |
| Sacrifice is pre-required by a victory route | High | No generic route requirement; future reaction content needs separate approval |
| Paper value 12 is mistaken for final balance | High | Value remains provisional and requires later deterministic/human evidence |

No P0/P1 documentation contradiction remains under these safeguards. The dominant
untested exploit is repeatedly choosing the same lowest-value Critical or unstable
graft; future paper/runtime evidence must compare choice distributions and resulting
capability loss before balance approval.

## 19. Owner approval and deferrals

Approved on paper:

- Package A Chosen Irrevocable Sacrifice;
- one visible tutorial-scope run-level charge;
- exact eligible limb choice plus explicit refusal;
- attached usable arm/Legs eligibility, including grafted/integrated/Critical limbs;
- atomic severance, untreated stump, no-harvest, final-net-12 chain;
- complete capability/lock recomputation;
- strict separation from catastrophic Torso failure;
- actor-explicit availability with symmetric causality;
- future cases and requirements CIS-A-001 through CIS-A-016.

Still deferred:

- the affordance's exact fiction and presentation language;
- final restore value, balance, AI choice policy, and production availability;
- final UI, accessibility, tutorialization, and human-experience evidence;
- exact production characters, cards, items, routes, and encounters;
- runtime, configuration, tests, Unity, and engine work;
- mental defeat, surrender, mercy, negotiation, and final encounter outcomes.

## 20. Recommended next decision

Resolve **mental defeat, surrender, and mercy** as the next dependency-safe paper
gate: state-derived surrender thresholds, voluntary surrender, mercy/refusal outcomes,
and their exact order after physical incapacity and catastrophic survival. Do not begin
negotiation, runtime implementation, or production content from this recommendation.
