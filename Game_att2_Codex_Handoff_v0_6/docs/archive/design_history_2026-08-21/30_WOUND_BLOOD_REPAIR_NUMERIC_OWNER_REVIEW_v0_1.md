# Game att2 - Wound, Blood, Repair, and Torso Numeric Package

Status date: 2026-08-16

Status: **OWNER-APPROVED PROVISIONAL PAPER BASELINE - RUNTIME NOT APPROVED; EXACT VALUES REMAIN TUNABLE**

This document supplies the first numeric paper baseline for the wound meanings
approved in document 27. It consumes the action-produced range direction and the
Attention Slot/Preparation/Main cadence without changing either one.

It covers:

- wound creation thresholds;
- immediate and periodic Blood pressure;
- Control and Stabilization duration/cost baselines;
- Field and Reconstructive Repair amounts;
- wounded-limb self-risk;
- the Ruined-Torso rescue requirement and deadline;
- deterministic paper checks and rejection criteria.

The owner approved WNR-0.1 on 2026-08-14 as the provisional paper baseline. This does
not authorize runtime migration, configuration changes, new items/cards/characters,
final balance, or human-experience claims. Exact values may be rearranged after every
system that affects them or is affected by them is defined and tested.

The approved meanings and relationships must not change silently during tuning:

- Closed Trauma has no ordinary Blood pressure;
- Open is lighter than Major;
- violent Stump pressure is greater than clean Stump pressure;
- Control is temporary while Stabilization lasts for the encounter;
- repair is separate from treatment, Blood restoration, and grafting;
- ordinary wounded-limb use is free, while authored Wound Stress is previewed;
- Ruined Torso receives one explicit rescue window.

The exact numbers in the tables are configuration candidates, not final balance locks.

## 1. Plain-language result

- A blunt injury can damage or ruin a limb without automatically causing bleeding.
- An Open Wound causes small immediate and continuing Blood loss.
- A Major Wound is urgent but normally leaves at least one meaningful treatment or
  commitment decision.
- A clean stump is dangerous; a violent stump is substantially worse.
- Control buys two wound ticks. Stabilization lasts for the encounter.
- Repair restores attached structure but does not treat a wound or restore Blood.
- Ordinary wounded-limb cards remain free. Only cards visibly marked as stressful
  worsen bleeding.
- Ruined Torso gives exactly one visible rescue window. Stabilization saves it;
  Control alone does not.

## 2. Existing numeric anchors retained

This package keeps rather than discards the current prototype relationships:

| Existing rule | Retained use |
|---|---|
| Basic bleeding `5` | Open Wound periodic loss |
| Severe bleeding `8` | Major and clean-stump periodic loss |
| Periodic cap `20` | Aggregate wound loss per actor per tick |
| Clotting Cream cost `8` | Representative Control cost |
| Blood Bag `25`, or `15` while actively bleeding | Preserved as a treatment-order incentive |
| Panic below `25`, gain `10`, cap `35` | Applies to all new Blood transactions normally |
| Blood `0` | Death unless the existing Limb for Life rule resolves |

The current loose `BLEEDING` tag remains the runtime authority until a separately
approved migration replaces it. These paper values must not run beside that tag and
charge Blood twice.

## 3. Wound creation baseline

A wound is checked only when at least one of these events occurs:

1. an action explicitly declares a wound result;
2. a hit first moves an attached slot into Critical;
3. a single exposed hit deals **more than 50% of the target's maximum integrity**;
4. an attached slot becomes Ruined;
5. a part becomes Severed.

The strongest result from one single-hit resolution is applied once:

| Event | Blunt/closed result | Cutting, surgical, saw, or explicitly exposed result |
|---|---|---|
| First entry into Critical | Closed Trauma | Open Wound |
| Single hit `>50%` maximum integrity without Ruin | Closed Trauma unless action says destructive | Major Wound |
| Ruin | Major Wound | Major Wound |
| Sever | Severed Stump | Severed Stump |

Rules:

- crossing only into Damaged does not create a threshold wound;
- an action-authored wound result may occur earlier than a threshold result;
- exact `50%` does not satisfy the destructive-single-hit rule;
- if Ruin and `>50%` happen together, one Major event is applied, not two;
- multi-hit actions resolve hits sequentially, so two separately qualifying Major
  results can trigger repeat-Major collapse;
- the second qualifying Major on the same unresolved arm or Legs wound Ruins it as
  already approved;
- Head, Torso, and Core do not use the repeat-Major collapse rule;
- no result creates Clean harvest without a separate sever/harvest rule.

