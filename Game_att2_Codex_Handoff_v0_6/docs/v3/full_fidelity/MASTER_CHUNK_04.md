# V3 Full-Fidelity Master — sequential chunk 04/12

### Archived doc 39
Brain performed weighted hand selection, no Attack/Defence guarantees, hard filters possible.

### Archived doc 41
Superseded doc 39: player authored active deck; ordinary draw; Brain only deterministic hand interpreter, not selector.

### V2 living doc 2026-08-25
Returned to imperfect Attention + Brain-Part configured weighted selection after Concept Deck construction, with no category guarantee as a diagnostic baseline.

### V3 owner decision
New synthesis:
- Brain Architecture is distinct from Brain Parts;
- Brain Architecture may guarantee tactical slot classes;
- Brain Architecture may have flexible slots and parameter biases;
- Attention chooses exact legal expression through complex weighting;
- player may configure Brain at safe boundaries;
- different Brains may have different architecture;
- Brain Parts modify architecture/access/execution downstream.

Thus:
V3 supersedes both "no guarantee" and "Brain must never affect selection" as universal claims.

## 8. Brain slots

Example only:
Attack / Attack / Defence / Flexible.

Hard guarantee answers "what tactical opportunity class exists".
Attention answers "which exact body expression fills it".

## 9. Flexible slot

May use distribution across:
Attack / Defence / Utility / Preparation / Recovery.

Exact categories OPEN.

## 10. Brain biases

May reference:
- class;
- Heavy/Light;
- damage magnitude;
- Blood cost;
- Precision;
- Control;
- Recovery;
- source family;
- other functional labels.

## 11. Limb base distribution

Each source/card family can have intrinsic base weights.

Example:
one arm may naturally favor Heavy over Light.
This is part of limb identity.

## 12. Recency

Recent surfaced cards receive soft suppression.

Purpose:
- avoid repetitive hands;
- expose body vocabulary.

Not a default hard cooldown.

## 13. Source state

Degradation may alter:
- legality;
- effect profile;
- Attention weight.

A damaged heavy limb may surface a desperate technique more often than a controlled one if authored.

## 14. Context

Allowed only when explicit/causal.
No hidden "player needs defense, secretly give defense" pity rule.

## 15. Weight formula — working prototype

`W = W_limb × W_brain × W_recency × W_state × W_concept × W_context`

This is replaceable if diagnostics show bad behavior.

## 16. Selection order

1. resolve slot role;
2. build source-valid expressions;
3. Concept exchange/filter;
4. state legality;
5. slot compatibility;
6. base weight;
7. Brain bias;
8. recency;
9. state factor;
10. Concept factor;
11. context;
12. normalize;
13. seeded weighted select;
14. log trace.

## 17. Empty slot

Never fabricate a card.

If guaranteed class has no legal physical expression, the system must expose the real contradiction:
- shaded/empty;
- fallback state-required action only if separately legal;
- or Brain architecture legality/preparation constraint during configuration.

Exact UX OPEN.

## 18. Persistent hand lifecycle

V2 useful baseline:
unused valid options persist;
played becomes Spent;
Spent/Invalid refill at Decision Refresh;
source invalidation removes dependent card immediately;
no mid-exchange replacement by default.

V3 keeps this as a **preferred V3-1 comparison baseline**, not final lifecycle.

## 19. Attention control

### Drop
No unrestricted immediate refill.

### Focus
Bias a source/family, not exact card guarantee.

### Blood Redraw
Bounded immediate reroll.
Recommended inherited safeguard: if no legal alternative, disable and spend nothing.

## 20. Player-facing opacity

Default UI:
qualitative tendencies, not percentages/equation.

Debug:
full exact weights and roll.

## 21. Specialization

Reducing eligible sources may intentionally increase consistency.
This is valid if body opportunity costs remain real.

## 22. Brain Parts

