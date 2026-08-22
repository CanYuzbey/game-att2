# Game att2 - Combat, Body, and Blood

Status date: 2026-08-23

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

## Active-demo Blood reward boundary

`PAPER RULE`: the active demo's ordinary opponent-derived Blood gain requires killing
that opponent. An eligible kill outcome grants a positive Blood reward sourced from
the dead opponent and permanently closes access to that opponent's limb reward for
the current day. Merely damaging, wounding, disabling, or bringing the opponent to a
surrender state grants no Blood.

Accepting a living, state-derived surrender produces the opposite reward: the agreed
limb becomes available through the Grafting Table, but the player receives no
kill-Blood reward. Corpse limb extraction remains prohibited. The Blood reward is not
a limb object and does not reopen corpse-part access.

The exact Blood yield, collection timing and presentation, whether wound state changes
yield, maximum/cap behavior, and relation to voluntary Blood spending remain `OPEN`.
Named internal emergency effects such as Panic Pulse are not opponent-derived reward
gains and retain their separate contracts. No ordinary active-demo item, damage event,
surrender, or objective completion grants Blood; a later owner decision is required
to add another ordinary acquisition route. No active-demo runtime implements this
paper rule.

The intended balance is not that surrender always dominates whenever the opponent
has a desirable limb. A player who reaches that opponent without enough Blood for the
intended downstream route may rationally kill for Blood and sacrifice the desired
limb. A different attempt may preserve enough Blood to accept surrender and take the
limb instead. Conversely, earlier choices may leave the player rich in Blood after
making that limb inaccessible. These states must follow disclosed prior choices and
state mutations; current Blood must never secretly control whether the desired limb
spawns.

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

`PAPER RULE`: the active demo places its short timing input on incoming defense, not
on player attack cards. Playing `Punch`, `Kick`, `Headbutt`, or another offensive card
declares and pays for the attack; it does not start an attack-side QTE.

Every incoming attack must expose one redundant threat cue before its consequence:

| Cue | Meaning | Legal reflex routes |
|---|---|---|
| Yellow | The attack can be met physically | `Block` or `Parry` |
| Red | The attack cannot be blocked or parried | `Evade` only |

Yellow and red are semantic labels, not permission to communicate through color
alone. Production presentation must pair color with at least one distinct readable
shape/icon, animation language, or audio cue. Cue duration, exact animation, audio,
input binding, and accessibility-assist values remain `OPEN`.

The three active-demo defense routes are:

| Route | Paper consequence |
|---|---|
| `Block` | Against Yellow, choose another legal usable body part and interpose it before the declared target. The original target avoids the direct hit; the chosen guarding part becomes the final structural recipient, loses Integrity, and may lose dependent capability. Exact loss, eligible guarding slots, and wound/Blood escalation remain `OPEN`. |
| `Parry` | Against Yellow, attempt the deliberately narrow precision window. Success prevents all incoming Integrity, wound, and Blood consequences from that attack and reduces the attacker's visible `Will (İrade)`. A miss applies the original attack without an additional hidden miss penalty. Exact source requirement, window, Will loss, and assistance settings remain `OPEN`. |
| `Evade` | Against Red, use the required avoidance response. Success prevents the incoming consequence; failure applies it. Evade creates no range, distance, or reposition state. Exact source requirement, input form, window, and assistance settings remain `OPEN`. |

Block is therefore body budgeting, not a free universal damage cancel. Repeatedly
shielding with the same part degrades the source and its actions; changing the
guarding part, accepting another injury profile, or later replacing/grafting a part
becomes a tactical body decision. There is no hidden fallback limb when the chosen
guarding source is illegal or fails revalidation.

Defense retains bounded layers:

```text
chosen preparation/stance, if any
-> Yellow Block/Parry or Red Evade reflex opportunity
-> one compatible passive per unresolved consequence type
-> final recipient, integrity, wound, Blood, and capability consequences
```

Block, Parry, and Evade are response routes, not hand cards and do not spend Mana or a
voluntary card play. The incoming cue and current body/build determine legality. An
unusable or incompatibly committed required source removes its route. Prepared
defense and its linked reflex are one defense, not duplicate reductions.