The strict `>50%` boundary prevents a 10-damage Grip Strike against a 20-integrity arm
from becoming Major merely because it dealt exactly half. A free basic attack that
eventually Ruins the slot still creates one Major event, as approved.

## 4. Blood-pressure table

| Wound/profile | Immediate loss on creation | Periodic loss | Reopen/aggravation | Wound-stress loss |
|---|---:|---:|---:|---:|
| Closed Trauma | 0 | 0 | 0 | 0 |
| Open Wound | 3 | 5 | 2 | 2 |
| Major Wound | 8 | 8 | 4 | 4 |
| Severed Stump - clean | 10 | 8 | 4 | Not applicable; source is unusable |
| Severed Stump - violent/improvised | 15 | 12 | 6 | Not applicable; source is unusable |

### Immediate loss

- applies once when the dominant wound is created or escalates into a stronger family;
- is a separate Blood transaction and is not limited by the periodic cap;
- triggers Panic, Blood-0, and Limb for Life in the existing order;
- an Open-to-Major escalation applies the Major creation value `8`, not only the
  difference between `3` and `8`;
- a repeat qualifying Major on an existing Major wound applies aggravation `4`, not a
  second creation value `8`.

### Periodic loss

- is calculated at the approved start-of-round wound tick;
- sums all eligible Untreated wounds on the actor;
- is clamped once to `20` after summing;
- is logged as one Blood transaction with per-wound contributions;
- Controlled, Stabilized, and Resolved wounds contribute `0`;
- immediate, action-cost, and wound-stress Blood are not included in this cap.

### Repeat and escalation

- repeating Open on an Untreated Open wound applies reopen `2` and does not create a
  second record;
- a qualifying hit on a Controlled Open/Major wound applies its reopen value, returns
  it to Untreated, and clears remaining Control ticks;
- a new qualifying Major or Sever result breaks Stabilization, applies the new
  creation result, and returns the wound to Untreated;
- an ordinary Open result does not break Stabilization unless the action explicitly
  declares `REOPEN_STABILIZED`;
- no wound worsens through an unshown random roll in this baseline.

The last rule is deliberate: urgency comes from visible Blood pressure, later hits,
and chosen exertion rather than a hidden deterioration coin flip.

## 5. Treatment states and representative paper costs

The shared wound effect does not require every item, skill, spell, or table action to
use the same fictional source. For comparable paper testing, use these neutral test
profiles:

| Effect | Representative timing | Blood cost | Result |
|---|---|---:|---|
| Control | Preparation | 8 | Suppress the next two periodic ticks for one eligible wound |
| Stabilize | Main | 12 | Suppress normal periodic loss and worsening for the rest of the encounter |
| Resolve | Between-encounter/table timing | Content-defined later | Close the wound and clear active Major Trauma; does not restore integrity |

These costs are test tokens, not new item definitions. Existing Clotting Cream retains
its current runtime Fast timing and cost until the item-timing and migration gate.
Anna's Black Stitch retains its authored encounter route rather than automatically
charging the generic Stabilize cost.

### Controlled

- store `control_ticks_remaining = 2`;
- each eligible periodic wound tick is suppressed and then subtracts one;
- after the second suppressed tick, the wound returns to Untreated;
- a new qualifying reopen/escalation clears the remaining ticks immediately;
- Control does not clear Major Trauma, repair integrity, restore Blood, or rescue a
  Ruined Torso.

### Stabilized

- lasts for the remainder of the encounter;
- contributes no normal periodic Blood loss;
- satisfies exposed-wound requirements for repair;
- does not clear Major Trauma or restore capability;
- can be broken only by a new Major, Sever, or explicitly marked stabilized-reopen
  result.

### Resolved

- is normally outside the active duel;
- clears the active wound's Major Trauma mark;
- does not repair a Ruined part;
- does not restore Blood;
- preserves the wound history for evidence.

### Blood Bag interaction

For the paper package, "actively bleeding" means at least one Untreated Open, Major,
or Stump wound. Blood Bag grants `15` in that state. If every wound is Controlled,
Stabilized, Resolved, or Closed Trauma, it grants its normal `25`.

This makes treatment order meaningful without merging treatment and Blood restoration.

## 6. Integrity-repair values

Repair is a Main commitment in the representative combat paper profile. A future
source may use different timing only when its card states the tradeoff explicitly.

