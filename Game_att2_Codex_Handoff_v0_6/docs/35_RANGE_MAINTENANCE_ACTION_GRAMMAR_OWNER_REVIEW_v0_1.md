# Game att2 - Resolution-Bound Range Maintenance Grammar v0.1

Status date: 2026-08-17

Status: **Package C - Resolution-Bound Range Tenure is owner-approved as paper
design authority. Runtime, configuration, production action profiles, final values,
UI, and human-experience claims remain unapproved.**

## 1. Decision and authority boundary

The owner selected Package C on 2026-08-17 as the paper answer to the
range-maintenance action-grammar gate.

The governing statement is:

> Clinch or Distant persists only when a resolved, explicitly authored tactical
> outcome creates, recreates, or maintains that state. Merely acting while an
> exceptional range exists does not maintain it. Preparation may enable or improve
> a later range result, but cannot refresh range by itself.

This package consumes the approved Clinch/Engaged/Distant cadence, Attention Slot
budget, automatic-defense boundary, public Lead/two-lock order, source profiles, and
readied-inventory rules without changing them. It adds no universal movement command,
action points, upkeep resource, free range contest, production card, or runtime rule.

The current simulator remains governed by Combat Rules v0.5. Its Focus, Fast-item,
Main, player-first, and enemy-resolution sequence remains unchanged.

## 2. Range profile classifications

Every future authored range profile declares one current role:

| Classification | Meaning | Counter effect |
|---|---|---|
| Neutral | The action is usable but gains no authored range benefit and creates no spatial result. | None |
| Exploit | The profile gains an authored trade-off from the current range without sustaining it. | None |
| Maintain | A resolved result preserves the same exceptional state. | Refresh to the approved base |
| Shift/Create | A resolved result creates a named different state. | Replace with the new state's base |
| Release | A resolved result intentionally ends the current maintained state through a named destination. | Replace with the destination state |

These roles belong to the resolved profile, not to an animation, action name, card
origin, or presentation position. Missing range-result data means no mutation and no
maintenance. The system never infers that an ordinary action maintains range merely
because it was legal there.

Engaged is neutral and has no maintenance counter. An action may explicitly produce
or preserve Engaged, but that is not exceptional-range maintenance.

## 3. Approved maintenance contract

Maintenance applies only when all of the following are true:

1. The shared current range is the same exceptional state named by the profile.
2. The action, source, target, timing, cost, posture, and commitments are legal.
3. The exact Full, Strained, or Desperate profile declares `Maintain`.
4. The action begins execution and satisfies any visible authored result condition.
5. The final spatial result of the atomic action/response chain remains `Maintain`.

The approved behavior is:

- successful Clinch maintenance refreshes its counter to `1`;
- successful Distant maintenance refreshes its counter to `2`;
- counters never stack or rise above those approved bases;
- rejected or pre-execution-canceled commitments provide no maintenance;
- a started atomic action completes and may produce its authored range result;
- later source loss removes future maintenance access but does not retroactively
  erase a spatial result already produced;
- an explicit later Shift/Create or Release result replaces earlier maintenance;
- player and enemy use the same contract except for visible authored exceptions.

No Blood, readiness/Stamina, integrity, or item cost is added merely because a result
maintains range. Any such cost must already be an authored, previewed part of that
action profile under the approved shared systems.

## 4. Neutral settling

Document 28's cadence remains unchanged:

- Clinch created or maintained this round receives one complete later playable
  round before neutral return;
- Distant created or maintained this round receives two complete later playable
  rounds before neutral return;
- the same round that created, recreated, shifted, or maintained an exceptional
  state does not decrement its counter;
- at the end of a later complete round with no qualifying range result, reduce the
  counter by one;
- when the counter reaches zero, the next round begins Engaged;
- Engaged has no counter.

An ordinary attack, Focus, treatment, Pass, or other action does not pause the clock.
The interface and paper record must show whether the round created, maintained,
shifted, released, or merely exploited range.

