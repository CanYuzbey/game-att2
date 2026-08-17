# Game att2 - Approved Strategic Defense Contract

Status date: 2026-08-16

Status: **OWNER-APPROVED PAPER DESIGN DIRECTION ONLY; RUNTIME, CONFIGURATION,
DETAILED REFLEX EXECUTION, AND FINAL VALUES NOT APPROVED**

This document records the owner's approval of Package A, revised by the owner's
clarification that reflexive defense is not a card the player manually plays. A legal
reflex-defense event appears automatically when an incoming action, the current build,
and the current physical state support it. The build raises or lowers the response's
effective success profile. The player does not spend an Attention Slot card or a
voluntary action to make that event exist.

This approval closes the architecture-level strategic-defense gate. It does not
activate Cover It in the simulator, change Guard Flesh's current simulator behavior,
implement Dodge/Evade, choose input families, approve production readiness/Stamina,
or authorize new content.

## 1. Plain-language result

Defense has three bounded layers:

```text
chosen preparation or stance, if any
-> automatically surfaced legal reflex-defense event
-> one compatible passive modifier per unresolved consequence type
-> final body, wound, Blood, range, and capability consequences
```

The player may deliberately prepare Guard Flesh or Brace before an attack. When the
attack resolves, the game checks the attack and the fighter's actual build. If that
state supports a reflex defense, the event appears automatically. The player does not
need to draw, hold, or play a Block, Intercept, or Dodge card.

The automatic appearance of the event is not an automatic perfect defense. The
required body source, its condition, preparation, current range, posture, existing
commitments, the incoming attack, and later-approved reflex rules determine how likely
and how effective the response can be. An unusable source always removes the route.

## 2. Owner clarification and optimized interpretation

The owner's phrase "reflexive defense is not something you manually play" is
interpreted as follows:

1. A reflex defense is a transient, event-triggered affordance, not a persistent hand
   card and not a voluntary Preparation or Main play.
2. The game opens the reflex-defense event automatically after validating the incoming
   attack and current build.
3. The incoming attack supplies its compatible and expected response routes. The
   current build filters those routes and modifies their response profiles.
4. If more than one legal route exists, the event may expose one bounded alternate
   route as already allowed by the attack-led, player-directed reflex direction. This
   is choosing how to answer the event, not playing a card to create the event.
5. The later reflex gate decides the actual input grammar, timing model, assistance,
   and exact success calculation. This contract does not reopen that gate.

This preserves strategy: the player chooses the body, preparations, attacks, costs,
and commitments that shape later reflex opportunities. The reflex layer then tests or
resolves the response supported by that state; it does not invent a capability or
replace the strategic turn.

## 3. Approved defense architecture

### 3.1 Layer 1 - chosen preparation or stance

A proactive defense may consume its declared Preparation or Main timing. It declares:

- the required physical source;
- the target or consequence it protects;
- the source and posture it reserves;
- the compatible reflex route it enables or improves, when applicable;
- its cost, expiry, and visible trade-off;
- the Main and reflex routes made incompatible by its commitment.

A prepared defense is not an additional independent percentage reduction unless its
definition explicitly says so. When it improves a reflex route, the preparation and
the route form one defense rather than two stacked defenses.

### 3.2 Layer 2 - automatically surfaced reflex-defense event

For each eligible incoming action, the game automatically evaluates:

```text
incoming action remains legal and declares a reflex-defense route
-> minimum telegraph exists
-> required response source exists, is usable, and can reach the attack path
-> current range and posture support the route
-> source is not incompatibly committed
-> preparation and build modifiers are derived
-> one reflex-defense event is surfaced
```

The event itself consumes no Attention Slot and no additional voluntary play. At most
one active reflex route may resolve against one incoming action unless that action
explicitly defines a multi-stage reflex event. Block, Intercept, and Dodge/Evade are
therefore mutually exclusive routes for the same ordinary incoming action.

### 3.3 Build-derived response profile

The current build does not grant a flat unexplained defense stat. It contributes
traceable facts to a response profile:

- whether the required limb, graft, tool, passive, or equipment source exists;
- source integrity/state and approved tags;
- source-provided defensive properties or explicit passives;
- chosen preparation and reserved source;
- current range profile and posture;
- earlier physical commitments in the exchange;
- attack-defined difficulty, telegraph, blockability, and compatible routes;
- visible exceptions authored by an approved body part or action.

The later reflex specification may translate those facts into a baseline success
band, timing tolerance, grade ceiling, mitigation ceiling, exposure, or another
inspectable success model. It must not let a high result restore an unusable source,
ignore range, bypass a whole-body commitment, or guarantee a perfect counter.

