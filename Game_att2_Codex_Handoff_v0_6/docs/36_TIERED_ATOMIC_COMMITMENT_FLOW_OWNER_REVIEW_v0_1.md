# Game att2 - Tiered Atomic Treatment, Repair, Extraction, and Graft Commitments v0.1

Status date: **2026-08-17**

Status: **Package B - Tiered Atomic Commitments is owner-approved as paper design
authority. Runtime, configuration, production procedure profiles, exact values,
final UI, and human-experience claims remain unapproved.**

## 1. Decision and authority boundary

The owner selected Package B on 2026-08-17 as the paper answer to treatment, repair,
extraction, and graft commitment flow.

The contract is:

> Small field-control and Blood-restoration procedures may use Preparation when their
> explicit profile says so. Structural repair, claiming, extraction, and ordinary
> stabilization use Main by default. Once a procedure begins execution, its declared
> causal chain is atomic; before execution, cancellation loses reserved tempo but
> preserves unpaid costs and item/tool uses.

This document consumes rather than replaces the approved wound states and WNR-0.1
values in documents 27 and 30, the staged turn in document 29, the automatic-defense
boundary in document 31, sequential lock/revalidation in document 32, source profiles
in document 33, the inventory boundary in document 34, and the range grammar in
document 35.

Approval here does **not**:

- combine treatment, Blood restoration, structural repair, extraction, or grafting;
- create a universal surgery action, action points, or a free Fast-item rail;
- add an item, card, tool, character, wound, anatomy rule, or runtime scenario;
- approve Encounter 3 access, anatomy, rewards, surrender, or runtime content;
- change any current simulator cost, probability, threshold, configuration, or test;
- prove that the package is fun, balanced, comprehensible, or accessible.

Current runtime rules remain authoritative for the existing simulator until a later
implementation plan is separately approved.

## 2. Effect ownership remains separate

| Effect family | Owns | Must not own by implication |
|---|---|---|
| Treatment | Wound treatment-state movement such as Untreated to Controlled or Stabilized | Integrity repair, Blood restoration, severance, harvest quality, graft installation |
| Blood restoration | Explicit Blood gain from an owned source | Wound control, structural repair, stabilization, graft quality |
| Structural repair | Integrity restoration within the approved Field/Reconstructive ceiling | Wound treatment, Blood gain, Severed/Missing restoration, harvest quality |
| Extraction | Detachment, donor wound/consequence, and creation of a harvested-part object | Donor treatment, donor repair, automatic grafting, post-combat ownership invention |
| Grafting | Compatible harvested-part installation and its declared stability/integration state | Wound erasure, Blood restoration, harvest-quality improvement, free combat tempo |

A single authored procedure may declare more than one effect only by listing each
effect, source, cost, stage, and mutation separately. Naming a procedure does not
grant hidden bundled healing.

## 3. Timing classes and primary origin

Every procedure declares one primary origin under document 34 and one timing class
under document 29.

| Procedure family | Default timing | Primary origin | Paper rule |
|---|---|---|---|
| Control Open/Major/Stump wound | Preparation | Inventory or body, as authored | Suppresses approved wound pressure only; does not repair |
| Blood restoration | Preparation | Inventory or body, as authored | Restores Blood only |
| Stabilize | Main | Inventory, body, or contextual state | A specific visible profile may explicitly use Preparation; Main is the default |
| Field Repair | Main | Body, inventory/tool, or table | Requires an eligible attached structure and its wound prerequisite |
| Reconstructive Repair | Main | Body, inventory/tool, or table | Stabilized/Resolved attached Ruined only; never Severed/Missing |
| Claim the Cut | Main | Inventory | Marks one legal target; it does not extract |
| Bone Scissors / Hell Saw extraction | Main | Inventory tool plus required body sources | Atomic extraction chain after execution begins |
| Emergency Salvage | Contextual | State plus owned source/tool | Exists only after legal access to a valid target already exists |
| Emergency graft | Contextual between encounters | State plus owned harvested part and required sources | No bonus combat action and no invented harvested part |
| Resolve wound / integrate graft / table repair | Table or between-encounter | Table/contextual state | One selected table commitment; each effect logged separately |

