# Game att2 - Action-Produced Space and Reach Direction

Status date: 2026-08-13

Status: **OWNER-APPROVED DESIGN DIRECTION - RUNTIME IMPLEMENTATION NOT APPROVED**

This document replaces the earlier interpretation of range as something actors edit
with a general reposition command. The owner clarified that Game att2 has no
board-like movement layer. Clinch, Engaged, and Distant are dynamic combat states
created by attacks, defenses, reflex results, and other meaningful tactical actions.

The owner approved the complete latest direction, including the first neutral-settling
cadence, on 2026-08-13. Individual action/card profiles, balance values, hand rules,
data structures, and implementation remain proposals until separately approved.

### Approval record

The following meanings are approved:

- range is produced by action, defense, reflex, and other explicit combat outcomes;
- Clinch, Engaged, and Distant are the shared one-versus-one states;
- the same action may have different visible profiles at different ranges;
- unmaintained Clinch receives one complete later playable round before Engaged;
- unmaintained Distant receives two complete later playable rounds before Engaged;
- explicit range maintenance or a new range outcome resets or preserves the relevant
  state instead of allowing neutral settling to erase a dedicated range build;
- general builds do not receive a free universal reposition command or guaranteed
  indefinite range control;
- side-view presentation does not create blocks, coordinates, or travel turns.

This approval defines design behavior. It does not authorize runtime implementation,
card content, exact combat modifiers, draw rules, or broader reflex mechanics.

## 1. Simple summary

The game tracks one shared relationship between two fighters:

```text
CLINCH <-> ENGAGED <-> DISTANT
```

The player does not normally press **Move Closer** or **Move Away** to edit this state.
Instead, combat events produce it.

Examples supplied by the owner:

- a rival's charge may leave both fighters in Clinch for the next turn;
- a moving side-dodge may cause the charging rival to pass, leaving them Distant;
- a weapon action may work in several states but use a different timing, accuracy,
  offense, defense, damage, or exposure profile in each one;
- a long-sword hit at Clinch might be easier to place but deal less damage because
  there is not enough room for a full swing.

These examples explain the system. They do not approve a Charge card, side-dodge
card, long sword, or numeric modifiers as current content.

## 2. Owner-directed rules

The following directions are locked at the design level:

1. **Range is an outcome, not a freely editable control.** There is no universal
   range slider, movement-point path, or repeated walk command.
2. **Range is dynamic.** Attacks, defensive responses, reflex grades, pushes, pulls,
   evasions, charges, and other explicit effects may change the next combat state.
3. **Actions may have multiple range profiles.** The same action can be legal in
   more than one state and behave differently in each.
4. **Engaged is the neutral state.** Temporary Clinch and Distant situations naturally
   settle back toward Engaged when no action or effect sustains them.
5. **Range-focused builds are valid.** A build may repeatedly create or maintain
   Distant through its authored tactical tools. The neutral return rule must not erase
   that identity.
6. **General builds must not sustain exceptional range for free.** Their ordinary
   tactical hands should contain balanced access to range-changing cards/effects, not
   guaranteed endless retreat or lock-down.
7. **Presentation does not define the rules.** A two-dimensional side view may animate
   approach, collision, overshoot, or separation, but it does not create coordinates,
   blocks, tiles, or travel turns.
8. **Space remains subordinate to the card-and-reflex identity.** The important
   decision is the body-sourced tactical action and its execution, not walking across
   a battlefield.

## 3. Correct mental model

### Rejected interpretation

```text
choose Move Closer
-> spend several turns crossing space
-> finally enter attack range
-> attack
-> choose Move Away
```

This would reproduce the exact generic turn-based movement problem the owner wants to
avoid.

### Intended interpretation

```text
read current bodies, intent, hand, and range state
-> choose a legal body-sourced tactical action/card
-> resolve its attack, defense, or reflex interaction
-> that result may create Clinch, Engaged, or Distant
-> use the new range profile on the next tactical opportunity
-> if nobody sustains the exceptional state, it settles toward Engaged
```

Range is therefore a **consequence and context**. It is not a separate locomotion
game.

## 3A. What remains useful from the earlier comparison

