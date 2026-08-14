# Game att2 - Approved Aimed Wound System Direction

Status date: 2026-08-13

Status: **OWNER-APPROVED DESIGN DIRECTION — RUNTIME IMPLEMENTATION NOT APPROVED**

The owner approved this complete aimed-wound design direction on 2026-08-13. It
defines the intended meanings and boundaries and is promoted through the dated owner
amendments in the Development Master, Combat Rules, decision ledger, and current lead
brief. It does not by itself approve configuration, simulator behavior, or numeric
balance. Ordinary runtime limb damage must not create the new wound consequences
until a separately approved implementation package supplies the missing values,
validated configuration, migration, and tests.

Exact Blood values, wound probabilities, recovery times, and final balance are not
chosen here. They depend on the later strategic action-economy and cadence decisions.

### Owner direction incorporated on 2026-08-13

The owner added two required design directions after reviewing the first proposal:

1. items, skills, spells, table actions, or other explicit effects must be able to
   repair limb integrity;
2. a second qualifying Major Wound on the same limb must make that limb unusable.

The principles and optimized operational rules below are owner-approved design
direction. Runtime implementation remains separately gated.

### Approval record

The owner approved every recommendation and all eight decisions in this document:

1. four wound families;
2. repeat-Major collapse to Ruined for arms and Legs;
3. Field Repair, Reconstructive Repair, and graft boundaries;
4. one dominant wound per body slot;
5. lower stump pressure from clean severance than violent severance;
6. player/enemy symmetry with explicit visible exceptions only;
7. Major Wound pressure from a basic attack that Ruins a limb, while still denying
   Clean harvest;
8. conditional fatality with one explicit rescue window for Ruined Torso.

Where later sections retain the word “recommendation,” it records the rationale that
the owner accepted. Explicit non-goals, numeric deferrals, implementation gates, and
required validation remain in force.

## 1. Simple summary

An aimed wound system means the player chooses a body part and that choice changes
what happens next. Damage is not only a smaller health number.

The approved model has five separate questions:

1. **What happened to the body part?** Its integrity and limb state answer this.
2. **What wound was created?** Closed Trauma, Open Wound, Major Wound, or Severed
   Stump answer this.
3. **What can the actor still do?** The limb state and action-source rules answer
   this.
4. **What must be treated now?** The wound and its treatment state answer this.
5. **Can the part be repaired?** A separate integrity-repair effect answers this.

The key rule is: **limb damage and Blood loss are related, but they are not the same
thing.** A crushed arm can be useless without bleeding. A smaller open wound can
bleed while the limb still works. A cleanly removed arm can produce a valuable part
while leaving a dangerous stump on its former owner.

## 2. Approved direction

Use a bounded, aimed wound model with:

- the existing six body slots and existing limb-integrity states;
- four wound families: `CLOSED_TRAUMA`, `OPEN_WOUND`, `MAJOR_WOUND`, and
  `SEVERED_STUMP`;
- one dominant active wound per body slot;
- four treatment states: Untreated, Controlled, Stabilized, and Resolved;
- wound creation only on explicit wound results, meaningful threshold crossings,
  destructive single hits, ruin, or severance—not on every hit;
- separate immediate and start-of-round Blood transactions;
- limb state as the normal owner of capability penalties, preventing double
  punishment from both limb state and wound name;
- separate donor-wound and harvested-part records;
- an explicit `repair_integrity` effect usable by future items, skills, spells, and
  table actions without creating separate repair systems for each content type;
- a visible Major Trauma counter where the second qualifying Major result Ruins an
  attached arm or Legs slot, making it unusable without automatically severing it;
- the same causal rules for player and enemy unless an exception is explicitly
  documented.

This gives the project the useful parts of detailed injury systems—target choice,
urgency, readable consequences, treatment decisions, and body-based stories—without
adding organs, tissue layers, infections, pain simulation, or a large medical menu.

## 3. Authority and evidence boundary

### Current project authority

The following existing rules remain unchanged:

- Blood is health, currency, and ability fuel.
- The body has Head, Torso, Left Arm, Right Arm, Legs, and Core slots.
- Limb integrity and limb state are separate from Blood.
- Wounds may eventually cause immediate Blood loss, periodic loss, both, or neither.
- Blood at 0 causes death unless Limb for Life resolves.
- Basic attacks may disable or ruin, but cannot independently create Clean harvest.
- Harvest quality is Clean, Stressed, or Ruined.
- Current bleeding configuration contains basic `-5`, severe `-8`, and a `-20`
  per-round cap, but those values are legacy prototype values and are not approved as
  the future numeric wound table by this approval.

### Current simulator snapshot

The current runtime does not yet contain wound records or wound families. It stores
`BLEEDING` as a tag on a limb. At the start of a round, each tagged limb separately
applies the configured basic loss. The configured severe-loss value and per-round cap
are not currently consumed by the runtime rules.

This is acceptable only as a narrow prototype placeholder. It creates four gaps that
the later implementation package must close:

1. the tag cannot explain what kind of wound exists;
2. it cannot distinguish immediate loss from ongoing loss;
3. it cannot represent Controlled versus Stabilized treatment;
4. several bleeding limbs can bypass the intended meaning of a round cap because the
   runtime does not currently aggregate them before applying Blood loss.

The migration should replace the loose bleeding fact with state derived from wound
records. It must not keep both systems active, which would charge Blood twice.

### External evidence limit

The examples below are official developer descriptions of systems implemented in
established, shipped games. They show useful methods and production lessons. They do
**not** prove that an injury system caused a game's critical or commercial success.
No claim of market demand, fun, or balance is made for Game att2.

## 4. What other developers did

| Game and method | Useful lesson | Fit for Game att2 | What not to copy |
|---|---|---|---|
| **Battle Brothers:** a serious injury requires a single attack to cross a damage threshold relative to maximum health; injury type depends on weapon type; injury location affects movement, offense, or vision; temporary and permanent injuries serve different campaign purposes. [Official developer explanation](https://battlebrothersgame.com/dev-blog-79-progress-update-injury-mechanics/) | Do not create an injury for every small hit. Use hit magnitude, damage method, and target location. Make an injured actor meaningfully different from a fresh actor. | Strong fit. Game att2 already has target slots, damage sources, limb states, and long-lived body consequences. | Do not add a large catalogue of named injuries or time-based campaign recovery before the core duel cadence is proven. |
| **Kenshi:** vital and non-vital body parts have different failure consequences; untreated damage can deteriorate; bandaging arrests the worsening; blood loss is a separate incapacitation path; severe non-vital damage can lead to limb loss. [Official developer update](https://store.steampowered.com/oldnews/?appgroupname=Kenshi&appids=233860&enddate=1391241600&feed=steam_community_announcements&headlines=0) | Separate structural damage, ongoing deterioration, Blood, treatment, and body-part loss. Treatment should stop a process rather than magically restore the part. | Very strong fit with Blood, stabilization, severance, grafting, and the desired survival pressure. | Do not copy unconsciousness, coma depth, vital-organ detail, or open-world rescue simulation. Game att2 needs a shorter, inspectable duel loop. |
| **Project Zomboid:** different injury types require different treatments, protective clothing changes injury risk, and injuries are made visible through impaired movement, posture, and animation. [Official medical-system update](https://projectzomboid.com/blog/news/2017/02/buildstatus/) and [official animation update](https://projectzomboid.com/blog/news/2019/07/wrong-way-down-a-one-way-streeeet/) | A wound is valuable only if the player can understand its effect and appropriate response. Visible condition is part of the rule, not decoration. | Strong fit with Ritualized Readability and the need to preview target, cost, consequence, and treatment. | Do not add survival-sandbox medical inventory, infection simulation, or many nearly equivalent treatment items. |
| **Dead Space remake:** visible layers of damage and dismemberment provide direct damage feedback and make targeting more strategic. [Official Motive article](https://www.ea.com/ea-studios/motive/news/inside-dead-space-1-remaking-a-classic) | The targeted part must visibly move through meaningful states, and removing a limb must change the threat. | Strong presentation lesson for future UI/art. The current simulator can express the same information through state panels and logs. | Do not copy action-shooter pacing or rely on gore alone to explain mechanics. Every result still needs text/state clarity and accessible alternatives. |
| **Dwarf Fortress:** tissue layers, arteries, fractures, bleeding, pain, surgery, and cumulative wounds create emergent outcomes, but developer logs also show recurring edge cases such as perpetual bleeding and incorrect anatomical interactions. [Official 2009 development log](https://www.bay12games.com/dwarves/dev_2009.html) and [official 2010 development log](https://www.bay12games.com/dwarves/dev_2010.html) | Deep anatomy can produce stories, but every additional layer multiplies rules, bugs, testing, and explanation cost. | Use the causal clarity, not the anatomical depth. Game att2 can produce emergence through six slots, graft identity, wound pressure, and treatment choices. | Do not simulate organs, arteries, tissue layers, embedded objects, pain, malpractice, or detailed surgery in the first complete design. |

## 5. Chosen synthesis for Game att2

The external systems share five successful design methods that fit this project:

1. **Thresholded injury:** meaningful wounds come from meaningful events, not every
   point of damage.
2. **Location matters:** the selected slot changes capability and future options.
3. **Damage method matters:** blunt force, piercing, cutting, and extraction should
   not produce identical wounds.
4. **Treatment controls consequences:** medical action stops bleeding or worsening;
   it does not silently restore integrity.
5. **State must be readable:** the player must see what changed, what will happen
   next, and what can prevent it.

Game att2 adds a sixth method central to its own identity:

6. **Donor consequence and harvested reward are separate:** the quality of a removed
   part and the wound left on the donor are related results of one event, not one
   shared state.

The owner direction adds two more:

7. **Damage can be repaired:** integrity is not only a countdown to permanent loss.
   Repair creates recovery, resource, and build decisions.
8. **Repeated major trauma causes structural collapse:** a player can deliberately
   disable an important limb without automatically earning a severed or Clean part.

## 6. The approved wound model

### 6.1 Layer A — structural condition

Each body slot retains:

- current integrity and maximum integrity;
- limb state such as Intact, Damaged, Critical, Disabled, Ruined, Severed, or
  Missing;
- action sources and approved tags.

Structural condition answers:

- Can this part act?
- At what effectiveness?
- Can it be targeted, extracted, grafted, repaired, or harvested?
- Has the actor lost an action source?

Structural damage does not automatically create Blood loss.

### 6.2 Layer B — wound record

Each body slot may hold at most one dominant active wound. The wound answers:

- Is the injury closed or exposed?
- Does it cause immediate Blood loss?
- Does it cause future Blood loss?
- Can it worsen if ignored?
- Which treatment controls it?

If a new wound is weaker than the existing wound, it does not create a duplicate.
If it is stronger, the existing wound escalates and preserves its history. This keeps
the interface readable and prevents repeated wound spam from becoming the dominant
strategy.

### 6.3 Layer C — treatment state

Treatment state is separate from wound family:

| State | Meaning | Blood effect | Structural effect |
|---|---|---|---|
| **Untreated** | The wound is active and unsecured. | Periodic loss and approved worsening may occur. | Does not change integrity. |
| **Controlled** | Immediate field treatment has arrested current bleeding. | Ongoing loss stops for the defined control window. A new damaging event may reopen or escalate it. | Does not restore integrity or capability. |
| **Stabilized** | The wound cannot worsen for the rest of the encounter unless a rule explicitly breaks stabilization. | No normal wound-generated periodic loss. | The damaged, critical, ruined, or severed part remains in that state. |
| **Resolved** | Later table or long-term care has closed the active wound. | No active wound loss. | May leave a permanent structural condition; restoration requires a separate repair or graft rule. |

`STABILIZED` already exists as a project term. A later rules pass must decide whether
the current tag is migrated to this wound treatment state or retained for a narrower
purpose. This approval does not silently redefine the runtime tag.

### 6.4 Layer D — integrity repair

Integrity repair is separate from wound treatment and Blood restoration.

- **Treatment** controls or resolves a wound.
- **Repair** restores integrity to an attached body part.
- **Blood restoration** changes the Blood resource.
- **Grafting** replaces a Severed or Missing slot with another part.

An item, skill, spell, table action, or future limb ability may invoke the same
`repair_integrity` effect. This avoids building five nearly identical healing
systems. A source can combine repair and treatment only when both effects are stated
explicitly in its definition and evidence.

Every repair source declares:

- compatible target/body tags;
- integrity restored or a configured repair profile;
- maximum resulting state or integrity ceiling;
- whether it can reconstruct an attached Ruined part;
- required wound treatment state;
- cost, timing, uses, and action source once those systems are approved.

Recommended repair categories:

| Category | Eligible target | Recommended ceiling | Purpose |
|---|---|---|---|
| **Field Repair** | Attached Damaged or Critical part; exposed Major/Open wound must first be Controlled or Stabilized | May improve normal integrity, but cannot revive Ruined | A usable combat recovery option without erasing destruction |
| **Reconstructive Repair** | Attached Ruined part after its wound is Stabilized or Resolved | Revives only to Critical on the first reconstruction | Rare recovery that requires another decision before full strength |
| **Grafting** | Severed or Missing slot with a legal harvested part | Uses existing graft integrity/stability rules | Replacement, not repair |

The existing Grafting Table `Repair Damaged Human Torso` option already establishes
repair as part of the project's maintenance loop. A later implementation should
express it through the common repair contract while preserving its approved cost and
definition change until separate balance approval. It must not silently become a
universal in-combat full heal.

## 7. The four wound families

### 7.1 Closed Trauma

Plain meaning: the part is crushed, bruised, fractured, or internally stressed, but
there is no exposed wound represented by the prototype.

Rules:

- default family for blunt damage that crosses a wound threshold;
- may reduce integrity and therefore change limb state or capability;
- normally causes no periodic Blood loss;
- normally causes no immediate Blood loss in the first implementation;
- cannot be treated with Clotting Cream because there is nothing exposed to clot;
- may later require table repair, but detailed recovery is out of scope;
- can escalate to Major Wound if a destructive result ruins the slot.

Player meaning: **the part works worse, but the urgent problem is capability rather
than bleeding.**

### 7.2 Open Wound

Plain meaning: a cut, puncture, tear, or reopened injury has exposed the part.

Rules:

- default family for an approved cutting, piercing, or surgical wound result;
- may cause a small immediate loss, periodic loss, or both once values are approved;
- Clotting Cream or an approved medical action can move it to Controlled;
- treatment stops the wound's Blood pressure but restores neither Blood nor integrity;
- a later strike can reopen or escalate it;
- repeated applications to the same slot escalate/update the existing record instead
  of creating multiple Open Wounds.

Player meaning: **the part may still function, but ignoring it makes future rounds
more dangerous.**

### 7.3 Major Wound

Plain meaning: the part has suffered a destructive exposed injury but remains
attached.

Rules:

- created by a large single hit, a destructive threshold crossing, a Ruined result,
  or an explicitly severe action outcome;
- may combine immediate and periodic Blood loss once values are approved;
- requires urgent control or stabilization;
- can carry approved worsening pressure while Untreated;
- does not automatically kill the actor;
- does not by itself mean the part is harvestable or Clean;
- its capability effect comes from the resulting limb state, not an extra generic
  wound penalty;
- carries one visible `Major Trauma` mark when first created on an arm or Legs;
- a second qualifying Major result on that same unresolved wound causes structural
  collapse under the repeat-major rule below.

Player meaning: **this is an emergency, but the player should still have a visible
choice between treatment, finishing the fight, extraction, or another costly plan.**

### 7.4 Severed Stump

Plain meaning: a part has been removed and the former owner now has a stump wound.

Rules:

- created whenever an attached part becomes Severed;
- the donor receives the stump wound; the removed part becomes a separate harvested
  object;
- may cause immediate and periodic Blood loss once values are approved;
- clean extraction causes lower ongoing pressure than violent or
  improvised severance, but it is never harmless;
- control/stabilization treats the donor wound only;
- treatment cannot improve the harvested part's quality;
- the slot remains Severed or Missing until a separate graft rule changes it.

Player meaning: **a valuable Clean part can exist at the same time as a dangerous
donor wound.**

### 7.5 Ruined Torso is not a fifth ordinary wound family

Ruined Torso should be a special consequence flag resolved after the normal wound
result. Otherwise one label would incorrectly mix structure, bleeding, capability,
and death.

Approved direction: Ruined Torso creates a Major Wound plus **conditional
fatality with one explicit rescue window**. The player sees the required rescue and
the consequence of refusing it. Immediate unexplained death is less interactive;
ordinary nonfatal treatment risks making Torso feel no more important than an arm.

The exact rescue requirement and timing remain deferred until treatment and cadence
rules are approved.

## 8. When a wound is created

A wound check occurs only when at least one of these triggers is present:

1. the action explicitly says it can create a wound, such as an approved Surgical
   Jab result;
2. one hit crosses a configured fraction of that slot's maximum integrity;
3. the hit crosses into Damaged, Critical, Disabled, or Ruined;
4. the action ruins or severs the part;
5. an existing wound is explicitly reopened or worsened.

The resolver considers, in order:

1. action and damage method;
2. single-hit magnitude relative to the slot's maximum integrity;
3. previous and resulting limb states;
4. existing wound family and treatment state;
5. extraction method and harvest result, if any;
6. seeded or scripted randomness only where the approved action requires it.

Chip damage that crosses none of these gates creates no wound. Several small attacks
may still eventually cross a limb-state boundary and then cause one wound check.

### 8.1 Repeat-Major structural collapse

Recommended optimized rule for arms and the current combined Legs slot:

```text
first qualifying Major result
-> one dominant Major Wound, Major Trauma 1/2
-> limb retains the integrity/state produced by the attack

second qualifying Major result before that wound is Resolved
-> integrity becomes 0
-> primary limb state becomes Ruined
-> every action requiring that slot becomes illegal
-> the part remains attached
-> no Clean harvest is created
```

Why `Ruined` is the correct existing state:

- `Ruined` already means attached, unusable, low-value, and unsuitable for normal
  emergency grafting;
- `Disabled` is better reserved for temporary or non-destructive loss of function;
- `Severed` means physically detached and must remain the result of an explicit
  severing/extraction rule;
- setting integrity to 0 makes the structural consequence inspectable and compatible
  with the existing limb-state system.

For a multi-hit action, resolve hits sequentially. If hit one creates Major Trauma
1/2 and hit two independently qualifies as Major, hit two Ruins the limb. An action
that explicitly has a legal sever result may Sever instead; ordinary repeat trauma
cannot impersonate extraction.

Repairing integrity alone does not remove the Major Trauma mark. This prevents a
small repeatable repair from resetting the two-hit threat. The mark clears when the
wound becomes Resolved. If the part was already Ruined, resolution does not restore
it; Reconstructive Repair or grafting is still required.

This repeat-major rule applies to arms and Legs only in the first package.
Head, Torso, and Core already touch death, Focus, Blood-0, and special survival rules;
their second-Major outcomes remain explicit owner choices rather than inheriting a
hidden universal destruction rule.

### 8.2 Integrity-repair resolution

Proposed order for every repair source:

1. validate the source, timing, target slot, compatibility, cost, and remaining use;
2. reject Severed or Missing targets—those require grafting;
3. reject Ruined unless the source explicitly permits Reconstructive Repair;
4. for an exposed Open or Major Wound, require the configured treatment state;
5. commit the action and cost atomically;
6. restore integrity without exceeding maximum integrity or the source's ceiling;
7. recompute limb state and all sourced actions;
8. leave Blood, wound family, Major Trauma marks, graft stability, and harvest quality
   unchanged unless the same source explicitly defines another effect;
9. log the repair and every capability restored.

Recommended default: Field Repair requires an Open/Major wound to be Controlled or
Stabilized; Reconstructive Repair requires Stabilized or Resolved. Closed Trauma may
be repaired directly because it has no exposed bleeding process in this model.

## 9. Qualitative action-to-wound map

This map defines approved meanings, not numeric values.

| Existing action/result | Proposed structural result | Proposed wound result | Harvest result |
|---|---|---|---|
| **Grip Strike / ordinary blunt hit** below a wound trigger | Integrity loss only | None | None |
| **Grip Strike / blunt hit** crossing a meaningful threshold | Existing limb-state transition | Closed Trauma | None |
| **Grip Strike / ordinary attack** ruins the part | Ruined or Disabled according to current rule authority | Major Wound; balance test required because a free attack can now create Blood pressure | Never Clean; current no-free-premium-harvest rule remains |
| **Desperate Swing** | Existing integrity/state result | Closed Trauma by default; Major Wound only on an approved destructive result | Current harvest limits remain |
| **Surgical Jab** succeeds on its approved bleeding result | Existing integrity/state result | Open Wound, or escalation of the slot's current wound | None by itself |
| **Bone Scissors** performs a valid controlled sever | Severed slot | Severed Stump with the lower-pressure sever profile | Clean when current extraction requirements say so |
| **Hell Saw** succeeds | Severed slot | Severed Stump; pressure depends on the approved extraction/result profile | Clean, Stressed, or Ruined remains a separate quality decision |
| **Hell Saw** fails and damages the target | Existing integrity/state result | Open Wound or Major Wound only if the resulting damage supports it; Rage remains separate | No invented premium result |
| **Basic attack at zero integrity** | Ruined/Disabled under current authority | Major Wound if approved | Never Clean |
| **Second qualifying Major result on an arm/Legs** | Integrity 0, Ruined, all slot-sourced actions illegal | Existing Major Wound reaches Major Trauma 2/2; do not add another wound icon | Never creates Clean or automatic Severed |
| **Claim** | No body damage | No wound | Existing claim result only |
| **Guard Flesh** | Reduces damage before state/wound resolution | May prevent a threshold wound because the final damage is lower | None |
| **Clotting Cream** | No integrity restoration | Moves one eligible bleeding wound to Controlled | No quality change |
| **Blood Bag** | No integrity restoration | Does not control or stabilize a wound | Restores Blood under its separate item rule |
| **Anna / Black Stitch treatment** | No automatic integrity restoration | Proposed route to Stabilized where its encounter rule permits | No quality change |
| **Field Repair effect** | Restores configured integrity to an attached eligible part, within its ceiling | Does not control, stabilize, resolve, or clear Major Trauma unless explicitly combined | No quality change |
| **Reconstructive Repair effect** | May restore an attached Ruined part to Critical, then recomputes legal actions | Requires the approved wound state; does not itself erase Blood loss already paid | No quality change |
| **Grafting Table torso repair** | Preserves its approved torso-definition repair and cost; later migrates to the common repair contract | Any wound effect must be explicit rather than assumed | No quality change |

## 10. Blood rules

### 10.1 Two separate Blood effects

Every bleeding wound may define two independent values later:

- **Immediate loss:** paid once when the wound is created or escalated.
- **Periodic loss:** paid at the start of each round while the wound remains eligible.

A wound can have neither, either, or both. Closed Trauma normally has neither. This
preserves the approved rule that not all limb damage reduces Blood.

### 10.2 Start-of-round order

Proposed order:

1. collect every active Untreated wound eligible to bleed;
2. calculate each wound's periodic contribution;
3. sum the contributions;
4. apply the approved per-round cap;
5. record one total Blood transaction and its per-wound sources;
6. resolve Blood-0 death and Limb for Life under existing authority;
7. resolve any separately approved worsening checks;
8. refresh the public danger preview.

The current `-20` cap remains untouched until numeric tuning. The later tuning pass
must test whether it still makes multiple wounds meaningfully more dangerous without
making treatment irrelevant.

### 10.3 Treatment, repair, and Blood restoration are separate

- Clotting Cream controls an eligible wound; it does not restore Blood.
- A Blood Bag restores Blood; it does not control a wound.
- Stabilization prevents ordinary worsening/bleeding for its window; it does not
  repair the part.
- Repair changes integrity or structural state only through its explicit rule; it
  does not automatically treat the wound or clear Major Trauma.
- Grafting replaces or changes a slot only through its explicit cost and stability
  rules.

A source may combine these effects, but its preview and event record must list each
one separately. For example: `Control Open Wound + Repair 6 Integrity` is valid as an
explicit composite effect; the word `heal` alone is not a sufficient rule.

These separations keep Blood decisions understandable. The player can knowingly buy
time with restored Blood while still bleeding, or stop the bleed while remaining at
dangerously low Blood.

## 11. Capability rules and avoiding double punishment

The existing limb state should normally own capability:

- Intact: normal source and effectiveness;
- Damaged: existing reduced effectiveness;
- Critical: existing greater reduction;
- Disabled, Ruined, Severed, or Missing: the affected source is illegal where the
  action requires it.

Wound family normally owns Blood urgency and treatment. It does not automatically
add a second universal accuracy, damage, action-cost, or readiness penalty.

Special wound-specific effects may be proposed later only when they create a unique,
readable choice that limb state cannot express. Pain, shock, infection, universal
stat debuffs, and detailed recovery timers are excluded from the first package.

For repeat Major trauma, the wound resolver explicitly changes the limb state to
Ruined. That is a structural transition, not an extra wound penalty. Reconstructive
Repair may later return it to Critical and restore its actions at the existing 50%
effectiveness. Standard Field Repair cannot revive it.

## 12. Extraction, harvest, and graft integration

One sever event produces two records:

```text
donor slot -> Severed state + Severed Stump wound
removed part -> integrity snapshot + harvest quality + approved tags
```

Important invariants:

- Clean describes part quality, not donor safety.
- A clean extraction can lower stump pressure but cannot erase the stump.
- Treatment of the donor cannot upgrade the removed part.
- Damage to the donor after severance cannot mutate an already separated part unless
  a rule targets that object directly.
- Basic attacks may force incapacity or ruin a part but never create Clean harvest.
- Emergency graft cost and Unstable rules already represent surgical risk. The first
  wound package should not add an automatic fresh-graft wound, which would charge the
  same event twice without evidence.

The Blood Hoarder strategy must be retested when wound pressure is implemented. A
free attack that creates Major Wound pressure could become a low-cost kill route even
without granting premium harvest.

## 13. Exact causal resolution order

```text
read prior actor, body, wound, and item state
-> validate actor, source limb, target slot, cost, and timing
-> resolve hit, damage, guard, extraction, and approved RNG
-> apply base integrity damage and provisional limb state
-> resolve at most one wound outcome for that slot
-> apply repeat-Major structural collapse or explicit severance when triggered
-> apply and log immediate Blood loss
-> recompute legal actions and capability
-> resolve Blood-0, Limb for Life, incapacity, and Plead checks
-> expose treatment or continuation choices
-> at the next round start, resolve periodic wound pressure
-> emit structured evidence and refresh previews
```

No later step may invent a fact missing from an earlier state mutation. For example,
the renderer cannot label a wound Major merely because Blood is low, and a harvested
part cannot become Clean merely because the donor was stabilized.

## 14. What the player must be shown

After every wound-capable action, the interface or CLI must show:

- targeted body slot;
- integrity before and after;
- limb state before and after;
- wound created, escalated, reopened, or unchanged;
- immediate Blood change and source;
- projected start-of-next-round Blood loss;
- whether the wound can worsen;
- available treatment and what that treatment will and will not fix;
- action sources lost or retained;
- harvest consequence, when applicable;
- Major Trauma count and a warning when another Major result would Ruin the slot;
- integrity repair options, their ceiling, and whether wound control is required.

Minimum compact example:

```text
RIGHT ARM: Damaged -> Critical
WOUND: Open Wound (Untreated)
BLOOD NOW: -3
NEXT ROUND: projected -5 if untreated
CAPABILITY: Right-arm actions remain legal at Critical effectiveness
OPTIONS: Clotting Cream controls bleeding; it does not repair the arm
```

Repeat-Major warning example:

```text
RIGHT ARM: Critical, 7/30 Integrity
WOUND: Major Wound (Untreated), Major Trauma 1/2
WARNING: another Major result will Ruin this arm: 0 Integrity, unusable, attached
REPAIR: blocked until wound is Controlled; Field Repair cannot revive Ruined
```

The values above are illustrative only, not a proposed numeric table.

## 15. Proposed data contract

Later implementation should keep definitions in configuration and mutable state in a
runtime wound record.

### Immutable definition fields

- wound family ID;
- eligible damage/action profiles;
- minimum trigger or threshold band;
- immediate Blood profile;
- periodic Blood profile;
- worsening rule, if any;
- eligible treatment methods;
- public name and explanation.

Repair definitions additionally require:

- repair amount/profile and integrity ceiling;
- `allows_ruined_reconstruction`;
- compatible target tags;
- required treatment state;
- any explicit combined wound-treatment effect.

### Mutable runtime fields

- wound instance ID;
- owner actor ID and body slot;
- family and severity/escalation level;
- treatment state;
- source action and source actor;
- created round and last-changed round;
- immediate Blood already applied;
- current periodic contribution;
- stabilization/control expiry, if any;
- visible Major Trauma marks, with a maximum of two for the approved limb rule.

### Required structured events

- `wound_created`;
- `wound_escalated`;
- `wound_reopened`;
- `wound_controlled`;
- `wound_stabilized`;
- `wound_resolved`;
- `wound_periodic_pressure_calculated`;
- `blood_changed` with wound/action/source IDs;
- `limb_severed` linking donor wound and harvested-part IDs;
- `major_trauma_marked`;
- `limb_ruined_by_repeat_major`;
- `integrity_repaired` with source, before, delta, after, ceiling, and resulting state;
- `repair_rejected` with a state-derived reason.

All random resolution must use the existing seeded RNG service and must be logged.

## 16. Core invariants

1. Integrity damage alone does not imply Blood loss.
2. A wound never restores integrity.
3. Treatment never improves harvest quality.
4. Clean harvest never means the donor suffered no wound.
5. Disabled and Severed remain different states.
6. One slot cannot accumulate duplicate active wounds.
7. A stronger wound escalates the dominant record; a weaker duplicate does not stack.
8. An unusable action source cannot act because its wound was treated.
9. Blood restoration does not treat a wound.
10. No wound causes death outside Blood 0 or a separately approved catastrophic rule.
11. Player and enemy use the same wound logic unless an exception is documented and
    tested.
12. A wound result and every Blood transaction are state-derived and reproducible.
13. The second qualifying Major result Ruins an arm/Legs but never silently Severs it.
14. Repair never targets Severed or Missing; grafting owns replacement.
15. Standard Field Repair cannot revive Ruined.
16. Repair cannot clear Major Trauma while the wound remains unresolved.
17. Every restored action comes from the recomputed limb state, never from a repair
    script bypass.

## 17. Acceptance tests required before runtime approval

### Creation and mapping

- chip damage below every trigger creates no wound;
- each threshold boundary produces only its approved check;
- blunt, piercing/surgical, destructive, and severing results map correctly;
- the same seed and state reproduce the same wound;
- an action cannot create a wound family absent from its configuration.

### Stacking and escalation

- one slot holds at most one dominant active wound;
- repeat Open Wound updates/escalates rather than duplicates;
- a weaker wound does not replace a stronger one;
- wounds on different slots remain independently treatable;
- the round cap applies after summing eligible wounds;
- first Major result records visible Major Trauma 1/2;
- second qualifying Major result on the same unresolved arm/Legs wound sets integrity
  to 0 and state to Ruined;
- two qualifying hits in one multi-hit action are resolved sequentially;
- repeat Major never produces Severed or Clean without an explicit sever rule;
- resolving the wound clears its active Major Trauma mark, but does not restore a
  Ruined part.

### Blood and treatment

- immediate and periodic loss are separate logged transactions;
- periodic loss occurs at the approved round boundary only;
- Controlled and Stabilized wounds behave according to their windows;
- Clotting Cream does not restore Blood or integrity;
- Blood Bag does not control bleeding;
- treatment cannot change harvest quality;
- Blood 0 and Limb for Life preserve current rule order.

### Integrity repair

- repair rejects incompatible, Severed, and Missing targets atomically;
- ordinary Field Repair rejects Ruined;
- exposed Open/Major wounds require their configured treatment state before repair;
- repair clamps to maximum integrity and its own ceiling;
- repair recomputes state and restores only state-legal actions;
- repair changes neither Blood nor wound state unless explicitly combined;
- repair does not clear Major Trauma before wound resolution;
- Reconstructive Repair moves Ruined only to Critical on its first approved use;
- Grafting Table torso repair remains consistent with its approved cost and target;
- deterministic logs explain rejection, restoration, and every regained capability.

### Capability and extraction

- capability follows limb state without duplicate generic wound penalties;
- a treated Ruined/Severed source remains illegal;
- clean sever produces both a harvested part and donor stump;
- violent sever produces its approved stump pressure independently of quality;
- basic attack never produces Clean harvest;
- emergency graft does not receive an unapproved duplicate wound cost.

### Evidence and regression

- every event identifies actor, slot, action, wound, and before/after state;
- scripted replay is byte-stable where the existing contract requires it;
- current seven approved scenarios change only where the approved wound package says
  they should;
- Blood Hoarder and other strategy diagnostics are rerun without treating their
  behavior as human balance evidence;
- Ruined Torso runtime tests remain blocked until the rescue requirement, timing, and
  numeric configuration are approved.

## 18. Hostile review and risks

| Risk | Why it matters | Required control |
|---|---|---|
| **Death spiral** | Limb impairment plus bleeding may make the losing actor unable to recover. | Limb state owns capability; avoid automatic wound stat penalties; guarantee readable treatment/exit choices. |
| **Free-attack bleed exploit** | Repeated basic attacks could become a zero-cost Blood kill route. | One dominant wound per slot, threshold creation, no duplicate stacking, and strategy diagnostics. |
| **Medical-item tax** | If every hit bleeds, Clotting Cream becomes compulsory rather than strategic. | No wound on chip damage; Closed Trauma does not bleed; treatment supply tested against encounter cadence. |
| **Clean-extraction contradiction** | Players may read Clean as painless or safe. | Always display donor stump and harvested quality separately. |
| **Too many labels** | Multiple states can overwhelm a small duel interface. | Four families, four treatment states, one wound per slot, plain-language previews. |
| **Double punishment** | Limb state and wound can both reduce the same action. | Capability belongs to limb state unless a special rule is separately approved. |
| **Torso arbitrariness** | Instant death can feel unexplained; nonfatal Torso can feel unimportant. | Use the approved conditional-fatal chain; define and preview its exact rescue timing before implementation. |
| **False realism** | Anatomical detail can expand scope without improving decisions. | No organs, tissue layers, pain, infection, or surgery simulation in this package. |
| **Player/enemy asymmetry** | Hidden exceptions make aimed choices hard to learn. | Symmetric baseline with named, visible, tested exceptions only. |
| **Numeric lock-in too early** | Bleed values depend on rounds, actions, movement, and defense cadence. | Approve meanings first; tune values only after action economy and cadence. |
| **Repair loop erases danger** | Cheap repair could reset Major Trauma indefinitely. | Integrity repair does not clear Major Trauma; only wound resolution clears the mark. |
| **Repair becomes mandatory** | If every encounter assumes repair, build choice becomes an item tax. | Use compatible alternatives, limited sources, ceilings, and encounter diagnostics; do not assume universal access. |
| **Two-hit disable is too easy** | Fast or multi-hit actions could erase a limb before a meaningful response. | Each hit must independently qualify as Major; preview the threat; set costs/timing after cadence is known. |
| **Ruined/Severed confusion** | Players may think a destroyed attached arm is already loot. | Show `Ruined — attached, unusable` and keep sever/extraction as a separate action. |

## 19. Explicit non-goals and deferred work

This approval does not include:

- final Blood values or probabilities;
- final wound thresholds;
- exact Ruined-Torso rescue requirement, duration, and numeric consequences;
- Torso-specific capability penalties;
- pain, shock, infection, disease, scars, organs, tissue layers, or malpractice;
- long-term healing time or recovery facilities;
- armor/material penetration simulation;
- specific repair items, skills, spells, or new content definitions beyond the shared
  repair-effect contract;
- fresh-graft wound rules;
- movement, space/reach, action-economy, defense, reflex, or final UI rules;
- new characters, items, encounters, Unity work, or production claims.

## 20. Approved owner decisions

These decisions were approved together on 2026-08-13. Their order remains important
for implementation and later numeric tuning.

### Decision 1 — minimum wound families

Approved wound meanings:

1. Closed Trauma;
2. Open Wound;
3. Major Wound;
4. Severed Stump.

**Recommendation:** approve all four. Removing Stump confuses donor risk with harvest;
removing Closed Trauma makes every meaningful hit bleed; splitting the list further
adds detail before it adds decisions.

### Decision 2 — repeat-Major collapse scope

Approved: the second-Major rule uses the proposed mapping and initially applies to
arms plus the combined Legs slot.

**Recommendation:** second qualifying Major result sets integrity to 0 and state to
Ruined, leaving the part attached and non-Clean. Apply it to arms and Legs. Keep Head,
Torso, and Core on separately approved catastrophic rules.

### Decision 3 — repair boundary

Approved repair boundary:

**Recommendation:** ordinary Field Repair works only on attached Damaged/Critical
parts. Rare Reconstructive Repair may return an attached Ruined part to Critical.
Severed/Missing always requires grafting. Integrity repair does not clear Major Trauma
until the wound itself is Resolved.

### Decision 4 — wound occupancy

Approved: one dominant active wound per body slot.

**Recommendation:** one dominant wound per slot, with escalation and event history.

### Decision 5 — clean versus violent severance

Approved: clean severance also reduces donor wound pressure compared with violent
severance.

**Recommendation:** clean severance produces lower ongoing stump pressure than
violent severance, but both are dangerous and both create a stump.

### Decision 6 — player/enemy symmetry

Approved: both sides use the same wound rules except for explicit visible exceptions.

**Recommendation:** yes. Allow only visible, named exceptions such as anatomy or an
explicit passive.

### Decision 7 — free basic attack at zero integrity

Approved: it creates Major Wound/Blood pressure while still denying Clean harvest,
subject to the required exploit validation before runtime acceptance.

**Recommendation:** yes, provisionally. It makes ruin physically meaningful, but it
must pass a Blood Hoarder exploit test before runtime approval.

### Decision 8 — Ruined Torso consequence

Approved: conditional fatality with one explicit rescue window. The exact rescue
requirement and timing remain dependent on later treatment and cadence rules.

**Recommendation:** conditional fatality with one explicit rescue window. Define the
rescue only after wound treatment and strategic cadence are known.

## 21. Recommended next step

This document's former next dependencies—space/reach and strategic cadence—were later
resolved in documents 28 and 29. The owner approved document 30's WNR-0.1 as a
provisional numeric paper baseline on 2026-08-14. Exact values remain tunable and
outside runtime until a separate implementation gate.