Guard Flesh, Brace, Braced Legs, and Cover It retain their paper roles and existing
runtime boundaries only where compatible with the active-demo rules above. Historical
`Intercept` is represented in the active demo by the player-chosen guarding part in
Block; it is not a fourth QTE route. The frozen simulator and isolated H1/visual-lab
artifacts do not implement or prove this Yellow/Red defense contract.

### DWF-0.1 defense comparison — working hypothesis

`WORKING HYPOTHESIS`: the bounded `DWF-0.1` comparison gives every part explicit
`CanGuard`, `GuardFactor`, `CanParry`, `CanEvade`, and minimum-state tags. Ordinary
Arms support Block and Parry while Full or Strained; Legs support Evade while Full or
Strained. Head, Torso, and Core do not provide a default reflex route, and Legs Block
only when a visible Brace/Guard profile grants it. Desperate sources require an
authored Desperate route; there is no hidden substitution.

For an incoming structural impact `D`, the proposed Block loss is:

```text
projected_guard_loss = ceil(D * 0.75 * GuardFactor)

GuardFactor: reinforced 0.80; ordinary 1.00; fragile 1.20
```

Block is legal only if the chosen source is not the declared target, is available and
Full/Strained, and has at least `projected_guard_loss` Integrity. On success the target
takes zero structural loss and the guarding source pays the previewed amount. This
closes the one-Integrity disposable-shield exploit without an invented overflow rule.
Block itself creates no random wound or Blood loss; only an attack's disclosed contact
profile can apply such a consequence to the guarding source. There is no additional
Stamina, Mana, repeat multiplier, or hidden timing shrink.

The proposed normal-speed contact contract is a minimum `900 ms` cue, Block held by
`250 ms` before contact, Parry within `±90 ms`, and Evade within `±180 ms`. The player
selects the physical defense source on the paused intent surface before the timed
animation. Block, Parry, and Evade use separate remappable digital actions; the first
accepted route commits, and a missed Parry never falls through to Block.

Timing assists are independently `100%`, `140%`, `200%`, or per-route automation;
defense speed is independently `100%`, `75%`, `50%`, or pause-on-contact. Body, Blood,
and Will state never shrink the timing window. Production still requires redundant
shape/animation/audio cues, full remapping, tap/hold alternatives, latency calibration,
practice, and causal early/late/wrong-route/invalid-source feedback. Assistance never
reduces Will effect or reward.

These values are a falsifiable comparison package, not a promoted `PAPER RULE`. The
evidence, formula boundaries, examples, and reject criteria are recorded in
`../research/defense_will_npc_balance_v0_1.md`. In particular, the `0.75` Block
coefficient remains the weakest numeric assumption and must be compared against
`0.60` and `0.90`.

## Will (İrade) and living surrender

`PAPER RULE`: the active-demo duel opponent has a visible `Will (İrade)` state.
Successful Parry reduces it; ordinary damage is not silently treated as Will damage.
Other authored Will mutation sources, starting value, recovery, thresholds, and exact
Parry loss remain `OPEN`.

When the living opponent's Will reaches its broken state, combat surrender and the
limb-bargain opportunity trigger. The actor must still be alive, the agreed limb must
remain legally transferable, and the player must remain a credible threat; a dead
actor or unavailable limb cannot be repaired into a reward by Will. Accepting this
surrender grants the agreed limb through the Grafting Table and no kill-Blood reward.
Continuing to kill instead grants Blood and permanently closes that limb opportunity
for the current day.

Will is the explicit combat-surrender state, not a decorative second health bar. Its
mutations and break must be shown causally, and breaking it does not itself damage,
sever, or transfer a limb. Exact refusal behavior, exceptional actors, dialogue
effects, and whether any non-Parry event can change Will remain `OPEN`.

`WORKING HYPOTHESIS DWF-0.1`: Will is bilateral and means an actor's confidence that
continuing the current conflict can still protect its declared goal and Red Line.
Both ordinary actors start at visible `90 Will`, recover `0` during the encounter, and
lose `24/30/36` after a successful Parry of a visible Routine/Committed/Critical
attack:

```text
Parry Will loss = min(current Will, 18 + 6 * attack commitment tier)
```

