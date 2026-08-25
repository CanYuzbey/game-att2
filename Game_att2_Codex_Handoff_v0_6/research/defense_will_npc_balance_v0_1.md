# Defense, Will, and Goal-Driven NPC Balance Research v0.1

Status date: 2026-08-22

Status: **PAPER-ONLY RESEARCH RECORD. EVERY NUMERIC VALUE AND THE GUARD PACKAGE BELOW
IS A `WORKING HYPOTHESIS`; NONE IS A FINAL RULE, IMPLEMENTED BEHAVIOR, OR EVIDENCE OF
FUN.**

## Bounded question

This record investigates only the active-demo decisions named in the owner request:

- Block wear and legal guarding body sources;
- Parry/Evade timing, controls, and accessibility;
- bilateral Will values and legal Broken-Will consequences;
- the Guard's exact demand and the resulting weaker-but-free player states; and
- the minimum goal/need/claim contract that prevents an NPC from behaving like an
  idle body-part container.

It does not decide current card cadence, card damage, the duel actor's identity, the Grafting Table,
the demo ending, full-game world simulation, or an engine/runtime implementation.

## Result in one page

`DWF-0.1 WORKING HYPOTHESIS`:

| Variable | Test value |
|---|---:|
| Ordinary Block transfer | `0.75` of declared structural impact |
| Guard factors | reinforced `0.80`; ordinary `1.00`; fragile `1.20` |
| Default Block sources | Full/Strained Arms with `CanGuard` |
| Default Parry sources | Full/Strained Arms with `CanParry` |
| Default Evade source | Full/Strained Legs with `CanEvade` |
| Cue-to-impact at normal speed | at least `900 ms` |
| Block commitment | held by `250 ms` of authored time before impact and through contact |
| Parry input window | `±90 ms` around contact (`180 ms` total) |
| Evade input window | `±180 ms` around contact (`360 ms` total) |
| Timing assists | `100%`, `140%`, `200%`, or per-route automation |
| Defense speed | `100%`, `75%`, `50%`, or pause-on-contact |
| Standard Will | `90`, visible, bilateral, no passive encounter recovery |
| Parry Will loss | Routine `24`; Committed `30`; Critical `36` |
| Ordinary damage Will loss | `0` |
| Intended competent-player duel band | median `5-7` rounds, to be tested |

The Guard test package starts the captive at `70 Blood` with a complete Full body and
offers one authored exchange:

- pay `20 Blood` and leave at `50 Blood` with the complete body; or
- surrender the Full Right Arm through controlled removal, pay the provisional
  `10 Blood` Clean-Stump consequence, and leave at `60 Blood` with a Missing Right Arm
  and a Controlled stump.

The Guard wants a usable arm because its own guarding arm is failing before a duty
inspection; `20 Blood` is its authored replacement/treatment fund. This is subjective
need coverage, not a universal limb exchange rate.

## Evidence discipline

Evidence grades in this record:

- `A`: developer, publisher, official support, official accessibility guidance, or
  primary study;
- `B`: versioned data extraction or maintained mechanics database;
- `C`: unverified community observation, used only to find risks or a broad range.

No comparable game supplies a correct Game att2 formula. Comparables bound the search
space; the values above remain test seeds.

## Comparable-system findings

