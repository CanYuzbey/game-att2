# Game att2 - Combat, Body, and Blood

Status date: 2026-08-22

Status: **CURRENT LIVING PAPER-DESIGN AUTHORITY. PROVISIONAL VALUES ARE LABELLED;
CURRENT SIMULATOR RULES REMAIN IN DOCUMENT 03. NO MIGRATION OR RUNTIME APPROVAL.**

## Body and capability

The body has six slots: Head, Torso, Left Arm, Right Arm, Legs, and Core. Every
voluntary action, preparation, tool use, procedure, and automatic response declares
its required physical sources.

| Source state | Future paper capability |
|---|---|
| Intact | Full authored profile |
| Damaged | Strained profile with one visible local deterioration |
| Critical | Authored Desperate profile or Dormant |
| Occupied/Reserved | Temporarily Dormant when incompatible |
| Disabled/Ruined/Severed/Missing | Offline; dependent opportunity Invalid |

Damage primarily affects actions owned by that source. Another valid limb is not
weakened merely because both belong to the same actor. Multi-source actions use the
weakest required source. There is no hidden source substitution after commitment.

Local profiles may alter one declared axis such as effect, cost, exposure,
information clarity, target access, or defense quality. A Desperate profile must show
its additional price or risk.

Every technique card declares the exact source or source set and the minimum source
condition required to play it. The condition scale and thresholds are `OPEN`; values
such as `2/6 arm` or `4/6 legs` are examples only. A card that fails its minimum is
Dormant/illegal, not silently weakened into legality unless that card declares a
separate Strained/Desperate profile.

## Whole-body depth

Source-local consequences remain primary. The earlier paper package also permits a
small, visible, capped `Integrity Echo` derived from deterioration relative to the
actor's own coherent encounter-start body—not ideal human anatomy. Its exact inputs
and values remain provisional, and it may never change legality, slots, action count,
Lead, wounds, Blood, death, surrender, success, or failure. It must not duplicate the
same axis already worsened by local source damage.

## Wounds

Integrity, limb state, wound, treatment state, Blood, and harvested-part quality are
separate facts.

Four paper wound families are approved:

- `Closed Trauma`: structural/capability pressure without ordinary bleeding.
- `Open Wound`: exposed injury with continuing Blood pressure.
- `Major Wound`: urgent destructive attached injury.
- `Severed Stump`: donor wound after a part is removed.

Each slot holds at most one dominant active wound. A stronger result escalates it;
weaker duplicates do not stack. The second qualifying unresolved Major result Ruins
an attached arm or Legs without silently Severing it. Head, Torso, and Core use their
separately authored catastrophic rules.

Treatment states are Untreated, Controlled, Stabilized, and Resolved. Treatment does
not restore integrity or Blood. Repair does not treat a wound. Blood restoration does
not repair or treat. Grafting replaces Severed/Missing anatomy and is not repair.

## Provisional WNR-0.1 values

These are paper comparison values, not final balance or runtime configuration:

| Wound/profile | Immediate Blood | Periodic Blood |
|---|---:|---:|
| Closed Trauma | 0 | 0 |
| Open Wound | 3 | 5 |
| Major Wound | 8 | 8 |
| Clean Stump | 10 | 8 |
| Violent/Improvised Stump | 15 | 12 |

- Aggregate periodic wound loss caps at 20 per tick.
- Control: representative cost 8; suppress two wound ticks.
- Stabilize: representative cost 12; lasts for the encounter.
- Field Repair: cost 10; restore 25% maximum integrity, capped at 70%; cannot revive
  Ruined.
- Reconstructive Repair: cost 18; attached Ruined part returns to 35%/Critical, once
  per slot per encounter; cannot target Severed/Missing.
- A card creates Wound Stress only when it visibly declares it: 2 Blood for Open,
  4 for Major. There is no universal random self-injury roll.

The current runtime `BLEEDING` behavior remains authoritative until a separate
migration prevents double charging.

## Ruined Torso