INHERITED ACTIVE DOWNSTREAM:
rare persistent boss/progression rewards;
paired buff/nerf;
one primary lever;
no source/card invention;
no hidden punishment;
no ordinary extra action by default.

## 23. Embodied instability doctrine migration

Archived doc 41 correctly rejected:
- generic insanity;
- hidden control theft;
- arbitrary random punishment.

V3 preserves that.

However Brain is no longer prohibited from influencing access.
Embodied instability becomes one possible modifier/cost channel derived from current body composition, not the total Brain identity.

## 24. Enemy symmetry

Preferred implementation direction:
enemy uses same internal source legality / Attention engine where useful;
hidden from player;
AI may rank only cards actually present/available;
cannot choose absent/illegal card.

V3-1 can omit enemy Brain complexity if not needed for the test.

## 25. V3-1 Hardening Amendments — Deterministic Fixture Result

The V3-1 architecture fixture established four additional binding invariants.

### V3-RQ-053 — Guaranteed Duty != Guaranteed Card

A Brain slot may guarantee a tactical **duty** such as Attack or Defence.

It does **not** guarantee that the current body can physically supply a legal expression for that duty.

```text
Brain guarantees duty
→ Body supplies legal expressions
→ Attention selects among those expressions
→ if pool is empty: slot is SHADED / EMPTY
→ no class substitution
→ no source invention
```

This wording supersedes loose V3 phrases such as “guaranteed Attack card”.

### V3-RQ-054 — Architecture Feasibility Warning

At a Brain-configuration boundary, the system should calculate visible coverage:

```text
Attack Duty Coverage: available legal Attack expressions / guaranteed Attack duties
Defence Duty Coverage: available legal Defence expressions / guaranteed Defence duties
```

Insufficient coverage is not automatically forbidden because deliberate specialization is legal.
It must, however, be visible before commitment/configuration.

### V3-RQ-055 — Redraw Alternative Invariant

A Blood-paid redraw is legal only when a **distinct legal alternative** exists for that slot duty.

If no legal alternative exists:

```text
redraw disabled
→ no Blood spent
→ current option remains
```

The system may not charge Blood for a no-op reroll.

### V3-RQ-056 — Causal Specialization

The system must not secretly normalize away extreme specialization.

If one Attack expression is the only legal Attack expression, it may become perfectly consistent in the first satisfiable Attack duty. Additional Attack duties may shade if no distinct legal expression remains.

The downside must emerge from actual lost body coverage, redundancy, defence, or world capability—not a hidden anti-specialization penalty.

---

# SOURCE DOCUMENT: docs/07_INVENTORY_READIED_ITEMS_AND_OPPORTUNITY_ORIGINS_V3.md

# Inventory, Readied Items, and Opportunity Origins V3

**Status:** INHERITED ACTIVE DIRECTION; CONTENT DOWNSTREAM

## 1. Canonical origins

- Body
- Inventory
- State-required
- Automatic

Opportunity origin is immutable for rules purposes.

## 2. Final V2 Readied Item contract inherited into V3

One owned Item Card may be deliberately readied:
- before encounter or approved boundary;
- separate visible lane;
- no Attention capacity cost;
- exact item ownership/quantity/use/expiry/source/target/timing/cost;
- consumes Preparation or Main according to definition;
- maximum one voluntary inventory-origin action per actor/round;
- used/lost/expired/invalid lane becomes empty;
- no automatic replacement.

In-encounter re-readiness remains OPEN.

## 3. Historical A2 readiness model

Archived doc 34 originally put inventory in an Adaptive Attention slot.
Doc 39 superseded that requirement.
V3 does not restore inventory to ordinary Attention.

Retained from doc 34:
- ownership;
- quantity/use/expiry;
- source reservation;
- no substitution;
- pay-on-execution distinction;
- one inventory action/round;
- passive/active separation;
- multi-source tool validation;
- signature override governance.

## 4. Cost timing

Definitions may declare:
- on_lock;
- on_execution.