If a binding encounter result occurs before another round, no cosmetic settling step
is required. Range cannot override death, surrender, escape, incapacity, or another
approved state-derived resolution.

## 5. Preparation, Main, automatic response, and passives

### Preparation

A Preparation may reserve a source, improve a later Main profile, improve an
automatic defense route, or reveal spatial consequences. It cannot refresh an
exceptional range by itself. This prevents Focus, treatment, and inventory
Preparation from becoming free Clinch or Distant upkeep.

### Main

A resolved Main may Maintain, Shift/Create, or Release only when its exact current
profile declares that result. Main timing supplies opportunity cost; it does not
grant range authority automatically.

### Automatic defense

An incoming action and one legal automatic response resolve to one authored final
spatial outcome. Block, Intercept, Dodge/Evade, or another future response receives
no default maintenance. The route may create, recreate, maintain, shift, or release
range only when the incoming action/response profile defines that outcome.

### Passives

A passive may modify an already legal range result but cannot ambiently refresh the
counter. A future signature exception would require its own visible owner-approved
profile, paper case, and eventual negative tests.

## 6. Source condition and commitments

Package D governs range maintenance:

| Source condition | Maintenance result |
|---|---|
| Intact | Use the authored Full profile. |
| Damaged | Use the authored Strained profile; maintenance remains only if that profile declares it. |
| Critical | Use an explicit Desperate profile or become Dormant. |
| Occupied or Reserved incompatibly | Dormant; no execution and no refresh. |
| Disabled, Ruined, Severed, Missing, destroyed item, or otherwise Offline | Invalid; no execution and no refresh. |

An action with multiple required sources uses the weakest required source. The same
locked action re-derives its current profile after source damage. No replacement card,
source, grip, tool, or target is selected.

Range consequence remains one permitted local deterioration axis. A Strained profile
may, for example, keep its ordinary effect but lose maintenance and become Exploit.
That degradation must be authored and previewed; it is not a universal rule for every
damaged source.

Integrity Echo cannot create or remove maintenance, change the counter, shift range,
alter legality, or preserve an invalid plan.

## 7. Lead, Reply, and range contest

Package C adds no movement phase or contest roll. Range conflict occurs through the
existing commitments and sequential causal order:

1. Lead locks its action, source, target, mode, and current profile.
2. Reply receives the permitted telegraph and locks its unchanged commitment.
3. Lead resolves and applies its final spatial result.
4. Reply revalidates the same card against the new body, source, target, and range.
5. If legal, Reply resolves its current authored profile and may replace the Lead's
   range result.
6. If canceled, Reply receives no maintenance, release, substitute, or consolation
   action.

The later successfully resolved authored mutation wins because it is the later state
change, not because Reply owns a hidden range advantage. Lead alternation,
information asymmetry, cancellation risk, and profile legality remain the balancing
facts.

Conflicting range results inside one atomic attack/defense chain must be reduced by
the definition to one final outcome. Ambiguous definitions fail paper acceptance and
must not rely on renderer order.

## 8. Existing-content disposition

Package C deliberately approves no existing production action as a range maintainer
or intentional releaser. Current action meanings are too narrow to justify those
spatial behaviors without invention.

The first paper classification is:

| Existing action or category | Paper range role | Maintenance/release disposition |
|---|---|---|
| Focus | Range-neutral Preparation; visibility may later vary by profile | Never maintains or releases |
| Blood Bag / Clotting Cream | Range-neutral Preparation under Package A2 paper timing | Never maintains or releases |
| Claim the Cut | Marks extraction intent without editing range | Never maintains or releases |
| Guard Flesh | Prepared-defense Main that may modify a later automatic Block | Guard itself never maintains |
| Brace / Stand | Posture or state actions | No implicit range result |
| Grip Strike | Proposed Clinch/Engaged exploit profiles | Does not maintain by default |
| Surgical Jab | Proposed Clinch/Engaged exploit profiles | Does not maintain by default |
| Bone Scissors | Proposed Clinch-oriented extraction exploit | Does not maintain by default |
| Hell Saw | Proposed Clinch/Engaged risk profiles | Does not maintain by default |
| Desperate Swing | Strong Engaged proposal | Clinch/Distant behavior remains deferred |
| Cover It, Calm Guard, Black Stitch, Trade Offer | Insufficient source/range behavior | Deferred |

