# Game att2 - Initiative and Conflict Resolution Owner Review v0.1

Status date: 2026-08-16

Status: **Package A owner-approved as paper design authority. Runtime,
configuration, individual action content, exact information presentation, and reflex
execution remain unapproved.**

## 1. Decision and boundary

The owner approved Package A: **Public Lead with two intention locks and sequential
causal resolution**.

Each ordinary round has one visible Lead and one Reply. The Lead gains first
resolution, but must prepare and lock a Main commitment first. The Reply receives the
permitted telegraph, then prepares and locks a Main commitment. The two actions do not
become artificially simultaneous: the Lead resolves, all consequences and forced
checks settle, and only then is the Reply's unchanged commitment revalidated.

This document closes the architecture-level initiative/conflict-resolution decision.
It does not authorize simulator or configuration changes. The current simulator order
in document 03 remains the runtime authority until a separate implementation plan is
approved.

## 2. Approved round contract

```text
1. Resolve start-of-round scheduled effects and forced checks.
2. Perform Decision Refresh.
3. Establish and publicly show the Lead.
4. Lead takes Preparation, then locks one Main commitment or passes.
5. Reveal the permitted Lead-intent information.
6. Reply takes Preparation, then locks one Main commitment or passes.
7. Activate explicit on-lock stances, reservations, and their costs.
8. Revalidate and resolve the Lead commitment.
9. Apply all consequences, forced checks, and capability changes; recompute state.
10. Revalidate the Reply's same locked commitment and resolve it if still legal.
11. Resolve end-of-round expiry and neutral range settling.
```

Zero-or-one Preparation and zero-or-one Main per actor remain the approved voluntary
budget. Automatic reflex-defense events are not extra plays and do not occupy an
Attention Slot.

### 2.1 Same-timing scheduled effects

Scheduled effects that share one timing point are collected from the same prior state
and resolved as a deterministic batch. Panic, Limb for Life, death, Torso deadlines,
and other forced consequences then evaluate from the batch result in their authored
order. An actor killed or made incapable during this step cannot make a new round
commitment.

This batch exception prevents arbitrary ordering from deciding genuinely
same-timing outcomes. It does not turn the two voluntary Main actions into a batch.

## 3. Public Lead

- The first-round Lead is authored by the encounter and shown before either actor
  commits.
- After an ordinary completed round, Lead alternates.
- A future explicit action, body effect, or encounter rule may seize or retain Lead,
  but must declare that effect visibly and deterministically.
- There is no hidden initiative roll and no generic Speed statistic.
- Exact body-state contributors are deferred to the next decision package; this
  document defines the timing slot they may affect, not their content.

Lead is therefore a readable tempo resource. It is not a permanent first-player
advantage and it cannot be silently reassigned by AI preference or presentation.

## 4. Two intention locks and information

### 4.1 Lead lock

The Lead may take one legal Preparation, then locks a Main action, its source, target
or target category, current range profile, declared reservations, and any authored
mode. After this lock, the Lead cannot revise the commitment because of the Reply's
choice.

### 4.2 Permitted telegraph

Before the Reply locks, the game exposes at least:

- the Lead action family;
- the visible source;
- the target or target category when the action declares one;
- the current range profile; and
- important possible consequence families that the current information rules allow.

Exact values, hidden modifiers, final success, and the production display grammar
remain later information-design work. The telegraph must be enough to support a
meaningful commitment without becoming perfect foreknowledge.

### 4.3 Reply lock

The Reply then takes one legal Preparation and locks one Main commitment under the
same body, item, range, and Attention Slot rules. The Reply does not receive a
guaranteed counter. Once locked, the Reply commitment becomes visible, but the Lead
still cannot revise.

## 5. Commitment, reservation, and cost timing

Most Main locks reserve their declared source, target, range profile, item, and other
physical commitments. Locking alone does not apply the action's ordinary effect or
pay its execution-time cost.

