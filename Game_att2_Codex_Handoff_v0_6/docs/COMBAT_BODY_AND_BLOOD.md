# Game att2 — Combat, Body, and Blood

Status date: 2026-09-15

**CURRENT LIVING PAPER AUTHORITY — Z fixture v0.1.** Mechanic choices are owner
Z01–Z55 answers; exact numbers/profiles are delegated Z48/A content. Arithmetic
evidence is isolated research, not a demo runtime or human balance result.
Legacy Combat Rules/YAML retain their own behavior.

## P01 — Initial body and capability

Two protagonist profiles have identical starting mechanics. Body Blood is 80/80;
bowl 0/40; Will 90; one reusable cutter, three-use kit, Kit readied.
The prior Right Arm injury has already occurred: do not re-charge its immediate
Open-Wound loss at launch.

| Slot | Maximum | Current | State | Starting wound | Exact capability |
|---|---:|---:|---|---|---|
| Head | 25 | 25 | Full | None | Headbutt; Feint source |
| Torso | 45 | 45 | Full | None | Living structural support; no default reflex |
| Left Arm | 30 | 30 | Full | None | Punch, Block/Parry, kit/cutter/bowl handling |
| Right Arm | 30 | 18 | Strained | Open Wound, Untreated | Weaker Punch, Block/ordinary Parry, item handling; no Charge Parry |
| Legs | 35 | 35 | Full | None | Kick/Evade; eight-direction traversal; ordinary retreat |
| Core | 35 | 35 | Full | None | Living support; no attack/reflex |

Full >70% max, Strained >30% through 70%, Desperate >0 through 30%, Ruined=0.
Missing/Severed are distinct, not 0 Integrity aliases. Ordinary attacks, item handling
and defense require Full/Strained; no default Desperate action is authored.
A lost source invalidates its expression; no hidden substitution or other-arm penalty.
For a 30-max arm: 22 Full, 21 Strained, 10 Strained, 9 Desperate, 1 Desperate,
0 Ruined. Charge Parry from a normal arm requires at least 22.

## P02 — Wounds, treatment, death and charges

Four wound families, one dominant wound per slot. A new stronger wound replaces it,
applies its immediate loss once, and resets treatment. An equal/weaker repeat does
not stack immediate/tick loss; its separately declared structural impact still applies.
A second qualifying unresolved Major result ruins an attached Arm/Legs, not severs it.
Head/Core at 0 are immediately fatal; a ruined Torso follows the rescue rule below.

| Wound/procedure profile | Immediate Blood | Per tick Blood |
|---|---:|---:|
| Closed Trauma | 0 | 0 |
| Open Wound | 3 | 5 |
| Major Wound | 8 | 8 |
| Clean Severed Stump | 10 | 8 |
| Violent/Improvised Stump | 15 | 12 |

Aggregate periodic loss caps at 20 per actor/tick, not per wound. Controlled suppresses
exactly the next two scheduled ticks of that wound; Stable suppresses subsequent
ticks until a new stronger wound or a new operation replaces it. Resolved is no
active wound. Neither Control nor Stabilize restores Integrity or Blood.

| Kit operation | Uses | Actor Blood cost | Source/target | Result |
|---|---:|---:|---|---|
| Control | 1 | 4 | One free Full/Strained tool-capable arm; one active wound | Suppress two wound ticks |
| Stabilize | 1 | 8 | Same | Suppress wound ticks for this attempt until superseded |
| Graft protocol | 1 | 6 surgery + 10 recipient Clean-Stump loss | Free legal Left Arm + cutter + table; living donor bargain | Atomic P08 replacement; donor/recipient wound care included |
| Old-arm return | 1 | 4 surgery + 10 recipient Clean-Stump loss | Same; saved original arm; return-unused | One atomic return, preserving stored condition |