Blood pressure, shared readiness, repetition strain, accessibility profiles, and exact
numeric weights remain deferred to the later reflex gate. This document neither
promotes the visual-lab readiness values nor assumes a hidden random defense roll.

### 3.4 Layer 3 - compatible passive modifier

After the reflex result, one compatible passive may modify each still-unresolved
consequence type. Two passives cannot repeatedly reduce the same damage, Knockdown,
range, or status channel. If several passives match one channel, the highest-priority
applicable effect resolves unless an explicit composite rule says otherwise.

A passive charge is consumed only when its consequence still exists after earlier
layers. A passive is not spent when the reflex route avoids the attack or a prepared
state has already removed that consequence.

### 3.5 Final consequence ownership

Defense resolves before the approved wound and Blood pipeline:

```text
validate incoming action and final response route
-> resolve avoid, reduce, redirect, or prepared prevention
-> apply one compatible passive per unresolved consequence type
-> determine the actual target and final integrity damage
-> resolve wound threshold and dominant wound on that actual target
-> apply approved immediate Blood pressure
-> apply authored range result
-> recompute action and reflex capability
-> evaluate forced consequences and encounter viability
```

Reduced damage uses the final value for integrity thresholds and wound creation.
Redirected damage creates structural, wound, and Blood consequences on the source that
actually receives it. A successfully avoided direct hit does not create that hit's
direct wound. No defense may silently treat wounds, restore Blood, repair integrity,
or improve harvest quality.

## 4. Approved roles

### 4.1 Guard Flesh

- Proactive Main-action guard sourced by the usable Grafted Human Right Arm.
- Retains the current declared Blood cost of `4`.
- Declares one protected body slot for the round.
- Reserves the Right Arm and improves the compatible automatic Block event when a
  blockable direct attack threatens that slot.
- The same arm may execute that Block because Guard Flesh explicitly prepared it for
  that job; this is not incompatible double use.
- Guard Flesh and Block are one linked defense, not two additive damage reductions.
- The arm is occupied and may be exposed by the resolved Block profile.
- If no compatible attack occurs, the guard expires at the round boundary.

The simulator's current `50%` Guard Flesh effect remains the runtime baseline until a
separate implementation gate. This paper contract does not select its future numeric
mitigation or change existing code/configuration.

### 4.2 Brace - Manual Stance

- Proactive Main-action stance sourced by usable Legs.
- Prevents one otherwise-successful Knockdown during the round.
- Does not reduce direct damage, treat a wound, or independently change range.
- Occupies the Legs/posture, so an ordinary Dodge/Evade route is unavailable during
  the same exchange.
- An upper-body automatic Block may still appear when its arm source and the incoming
  action remain compatible because it addresses another consequence with another
  source.
- Retains its current once-per-encounter prototype limit unless later tuning changes
  that value through a separate decision.

### 4.3 Braced Legs

- Passive automatic prevention of one otherwise-successful Knockdown per encounter.
- Requires usable Legs.
- Resolves only if Knockdown remains after the reflex and prepared layers.
- Is not consumed when Dodge avoids the incoming action or manual Brace already
  prevents Knockdown.
- Does not reduce direct damage or create an unauthored range outcome.

### 4.4 Cover It

- Proactive one-round Main-action protection of one declared valued limb.
- Requires another usable, declared covering source; the default physical hypothesis
  is another arm, while any tool or other source requires explicit authored content.
- Opens an automatic Intercept event when a compatible direct attack threatens the
  protected limb.
- A resolved Intercept redirects the protected limb's direct structural pressure to
  the covering source; it does not automatically reduce the redirected consequence.
- The covering source cannot protect itself through this rule.
- Blood costs, self-risk, unblockable effects, and unrelated consequences are not
  redirected unless explicitly authored.
- Its trade-offs are the spent Main action, occupied/exposed covering source, actual
  consequences on that source, and round-end expiry.

Cover It remains inactive in runtime until a separately approved implementation plan,
configuration migration, and deterministic tests exist.

### 4.5 Dodge/Evade boundary

- Dodge/Evade is an automatically surfaced reflex route, not a hand card played after
  seeing the attack.
- It requires a compatible incoming action, usable supporting body source, current
  range/profile, and uncommitted posture.
- A whole-body or Legs-heavy Charge blocks ordinary Dodge/Evade during the same
  exchange unless a visible explicit exception permits both.