If canceled before execution:
unpaid execution-time resources/uses remain unspent.

A protective effect that explicitly activates on lock may keep its lock cost.

## 5. Multi-source tool

Declares exact item + exact body sources.
No silent other-hand grip or substitute copy.

## 6. Passive equipment

Passive is automatic/passive.
Activated ability remains voluntary inventory-origin and must obey action budget.

## 7. State-required item rescue

If a state-required action permits item input:
- show only actually owned legal items;
- no generated item;
- normal source/use/cost/timing remains;
- activation still counts inventory-origin action.

## 8. V1 item migration

Blood Bag / Clotting Cream / Bone Scissors / Hell Saw / Claim the Cut / Black Stitch are legacy fixtures, not active V3 content by default.

Their strongest preserved lessons:
- recovery can distort Blood economy;
- extraction tool must own clear source/commitment;
- consumable vs per-fight refresh must be explicit;
- treatment effect should not create a full inventory magic system accidentally.

## 9. Definition schema

```text
opportunity_id
origin
timing
definition_source
required_sources
reserved_sources
item_instance/stack
uses/expiry
full/strained/desperate profile
cost_timing
costs
target
effect package
lifecycle
invalid/dormant reason
signature override
```

Range profiles from older docs are removed from active V3 sample.

---

# SOURCE DOCUMENT: docs/08_DEFENSE_WILL_SURRENDER_AND_RESOLUTION_V3_FULL.md

# Defense, Will, Surrender, Claims, and Resolution V3 — Full

**Status:** ACTIVE PAPER RULES + RESEARCH NUMERICS

## 1. Threat cues

Yellow → Block/Parry.
Red → Evade.

Color requires redundant visual/audio language.

## 2. Block

- exact guarding source chosen;
- source legal/usable;
- target not silently changed except through Block rule;
- guarding source becomes final structural recipient;
- can lose capability;
- no one-integrity disposable exploit if later numeric formula is used.

## 3. DWF-0.1 research comparison

Preserve, do not activate:
- `projected_guard_loss = ceil(D * 0.75 * GuardFactor)`
- GuardFactor reinforced .80 / ordinary 1.00 / fragile 1.20
- minimum 900ms cue
- Block lock 250ms before contact
- Parry ±90ms
- Evade ±180ms
- assists 100/140/200%
- defense speed 100/75/50/pause
- bilateral Will 90
- Parry loss 24/30/36
- no passive Will recovery

These are research values only.

## 4. Parry

Success:
- prevents incoming Integrity/wound/Blood consequence under current paper rule;
- reduces Will.
Failure:
- original attack applies;
- no extra hidden penalty.

## 5. Evade

Red-only default.
No range state.

## 6. Accessibility

Timing assists never:
- reduce reward;
- alter legal source;
- convert Red to Block;
- create extra action.

## 7. Will

Visible continuation/confidence state.
No ordinary damage conversion.

Possible explicit sources:
- successful Parry;
- GoalCritical source shock;
- goal/objective loss;
- future authored event.

Exact V3 mutation set OPEN.

## 8. DWF Will research

Historical comparison:
90 starting, 0 recovery, Parry 24/30/36,
GoalCritical strain 6 / desperate 9 / offline15,
claim unavailable18.

Research only.

## 9. ClaimWindow

Broken Will transfers nothing.

Validate:
- both alive where required;
- credible threat;
- pre-disclosed claim;
- useful/transferable;
- advances Goal/Need;
- nonlethal release remains playable where content contract requires.

## 10. Defy fork

OPEN.

Enforced claim:
valid claim applies at Broken Will.

One-Defy:
one final option to reject nonlethal resolution and continue under lethal stakes if a legal physical continuation exists.

No second surrender after Defy under that hypothesis.

## 11. Player retreat/surrender/bargain

Allowed where legal route/counterparty exists.
Consequence must be disclosed/current-state based.
No inventory scan for "worst punishment".

## 12. State-derived outcome