This blocks a zero-cost Grip Strike from becoming universal permanent Clinch and
blocks observation, treatment, or item preparation from becoming free Distant upkeep.

A future range-specialist body or action may earn maintenance through an approved
profile. Package C supplies its grammar but does not approve that content.

## 9. Readability contract

Before commitment, show:

- current shared range and remaining counter;
- current profile classification;
- whether the result is unconditional or conditional;
- the required source and Full/Strained/Desperate state;
- the destination and new counter for Maintain, Shift/Create, or Release;
- any Preparation, commitment, automatic-response, or source conflict;
- the result if Lead changes range before Reply execution;
- why the profile is Dormant or Invalid.

After resolution, log:

- prior range and counter;
- action, source profile, and classification;
- legality and revalidation result;
- automatic response and final spatial outcome;
- final range and counter;
- whether neutral settling advanced and why.

Sprite positions, camera motion, and animation never override the recorded state.

## 10. Complete causal order

```text
prior body, inventory, wounds, range, counter, slots, Lead, and commitments
-> enumerate current source-supported opportunities and range profiles
-> derive Full, Strained, Desperate, Dormant, or Invalid state
-> expose classification, destination, condition, counter, cost, and blocked routes
-> take Preparation and lock Main under the public-Lead contract
-> revalidate exact action, source, target, range profile, item, and costs
-> if legal, pay the authored execution cost and begin the atomic action
-> resolve the incoming action and one compatible automatic defense route
-> determine final recipient, structural pressure, wounds, Blood, and other effects
-> apply one authored final range result: none, maintain, shift/create, or release
-> refresh or replace the counter without stacking
-> recompute source capability, card state, and Reply legality
-> resolve or cancel the unchanged Reply commitment
-> evaluate forced consequences and encounter viability
-> at the complete-round boundary, advance neutral settling only when unmaintained
-> emit structured deterministic evidence
```

Range never restores a source, treats a wound, changes harvest quality, waives a cost,
creates an item, or selects an encounter ending.

## 11. Minimum bounded paper fixture

Use existing S-001 and Anna body/action names plus one neutral
`RANGE_DIAGNOSTIC_MAIN` record. That record is allowed only as a three-range paper
diagnostic under Document 34; it is not a card, item, action, character ability, or
production-content approval.

| Case | Setup | Required result |
|---|---|---|
| RMG-C-01 | Clinch `1`; existing Grip Strike/Surgical Jab exploit profiles resolve | No implicit refresh; next round begins Engaged |
| RMG-C-02 | Distant `2`; Focus, Guard Flesh, Brace, treatment, or Pass occurs | Legal neutral actions do not maintain; counter advances visibly |
| RMG-C-03 | Full diagnostic Main declares Maintain | Refresh to the approved base; never stack above it |
| RMG-C-04 | Strained profile omits Maintain | Action may resolve as Exploit; no refresh |
| RMG-C-05 | Critical source with and without Desperate profile | Explicit Desperate maintenance or Dormant; no inference |
| RMG-C-06 | Lead disables Reply's maintaining source after lock | Reply cancels; no refresh and no substitution |
| RMG-C-07 | Lead maintains; legal Reply later releases or shifts | Reply's later authored mutation becomes final |
| RMG-C-08 | Automatic defense has no spatial result | No maintenance merely because defense occurred |
| RMG-C-09 | Automatic defense declares a final spatial result | Apply that one result to the actual action/response chain |
| RMG-C-10 | Player/enemy states are identical | Resolve the same classification and counter evidence |

Designer self-play of this fixture is diagnostic only. It cannot establish that
maintenance is fun, legible, fair, balanced, or desirable in production content.

## 12. Requirements and future traceability