Graft/return use one dedicated surgical kit protocol, explicitly caring for the new
donor stump and recipient attachment in that chain. It does not treat other wounds.
Donor arm removal costs that donor 10 Blood, creates a Stabilized Stump, and creates
one arm object with its pre-removal quality. Recipient removal costs the recipient
10 Blood; the replacement attachment is an Open Wound immediately Stabilized by
the protocol, with no second 3-Blood charge. This is a declared combined operation,
not ordinary kit stabilization applied to unlimited wounds.

Wound Stress is +2 Blood for an Open source or +4 for a Major source on a marked
source-using card, until Stabilized/Resolved. Control suppresses ticking, not stress.
All source-using attack cards/Grip below expose this stress; no random self-injury.
No structural repair, ruined reconstruction, Integrity Echo, Panic Pulse or Limb for
Life is in this demo fixture. The older provisional WNR treatment prices (8/12) are
now 4/8 under Z48/A, to leave a viable initial three-charge maintenance budget;
wound losses retain the WNR numerical baseline.

Ruined Torso sets pending fatality. The next genuinely available player Main must
Stabilize that Torso; Control/repair is insufficient. Stun's removed Main does not
consume the rescue. On a later unprotected hit the opponent targets the next living
vital, not an already-ruined Torso for zero damage. Skipping/failing the available
rescue is fatal. A stabilized ruined Torso stays structurally 0; no repair is fabricated.

Complete started atomic chains before death checks. Then Blood=0 or Head/Core=0
death, then expired Torso rescue, then legal living claims. Simultaneous player/NPC
death records both and grants no continuation reward to the dead player.

## P03 — Defense profiles and timing

Normal arms (Full/Strained) Block/Parry; Legs (Full/Strained) Evade.
A legal Block source is available, not the attacked target, and can pay
ceil(Impact * 0.75 * GuardFactor) Integrity. Ordinary factor 1.00, clean clamp 0.80,
Stressed clamp 1.00. No overflow shield, disposable 1-Integrity guard, automatic
substitute, random Block wound or hidden repeat multiplier.

**Z30/B delegated defense cost:** every accepted Block/Parry/Evade activation pays
1 Blood before timed resolution, success or miss. This is explicitly the player's
use cost, not incoming damage: successful Parry still prevents all incoming
Integrity/wound/Blood effects. Invalid preflight source/route pays nothing; choosing
no legal defense receives the original hit. A failed timed attempt creates no extra
miss penalty beyond its disclosed activation cost and original contact.

| Incoming cue | Legal response | Successful effect |
|---|---|---|
| Yellow shield + two-blade icon | Block or Parry | Block interposes/pays guarding structure; Parry cancels contact and subtracts Will |
| Red broken-shield + feet icon | Evade only | Cancel contact; no reposition/range |
| Boneatour horn/split-arrow Charge icon + explicit text | Charge Parry or Evade; Block illegal | Parry stops Charge and prevents damage/stun, reduces Will; Evade prevents damage/stun but does not stop Charge or affect Will |

Normal cue 900 ms minimum; Charge 1100 ms; Block lock at least 250 ms before contact;
Parry ±90 ms; Evade ±180 ms. D2 preselects source/intent on the paused surface;
Space or a remapped digital action performs it. Inclusive timing bounds use elapsed
input time, not rendered frame count. No state shrinks windows.

Separate window scales 100/140/200%, defense speed 100/75/50% and correctly selected
route automation preserve effects/rewards and source legality. Pause-on-contact,
tap/hold equivalence, remap, practice/calibration, redundant icons, text/audio and
early/late/wrong-route/no-source feedback are required presentation acceptance.
An input that would be a missed Parry never becomes Block. Alt-tab clears input;
returning key releases cannot execute a queued Parry.

NPC defenses share costs, source checks and Will consequences. Their authored
policy attempts ordinary Parry when an available arm and Blood permit it; its
success/miss is an explicit injected outcome in paper route witnesses, not an
engine AI/timing implementation claim. Outgoing player attacks have no player QTE.

## P07 — Actor anatomy and attacks