`Preparation Stabilize` is a permitted future profile signature, not a production
profile approved by this package. It must be visible before commitment and cannot
waive ownership, source legality, the one-inventory-action limit, or any cost.

## 4. Commitment tiers

### 4.1 Opportunity presentation

A presented opportunity identifies:

- actor, patient, donor, and target slot as applicable;
- primary origin and timing class;
- exact body sources, item/tool, and any table/context source;
- required wound, integrity, attachment, harvest, compatibility, and access states;
- execution costs, item/tool uses, and explicit on-lock costs if any;
- every separate effect and its ordered mutation stage;
- cancellation and failure result;
- whether randomness is used and the visible result range.

### 4.2 Lock and reservation

- A locked Preparation reserves its exact declared sources until it executes or is
  canceled. After execution, those sources release unless the profile declares a
  visible persistent commitment.
- A locked Main reserves its exact declared sources and Main tempo. The sources remain
  occupied through the complete atomic execution chain.
- Reservation never substitutes a different item, tool, grip, body part, patient,
  donor, harvested part, or destination after lock.
- Multi-source procedures use document 33's weakest-required-source rule.
- State-required rescue presentation never invents ownership, medicine, a usable
  source, or an extra action.

### 4.3 Payment and cancellation

The neutral default is **pay on execution**.

- Ordinary Blood costs and item/tool uses are not deducted at lock.
- An explicit persistent prepared state may declare an on-lock cost, following
  document 32; Package B creates none by default.
- If revalidation fails before execution, the commitment is canceled. Its reserved
  Preparation/Main tempo is lost, but unpaid Blood and execution-time uses remain.
- If the actor voluntarily abandons a locked Main before execution where cancellation
  is legal, Main tempo is lost and unpaid execution costs remain.
- Once execution begins, costs are paid, the opportunity becomes Spent, and the
  declared atomic chain completes before downstream forced consequences are checked.
- A failed random outcome is still an executed procedure. Its declared failure chain
  and paid costs/uses stand.

## 5. Round-budget consequences

Package B stays inside the approved budget of zero or one Preparation, then zero or
one Main commitment, with automatic defense surfaced only by incoming actions.

- A Preparation medical item may be followed by a body-origin Main action.
- A Preparation inventory action may **not** be followed by a second voluntary
  inventory-origin Main action in the same round.
- Claim the Cut and an inventory extraction tool therefore normally require separate
  rounds.
- A body-origin Preparation and an inventory-origin Main remain possible only if both
  exact profiles are legal and no shared source is occupied.
- A contextual between-encounter graft does not consume or grant combat Preparation
  or Main tempo.
- Automatic defense is not a procedure and is never manually played as medical
  interruption.

## 6. Treatment and Blood restoration

### 6.1 Control

Control validates an eligible wound, patient access, the exact treatment source, and
the WNR-0.1 treatment-state transition. On execution it pays its declared cost/use,
applies only the approved treatment mutation, updates projected wound pressure, and
logs the result. It restores no integrity or Blood unless separately authored effects
declare and pay for those mutations.

### 6.2 Blood restoration

Blood restoration validates the exact owned source and target, pays its declared
use/cost on execution, mutates Blood, then evaluates Blood-dependent consequences.
It does not change wound or structure state.

### 6.3 Stabilize

Stabilize is Main by default because it closes encounter-scale danger rather than
providing a minor field-control adjustment. A future source may explicitly define a
Preparation profile when its complete visible signature justifies it. Stabilize does
not repair structure, replace a missing part, restore Blood, or resolve a wound.

## 7. Structural repair

Field Repair validates:

- an attached, repair-eligible target;
- the required structural band and ceiling from document 30;
- the required wound treatment state;
- the exact repair source/tool and usable physical sources;
- the declared Blood/use cost and Main timing.

Reconstructive Repair additionally requires an attached Ruined target whose wound is
Stabilized or Resolved. It may restore only to the approved Reconstructive ceiling.
It cannot affect Severed or Missing targets; grafting owns those states.

Repair execution applies the declared integrity mutation, recomputes source profiles
and legal capabilities, and leaves wound treatment and Blood unchanged except for
explicit procedure costs.

## 8. Claiming, extraction, and harvested objects

### 8.1 Claim the Cut