| Repair profile | Representative Blood cost | Structural result | Ceiling/limit |
|---|---:|---|---|
| Field Repair | 10 | Restore 25% maximum integrity, round half up | Cannot exceed floor(70% maximum); cannot repair Ruined |
| Reconstructive Repair | 18 | Set attached Ruined part to floor(35% maximum) and Critical | Once successfully per slot per encounter; cannot target Severed/Missing |

Representative results:

| Maximum integrity | Field delta | Field ceiling | Reconstruct to |
|---:|---:|---:|---:|
| 25 | 6 | 17 | 8 |
| 30 | 8 | 21 | 10 |
| 35 | 9 | 24 | 12 |
| 45 | 11 | 31 | 15 |

Rules:

- Closed Trauma may be Field Repaired directly;
- an Open or Major wound must be Controlled or Stabilized before Field Repair;
- Reconstructive Repair requires Stabilized or Resolved;
- Field Repair may restore Critical to Damaged but never to Intact;
- Reconstructive Repair restores only to Critical; a later separate Field Repair is
  needed to reach Damaged;
- repair never clears wound family, treatment cost, Major Trauma, Blood already lost,
  graft stability, or harvest state;
- a second reconstruction of the same slot in one encounter is rejected atomically;
- repair costs are validated before commitment; invalid repair consumes nothing;
- the existing Grafting Table torso option remains unchanged until its own migration
  explicitly maps its definition change into this contract.

The ceilings stop repeated repair from resetting a fight, while the percentage values
remain useful across current 25-45 integrity parts.

## 7. Wounded-limb self-risk

Ordinary limb use has no wound surcharge. A card must visibly declare `WOUND_STRESS`
before this rule applies.

After the action resolves:

| Source wound state | `WOUND_STRESS` consequence |
|---|---|
| Closed Trauma | No Blood loss; only a separately printed integrity cost applies |
| Untreated Open | Lose 2 Blood |
| Untreated Major | Lose 4 Blood |
| Controlled Open | Lose 2 Blood, clear Control, return to Untreated |
| Controlled Major | Lose 4 Blood, clear Control, return to Untreated |
| Stabilized Open/Major | No effect unless the card explicitly breaks Stabilization |
| Resolved | No wound-stress effect |

If a card explicitly breaks Stabilization, apply the same `2` or `4`, return the wound
to Untreated, and preview that result before commitment.

For multiple required wounded sources, sum the visible source consequences. This is
not part of the periodic `20` cap. The action resolves before the self-risk transaction,
so a desperate final action can succeed and then trigger Panic, Limb for Life, or
death. The preview must show that possibility.

A card may print a different integrity or Blood consequence, but an exception is
explicit, source-specific, and logged. There is no universal random self-injury roll.

## 8. Ruined-Torso rescue contract

When an attached Torso becomes Ruined:

1. create/escalate its Major Wound and apply immediate loss `8`;
2. set `TORSO_FATALITY_PENDING`;
3. finish the current action and normal immediate Blood/Panic/Limb-for-Life checks;
4. defer this Torso wound's first periodic contribution so the actor receives the
   promised rescue decision; other wounds still tick normally;
5. at the actor's next Decision Refresh, surface a legal Stabilize opportunity if the
   actor actually owns a valid source, item, skill, spell, or system affordance;
6. the actor has its Preparation and Main window to reach Stabilized or Resolved;
7. at the end of that Main opportunity, remove pending fatality if rescued; otherwise
   apply `CATASTROPHIC_TORSO_FAILURE` and death.

Additional rules:

- Control alone is not rescue;
- a surfaced rescue occupies the appropriate existing Attention Slot duty and its
  declared Preparation/Main timing; it creates neither a bonus slot nor a bonus play;
- integrity repair alone is not rescue and is normally blocked until Stabilized;
- taking a non-rescue Main action is an explicit refusal: that action resolves, then
  catastrophic death applies;
- skipping Main also reaches the deadline;
- the selector may surface only an actually legal rescue; it cannot invent medicine;
- if no rescue exists, the actor still sees the fatal state and may take one final
  legal Main action;
- an encounter cannot record the actor as a survivor while Torso fatality is pending;
- Blood-0 death can still happen earlier through another transaction;
- Limb for Life prevents Blood-0 death only; sacrificing a limb does not stabilize a
  Ruined Torso;
- player and enemies use the same deadline and legality rules.

For paper comparison, a generic valid Stabilize test token uses the representative
Main cost `12`. This is not a promise that every build receives such a token.

## 9. Causal transaction order