An attached Ruined Torso creates a visible pending fatality. The actor receives its
next ordinary Main opportunity to reach Stabilized or Resolved using a real legal
source. Control or repair alone is insufficient. Refusal, skipping Main, or failing
to stabilize produces catastrophic Torso failure. Limb for Life cannot prevent that
non-Blood fatality.

## Defense

Defense has bounded layers:

```text
chosen preparation/stance, if any
-> one automatically surfaced legal reflex-defense route
-> one compatible passive per unresolved consequence type
-> final recipient, integrity, wound, Blood, and capability consequences
```

Block, Intercept, and Dodge/Evade are response routes, not hand cards. The incoming
action and current body/build determine legality. An unusable, unreachable, or
incompatibly committed source removes the route. Prepared defense and its linked
reflex are one defense, not duplicate reductions.

Guard Flesh, Brace, Braced Legs, and Cover It retain their paper roles and existing
runtime boundaries. Cover It and detailed Dodge/Evade remain unimplemented.

## Target regions and no-range boundary

Each offensive technique selects one declared target body region before commitment.
The player can inspect whether that target is legal, what state change is expected,
which capabilities depend on it, and whether the intended limb reward is endangered.
Targeting is therefore a strategic choice, not a cosmetic damage-location label.

The active demo has no `Clinch`, `Engaged`, `Distant`, reach band, range counter,
neutral settling, or voluntary reposition system. Do not rename or reintroduce this
removed system through card tags, target rules, camera changes, or hidden legality.
Ordinary traversal stops while the interaction state is paused.

Exact target regions, per-region effects, multi-region attacks, defense redirection,
and target-preview grammar remain `OPEN`.

## Procedures and inventory

Treatment, Blood restoration, repair, claiming, extraction, salvage, grafting, and
table operations reserve exact sources/objects and pay ordinary costs when execution
begins. Cancellation before execution creates no partial mutation. Once a procedure
begins, its declared chain completes atomically.

Extraction creates two separate records: the donor's structural/wound consequence
and one harvested object. Treating the donor cannot improve that object. Clean quality
does not imply donor safety. Basic attacks do not create premium Clean harvest.

For the active demo, a harvested/transferred body part can be created only from a
living actor after state-derived surrender and an accepted survival bargain grant
access. Corpse extraction is prohibited. Killing the actor removes access to that
part reward for the current day.

Surrender is not an isolated Blood/HP threshold. Recompute whether the actor can still
threaten, defend, escape, recover, or achieve its objective and whether it still
expects meaningful survival or victory. A surrendered actor accepts the agreed limb
transfer because refusing means resuming a fight it now expects to lose, likely by
death. This is coerced survival bargaining, not free consent. Acceptance enters a
Grafting Table transition; the exact animation, attachment cost, replacement, and
post-procedure state remain `OPEN`.

## Limb for Life

The current tutorial paper package has one visible charge. Its eventual production
reset boundary follows the still-open run definition. After an atomic chain and Panic
Pulse leave Blood at 0, the player may choose one exact attached usable Left Arm,
Right Arm, or Legs, or accept death.

Acceptance atomically:

- consumes the chosen part;
- creates an Untreated Stump;
- creates no harvested object;
- ends the exceptional chain at provisional net Blood 12;
- recomputes every dependent capability and commitment;
- preserves any independent Ruined-Torso fatality.

It consumes no card, item, Preparation, Main, Lead, Reply, or reflex opportunity.

## Shared causal rule

```text
read prior state
-> validate actor, exact sources, target region, timing, and costs
-> derive current local profile and visible modifiers
-> lock/revalidate under the current turn/sequence contract
-> pay when execution begins
-> resolve automatic defense and final recipient
-> apply structure, wound, Blood, inventory, and procedure mutations
-> complete started atomic chains
-> recompute capability and legal affordances
-> resolve Panic, survival, catastrophic, incapacity, and encounter facts
-> emit deterministic evidence
```

Player and enemy use the same causal rules except for visible authored exceptions.