Six slots always remain; horns are Head-owned subtargets. All player/normals have
living Blood; wounds and structural loss remain distinct.

| Actor | Blood | Will | Head | Torso | Left Arm | Right Arm | Legs | Core |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| Rusk, asymmetric donor | 300 | 90 | 20 | 36 | Missing, healed | 50, Clean clamp | 32 | 30 |
| Mara, human | 300 | 90 | 20 | 36 | 30 | 30 | 35 | 30 |
| Boneatour | 900 | 90 | 600 | 600 | 600 | 600 | 600 | 600 |

Normals start at their maxima except the donor's healed Missing Left Arm; neither
has an active starting wound. Rusk's clamp remains Full and unwounded. NPC goals and
claim outcomes are in [World P07](WORLD_PROGRESSION_AND_DECISIONS.md#p07--actors-and-preauthored-claims).

| Actor/Main | Source | Target | Impact Full/Strained | Cue/tier | Actor cost/contact |
|---|---|---|---|---|---|
| Rusk Clamp Swipe | Right Arm | First living Torso/Core/Head | 8/6 | Yellow, Committed | 1 Blood; Closed Trauma |
| Rusk Stomp fallback | Legs | Same | 8/6 | Red, Routine | 1 Blood; Closed Trauma |
| Mara Straight Punch | Right Arm, else Left Arm | Same | 8/6 | Yellow, Committed | 1 Blood; Closed Trauma |
| Mara Front Kick fallback | Legs | Same | 8/6 | Red, Routine | 1 Blood; Closed Trauma |
| Boneatour Palm Hammer | Higher-current legal Arm, right tie-break | First living Torso/Core/Head | 12/10 | Yellow, Committed | 1 Blood; 4 direct target Blood, Closed Trauma |
| Boneatour Hoof Sweep | Legs | Same | 10/10 | Red, Routine | 1 Blood; 4 direct target Blood, Closed Trauma |
| Boneatour Charge | Head + Legs + at least one live horn | Same | 18 with two horns, 12 with one | Special, Critical | 1 Blood; 6 direct target Blood, Closed Trauma, next-round stun |

Rusk/Mara prefer the named arm Main; reveal the leg fallback only at refresh if arm
unavailable. A Grip cancellation does not silently choose a second source. They
have no Preparation in the route witness; a later authored Brace can use at most
one Preparation and 1 Blood, but it is not in the v0.1 actor catalogue.
Their starting 300 Blood is a conservative paper value: even maximal pre-kill
stalling and NPC activation costs leave at least the declared 30-Blood kill source
under the player's finite pre-reward budget.

## P08 — Living transfers and reward accounting

Transfer quality: Full, unwounded compatible arm plus valid living procedure gives
Clean; attached damaged/wounded source gives Stressed; Ruined/Severed/Missing is
untransferable. Basic attacks alone never create premium Clean.

An installed part preserves the donor's actual maximum/current Integrity. Quality
never normalizes a damaged part into Full or heals it; Stressed rows below are
representative donor conditions, not automatic replacement values. Surgical care
stabilizes the affected attachment slot but restores no structure.

| Arm installed | Maximum/current | Capabilities gained/lost | Physical drawback |
|---|---|---|---|
| Clean Rusk clamp | 50/50 | CanGrip; Block factor .80; ordinary Parry; free Full clamp can Charge Parry; human Right-Punch expression Invalid | Holding consumes that Right Arm for attack/Block/Parry until the opponent's selected response |
| Stressed Rusk clamp | 50/30 | CanGrip, Block factor 1.00, ordinary Parry while >30%; no Charge Parry until Full | Same occupancy; no repair to make it Full |
| Clean human arm | 30/30 | Human Punch/tool handling, Block factor1, normal Full-arm Charge Parry | Loses CanGrip if replacing clamp; no extra technique reward |
| Stressed human arm | 30/18 | Weaker Punch, normal Block/Parry; no Charge Parry | Lower local condition only |

Graft is one table transaction: validate both living actors, agreement, transferable
Right Arm, recipient's free legal Left Arm, cutter, kit use and total 16 Blood.
Commit surgery/stump loss, original-arm removal/storage, one donor object, installation,
wound stabilization and capability recompute once. A failed precondition changes
neither actor, object, Blood, uses nor deck. The optional card swap is a separate
visible knowledge step after surgery, not automatic slotting.

Z34/B stores only the original Right Arm at the first replacement table (normally
A; if the first replacement is Mara's arm, at the S2 care surface). Later replacement
never overwrites that saved original; the removed replacement is disposed. One return costs total
14 Blood and one kit use, reinstalls that arm at its stored 18/30 with stored
Stabilized Open Wound (if treated initially), and removes the currently equipped arm
as a disclosed disposal result. No second arm stock or repeat-return loop is created.
The current attachment starts Stabilized; future stronger wounds and lost cards'
source compatibility are not erased. Return-used flag persists through retreat.
If surgery would leave Blood=0, reject elective nonlethal transfer atomically.

Mara's surrender can provide one ordinary Right Arm for the same 16-Blood/one-use
protocol at the now-accessible maintenance surface, or reward-free mercy. Taking
a human arm is not another free clamp/Concept/Brain award.

Both eligible normal kills give 30 Blood **once, into the 40-cap bowl first**.
Body receives none automatically. Overflow is lost with a preview. Wound quality
does not alter yield. The 300-start NPC budget keeps this yield genuinely sourced;
collection subtracts30 from the killed actor's remaining Blood once; the uncollected
remainder is inaccessible under this fixture. No payout to a dead player.
Kill permanently closes that NPC's limb for this attempt.
Living accepted surrender, service, mercy and ordinary items give zero Blood.

Pour costs one Main and 1 activation Blood, uses a free tool-capable Full/Strained
arm, requires Bowl readied and owned Blood, and consumes no kit use.
Maximum transfer = min(bowl, 80 - body + activation cost). Pay then transfer in one
atomic operation, never create Blood; a cap-full body cannot pour solely to burn/refill.
Readiness is free on a paused out-of-combat care surface; in battle re-readiness
uses Preparation. Activation is part of the chain before final death checking.

## P08 — Two concrete route witnesses

All starting care is paused, with zero exploration tick; first action Stabilize costs
8 Blood and one kit use. Thus body=72, kit=2, original Right Arm still 18/30.
This is a favorable reachable input/Attention fixture, not success for all play.

**Graft/no-kill witness:** Pass and successfully Parry Rusk's three Committed Swipes
with Left Arm: 72 -> 69 Blood, Will 90 -> 60 -> 30 -> 0, clamp 50/50 preserved.
Rusk's own 3 Main costs leave it at297 Blood; extraction/stump leaves287, alive.
Complete 16-Blood/one-kit graft: player=53, kit=1.
Learn/unlock Grip through the first successful Parry achievement; deliberately
replace Right Punch at the table. In Mara round 1, Grip its Right Arm for 2 Blood;
Mara's explicit Parry attempt against Grip misses; Grip causes no base structural
damage and its declared Punch is canceled, demonstrating occupied-clamp loss of Block/Parry.
Release only after that response. Pass/Parry Mara in rounds 2–4 for 3 Blood:
player=48, Mara Will=0. Choose reward-free mercy, no human arm or Blood.
Boss entry: body=48, bowl=0, kit=1, Left Arm30 Full, clamp50 Full, Legs35 Full.

**Kill/Blood witness:** Fixed legal opening Attention includes both Headbutt copies;
NPC's two Parry attempts explicitly miss. Two Headbutts of10 to Rusk Head20 cost
6 Blood; one incoming Parry between them costs1. Player=65, Rusk dies; bowl=30,
clamp opportunity closed. Rusk's own defense/Main costs are recorded separately and
leave ample yield. Care Pour costs1 and transfers16:
body=80, bowl=14. Same two Headbutts and one incoming Parry kill Mara:
body=73, bowl preview14+30=44 ->40, overflow4. Care Pour costs1 and transfers8:
boss entry body=80, bowl=32, kit=2, normal Left Arm30 Full, Right Arm18 Strained.
Player-owned liquid Blood is112, with no clamp or human-limb reward.

Both entries can damage a horn18 using three Full Left-Punch plays of8 (final
overdamage discarded) and three 1-Blood responses: total9 Blood. Then horn count2->1
changes Charge18->12. The no-graft route retains a Full normal-arm Charge Parry;
the clamp is not a key. It is also possible to take no kill-Blood at all: the graft
witness reaches the boss with48. The analytic upper bound deliberately grants more
resources than either witness to test the certain-death claim.

Old-arm return after the A graft: 53 ->39 Blood, kit1->0, original arm18 restored,
clamp discarded and Grip incompatible. Taking Mara's clean human arm instead after
the graft witness: 48 ->32, kit1->0, Grip incompatible, ordinary Right Arm30 Full.
Kill-A then living human-arm transfer: care body80/bowl14, three incoming Parries
->77, human transfer16 ->61, kit2->1; no second kill reward.
These are additional affordable branches, not discarded exceptions.

## P10 — Horns, Charge, Will and fatality

Each horn is an 18-current/max Head-owned nonvascular subpart. Player attacks may
target left/right horn explicitly. Excess horn damage is discarded: no vital overflow
or vascular wound. Losing a horn changes physical Charge once. Parent Head at0 is fatal and
disables both horns, but the 560-damage upper bound cannot reach its600.

Charge requires usable Head/Legs (>30%), at least one horn, Will<=66, and at least
two resolved non-Charge enemy Main opportunities since the previous Charge.
First boss action is familiar Palm Hammer. Otherwise alternate Palm Hammer and
Hoof Sweep, revalidating sources at refresh. A canceled Charge selects a visible
ordinary fallback at refresh. This opportunity counts as non-Charge recovery.
With one horn Charge impact12; with none, Charge becomes illegal and ordinary
attacks continue. No hidden regrowth, health clamp or temporary invulnerability.

A stopped Charge still resets its reuse counter; missed Charge sets next-round
stun once. The cooldown and nonstacking stun leave a later free decision round.
Successful Evade avoids its contact/stun without stopping Charge or Will damage.
Successful Charge Parry requires a free Full arm (normal or clamp); normal Strained
Parry does not suffice. G2 Grip can suppress only the selected ordinary arm action,
never the multi-source Charge.

Will90 falls normally. First break sets one pending Charge-cancel flag; once consumed
it stays consumed. Broken Will does not heal/damage the boss. If horns are already
gone, no legal Charge remains to cancel: display that fact, not a manufactured effect.

Boss Head/Torso/Core/Arms/Legs are bone profiles receiving Closed Trauma from this
catalogue; nonvascular horns bleed0. No Open/Major ticking source is authored for
this boss in v0.1; their biological difference is visible in inspect (Z41/B).
These are explicit anatomy/contact profiles, not blanket immunity to structural
damage, a shared fleshy bleeding profile, or a new life currency.
See [Core P05](CORE_LOOP_ENCOUNTER_AND_RUN.md#p05--finite-state-and-death-bound)
for paid-cost, vital/source and boss-Blood bounds.

## Negative acceptance cases

Require atomic rejection at Blood15/kit0/illegal Left Arm for a16-Blood graft,
Blood14 for elective return, ruined donor, dead donor, double reward/transfer or
repeat old-arm return. Check horn overdamage, both-horn loss, boss Will at0,
Grip held/early release, Charge under Strained arm, exact30/70% boundaries,
failed Parry without Block fallthrough, late/early input, missed Charge then next
stun turn and rescue opportunity, simultaneous death, cap/overflow Pour, retreat
reentry flags and zero-eligible-card redraw. These require future runtime/input tests;
isolated arithmetic checks do not mark them implemented.