| Requirement | Paper contract | Future verification obligation |
|---|---|---|
| RMG-C-001 | Every profile declares Neutral, Exploit, Maintain, Shift/Create, or Release. | Reject ambiguous or inferred spatial authority. |
| RMG-C-002 | Acting at exceptional range never implicitly maintains it. | Neutral/exploit negative cases. |
| RMG-C-003 | Preparation cannot refresh range by itself. | Focus, treatment, and item negative tests. |
| RMG-C-004 | Maintenance requires legal execution and an authored final result. | Rejection, cancellation, and success cases. |
| RMG-C-005 | Counters refresh to fixed bases and never stack. | Repeated-maintenance boundaries. |
| RMG-C-006 | Source profiles, weakest source, Dormant, Invalid, and no substitution govern maintenance. | Source-state matrix and post-lock invalidation. |
| RMG-C-007 | Automatic defense has no default range authority. | Block/Intercept/Dodge negative and authored-result cases. |
| RMG-C-008 | Lead/Reply contest uses sequential resolution and unchanged commitment. | Both Lead orders, changed-range revalidation, and cancellation. |
| RMG-C-009 | Current production actions receive no maintenance/release by implication. | Content-catalogue and definition audit. |
| RMG-C-010 | Neutral diagnostic records never enter production content. | Catalogue/runtime/config negative audit. |
| RMG-C-011 | Player-facing preview and logs expose classification, cause, and counter. | Information-contract review. |
| RMG-C-012 | Player/enemy rules remain symmetric. | Mirrored fixture comparison. |

No runtime test is required or authorized until an owner-approved implementation plan
defines data migration, exact production profiles, and deterministic acceptance.

## 13. Comparable-system evidence and limits

Sources were checked on 2026-08-17.