Claim the Cut is a Main inventory commitment. It validates and marks one legal target
on execution. The mark may later influence quality under existing authority. It does
not reserve a later extraction, bypass access, sever the target, or create an object.

### 8.2 Extraction atomic chain

An extraction locks the exact tool, required body sources, donor, target slot, target
state, access predicate, quality profile, costs, and failure profile. Immediately
before execution, all are revalidated.

After execution begins, resolve in this order:

```text
pay declared Blood cost and tool use
-> resolve approved extraction rule and injected randomness
-> mutate donor structure to the declared detached state
-> create and log the donor's separate Stump/other approved wound and Blood pressure
-> create one separate harvested-part object from the extraction snapshot
-> assign quality only from the approved mark/tool/target/outcome rule
-> recompute donor and extractor capabilities
-> evaluate Blood-0, incapacity, surrender, and other forced consequences
```

The donor wound and harvested object are different state records. Treating the donor
later cannot improve the harvested object's quality. Repairing or grafting the donor
cannot retroactively erase the extraction event.

If extraction is canceled before execution, there is no cost, tool use, donor wound,
detachment, or harvested object. Once execution begins, the complete declared success
or failure chain resolves atomically.

## 9. Contextual salvage and emergency graft

### 9.1 Access and ownership boundary

Emergency Salvage and emergency graft are contextual opportunities, not universal
actions. They appear only when prior state already establishes every required fact:

- legal access to the target or harvested object;
- ownership/control of the exact item, tool, or part;
- a compatible destination and legal patient;
- usable required physical sources;
- affordable costs and available uses;
- any encounter-ending or between-encounter timing predicate.

Package B does not decide how a living, resisting, surrendered, escaped, or otherwise
resolved opponent becomes legally accessible. That predicate belongs to the later
encounter-resolution package. Until then, unsupported access is `DEFERRED`, never
assumed.

### 9.2 Emergency Salvage

Emergency Salvage pays on execution and resolves its declared success/failure
atomically. It may create one harvested object with the approved result quality. It
does not grant access, ownership, treatment, repair, or graft installation.

### 9.3 Emergency graft

Emergency graft is contextual between encounters in the current paper package:

```text
validate owned compatible harvested part, patient, destination, and required sources
-> lock exact part and destination
-> revalidate immediately before execution
-> pay declared Blood cost
-> resolve approved stability randomness through injected RNG
-> install the part with its declared graft/stability tags
-> recompute body sources, capabilities, and legal opportunities
-> evaluate forced consequences
-> log the complete trace
```

The graft does not erase an existing Stump wound, restore Blood, improve harvested
quality, or add an automatic fresh-graft wound unless a later approved effect
explicitly says so. It grants no free combat action.

## 10. Table commitments

Resolve wound, integrate graft, and structural table repair remain separate effects.
Selecting one Grafting Table option creates one contextual table commitment:

- validate the selected option, patient, target, table access, and cost;
- reserve the exact target and table opportunity;
- pay on execution unless the option explicitly says otherwise;
- apply only the option's listed effects in their declared order;
- recompute capabilities and forced consequences;
- log each separate mutation.

One table option cannot silently perform another option. Package B does not change the
current Table v0.2 choices or numbers.

## 11. Ruined-Torso rescue

Document 30's deadline remains binding: a Ruined Torso must be Stabilized by the end
of the actor's next Main opportunity, while the actor retains the approved final
refusal action.

- The rescue opportunity is surfaced only if a real legal Stabilize profile exists.
- Main is the default timing; an explicit Preparation signature must be separately
  visible and approved for that source.
- The opportunity uses the normal timing and inventory budgets.
- It does not create medicine, ignore source occupation, waive cost, or bypass Lead
  and Reply revalidation.
- If no legal source exists, the system shows the deadline and absence of rescue; it
  does not fabricate an action.
- A pre-execution cancellation pays no ordinary execution cost but consumes the
  reserved tempo and does not count as stabilization.

The exact interaction between the rescue deadline and Limb for Life is the next
catastrophic-survival gate, not decided here.

## 12. Information and evidence record

Every material procedure trace must expose:

```text
prior actor, patient, donor, body, wound, part, item, tool, range, and outcome state
-> presented opportunity origin, timing, sources, costs, uses, target, and effects
-> lock and reservations
-> pre-execution revalidation
-> cancellation reason or execution payment
-> injected random result, if any
-> each ordered state mutation
-> capability and affordance recomputation
-> forced consequence checks
-> final procedure, donor, harvested-object, graft, and encounter state
```