Ordinary Integrity, wound, or Blood loss changes Will by `0`. A source explicitly
tagged `GoalCritical` may instead create one named, idempotent shock when it first
becomes Strained (`6`), Desperate (`9`), or Offline (`15`); making the declared
claim/objective unavailable produces `18` instead of the same event's state shock.
Low Will applies no combat-stat, timing-window, or card-cost penalty.

Broken Will opens a `ClaimWindow`; it transfers nothing by itself. Both actors must be
alive, the winner must remain a credible legal threat, and the pre-disclosed claim must
still exist, be transferable, advance the winner's Goal/Need, and preserve the bounded
playability contract after a nonlethal release. An NPC may not inspect the player's
inventory at break and invent the most painful demand. Whether Broken player Will
enforces the disclosed claim immediately or offers one final lethal `Defy` remains an
identity-level `OPEN` owner choice.

## Target regions and no-range boundary

Each offensive technique selects one declared target body region before commitment.
The player can inspect whether that target is legal, what state change is expected,
which capabilities depend on it, and whether the intended limb reward is endangered.
Targeting is therefore a strategic choice, not a cosmetic damage-location label.

The active demo has no `Clinch`, `Engaged`, `Distant`, reach band, range counter,
neutral settling, or voluntary reposition system. Do not rename or reintroduce this
removed system through card tags, target rules, camera changes, or hidden legality.
Ordinary traversal stops while the interaction state is paused.

Exact target regions, per-region effects, multi-region attacks, Block loss values,
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
access. Corpse limb extraction is prohibited. Killing the actor removes access to
that part reward for the current day and instead grants the opponent-sourced Blood
reward defined above.

Surrender is not an isolated Blood/HP threshold. In the active-demo duel, the visible
Will state carries the opponent's remaining resistance and breaks through disclosed
causal mutations, including successful Parry. A surrendered actor accepts the agreed
limb transfer because refusing means resuming a fight it now expects to lose, likely
by death. This is coerced survival bargaining, not free consent. Acceptance enters a
Grafting Table transition; the exact animation, attachment cost, replacement, and
post-procedure state remain `OPEN`.

### Active-demo graft capability-delta comparison

`WORKING HYPOTHESIS`: the first graft is closed as a before/after capability ledger,
not as an item-level or generic stat upgrade. One comparison must disclose:

```text
replaced/filled body slot and procedure cost
-> exact old source capabilities lost or still absent
-> exact new source capabilities gained
-> known cards that change Ready/Dormant/Invalid state
-> one defense, passive, or world-interaction change that is not draw-dependent
-> one physical drawback, burden, wound, or lost route
-> one changed option in a later pre-boss fight or the gate-boss confrontation
```

For the cleanest first causal proof, the relevant technique knowledge exists before
the graft but is source-incompatible. The graft supplies physical permission only;
the player must deliberately place the newly compatible technique in the active deck
at the table. The Brain may not learn it, auto-slot it, or guarantee its draw. A
non-card source capability must also change so the graft consequence can be observed
even when that technique is not drawn immediately.

Negative cases are part of the proof: without the graft the technique stays illegal;
with the graft but without known/slotted technique it does not appear as a card; and a
lost or ruined source makes it Dormant/Invalid again. The kill-for-Blood route and the
living-limb route must each retain a disclosed way to defeat the gate boss; neither
reward may be a disguised mandatory key. Exact limb, technique, cost, drawback, and
the two boss routes remain `OPEN`.

The gate boss is an integrated-combat test, not a graft-shaped lock. If a second
pre-boss fight is used, it must carry the cleanest graft before/after proof so the
boss can combine already-understood rules. If the sample uses only one pre-boss fight,
the boss must expose the downstream graft delta, but that teaching/evidence overlap must
remain visible in playtest interpretation.

### Blood-0 wording clarification — OPEN

The owner's phrase "Blood reaches zero and no passive properties remain" is not yet
promoted as a generic passive rule. Current paper authority checks the named Panic
Pulse and one tutorial-scope Limb for Life opportunity before final Blood-0 death; an
unrelated body passive does not currently keep a run alive. If "passive properties"
means a new family of finite death-prevention charges, that is a separate owner rule
that must replace or compose explicitly with this sequence.

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