- *Fights in Tight Spaces* integrates attacks, shoves, throws, dodges, and position
  into card decisions; its developer identified overpowered movement as an early
  design problem. The transferable lesson is bounded tactical access to spatial
  control. Game att2 does not copy its grid, movement cards, or combo resource.
  [Developer account](https://news.xbox.com/en-us/2020/11/12/fights-in-tight-spaces-packs-a-punch/)
- *Into the Breach* exposes incoming attacks before the counter-decision. The
  transferable lesson is pre-commitment preview of a possible spatial mutation. Game
  att2 does not copy its grid puzzle or guarantee a perfect counter.
  [Official page](https://subsetgames.com/itb.html)
- *Battle Brothers* uses explicit melee engagement, source/equipment skills, and
  costly disengagement. The transferable lesson is that close control needs a visible
  source and consequence. Game att2 does not copy hexes, action points, fatigue,
  opportunity attacks, or permanent Zone-of-Control lock.
  [Developer combat article](https://battlebrothersgame.com/tactical-combat-mechanics/)

These are shipped-system and developer evidence, not proof that one mechanic caused
fun, accessibility, sales, retention, or balance.

Game att2's positive hypothesis is narrower: transient pairwise range, body-source
degradation, fixed visible settling, extraction value, and Lead/Reply revalidation
may make range feel like a consequence of rebuilding and risking the body. This is a
design interpretation, not a market-uniqueness claim.

## 14. Evidence card

| Field | Record |
|---|---|
| Question | Can exceptional range persist through body-sourced tactical commitment without free movement, dead turns, or permanent control? |
| Mechanic variant | Package C - Resolution-Bound Range Tenure |
| Expected dynamic | Specialists repeatedly invest legal sourced results; general builds exploit temporary states but cannot sustain them automatically. |
| Desired player experience | "I held this distance with this body and commitment," not "I pressed Move Away again." |
| Instrumentation | Prior/final range, counter, classification, source profile, locks, maintenance condition, cancellation, automatic response, and settling reason. |
| Continue criteria | Maintenance competes with meaningful Main choices; source damage removes future access; no universal kiting or Clinch loop. |
| Revise criteria | Maintenance becomes mandatory, Reply always controls final range, or Distant repeatedly creates non-decisions. |
| Kill criteria | The grammar needs a universal movement action, ambient upkeep, hidden refresh, new resource, or invented production content. |
| Evidence class | Owner-approved paper architecture informed by primary comparable-system evidence; no runtime or human-experience evidence. |
| Contamination risks | Designer familiarity, neutral diagnostic promotion, explanatory prompting, and paper clarity mistaken for player comprehension. |
| Decision owner | Can Yuzbey. |

## 15. Hostile review

| Risk | Severity | Required safeguard |
|---|---|---|
| Permanent Clinch through free Grip Strike | Critical | Existing Grip Strike is exploit-only in the fixture; no implicit maintenance. |
| Free Distant upkeep through Focus, treatment, or items | Critical | Preparation cannot refresh range. |
| Automatic defense maintains forever | Critical | No default spatial result; attack/response chain must explicitly author one. |
| Reply always owns final range | High | Alternate Lead, bounded telegraph, source legality, same-card revalidation, and cancellation cases. |
| Source loss has no consequence | Critical | Future maintenance access is re-derived immediately; no substitution. |
| Counter becomes hidden stacking | High | Fixed visible `1`/`2` bases and no accumulation. |
| Distant creates dead turns | High | Paper fixture records legal neutral actions, but current content cannot support experience claims about a Distant build. |
| Neutral fixture becomes a card | Critical | Named diagnostic boundary and catalogue/runtime negative audit. |
| Range edits wounds, Blood, harvest, or outcomes | Critical | Range has no authority over those systems. |
| New grammar silently changes simulator behavior | Critical | Documentation-only approval; runtime/config/tests remain unchanged. |

No P0 or P1 contradiction remains after disallowing implicit maintenance, keeping
Preparation non-maintaining, and refusing to promote current actions without authored
spatial behavior. The principal evidence gap is positive Distant-specialist play:
current content does not contain such a build, so the neutral diagnostic can validate
the grammar but not the experience.

## 16. Approval record and explicit deferrals

On 2026-08-17 the owner selected **Package C**.

Approved paper direction:

- Neutral, Exploit, Maintain, Shift/Create, and Release classifications;
- execution-bound, non-stacking maintenance;
- Preparation may enable but never refresh range alone;
- one final authored spatial result for an incoming action/automatic-response chain;
- Package D source profiles and document 32 cancellation/revalidation rules;
- sequential Lead/Reply range contest without another phase or roll;
- no implicit maintainer or releaser in current production content;
- one neutral diagnostic profile for bounded paper validation;
- deterministic evidence, visible counters, and player/enemy symmetry.

Deferred:

- runtime, configuration, implementation plan, and production tests;
- individual production Maintain, Shift/Create, Release, and exploit profiles;
- exact timing, damage, defense, exposure, accuracy, and reflex values;
- a production Distant or Clinch specialist body/action;
- detailed automatic Dodge/Evade, active Cover It, and broader reflex work;
- multi-actor range, movement maps, terrain, collision, pursuit, and escape;
- new cards, limbs, items, tools, characters, encounters, and rewards;
- final UI, accessibility implementation, balance, Unity, and product claims.

## 17. Recommended next decision at Package C approval

Resolve treatment, repair, extraction, and graft commitment flow as one paper package:
which actions use Preparation or Main, which activate on lock or execution, how source
occupation and cancellation work, and how those commitments preserve the separation
between treatment, structural repair, Blood restoration, extraction quality, and
grafting. Do not implement runtime or add production content from this recommendation.

## 18. Later Package B resolution (2026-08-17)

Document 36 resolves that decision with Tiered Atomic Commitments. Treatment, Blood
restoration, repair, Claim, extraction, salvage, graft, and table procedures are
range-neutral by default and gain no maintenance or release authority by implication.
Their Preparation/Main/contextual timing, exact-source reservation, execution-time
payment, cancellation, and atomic chains remain inside documents 29, 32, 33, and 34.
Runtime and production profiles remain unchanged. The next dependency-safe gate is
Limb for Life and catastrophic survival.