| Source | Supported observation | Transfer to Game att2 | Do not copy |
|---|---|---|---|
| [Clair Obscur developer overview](https://blog.playstation.com/2024/08/28/new-clair-obscur-expedition-33-gameplay-fighting-and-exploring-the-flying-waters-region/) and [official patch 1.3.0](https://www.expedition33.com/post/patch-1-3-0-is-now-live) (`A`) | Dodge is the larger safety window; Parry is the more precise mastery route. Story Mode later widened both windows by 40%. | Keep Evade wider than Parry and use `1.40` as the first tested timing-assist multiplier. | Attack-side QTEs, long memorized strings, or perfect reflex erasing all strategic errors. |
| [Sekiro mechanics guide](https://support.activision.com/sekiro/articles/sekiro-shadows-die-twice-game-mechanics) and [official gameplay overview](https://blog.activision.com/sekiro/2019-03/Sekiro-Shadows-Die-Twice-Gameplay-Overview-Trailer-is-Here) (`A`) | Attack and Deflect pressure enemy Posture; Block exposes the defender's finite Posture; Perilous attacks require a different answer. | A successful defense can pressure attacker Will, while safe defense consumes a finite body state. Red attacks can reject Block/Parry. | Regenerating Posture, hidden spam shrink, or making Will a second death bar. |
| [Sifu combat explanation](https://blog.playstation.com/?p=356872) (`A`) | Block fills the defender's Structure; Parry unbalances the attacker; Avoid answers threats differently. | Block, Parry, and Evade need different costs rather than different names for the same cancel. | Four or more defense verbs, directional analog QTEs, or opaque high/low memorization in the demo. |
| [Elden Ring 1.16 data extraction](https://steamcommunity.com/sharedfiles/filedetails/?id=3360984277) (`B`) | Extracted Parry active phases range roughly from 4 to 12 frames at 60 FPS after startup, depending on the tool. | A `180 ms` total Game att2 Parry input window is within a plausible precision range. | Treating unofficial frame data or invulnerability frames as a universal reaction-time law. |
| [CHI PLAY reaction-time study](https://web.cs.wpi.edu/~claypool/papers/reaction-time/paper.pdf) (`A`) | In the tested game tasks, mean response was roughly `325-350 ms`; adding choices substantially increased response time. | Author telegraph duration separately from the narrow contact window. The player must have time to identify a route before precision is measured. | Presenting a 180 ms flash and calling it a meaningful Block-versus-Parry decision. |
| [Xbox cue guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103), [input guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107), and [timing guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/116) (`A`) | Critical information cannot depend on color alone; actions should be remappable; precise or repeated timing needs alternatives. | Independent timing scale, game-speed, route automation, remap, redundant cues, calibration, and practice are part of the contract, not polish. | Lowering rewards because an accessibility option was used. |
| [Battle Brothers morale design](https://battlebrothersgame.com/dev-blog-20-bravery-morale/) (`A`) | Player and enemy morale use the same readable states and change after concrete events. | Will should be bilateral and every mutation should cite an event. | Low Will shrinking QTE windows and causing an accelerating death spiral. |
| [Bannerlord campaign AI](https://www.taleworlds.com/en/Games/Bannerlord/Blog/133) and [barter design](https://www.taleworlds.com/en/Games/Bannerlord/Blog/12) (`A`) | NPCs pursue needs under the same constraints as the player; barter value changes with context and actor need. | Claims must come from an authored need and the NPC must be able to use the result. | A universal price table or an NPC scanning for the player's most expensive possession. |
| [Shadow of Mordor manual](https://www.feralinteractive.com/en/manuals/shadowofmordor/latest/linux/) (`A`) and [Outward defeat scenarios](https://outward.wiki.gg/wiki/Defeat_Scenarios) (`B`) | Enemy victory can advance the enemy and create a remembered or location-specific consequence rather than only death. | A defeated player can survive in a changed body while the NPC visibly advances its own goal. | Persistent NPC memory across Game att2's world reset or a full Nemesis simulation for one demo. |
| [Kenshi official description](https://store.steampowered.com/app/233860/Kenshi/?l=english) (`A`, broad product claim) | NPCs are presented as actors with names, lives, goals, and desires; defeat can continue into another state. | An NPC needs a before/encounter/after activity and a reason to value Blood or a particular function. | Long loss-of-control captivity or reducing people to saleable meat units. |

## DWF-0.1: body-source states

The test reuses the existing research scale as a provisional active-demo comparison,
not as a runtime migration:

```text
ratio = current_integrity / maximum_integrity

Full       if ratio > 0.70
Strained   if 0.35 < ratio <= 0.70
Desperate  if 0 < ratio <= 0.35
Offline    if ratio = 0 or the part is Missing/Ruined/Severed/Disabled
```

Every part carries explicit capability tags. Slot names do not silently grant a route:

```text
CanGuard
GuardFactor
CanParry
CanEvade
minimum route state
```

Default demo tags for the comparison are deliberately small:

| Part | Block | Parry | Evade |
|---|---|---|---|
| Left/Right Arm | yes, Full or Strained | yes, Full or Strained | no |
| Legs | only with an explicit Brace/Guard graft | no | yes, Full or Strained |
| Head/Torso/Core | no | no | no |

A special part may author a visible `Desperate Block`, `Desperate Parry`, or
`Desperate Evade` profile. Without that profile, Desperate and Offline sources are
illegal. There is no hidden substitute.

## DWF-0.1: Block formula

Let:

- `D` be the incoming attack's previewed structural impact;
- `T = 0.75` be the provisional Block-transfer coefficient;
- `G` be the selected part's visible Guard factor; and
- `I` be that part's current Integrity.

```text
projected_guard_loss = ceil(D * T * G)

BlockLegal =
    attack_route == Yellow
    AND source != declared_target
    AND source has CanGuard
    AND source state is Full or Strained
    AND source is attached, available, and not incompatibly committed
    AND I >= projected_guard_loss

on legal Block:
    declared_target_loss = 0
    guarding_part_loss = projected_guard_loss
```

The final `I >= projected_guard_loss` check closes the disposable-one-Integrity shield
exploit without inventing hidden overflow. If the source would collapse before it can
carry the declared pressure, Block is visibly illegal before commitment. A later part
may explicitly author a sacrificial breakthrough profile; the default demo does not.

| Guard profile | `G` | D=5 | D=8 | D=12 |
|---|---:|---:|---:|---:|
| Reinforced | `0.80` | 3 | 5 | 8 |
| Ordinary | `1.00` | 4 | 6 | 9 |
| Fragile | `1.20` | 5 | 8 | 11 |

An ordinary `30 Integrity` Arm facing repeated `D=8` Yellow attacks can legally move
`30 -> 24 -> 18 -> 12 -> 6`; it is then Desperate and loses default Block. This is a
finite body budget, not proof that four Blocks is the final enjoyable number.

Block creates no random wound or Blood loss of its own. The attack's declared contact
profile is re-evaluated on the guarding part: a blunt attack may produce only Closed
Trauma, while an attack explicitly carrying `Open Wound on guard` may open the guarding
part. Repetition has no extra generic card-energy or secret timing penalty; decreasing
Integrity and capability are already the cost.

`T = 0.75` is the weakest numeric assumption in this package. Compare `0.60`, `0.75`,
and `0.90` before promotion.

## DWF-0.1: timing and controls

The incoming attack declares one visible contact event. Timing is evaluated in
milliseconds, not render frames:

```text
corrected_press = raw_press_time - calibrated_device_offset
delta = corrected_press - contact_time

base_half_window(Parry) = 90 ms
base_half_window(Evade) = 180 ms

game_half_window =
    clamp(base_half_window * TimingScale * AttackReadability,
          route_floor,
          route_ceiling)

wall_clock_half_window = game_half_window / DefenseSpeed
success = legal_route AND valid_source AND abs(delta) <= wall_clock_half_window
```

| Parameter | Test values |
|---|---|
| `TimingScale` | Standard `1.00`; Forgiving `1.40`; Extended `2.00`; Auto per route |
| `AttackReadability` | Severe `0.85`; Standard `1.00`; Clear `1.15`, always previewed |
| Parry half-window clamp | `60-240 ms` before speed scaling |
| Evade half-window clamp | `120-450 ms` before speed scaling |
| `DefenseSpeed` | `1.00`, `0.75`, `0.50`, or pause-on-contact |
| Minimum normal cue-to-impact | `900 ms / DefenseSpeed` wall-clock time |
| Block lead at slowed speed | `250 ms / DefenseSpeed` wall-clock time |

The baseline therefore gives Parry `180 ms` total and Evade `360 ms` total. Body
condition, Blood, and Will never shrink these windows. Body state changes legality and
physical consequence; it does not secretly remove an accessibility setting.

Control sequence:

1. The enemy intent surface pauses and previews target, route, source legality, and
   consequence. The player selects a defense source before the timed animation.
2. `Block`, `Parry`, and `Evade` are three separate remappable digital actions. No
   analog direction, simultaneous-button chord, or timed limb-menu navigation is used.
3. Block locks when held no later than `250 ms` of authored time before contact and
   kept held through contact. Defense slowdown expands that lead in wall-clock time.
   It has no precision grade.
4. On Yellow, the first accepted route input commits the result. A failed Parry never
   falls through to a held Block. On Red, Block/Parry produce `Wrong Route`, not a
   hidden Evade.
5. Only one rising input edge is judged per hit. Multi-hit sequences disclose every
   contact and may use a hold/automation assist; input spam never secretly shrinks the
   next window.

Accessibility is a set of independent controls, not one Easy Mode:

- full action remapping and prompts that update to the new binding;
- Timing Scale and Defense Speed controls above;
- separate Auto Block, Auto Evade, and Auto Parry options;
- tap/hold/toggle alternatives;
- Yellow/Red plus distinct icon/shape, animation rhythm, audio pattern, and optional
  haptic pattern;
- independent cue/SFX volume, flash, camera shake, and defense-VFX controls;
- latency calibration and real-enemy practice with no Blood/body loss;
- `Too Early`, `Too Late`, `Wrong Route`, and `Invalid Source` feedback; and
- no reduced Will effect, progression, or reward for using an assist.

Automation can make Parry the dominant route, so balance comparisons must report the
assist profile rather than averaging it into standard play. This is a test risk, not a
reason to punish assisted players.

## DWF-0.1: bilateral Will

Will means:

> The actor's current confidence that continuing this conflict can still protect its
> declared goal and Red Line.

It is not sanity, personality, obedience, hit points, or legal ownership.

```text
standard_max_will = 90
encounter_start_will = 90
passive_encounter_recovery = 0

attack_commitment q:
    Routine = 1
    Committed = 2
    Critical = 3

successful_parry_will_loss = min(current_will, 18 + 6*q)
                              # 24 / 30 / 36
ordinary_integrity_or_blood_damage_will_loss = 0
Broken Will when current_will <= 0
```

The same formula applies to player and NPC. An NPC Parry must come from a visible,
legal stance/route; it cannot be a hidden percentage roll that rejects an already-paid
player card.

One additional explicit event family is included for comparison. Only a source tagged
`GoalCritical` can produce it, and each source/state event fires at most once:

| Newly entered goal-critical state | Will shock |
|---|---:|
| Strained | 6 |
| Desperate | 9 |
| Offline | 15 |
| Declared claim/objective becomes unavailable | 18 instead of the same event's state shock |

This does not turn ordinary damage into Will damage. The UI must name the causal fact,
for example `Guarding arm lost -> Will -15`. Will applies no accuracy, QTE, card-cost,
or defense penalty at low values; those would create a self-accelerating collapse.

An exact independent-round toy calculation uses `75%` Yellow attacks,
Routine/Committed/Critical weights `50/35/15%`, no GoalCritical shocks, and the Parry
success probabilities below. It is a pacing check only:

| Parry success | Median Broken-Will round | 90th percentile |
|---:|---:|---:|
| 35% | 13 | 23 |
| 55% | 8 | 14 |
| 70% | 7 | 11 |
| 85% | 5 | 8 |

The test target is a competent-player median of `5-7` rounds, not a hard round cap.
Fun, perceived fairness, and real success distributions still require human play.
The deterministic calculator is
`defense_will_npc_balance_v0_1_model.py`; it uses exact rational probabilities rather
than random samples and also checks the Block matrix and both G1 release invariants.

## Broken-Will claim gate

Broken Will opens a resolution check; it transfers nothing by itself:

```text
ClaimWindow =
    loser is alive
    AND winner still presents a credible legal threat
    AND claim was disclosed before commitment
    AND claim still exists and is transferable
    AND claim advances winner Goal or closes winner Need
    AND winner can perform its promised Concession
    AND result violates no authored Red Line
    AND a nonlethal release preserves the required playability invariant
```

`WORKING HYPOTHESIS`: when the player breaks, the NPC may enforce exactly the disclosed
claim or one disclosed counterclaim. There is no inventory scan and no free last-second
substitution. Whether the player receives a final `Defy and make the conflict lethal`
choice is still an identity-level owner decision; the formula must not hide it.

The unresolved alternatives are deliberately concrete:

| Variant | Broken-player-Will result | Cost of refusal |
|---|---|---|
| Enforced claim | Apply the valid pre-disclosed claim, then the NPC performs its promised Concession | No further combat choice; the player accepted this risk before commitment |
| One `Defy` | Pause once before transfer; if the player still has a legal physical action, allow rejection | All nonlethal bargaining closes for this encounter, lethal conflict resumes, and there is no second surrender |

Defy is not available to a physically incapable actor and is not a free Will refill,
damage cancel, or claim substitution. This comparison preserves the real owner
question: whether pre-commitment legibility is enough agency, or whether one final
lethal refusal better serves the game's identity.

## Minimum NPC actor contract

NPC purpose has three authored layers:

```text
FactionDoctrine -> RoleDuty -> IndividualActorCard
```

- `FactionDoctrine` defines long-horizon resource logic, allies/enemies, and default
  priorities. It never forces every member to behave identically.
- `RoleDuty` defines the actor's present responsibility: guard a gate, collect debt,
  find treatment, carry a bounty, move goods, or simply reach safety.
- `IndividualActorCard` defines the actual encounter-facing Goal, Need, Want, RedLine,
  Leverage, ClaimList, Concession, and Fallback.

`Capability` and `RiskTolerance` are orthogonal inputs. They change which actions are
viable and how much danger the actor accepts, not what the actor ultimately wants.

`WORKING HYPOTHESIS` purpose families for comparison—not final names or lore:

| Family | Long-horizon doctrine | Typical claims and non-conflict routes |
|---|---|---|
| Blood accumulators / Houses | Turn Blood into debt coverage, treatment, status, or power | Blood payment, authored debt, profitable kill; may trade or withdraw when violence is a net loss |
| Flesh guilds / grafters | Acquire compatible functions while preserving usable tissue | A specified functional limb through living transfer; avoid attacks that would Ruin it |
| Wardens / authorities | Control territory, quotas, custody, and passage | Toll, compliance, service, detention, or access restriction |
| Hunters / claimants | Fulfil a named bounty, proof, capture, or revenge obligation | Death, capture, proof, or one target-specific asset |
| Free / unaffiliated | Survive, travel, heal, exchange information, or avoid factions | Trade, cooperate, flee, ignore, or explicit `NoClaim` |

The same family can contain strong and weak actors. A weak Blood collector may use
debt, allies, or ambush; a strong unaffiliated traveler may have no reason to attack.
`NoClaim` is a valid designed state whenever taking anything would not advance the
actor's Goal or close its Need.

Every consequential NPC needs these authored fields:

| Field | Meaning |
|---|---|
| `Goal` | A world state the NPC would pursue without the player: verb + object + horizon. |
| `Need` | A condition required to keep pursuing the Goal. |
| `Want` | A preferred but substitutable improvement. |
| `RedLine` | A result that is illegal for this actor, not merely expensive. |
| `Leverage` | A fact the NPC really controls now: bindings, key, exit, threat, debt, or custody. |
| `ClaimList` | One primary claim and at most one counterclaim, both authored before play. |
| `Concession` | The exact state change the NPC performs if a claim is met. |
| `Fallback` | What it does when the goal or claim becomes impossible. |

The NPC never generates a demand by scanning player value. It filters its authored
ClaimList, then uses this deterministic lexicographic order:

```text
legal under RedLines and transfer rules
> closes Need
> advances Goal (0..3)
> matches Want (0..2)
> improves survival (0..2)
> costs the smaller Concession (0..2)
> authored tie-break
```

During combat, an action that would Ruin the NPC's desired player asset is illegal
while a viable alternative exists. A simple test score for otherwise legal actions is:

```text
ActionScore =
    5*GoalProgress
  + 3*SurvivalGain
  + 2*AssetProtection
  - 3*SelfRisk
  - 2*FiniteCost
  - 4*DesiredAssetDamage
  - 2*RepeatCount

# every component is authored as 0, 1, or 2; ties use authored priority
```

This score is a bounded comparison aid, not personality. Dialogue and behavior must
make the underlying Goal/Need legible.

The minimum observable proof that an NPC is not an idle resource container is four
moments:

1. **Before:** it performs one Goal-related activity before the player engages it.
2. **Encounter:** behavior or one short line exposes Want and Red Line.
3. **Conflict:** its actions protect the asset it wants and pursue its declared claim.
4. **After:** victory or concession visibly changes what it does next.

The design must answer: `If the player never arrived, what would this NPC do next?`
No full off-screen life simulator is required for the demo.

## G1 Guard actor card and exact release comparison

`G1` is a `WORKING HYPOTHESIS`, not selected canon.

| Field | G1 value |
|---|---|
| Goal | Remain fit for duty through the coming shift inspection. |
| Need | Replace/treat its visibly failing guarding arm before inspection. |
| Want | One compatible Full Right Arm carrying `CanGuard`. |
| Red Line | No Strained/Desperate/incompatible part; never become undefended; never release without need coverage. |
| Leverage | The bound captive, room key, controlled exit, and a disclosed lethal advantage while the player is bound. |
| Primary Claim | Player's `30/30` Full Right Arm. |
| Counterclaim | Exactly `20 Blood`, its authored replacement/treatment fund. |
| Concession | Controlled removal if needed, stump control, unbinding, opened exit, and no pursuit for this same-day attempt. |
| Fallback | Refusal keeps captivity; hostile resistance makes the same claim the Guard's Will objective, with warned lethal escalation if no legal claim remains. |

The failing arm is visible before dialogue: the Guard re-wraps it and checks an
inspection mark beside an exact `20 Blood` clinic/replacement quote. After payment it
moves the Blood/arm toward that task. The demand therefore exists before the player,
has a disclosed reason for the exact number, and would still matter without them.

Starting comparison state:

```text
Blood      70
Head       25/25 Full
Torso      45/45 Full
Left Arm   30/30 Full; Punch, CanGuard, CanParry
Right Arm  30/30 Full; Punch, CanGuard, CanParry
Legs       35/35 Full; Kick, CanEvade
Core       35/35 Full
Headbutt   available from Head
```

| Accepted payment | Released state | Strategic cost |
|---|---|---|
| `20 Blood` | `50 Blood`; body and routes unchanged | Lower survival/economy reserve; both Arms retained. |
| Full Right Arm | `60 Blood` after the provisional `10 Blood` Clean-Stump consequence; Right Arm Missing; stump Controlled for the next two wound ticks | Loses one Punch/Block/Parry source and carries treatment debt; retains Left-Arm Punch/Block/Parry, Kick/Evade, and Headbutt. |

The Guard supplies the initial stump control as part of its Concession; this borrows
the research-only WNR-0.1 `10 Blood` Clean-Stump value and does not promote WNR to final
balance. Continuing treatment timing remains outside this record.

Every nonlethal NPC claim/release must pass:

```text
remaining Blood >= 35
AND at least two Ready attack families remain
AND at least one Block source remains
AND at least one Parry source remains
AND at least one Evade source remains
AND no mandatory traversal interaction is source-locked
```

Both G1 release branches pass this provisional invariant. The invariant is not a
promise that either branch is enjoyable.

If the player attacks and its Will breaks, G1 may take only the already disclosed Full
Right Arm, or `20 Blood` if that authored counterclaim remains payable. It cannot take
Head, Torso, Core, both Legs, the best current graft, or a newly discovered substitute.
If neither claim is legal, it returns to captivity or its warned lethal fallback; it
does not fabricate value.

## Failure and exploit review

- **Perfect-Parry dominance:** Parry gives zero damage plus Will pressure. Preserve
  Red attacks, source legality, and real Block value; if skilled players choose Parry
  on more than `80%` of Yellow attacks, revise the route mix/reward before blindly
  shrinking the window.
- **Double death spiral:** Integrity can remove routes, but Integrity/Blood/Will never
  shrink timing windows. There is no extra Block Stamina or repeat-window decay.
- **Disposable shield:** Full/Strained minimum state plus `I >= projected loss` closes
  one-point sacrificial guarding.
- **Desired-asset destruction:** an NPC may not destroy its own claim while another
  viable action exists. If the claim becomes illegal, only an authored fallback is
  available.
- **Adaptive punishment:** demands come only from ClaimList and appear before combat;
  no wallet/body scan chooses the player's most painful loss.
- **Will as second HP:** ordinary damage gives zero Will loss. Only Parry and named,
  idempotent GoalCritical events mutate it.
- **Player soft lock:** the playability invariant blocks a nonlethal claim that removes
  all required attack or defense sources.
- **Claim farming:** one actor can resolve only one claim/concession per same-day state.
  Surrender still grants no kill-Blood.
- **Cheap intentional defeat:** a Broken-Will claim may not be cheaper for the player
  than the pre-conflict offer unless the NPC's state causally reduced its leverage.
- **Reset mismatch:** NPC goals and state reset with the unaware world. Only the player
  remembers prior attempts; no Nemesis-style NPC memory is implied.
- **Remaining stall risk:** perfect Evade plus a no-cost pass can still create a
  no-change loop. The exact anti-stall resolution remains open and is not solved here.

## Falsifiable D0 checks

These are continuation criteria, not product claims:

- after three demonstrations, Yellow/Red route identification is at least `95%`;
- Standard first-contact Block succeeds `80-95%`, Evade `65-80%`, and Parry `25-45%`;
- after short practice, Standard Parry reaches `55-70%` without experienced play
  remaining above `90%` while ignoring body strategy;
- the intended competent-player Broken-Will median is `5-7` rounds;
- every Block preview names target saved, guarding part, projected loss, resulting
  state, and capability lost;
- an invalid source bypasses legality zero times across the state/source grid;
- every Will change names its exact cause and ordinary damage changes Will zero times;
- a Broken-Will claim is always disclosed, goal-linked, legal, and playable afterward;
- after 30 seconds, a tester can answer what G1 wants, why, what it gives, and what it
  would do if the player never arrived; and
- all accessibility profiles can progress with no reward or Will penalty.

Numerical simulation can reject pacing or legality failures. Only human sessions can
support claims about fun, fairness, mastery, comprehension, or accessibility.

## Single decision requested from the owner

Promote, revise, or reject `DWF-0.1 + G1` as the bounded D0 comparison package before
any runtime work. The identity-sensitive subchoice that must be explicit is whether
player Broken Will enforces the disclosed claim or offers one final lethal Defy.