- It cannot combine with Block or Intercept against the same ordinary incoming action.
- Clinch, Engaged, or Distant changes occur only when the attack-response profile
  explicitly assigns that result.

No Dodge/Evade content or runtime behavior is approved here.

## 5. Attention Slot reconciliation

Reflex defenses do not enter the persistent Attention Slot hand. Document 29's
Response-capable selection duty is clarified as **Response-supporting**:

- when the body has an eligible proactive guard, stance, intent-reading action, or
  other strategic preparation that can improve a future automatic reflex event, the
  selector may surface one such opportunity;
- the automatic Block, Intercept, Dodge/Evade, or later response event itself never
  occupies an Attention Slot;
- if no Response-supporting strategic opportunity exists, that duty becomes Adaptive;
- adding Attention Slots never grants more reflex events, better reflex grades, or a
  guaranteed counter;
- Ready, Dormant, Invalid, Spent, Reconsider, and Decision Refresh apply to voluntary
  cards, not transient reflex-defense events.

This amendment preserves three starting slots, five developed slots, and the approved
zero-or-one Preparation plus zero-or-one Main budget.

## 6. Source invalidation and interruption boundary

- Every response source is revalidated immediately before the reflex event opens.
- If the source is unusable, unreachable, or incompatibly committed, that route does
  not appear or is canceled with a visible reason.
- No hidden substitute source is selected.
- An independent passive may still apply when its own source remains valid.
- If a valid Block or Intercept redirects/absorbs damage into its source, that current
  response completes before the resulting source state removes future capability.
- Document 32 resolves the default external order and cancellation contract. An
  explicit prepared defense activates and pays on lock; ordinary execution costs are
  paid only when execution begins; a canceled locked Main loses tempo without paying
  unspent execution resources.

## 7. Requirements and future acceptance

| ID | Requirement |
|---|---|
| DEF-A-001 | A legal reflex-defense event appears from the incoming action and current build without a Response card play. |
| DEF-A-002 | Missing, Disabled, Ruined, Severed, or otherwise unusable required sources remove the route. |
| DEF-A-003 | Build facts modify one inspectable response profile rather than a hidden universal defense stat. |
| DEF-A-004 | One ordinary incoming action resolves at most one active reflex route. |
| DEF-A-005 | Preparation and its linked reflex route never apply as duplicate reductions. |
| DEF-A-006 | One passive per unresolved consequence type applies after the reflex result. |
| DEF-A-007 | Braced Legs are not consumed when an earlier layer already removed Knockdown. |
| DEF-A-008 | Charge/ordinary Dodge incompatibility derives from shared source/posture commitments. |
| DEF-A-009 | Redirected consequences use the actual recipient for integrity, wounds, and Blood. |
| DEF-A-010 | Source loss during a completed defense changes future capability without retroactively erasing the response. |
| DEF-A-011 | Reflex events consume no Attention Slot and slot growth grants no extra reflex events. |
| DEF-A-012 | Player and enemy use the same physical legality and consequence contract except for visible authored exceptions. |

Before runtime approval, a later specification must test at least:

- usable versus unusable required source;
- prepared versus unprepared response profile;
- arm committed to another action versus legally reserved by Guard Flesh;
- whole-body Charge suppressing ordinary Dodge/Evade;
- Block, Intercept, and Dodge being mutually exclusive for one action;
- manual Brace preserving the Braced Legs charge;
- Cover It redirection creating consequences on the covering source;
- defense damage preventing versus still crossing a wound threshold;
- source Ruin after a completed defense removing the next opportunity;
- player/enemy symmetry and deterministic evidence;
- no Attention Slot card being required to open the reflex event.

## 8. Evidence card

| Field | Record |
|---|---|
| Question | Can automatic, build-derived reflex defense coexist with strategic preparation and bounded passive protection without becoming free perfect defense? |
| Mechanic package | Package A with automatic event surfacing, one reflex route, one passive per unresolved consequence type, and final-state consequence ownership. |
| Expected dynamic | Build and preparation change which defense appears and its effective profile; source commitment and damage change future defense. |
| Desired experience | The player builds and prepares a body that reacts differently under pressure without playing a separate defense card. |
| Instrumentation | Source legality, attack route, build modifiers, surfaced event, chosen route if alternatives exist, execution result, passive trigger, final recipient, and capability change. |
| Continue criteria | Defense remains body-derived, preparation matters, passives retain distinct value, and no-progress stacking is bounded. |
| Revise criteria | Automatic events feel detached from build, Guard preparation is redundant, Cover It becomes free ablative armor, or passive ordering is unclear. |
| Kill criteria | The contract requires perfect-counter guarantees, hidden defense stats, multiple free active defenses, or Response cards that contradict the owner direction. |
| Evidence class | Owner-approved paper direction; no human-experience or runtime evidence. |
| Decision owner | Can Yuzbey. |