Player and enemy procedures use the same legality, reservation, payment, atomicity,
and logging rules. Content may differ; causality may not.

## 13. Minimum bounded paper fixture

These are acceptance fixtures, not production content.

| Case | Setup | Required result |
|---|---|---|
| TAC-B-01 | Legal inventory Control uses Preparation; legal body Main follows | Both execute; no bonus action exists |
| TAC-B-02 | Inventory Control uses Preparation; inventory extraction Main is attempted | Second voluntary inventory action is rejected |
| TAC-B-03 | Blood restoration executes on untreated wound patient | Blood changes; wound and integrity do not |
| TAC-B-04 | Main Stabilize is locked, source invalidates before execution | Main tempo lost; unpaid cost/use preserved; wound remains unstabilized |
| TAC-B-05 | Ruined Torso deadline exists but no legal Stabilize source exists | No rescue is invented; catastrophic check remains |
| TAC-B-06 | Field Repair targets an attached structure with an ineligible wound state | Commitment is rejected before lock/execution |
| TAC-B-07 | Reconstructive Repair targets Severed/Missing structure | Rejected; grafting owns restoration |
| TAC-B-08 | Claim executes, then same-round inventory extraction is attempted | Extraction is rejected; separate round normally required |
| TAC-B-09 | Extraction locks, then exact tool/source invalidates before execution | No Blood/use/donor wound/harvest object; Main tempo lost |
| TAC-B-10 | Legal extraction begins and succeeds | Cost/use, detachment, donor wound, harvested object, quality, and capabilities settle atomically |
| TAC-B-11 | Emergency Salvage is requested without established legal access | Opportunity absent or rejected; no ownership invented |
| TAC-B-12 | Legal emergency graft uses owned compatible part | Cost, stability, install, tags, recomputation, and consequences resolve; no bonus combat action |
| TAC-B-13 | Table integration option executes | Only declared integration effects apply; wound/repair/Blood restoration do not appear implicitly |
| TAC-B-14 | Mirrored enemy procedure uses same state and sources | Same legality, cancellation, payment, and atomicity rules apply |

## 14. Future acceptance requirements

| Requirement | Binding paper rule | Minimum future evidence |
|---|---|---|
| TAC-B-001 | Treatment, Blood restoration, repair, extraction, and grafting remain separately owned effects. | Positive and negative effect-diff cases |
| TAC-B-002 | Every opportunity declares origin, timing, exact sources, target, costs, uses, and ordered effects. | Definition validation and trace inspection |
| TAC-B-003 | Control/Blood restoration may use Preparation; repair/claim/extraction and default Stabilize use Main. | Timing-budget cases |
| TAC-B-004 | Package A2's one voluntary inventory-origin action per round remains binding. | TAC-B-01, 02, 08 |
| TAC-B-005 | Ordinary procedure costs and uses are paid on execution; no new default on-lock payment exists. | Lock/cancel/execute accounting cases |
| TAC-B-006 | Pre-execution cancellation loses reserved tempo but preserves unpaid execution costs/uses. | TAC-B-04, 09 |
| TAC-B-007 | Started procedures complete their declared atomic success/failure chain before forced consequences. | Extraction, salvage, and graft traces |
| TAC-B-008 | Reservations use exact sources and document 33's weakest-source/no-substitution rules. | Source invalidation and substitution rejection |
| TAC-B-009 | Treatment never implies repair or Blood restoration. | TAC-B-03 and Control/Stabilize diffs |
| TAC-B-010 | Repair respects attachment, treatment-state, structural-band, and ceiling prerequisites; it never restores Severed/Missing. | TAC-B-06, 07 |
| TAC-B-011 | Extraction creates a donor consequence and a separate harvested object; later donor care cannot improve object quality. | TAC-B-10 plus post-treatment quality invariant |
| TAC-B-012 | Contextual salvage/graft requires already-established access and ownership. | TAC-B-11 and legal contrast |
| TAC-B-013 | Emergency graft grants no combat action, implicit wound erasure, Blood restoration, or quality improvement. | TAC-B-12 state diff |
| TAC-B-014 | One table commitment applies only its listed separately logged effects. | TAC-B-13 and option-isolation cases |
| TAC-B-015 | Player and enemy procedure causality is symmetric and fully logged. | TAC-B-14 and mirrored trace comparison |