An explicit protective stance that must already exist before the Lead action—such as
Guard Flesh, manual Brace, or Cover It—activates on lock. Its authored on-lock cost is
paid at that moment and is not refunded merely because the expected attack does not
arrive. This is not a hidden interrupt: it is the already-declared Main commitment.

The content must state whether a cost is:

- **on-lock**, because the state must exist before incoming resolution; or
- **on-execution**, because the cost belongs to an action that actually begins.

Costs cannot silently move between these phases.

## 6. Resolution and automatic defense

Immediately before each locked action begins, revalidate:

- actor viability;
- required and occupied body/tool sources;
- target and target category;
- current range and the card's profile at that range;
- posture and commitments;
- item availability;
- execution-time costs; and
- encounter/objective viability.

If legal, pay the execution-time costs and begin the action. A compatible reflex-
defense event then appears automatically inside the incoming action according to
document 31. It is not played from the hand. The incoming action, body/build, source
legality, range, posture, preparation, and commitments determine which response route
exists and how successful it can be.

Once an ordinary atomic action begins, its declared causal chain completes:

```text
validate and pay execution cost
-> surface and resolve automatic defense if compatible
-> establish final recipient and final pressure
-> apply integrity, wounds, Blood, item, posture, and range mutations
-> run forced consequences
-> recompute capability and legal affordances
```

Damage to the acting source during that chain does not retroactively erase the action.
It changes later capability.

## 7. Lead consequence and Reply revalidation

After the Lead action completes, apply and settle all resulting integrity, wounds,
Blood, range, item, posture, Panic, Limb for Life, death, Ruined-Torso, surrender, and
other forced-resolution facts before considering the Reply action.

The Reply must use the **same locked action**. It may not choose a replacement source,
target, card, or action after seeing the Lead result.

- If the shared range changed, re-evaluate the same card using its authored profile
  at the new range.
- If that profile is legal, execute it.
- If the commitment is temporarily illegal, cancel it and recompute the card as
  Dormant or Ready from current facts.
- If the required source, item, target, or opportunity is permanently gone, cancel it
  and recompute the card as Invalid where appropriate.
- If the encounter has already reached a binding end state, cancel the later action.

No hidden retarget, substitute source, or consolation action is allowed.

## 8. Cancellation and resource contract

| State | Main tempo | Execution-time costs and item uses | On-lock costs | Card result |
|---|---|---|---|---|
| Rejected before lock | Not consumed | Not paid | Not paid | Unchanged/current legality |
| Locked, then canceled before execution | Consumed for the round | Released or not paid | Remain paid | Recompute Ready, Dormant, or Invalid |
| Execution began | Consumed | Paid | Remain paid | Spent; atomic action completes |

Losing a locked Main is the tempo risk of committing second or making a fragile
prediction. Preserving unspent execution resources prevents cancellation from also
charging for an action that never existed in state.

There is no universal interrupt command. A later authored action may define an
explicit pre-execution or multi-stage checkpoint, but it must name the checkpoint,
legal responders, costs, source requirements, and cancellation result.

## 9. Death, catastrophic outcomes, and genuine simultaneity

- Death and Ruined-Torso deadlines are checked at their approved immediate timing.
- A dead or otherwise incapable actor cannot begin its later locked action.
- An approved surrender, escape, bargain, or other binding encounter outcome may
  cancel a later action. Detailed voluntary surrender and negotiation windows remain
  later work.
- A dying actor receives no revenge swing merely because it locked earlier.
- Mutual death is possible only when a genuine same-timing batch or one already-
  started atomic chain affects both actors—for example, an action followed by an
  authored Wound Stress consequence on its user.

This preserves physical causality: sequential intentions are sequential, while truly
shared timing remains shared.

## 10. Integration with approved systems

### Attention Slots and cards

Lead/Reply order changes when each actor commits; it does not add slots or plays.
Decision Refresh occurs before commitment. A canceled locked Main still spends round
tempo, while the card's Ready/Dormant/Invalid state is recomputed from final facts.