## 9. Hostile review

| Risk | Severity | Safeguard |
|---|---|---|
| Automatic defense removes player agency | High | Strategy chooses build, preparation, source commitments, and risk; any alternate reflex route is bounded and attack-compatible. |
| High-defense build becomes a permanent perfect counter | High | Attack compatibility, one active route, source occupation/damage, one passive per channel, and no guaranteed best route. |
| Attention Slots and reflex events duplicate each other | High | Reflex events are transient system affordances; only proactive support appears in the hand. |
| Guard Flesh double-dips with Block | High | Guard Flesh modifies the linked Block profile and is not a separate additive reduction. |
| Cover It becomes free armor | High | It spends Main tempo, requires another source, redirects full consequences, and expires. |
| Reflex work is silently reopened | High | Inputs, timing, readiness, repetition, accessibility, and numeric success remain deferred. |
| Wounds are calculated on the wrong body part | High | Final recipient and final damage are fixed before wound/Blood resolution. |
| Passive charge is wasted invisibly | Medium | Passive triggers only when its consequence survives earlier layers. |
| AI ignores physical rules | High | Player/enemy legality and consequence rules are symmetric. |

No P0 contradiction was found with the approved wound, range, Attention Slot, or
WNR-0.1 directions. Document 32 later resolves declaration visibility, interruption
order, simultaneous mutations, and canceled-action costs without changing the
automatic-defense architecture.

## 10. Approval record and boundary

On 2026-08-14 the owner selected Package A and clarified that reflexive defense is not
manually played. It appears as a game mechanic and becomes more or less successful
according to the current build. The optimized paper authority therefore approves:

- automatic event surfacing from attack compatibility and build/state legality;
- no Response card or voluntary play required to create the event;
- build-derived, inspectable response profiles;
- one active reflex route per ordinary incoming action;
- chosen preparation -> automatic reflex event -> compatible passive -> consequence;
- the Guard Flesh, Brace, Braced Legs, Cover It, and Dodge/Evade roles above;
- consequence ownership by the actual final target and damage;
- Attention Slot reconciliation through a Response-supporting strategic duty.

Not approved:

- runtime or configuration implementation;
- active Cover It or Dodge/Evade content;
- exact success percentages, damage reduction, timing windows, input families, or
  exposure values;
- production readiness/Stamina or repetition strain;
- final UI, animation, audio, or accessibility implementation;
- new characters, body parts, items, skills, spells, Encounter 3 runtime, or Unity.

## 11. Later disposition

Document 32 resolves initiative/conflict timing. Document 33 later resolves
body-state capability mapping through source-owned defense profiles, centralized
effect delivery, and bounded Integrity Echo.

## 12. Package D defense/effect boundary (2026-08-16)

- Full/Strained/Desperate source profiles may change a defense route's authored
  quality; an Offline source still removes the route.
- Integrity Echo may apply at most one `DEFENSE` micro-modifier and cannot remove or
  create a reflex route, stack onto the same locally degraded axis, or require a
  manual Response card.
- Contact-delivered modular effects evaluate only after the automatic defense and
  actual final recipient are known.
- Avoidance may prevent contact delivery; Block/Intercept/Cover It redirection sends
  compatible effects to the actual recipient.
- Effect protection/resistance and cleansing remain distinct from defense and from
  each other.

Exact defense profiles, effect values, and reflex execution remain runtime/content
deferred.

## 13. Later Package A2 disposition (2026-08-16)

Document 34 resolves card/item boundaries without changing this defense contract.
Preparation items consume Preparation, activated tools consume their declared timing,
and automatic Reflexive Defence/Intercept/passives remain outside cards and the one-
inventory-action limit. Passive equipment does not make an activated use free.
Runtime remains unchanged. At that decision point, the next decision was
range-maintenance action grammar; section 14 records its later resolution.

## 14. Later Package C disposition (2026-08-17)

Document 35 resolves the range consequence boundary. Preparation such as Guard Flesh
cannot refresh range by itself. An incoming action and its one legal automatic
defense route produce one authored final spatial outcome; Block, Intercept, and
Dodge/Evade receive no default maintenance. Source invalidation still removes the
route, and no reflex event gains a slot or voluntary play. Runtime and detailed
defense/range profiles remain deferred.