```text
validate action, source, timing, target, and stated costs
-> pay declared action costs
-> resolve integrity damage and state transition
-> choose the strongest wound trigger from this hit
-> mutate or escalate the one dominant wound
-> apply immediate or aggravation Blood transaction
-> recompute capabilities and Attention Slot validity
-> apply Torso pending-fatality state if required
-> finish action consequences
-> apply printed WOUND_STRESS after action resolution
-> resolve Panic, Blood-0, Limb for Life, incapacity, and encounter viability
-> at the wound tick, aggregate untreated periodic pressure and clamp to 20
-> at the next decision window, enforce any Torso rescue deadline
-> log every source and before/after state
```

Rejected actions are atomic. A deterministic self-risk that may become fatal is a
previewed consequence, not an up-front affordability requirement.

## 10. Paper arithmetic check

The following comparison starts at `85` Blood and includes the representative Control
cost `8` or Stabilize cost `12`:

| Wound | After creation | Untreated after 2 ticks | Controlled after 2 ticks | Controlled after tick 3 | Stabilized |
|---|---:|---:|---:|---:|---:|
| Open | 82 | 72 | 74 | 69 | 70 |
| Major | 77 | 61 | 69 | 61 | 65 |
| Clean Stump | 75 | 59 | 67 | 59 | 63 |
| Violent Stump | 70 | 46 | 62 | 50 | 58 |

Interpretation:

- Control is a modest two-tick answer to Open Wound rather than an automatic tax;
- Control is immediately valuable for Major and Stump wounds;
- Stabilize costs more now but becomes the better long-term answer from the third
  periodic tick onward;
- violent severance can push a normal actor into the Dangerous band within two ticks;
- Open `5` + Major `8` + violent Stump `12` totals `25`, then the periodic cap reduces
  the single tick to `20`.

Low-Blood check:

- `30` Blood taking Major creation `8` crosses below `25`, so Panic raises the actor
  to `32`; representative Stabilize then leaves `20`;
- `25` Blood taking Ruined-Torso creation `8` triggers Panic to `27`;
  representative rescue then leaves `15` and alive but Critical.

These checks establish arithmetic and decision separation only. They do not establish
fun, fairness, comprehension, or final balance.

The complete calculations are in the
[designer-only arithmetic ledger](../../../research/wound_numeric/WNR_0_1_DESIGNER_ARITHMETIC.md).

## 11. Required paper cases

Run the same deterministic sequence for both player and enemy:

1. Closed Trauma crossing Critical: structural impairment, no Blood pressure.
2. Open Wound ignored for three ticks.
3. Open Wound Controlled, then allowed to expire.
4. Major Wound Controlled versus Stabilized.
5. Clean versus violent Stump over two ticks.
6. Three simultaneous wounds proving one aggregate periodic cap.
7. Existing Blood Bag before and after Control.
8. Grip Strike ruining a limb without producing Clean harvest or duplicate Major
   events.
9. Two separately qualifying Major hits on an arm/Legs, including one multi-hit action.
10. Field Repair at Critical, its 70% ceiling, and invalid Ruined/Severed targets.
11. Reconstruction followed by Field Repair and rejection of a second reconstruction.
12. Ordinary wounded-limb card with no self-risk.
13. `WOUND_STRESS` from Untreated, Controlled, and Stabilized wounds.
14. Ruined Torso rescued during Preparation, rescued during Main, refused for a final
    action, and lacking a legal rescue source.
15. Blood-0/Limb-for-Life ordering versus catastrophic Torso death.

## 12. Continue, revise, and kill criteria

Continue toward an implementation specification only if paper traces show:

- Closed Trauma never leaks into Blood loss;
- Control and Stabilize have different useful time horizons;
- repeated basic attacks cannot stack unlimited wound records or bypass the cap;
- Field Repair cannot erase Ruin or Major Trauma;
- wounded-limb self-risk appears only on marked cards and is predictable;
- Torso always presents one readable decision window without invented rescue access;
- every Blood mutation identifies its wound/action source;
- player and enemy use identical rules.

Revise values if:

- Control is never chosen for Open wounds or always dominates Stabilize;
- one ordinary Major event routinely forces unavoidable Blood-0 from the Normal band;
- Field Repair replaces offense, treatment, or grafting as the universal best action;
- the periodic cap makes additional visible wounds feel consequence-free;
- `WOUND_STRESS` makes all wounded-limb cards practically unusable.

Kill this numeric model if it requires hidden deterioration rolls, multiple wounds per
slot, a generic action-point layer, free rescue cards unsupported by state, or a
separate repair system for every item/skill/spell source.