These requirements are obligations for a future approved implementation or paper-test
instrument. They do not authorize either.

## 15. Existing content disposition

| Existing content | Package B paper mapping | Runtime disposition |
|---|---|---|
| Blood Bag | Blood-restoration inventory Preparation under the paper architecture | Existing Fast runtime behavior unchanged |
| Clotting Cream | Treatment inventory Preparation under the paper architecture | Existing Fast runtime behavior unchanged |
| Claim the Cut | Main inventory commitment, pay on execution | Existing runtime unchanged |
| Bone Scissors | Main inventory-tool extraction | Existing runtime unchanged |
| Hell Saw | Main inventory-tool extraction with atomic success/failure chain | Existing runtime unchanged |
| Black Stitch | Stabilize effect; default Main unless its future explicit source profile says otherwise | Anna trade/treatment runtime unchanged |
| Marked/Unmarked Emergency Salvage | Contextual only after legal access exists | Existing runtime unchanged |
| Emergency graft | Contextual between encounters using an owned compatible harvested part | Existing runtime unchanged |
| Grafting Table options | One separately logged contextual commitment | Existing runtime unchanged |

The mappings are paper architecture, not migrated content definitions. This document
adds no content-catalogue entry.

## 16. Comparable evidence

### Stoneshard injury direction

Ink Stains Games described moving toward body-specific injuries and planned treatment
choices rather than leaving major bodily consequences as opaque noise:
<https://steamcommunity.com/groups/inkstainsgames/announcements/listing>.

Transferable lesson: treatment decisions should point to a visible affected body
state. Do not copy its realism load, pain simulation, or broader micromanagement.

### Battle Brothers battlefield injury split

Overhype Studios separates battlefield injury pressure from longer recovery and
describes distinct injury consequences:
<https://battlebrothersgame.com/dev-blog-79-progress-update-injury-mechanics/>.

Transferable lesson: immediate field control and deeper repair can have different
timing and ownership. Do not copy roster downtime or campaign-day healing.

### RimWorld operation inputs

RimWorld's documented surgery system presents operations with explicit medicine,
body-part, patient, and environmental inputs:
<https://rimworldwiki.com/wiki/Surgery>.

Transferable lesson: high-consequence procedures need inspectable inputs. This is a
community-maintained reference and therefore weaker than primary developer evidence.
Do not copy doctor-skill percentages, surgery rooms, or random catastrophe tables.

Comparable systems demonstrate alternatives, not proof that Package B is correct for
Game att2.

## 17. Evidence card

| Field | Package B record |
|---|---|
| Question | Can minor control, major procedures, extraction, and grafting share one readable commitment grammar without becoming one generic heal/surgery action? |
| Mechanic/config variant | Tiered Atomic Commitments: Preparation for small authored control/restoration, Main for structural/extraction/default Stabilize, contextual post-combat graft/table procedures, pay on execution |
| Expected runtime dynamic | Players can preserve Main tempo with limited field control but must reserve whole commitments for structural or acquisition decisions; invalidated procedures lose tempo without phantom resource loss |
| Desired player experience | Desperate maintenance feels deliberate, inspectable, and physically sourced while extraction/grafting remain consequential |
| Instrumentation | Opportunity profile, reservations, payment stage, item/tool use, ordered mutations, cancellation reason, donor wound, harvest object, graft state, recomputed capabilities |
| Continue criteria | At least two legal procedure sequences remain meaningful; effect ownership is correctly explained; cancellation and extraction traces are readable; no mandatory universal medical readiness appears |
| Revise criteria | One treatment dominates the flexible slot, procedure origins are confused, or Main procedures become unusably rare |
| Kill criteria | Package requires a free item rail, generic composite healing, invented access/ownership, hidden source substitution, or partial extraction commits |
| Evidence class | Owner-approved paper architecture plus deterministic future-fixture obligations; no human evidence |
| Contamination risks | Existing runtime Fast-item expectations, prototype costs, designer familiarity, and comparable-game conventions |
| Decision owner | Can Yüzbey |