The earlier research still supports parts of this revision, but none of these games
defines Game att2's solution:

- *Battle Brothers* demonstrates that spatial relationship should change action
  legality, while its grid, terrain, and Zone of Control are deliberately rejected
  here. [Official developer blog](https://battlebrothersgame.com/tactical-combat-mechanics/)
- *Into the Breach* demonstrates the value of previewing how a response changes the
  next state. Game att2 uses that readability lesson without adopting a multi-unit
  grid puzzle. [Official page](https://subsetgames.com/itb.html)
- The developer of *Fights in Tight Spaces* reported that movement risked becoming
  overpowered during prototyping. That supports keeping range control inside bounded
  tactical actions rather than making it a free subsystem.
  [Developer article](https://news.xbox.com/en-us/2020/11/12/fights-in-tight-spaces-packs-a-punch/)
- *Darkest Dungeon* demonstrates that one skill can have position-dependent
  availability and movement effects. Game att2 transfers the explicit-profile lesson,
  not its party-rank formation system.
  [Official patch notes](https://www.darkestdungeon.com/patch-notes/)
- *Buckshot Roulette* supports intimate, readable ritual staging. Game att2 preserves
  that staging while adding body-sourced cards, reflex execution, and dynamic range
  consequences rather than copying its fixed table mechanics.
  [Official Steam page](https://store.steampowered.com/app/2835570/BuckshotRoulette/)

These are shipped-design comparisons, not proof that any one mechanic caused success.

## 4. Range-state meanings

### Clinch

- The fighters are inside normal full-swing distance or in close physical pressure.
- Short, controlled, grappling-like, improvised, or extraction actions may benefit.
- Long or momentum-dependent actions may lose damage, defense, or timing quality.
- Clinch does not automatically mean grappled, restrained, or unable to act.
- It is normally temporary unless an explicit action/effect maintains it.

### Engaged

- The fighters are at ordinary exchange distance.
- This is the default encounter start and neutral resting state.
- General melee actions should normally have a useful Engaged profile.
- Engaged is not a grid adjacency rule or passive Zone of Control.

### Distant

- The fighters are outside ordinary immediate melee exchange distance.
- Long-reach, approach, observation, ranged, evasive, recovery, or escape-related
  actions may gain different opportunities here when explicitly authored.
- Distant does not mean safe, escaped, off-screen, or several turns of mandatory
  walking away.
- It is normally temporary unless a build or effect actively maintains it.

The states do not represent exact meters. They describe the tactical relationship
created by the latest meaningful exchange.

## 5. How actions create range

An action does not have one unconditional range result. Its result may depend on:

- current range;
- acting body/tool source;
- selected target;
- opponent's legal response;
- reflex result or execution grade;
- whether the action connects, is redirected, is evaded, or is interrupted;
- an explicit passive or status that changes the outcome.

Illustrative causal table only:

| Tactical event | Possible result | Next range |
|---|---|---|
| Charge makes close contact | Momentum carries both bodies together | Clinch |
| Defender side-evades a committed charge | Attacker passes the defender | Distant |
| Push creates separation | Bodies leave close pressure | One authored step farther or Distant, as the action states |
| Pull or hook closes space | Target is drawn into close pressure | Clinch |
| Ordinary exchange creates no spatial result | Relationship stays as it was until neutral settling applies | Unchanged |

Only an authored action/effect may claim one of these outcomes. The system must not
infer a range change merely from an animation name.

## 6. Multi-range action profiles

Each physical action/card should define a profile for every range where it is usable.
A profile may specify:

- legal or illegal;
- timing/reflex window shape;
- accuracy or resolution likelihood;
- damage or other consequence strength;
- offensive pressure;
- defensive protection or vulnerability;
- source exposure;
- valid targets or responses;
- resulting range on each meaningful resolution grade.

These properties are action-specific. This direction does **not** create universal
Attack Points, Defense Points, or generic hidden range modifiers.

Illustrative, non-canonical example:

| Long-sword profile | Accuracy | Damage | Explanation |
|---|---|---|---|
| Clinch | Higher | Lower | Target is close, but the blade cannot build a full swing. |
| Engaged | Standard | Standard or higher | Intended striking distance. |
| Distant | Illegal or requires an approach/lunge result | None until resolved | The action must explicitly bridge the separation. |

If the future game uses another resolution model instead of accuracy or damage
numbers, the same principle still applies: each range has a visible, authored
trade-off.

## 7. Neutral settling toward Engaged

Exceptional range must not create soft-locks or force general builds to wait for a
specific movement draw. Therefore Clinch and Distant naturally lose persistence when
nothing causally maintains them.

### Approved first cadence

- When an action/effect creates **Clinch**, set its neutral-settling counter to **one
  complete later combat round**.
- When an action/effect creates **Distant**, set its counter to **two complete later
  combat rounds**.
- Do not reduce the counter during the same round that created the state.
- At the end of a later complete round, if no action/effect changed or explicitly
  maintained range, reduce the counter by one.
- When the counter reaches zero, the next round begins **Engaged**.
- Engaged has no settling counter.

This is the approved interpretation of the owner's example: one playable later round
in Clinch or two playable later rounds at Distant before neutral engagement resumes.
The counts are locked design meanings but remain unimplemented and subject to later
evidence-led revision through a new owner decision.

### Why use complete rounds

The current combat already recognizes rounds containing opportunities for both
actors. Counting complete rounds is more symmetric than counting only one actor's
turn. If the later action-economy package replaces that structure, it must preserve
equivalent fair opportunity rather than copying the number mechanically.

### What resets or pauses settling

An explicit range effect can:

- create another range and replace its counter;
- maintain the current range and refresh/preserve its counter;
- force Engaged immediately;
- declare a special persistence rule.

Merely selecting an ordinary attack at the current range does not automatically
maintain it. Maintenance must be an authored result with a visible cause.

### What neutral settling means fictionally

It is not a free hidden movement action. It abstracts the natural continuation of a
duel: close bodies separate enough to exchange again, or separated fighters re-enter
ordinary pressure. The countdown and expected return must be visible to the player.

## 8. Range-focused builds

A Distant/evasion build is legitimate when it earns that identity through its body,
cards, passives, timing, or risk. It may repeatedly re-create or maintain Distant.

To prevent universal abuse:

- range control must belong to authored tactical opportunities, not a free command;
- the action must name a usable body/tool source;
- maintaining range should consume a meaningful card opportunity, carry exposure,
  require successful execution, or have another visible trade-off;
- general hands must not guarantee indefinite retreat every turn;
- opponents may have authored range profiles or counters, but no universal invisible
  anti-kiting rule is assumed;
- the neutral return clock affects unmaintained Distant but does not override an
  explicit maintenance result.

Exact deck access, draw probability, hand size, card cycling, counter frequency, and
cost are part of the later card/action-economy package.

## 9. Relationship to cards and the body

Range does not own actions. The body and authored content own them.

- A usable limb, graft, tool, skill, or other approved source may contribute tactical
  cards/opportunities.
- Current range selects the relevant profile and may make a card legal or illegal.
- An unusable source still cannot execute its card even at the ideal range.
- A range-changing result cannot repair a source, erase a wound, or create Clean
  harvest.
- Future hand-generation rules should avoid routinely giving general builds hands
  that are entirely unusable because of range, but the exact filtering/redraw rule is
  not decided here.

Movement-oriented cards are allowed, but they must be full tactical actions such as a
committed charge, evasive strike, retreating defense, pull, or pressure-hold. They are
not disguised buttons whose only meaning is `range +1` or `range -1`.

## 10. Reflex integration

Reflex execution may be one of the causes that selects a range outcome.

Required causal boundary:

```text
committed legal action and current range profile
-> compatible response route
-> reflex execution grade
-> attack/defense consequence
-> authored range outcome for that grade
```

A reflex result must not choose range arbitrarily. For example, a side-evade can
produce separation only when it is a valid response to the committed attack and the
action defines that consequence. A perfectly timed Block need not cause the same
range result as a side-evade.

Broader reflex implementation remains deferred. This section defines compatibility,
not timing values or response content.

## 11. Existing-action direction

The previous document proposed a fixed legal-band table for current actions. That
table is no longer sufficient because actions may have multiple profiles and
resolution-dependent range outcomes.

The following qualitative boundaries remain reasonable proposals:

| Current action/effect | Range direction | Status |
|---|---|---|
| Focus | Can read at all three states if visibility remains clear | Proposal; information strength may differ later |
| Self-treatment and self-repair | Not inherently blocked by range | Proposal; interruption/timing belongs later |
| Grip Strike | Needs authored Clinch and Engaged profiles | Proposal; exact trade-off undecided |
| Desperate Swing | Needs a strong Engaged profile; Clinch/Distant behavior must be authored rather than assumed | Open |
| Surgical Jab | Needs Clinch and Engaged profiles | Proposal |
| Guard Flesh and Brace | Self-states; may influence a later spatial result but do not directly edit range | Proposal |
| Claim the Cut | Marks intent and does not itself change range | Proposal |
| Bone Scissors | Clinch-oriented controlled extraction | Proposal |
| Hell Saw | May support Clinch and Engaged with different risk/quality profiles | Proposal |

No final numbers or new action cards are approved by this table.

## 12. Starting state, posture, and escape

- Ordinary ritual duels begin Engaged unless an encounter explicitly creates another
  opening state.
- Starting state is not randomized in the first package.
- Downed/Standing and range are separate facts.
- A Knockdown or Stand action changes range only when its authored result says so.
- Distant may be a prerequisite for a later escape attempt, but Distant is not escape
  or victory.
- Escape, pursuit, surrender, and encounter-resolution rules remain separate gates.

## 13. Required causal order

```text
read current body, hand, intent, posture, and shared range state
-> select a body-sourced action/card
-> select its current-range profile
-> validate source, target, cost, and response compatibility
-> preview profile trade-offs and possible range outcomes
-> commit the later-approved action cost
-> resolve action and reflex grade through approved rules
-> apply Blood, wound, body, defense, and extraction consequences
-> apply the authored range outcome
-> create, replace, or maintain the settling counter
-> recompute legal card/action profiles from the new state
-> at the valid round boundary, apply neutral settling if unmaintained
-> log the cause, prior range, result, counter, and new range
```

The range outcome must follow the action and response result. It cannot be selected
independently after seeing the consequences.

## 14. Player-facing readability

The interface or paper fixture must show:

- current range state;
- remaining neutral-settling duration when Clinch or Distant;
- whether the committed action will change, maintain, or leave range untouched;
- the current range profile for each offered card;
- important differences in timing, accuracy, consequence, offense, defense, and
  exposure compared with its other profiles;
- possible range outcomes of the opponent's telegraphed action and the selected
  defensive/reflex route;
- the body/tool source required;
- a plain reason for any illegal profile.

The player must never need to infer mechanical distance from sprite position alone.

## 15. Suggested future data contract

Implementation is not approved. A later technical design could represent:

```text
RangeState = CLINCH | ENGAGED | DISTANT

DuelState.range_state
DuelState.range_origin_event
DuelState.settling_rounds_remaining
DuelState.range_maintained_this_round

ActionDefinition.range_profiles[RangeState]
RangeProfile.legality
RangeProfile.timing_profile
RangeProfile.resolution_modifiers
RangeProfile.result_by_execution_grade
RangeResult.new_state
RangeResult.maintains_state
RangeResult.settling_override
```

Names are illustrative. The important contract is that the result belongs to the
action/profile/response outcome and remains deterministically logged.

Suggested events:

- `range_profile_selected`
- `range_outcome_previewed`
- `range_state_changed`
- `range_state_maintained`
- `range_settling_advanced`
- `range_settled_to_engaged`

## 16. Invariants

1. A one-versus-one duel has one shared range state.
2. Range cannot be freely edited through a generic control.
3. Every non-settling range change names an action/effect and resolution cause.
4. Reflex execution changes range only through the committed action's authored
   response outcome.
5. One action may have different visible profiles at different ranges.
6. No generic hidden modifier substitutes for those profiles.
7. Engaged is the neutral state.
8. Clinch and Distant settle only through the visible neutral rule or an authored
   effect.
9. An explicit maintenance result can support a range-focused build.
10. A general build is not guaranteed infinite range maintenance.
11. Range does not override body-source legality.
12. Range does not create wounds, Blood, repair, or harvest quality without another
   explicit consequence.
13. Distant is not escape; Clinch is not grappled.
14. Presentation coordinates do not become gameplay coordinates.
15. Player and enemy follow the same causal rules unless a visible exception exists.
16. The pairwise state is not silently extended to three or more actors.

## 17. Minimum later validation

Before runtime approval, paper and deterministic tests should establish:

- Charge-contact-to-Clinch and evade-overshoot-to-Distant examples can be represented
  without a standalone movement command;
- every range mutation is traceable to its action, response, and result grade;
- an action with three profiles exposes and applies the correct trade-offs;
- Clinch receives one full playable later round before the recommended neutral return;
- Distant receives two full playable later rounds before the recommended return;
- changing or maintaining range resets/preserves the correct counter;
- an unrelated action does not secretly maintain exceptional range;
- a dedicated range build can sustain Distant through authored opportunities;
- a general build cannot do so indefinitely without meaningful opportunity and risk;
- no normal encounter requires several dead walk turns before an attack;
- disabled sources cannot use range-changing cards;
- range changes do not create Clean harvest or bypass wound rules;
- Downed and Distant remain distinct;
- deterministic replays reproduce the same range events;
- players understand why the state changed and when it will settle.

## 18. Hostile review

| Risk | Failure pattern | Required control |
|---|---|---|
| Range becomes a movement minigame | Players spend turns choosing closer/farther without another tactical meaning | No universal reposition command; range comes from full actions and outcomes |
| Range is cosmetic | Every action behaves identically in all states | Require visible, authored profiles when an action spans states |
| Profiles become unreadable | Each card contains three pages of modifiers | Show only current profile plus concise comparison icons/details |
| Distant kiting becomes universal | Any build can retreat forever | Limited authored access, meaningful cost/risk, neutral settling, and counterplay |
| Neutral settling erases range builds | Distant automatically ends despite a build investing in it | Explicit maintenance/recreation results reset or preserve the state |
| Clinch/Distant creates dead hands | No offered card can act until a movement card appears | Later hand rules need bounded usability protection; actions can have multiple profiles |
| Reflex chooses outcomes arbitrarily | A button grade teleports fighters between states | Range outcome must belong to the committed action and response route |
| Range profiles become stat bloat | Many small bonuses recreate stat-menu dueling | Prefer qualitative trade-offs and only mechanically meaningful differences |
| Side-view animation becomes authority | Sprite coordinates contradict the state model | State label and logged outcome own mechanics; animation follows them |
| Settling feels unexplained | Fighters snap back to Engaged | Show countdown and narrate natural exchange resumption |
| Pairwise state fails with more actors | One shared value cannot describe three relationships | Keep current scope one-versus-one and reopen representation before expansion |

## 19. Explicit deferrals

This direction does not decide or approve:

- hand size, deck construction, draw, discard, retention, redraw, or usability rules;
- which existing or future cards change or maintain range;
- numeric timing, accuracy, damage, offense, defense, or exposure values;
- broader reflex interactions or timing windows;
- exact Legs impairment effects on range cards;
- pursuit, escape, initiative, simultaneous commitment, or cancellation costs;
- multi-actor combat, maps, terrain, facing, line of sight, or collision;
- new weapons, characters, items, skills, spells, or production UI;
- the deferred brain/Head progression concept;
- runtime source, configuration, or migration.

## 20. Decisions resolved and remaining

### Resolved by owner direction

- use Clinch, Engaged, and Distant as shared relational combat states;
- make distance an outcome of meaningful actions/events, not a freely editable move;
- allow action-specific profiles across multiple distances;
- make exceptional range dynamically settle toward Engaged when unmaintained;
- give unmaintained Clinch one complete later playable round and unmaintained Distant
  two complete later playable rounds before settling to Engaged;
- allow dedicated range/evasion builds to maintain their style through authored
  tactical tools;
- prevent general builds from receiving unlimited range control by default;
- do not let a two-dimensional presentation create map traversal rules.

### Remaining downstream decisions

Card availability, hand rules, individual range profiles, action costs, and strategic
cadence come later. None is approved by the space-direction approval.