### Range

Clinch, Engaged, and Distant remain shared action-produced states. Resolution never
teleports an actor to preserve a plan. The Reply's existing card uses its current
range profile after the Lead's outcome.

### Defense

Prepared defense may activate on lock; reflex defense appears automatically during
the incoming action; compatible passives then apply as document 31 specifies. No
manual Response card or universal defense interrupt is introduced.

### Wounds and Blood

Final recipient and pressure are established before wound/Blood mapping. Damage,
treatment state, self-risk, Torso rescue, and capability changes are fully applied
before the later commitment is revalidated.

## 11. Future acceptance requirements

| ID | Requirement |
|---|---|
| INIT-A-001 | First-round Lead is encounter-authored, public, and deterministic. |
| INIT-A-002 | Lead alternates after an ordinary completed round unless a visible explicit effect overrides it. |
| INIT-A-003 | Lead locks before Reply and cannot revise after Reply commits. |
| INIT-A-004 | Reply receives the permitted Lead telegraph before locking. |
| INIT-A-005 | Both actors use the approved Preparation/Main budget; reflex defense adds no play. |
| INIT-A-006 | Explicit prepared-defense states and costs activate on lock. |
| INIT-A-007 | Ordinary execution costs and item uses are paid only if execution begins. |
| INIT-A-008 | Lead consequences and forced checks fully settle before Reply revalidation. |
| INIT-A-009 | Reply cannot secretly retarget, substitute a source, or select a replacement action. |
| INIT-A-010 | Changed range uses the same card's current authored profile. |
| INIT-A-011 | A canceled locked commitment consumes Main tempo but preserves unpaid execution resources. |
| INIT-A-012 | A started atomic action completes even when it disables its own source. |
| INIT-A-013 | Dead or incapable actors do not execute later locked commitments. |
| INIT-A-014 | Same-timing scheduled effects derive from one prior state and batch-resolve deterministically. |
| INIT-A-015 | Mutual outcomes occur only through genuine batch timing or one atomic chain. |
| INIT-A-016 | Logs distinguish pre-lock rejection, pre-execution cancellation, and started execution. |
| INIT-A-017 | Player and enemy follow the same lock, revalidation, cost, and cancellation rules except for visible authored exceptions. |

Before runtime approval, tests must cover at least Lead alternation, explicit Lead
retention, Lead/Reply information asymmetry, prepared-defense activation, automatic
reflex defense, changed-range revalidation, source loss, target loss, insufficient
execution cost, canceled item use, death before Reply, atomic self-damage, batch
Bleeding, encounter-ending surrender, and deterministic replay.

## 12. Evidence card

| Field | Record |
|---|---|
| Question | Can readable first resolution and constrained counter-commitment create prediction without hidden initiative or artificial simultaneity? |
| Mechanic package | Public alternating Lead, Lead-first lock, bounded telegraph, Reply lock, sequential resolution, full recomputation, and explicit cancellation states. |
| Expected dynamic | Lead trades information exposure for first resolution; Reply trades information advantage for cancellation risk. |
| Desired experience | Players make informed physical commitments, understand why a later action vanished, and can build around tempo without chasing an opaque Speed number. |
| Instrumentation | Lead source, both locks, permitted telegraph, reservations, on-lock costs, revalidation results, execution costs, automatic defense route, final mutations, cancellation reason, and next Lead. |
| Continue criteria | Both order positions offer meaningful plans; cancellation is legible; body/range consequences naturally change the later action. |
| Revise criteria | Reply always finds a perfect counter, Lead alpha-strikes dominate, or cancellations feel causeless or doubly punitive. |
| Kill criteria | The package requires hidden initiative rolls, free post-result replacement actions, manual Response cards, or routine fake simultaneity. |
| Evidence class | Owner-approved paper direction; no runtime or human-experience evidence. |
| Decision owner | Can Yuzbey. |