## 18. Hostile review

| Finding tested | Severity if present | Safeguard/result |
|---|---:|---|
| Generic `heal` silently controls wounds, restores Blood, and repairs integrity | Critical | Separate effect ownership and per-effect mutations are binding |
| Post-combat procedure invents access to a living/resisting target | Critical | Access must already exist; encounter resolution owns that future predicate |
| Canceled extraction consumes Blood/tool or creates partial anatomy | Critical | Pay on execution; no mutation before execution; started chain atomic |
| Extraction treats donor care as harvest-quality improvement | High | Donor wound and harvested object are separate records |
| Emergency graft becomes a bonus combat action | High | Contextual between encounters; no combat tempo granted |
| Graft erases Stump wound, restores Blood, or improves quality | High | All prohibited unless separately approved effects explicitly declare them |
| Ruined-Torso rescue fabricates medicine or timing | Critical | Only real legal source; normal budget; absence remains visible |
| Preparation medical item enables a second inventory Main | High | One voluntary inventory-origin action per round remains binding |
| Claim and extraction collapse into one same-round inventory chain | High | Claim remains Main; separate round normally required |
| Main-only procedures make one medical item mandatory every Refresh | High | Mandatory-readiness pattern is an explicit revise trigger |
| Player and enemy procedures use different causal rules | High | Symmetric legality, payment, atomicity, and logging requirement |
| Existing values become approved balance | High | All current numbers remain provisional/current-runtime values only |

No P0/P1 documentation finding remains under these safeguards. Experience and balance
risks remain untested.

## 19. Owner approval and deferrals

Approved on paper:

- Package B Tiered Atomic Commitments;
- the timing-family matrix and separate effect ownership;
- exact-source reservation, pay-on-execution default, and pre-execution cancellation;
- atomic extraction, salvage, graft, and table chains;
- donor-wound/harvested-object separation;
- contextual access/ownership boundary;
- the future fixture and requirements TAC-B-001 through TAC-B-015.

Still deferred:

- exact production procedure/card/item profiles and signature exceptions;
- production values, success rates, costs, item quantities, and repair ceilings beyond
  current provisional authority;
- the encounter-resolution rule that establishes access to an opponent or their part;
- Limb for Life and catastrophic-survival interaction;
- detailed reflex interruption checkpoints, final UI, accessibility, and human tests;
- runtime, configuration, production content, Encounter 3, Unity, and engine work.

## 20. Recommended next decision

Resolve **Limb for Life and catastrophic survival** as the next paper gate: player
choice or randomness, refusal, eligible limbs, availability source, and ordering
against Ruined-Torso rescue and Blood-0 consequences. Do not implement runtime or add
production content from this recommendation.

## 21. Later Package A catastrophic-survival resolution (2026-08-19)

Document 37 resolves that gate with Chosen Irrevocable Sacrifice. A started procedure,
including a Stabilize whose execution cost reaches Blood 0, completes its declared
atomic chain before Panic Pulse and Limb for Life. The later sacrifice is not a
procedure, consumes no action budget, and cannot create treatment, repair, access,
ownership, or a harvested object. It creates one Untreated Severed Stump and finishes
the exceptional survival chain at provisional net Blood 12.

Limb for Life may restore Blood while Ruined-Torso fatality is pending, but it never
Stabilizes the Torso or prevents the deadline's catastrophic failure. Runtime,
configuration, procedures, values, and production content remain unchanged. The next
dependency-safe gate is mental defeat, surrender, and mercy.

## 22. Brain Module inventory reconciliation (2026-08-21)

Document 38 removes the Readied Inventory slot but does not change this package's
procedure timing or atomicity. Inventory treatment, Blood restoration, Claim, and
extraction tools are selected directly from owned legal inventory. They still consume
their authored Preparation or Main timing, obey the one-voluntary-inventory-action
limit, reserve exact sources/targets/items, pay on execution, and cannot substitute
after lock.

No procedure enters the body-card hand by implication. A rare future Brain Part may
explicitly affect an inventory action, but it cannot waive ownership, timing, the one-
inventory-action limit, source legality, atomic execution, or structured evidence.
Runtime, procedure content, Brain content, values, and UI remain unchanged.