## 13. Hostile review

| Risk | Severity | Control |
|---|---|---|
| Two-tick Control may be too generous in short fights | Medium | Compare one- and two-tick variants during paper tests; keep two as baseline because cost 8 exceeds one Open tick of 5 |
| Stabilize cost 12 may become mandatory for every Major | Medium | Preserve Control and finishing/escape choices; do not assume Stabilize access |
| Violent Stump `15 + 12/tick` may accelerate surrender/death too quickly | High | Test against current 70-85 Blood starts and the 20 cap before runtime approval |
| `>50%` threshold favors low-integrity parts differently | Medium | Use percent threshold, strict boundary, source mapping, and current 25-45 integrity fixtures |
| Repair costs may punish already-losing actors | Medium | Test Field Repair against one incoming 8-10 damage action and preserve ceilings |
| Final-action Torso refusal may enable mutual-kill exploits | Medium | Record encounter viability and outcome explicitly; do not erase either death |
| Guaranteed rescue presentation could be mistaken for guaranteed medicine | High | Surface only source-supported rescue and show fatality when none exists |
| Paper arithmetic may be mistaken for fun evidence | High | Keep evidence class explicit; require later human testing |

No P0 contradiction was found. The highest-risk values are violent Stump pressure and
the representative Stabilize cost; both remain paper-test variables.

## 14. Owner approval record

On 2026-08-14 the owner approved **WNR-0.1** as the first provisional paper numeric
baseline, with explicit permission to rearrange numeric values after all connected
systems are defined and their interactions can be evaluated:

- Open `3 immediate / 5 periodic`;
- Major `8 / 8`;
- clean Stump `10 / 8`;
- violent Stump `15 / 12`;
- periodic cap `20`;
- Control cost `8` for two ticks;
- Stabilize cost `12` for the encounter;
- Field Repair cost `10`, restore `25%`, cap at `70%`;
- Reconstruction cost `18`, restore to `35% Critical`, once per slot/encounter;
- Wound Stress `2` Open / `4` Major;
- Ruined Torso must be Stabilized by the end of the actor's next Main opportunity.

This approval promotes the package for future paper specifications and dependency
analysis only. Runtime/configuration implementation requires a separate approved plan,
migration away from the loose `BLEEDING` tag, deterministic tests, exploit checks,
and a fresh balance review.

## 15. Later Package D reconciliation (2026-08-16)

Package D does not change WNR-0.1 values. A modular effect that creates a wound,
Blood loss, treatment, repair, or `WOUND_STRESS` must invoke this numeric contract
explicitly rather than reproducing its arithmetic.

Structural repair may improve a source profile and reduce Integrity Echo when it
restores the actor toward the encounter-start coherent baseline. Control,
Stabilization, or Resolution without structural repair changes wound/Blood pressure
only and does not restore local capability or Integrity Echo. Exact Echo thresholds
and micro-values are separate tunable paper variables.

## 16. Later Package C reconciliation (2026-08-17)

Package C adds no Blood, wound, treatment, repair, integrity, or readiness cost for
range maintenance. Any such consequence must be explicitly authored and previewed by
the action profile, then invoke this numeric contract. Range cannot treat a wound,
restore Blood, repair structure, rescue a Ruined Torso, or alter `WOUND_STRESS`.
Runtime and values remain unchanged.

## 17. Later Package B reconciliation (2026-08-17)

Document 36 fixes commitment flow without changing WNR-0.1 numbers. Control and Blood
restoration may use Preparation; repair and ordinary Stabilize use Main; exact future
profiles remain explicit. Ordinary costs pay on execution, and a pre-execution
cancellation does not spend Blood or apply partial treatment/repair. The Ruined-Torso
rescue appears only when a real legal Stabilize source exists and uses the normal
timing budget. Runtime and values remain unchanged.

## 18. Later Package A catastrophic-survival reconciliation (2026-08-19)

Document 37 resolves the previously open case 15 boundary. Limb for Life may answer
Blood 0 after Ruined-Torso creation, but `TORSO_FATALITY_PENDING` and its deadline
remain. It never answers `CATASTROPHIC_TORSO_FAILURE`. A legal Stabilize procedure
whose execution cost reaches Blood 0 completes atomically before Blood survival is
checked. The accepted sacrifice creates an Untreated Stump and ends its exceptional
chain at provisional net Blood 12; later stump pressure remains. WNR-0.1 values and
runtime remain unchanged.