## 13. Hostile review

| Risk | Severity | Safeguard |
|---|---|---|
| Reply becomes a perfect counter-player | High | Telegraph is bounded; hand, body, source, range, and existing commitments still constrain the Reply. |
| Lead creates unavoidable alpha strikes | High | Automatic build-derived defense remains available; Lead alternates; explicit retention must be authored and visible. |
| Cancellation is excessively punitive | High | The locked Main is lost, but unpaid execution resources and item uses are preserved. |
| Players exploit cancellation to avoid all risk | Medium | Commitment still loses round tempo; no replacement action is granted. |
| Prepared defense pays for nothing | Medium | Only an explicit state that actually activates on lock pays then; the preview must disclose this risk. |
| Range changes create dead hands | High | The same locked card re-evaluates its authored current-range profile and may remain Dormant rather than being discarded. |
| Mutual death is arbitrarily suppressed | Medium | Genuine same-timing batches and shared atomic chains preserve mutual outcomes. |
| Initiative becomes another stat menu | High | Lead is a public token; only explicit authored effects may alter it. No generic Speed score is introduced. |
| Two cost phases become unreadable | High | Every cost is labeled on-lock or on-execution, previewed before commitment, and logged at the phase where it changes state. |

No P0 contradiction was found with documents 27 through 31. The principal complexity
is the two cost timings required to let prepared defense protect before first
resolution without charging ordinary actions that never execute. The explicit labels,
preview, cancellation table, and evidence log are mandatory safeguards.

## 14. Approval record and explicit deferrals

Following the earlier automatic-defense approval, on 2026-08-16 the owner approved
Package A for initiative and conflict resolution. Approved here:

- public deterministic Lead;
- two sequential intention locks with bounded Reply information;
- Lead-first causal resolution followed by full recomputation;
- unchanged Reply commitment and explicit cancellation states;
- on-lock prepared-defense activation versus on-execution ordinary costs;
- automatic reflex defense inside incoming-action resolution;
- atomic started actions and genuine same-timing batches;
- no universal interrupt, hidden retarget, substitute source, or revenge action.

Still deferred:

- exact body-state effects on Lead, initiative retention, or commitment legality;
- individual action/item interruption checkpoints;
- multi-stage treatment, extraction, repair, and graft timing;
- voluntary surrender, negotiation, and escape windows;
- exact intent-information and presentation grammar;
- exact reflex inputs, success calculation, readiness, and repetition;
- runtime, configuration, content, final UI, Unity, and production work.

## 15. Later Package D disposition (2026-08-16)

Document 33 resolves body-state capability mapping on paper. Local source profiles are
derived before lock and re-derived during pre-execution revalidation. A changed source
uses the same action's current Strained/Desperate profile or cancels when no legal
profile remains; source loss follows this document's cancellation table; an atomic
started action still completes. Integrity Echo cannot
seize, retain, or lose Lead, change the Preparation/Main budget, alter card legality,
or replace a source.

## 16. Later Package A2 disposition (2026-08-16)

Document 34 resolves card/item boundaries within this timing model. A readied item or
tool uses Preparation or Main; at most one voluntary inventory-origin action executes
per actor per round; Reconsider cannot refresh a Spent inventory slot; and locked
tools, items, grips, or sources cannot be substituted. Execution-time uses remain
unpaid when a lock is canceled before execution. Runtime remains unchanged. At that
decision point, the next decision was range-maintenance action grammar; the later
Package C disposition below records its resolution.

## 17. Later Package C disposition (2026-08-17)

Document 35 resolves range contest through this existing order. Lead applies its
authored spatial result; Reply revalidates the same locked action at the new range;
if Reply legally executes, its later authored result may replace Lead's state. A
canceled Reply provides no maintenance, release, substitute, or consolation action.
Counters refresh only after legal execution and never stack. Runtime remains
unchanged.
