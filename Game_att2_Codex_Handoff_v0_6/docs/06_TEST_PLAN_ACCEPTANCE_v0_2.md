# Game att2 — Simulator Test Plan and Acceptance v0.2

## Evidence goal

Tests prove faithful implementation and detect numerical/systemic problems. They do not prove fun.

Documents 27 through 39 contain later owner-approved paper directions, and document
40 reconciles their system boundaries. They do not change this simulator acceptance
baseline. Before any implementation of document 32,
an approved bounded plan must add deterministic tests for Lead assignment and
alternation, two-lock information order, on-lock versus on-execution costs, changed-
state Reply revalidation, cancellation states, automatic reflex integration, death
before Reply, atomic completion, and genuine same-timing batches.

For document 33, a future approved implementation plan must trace its
SMI-D requirements to deterministic tests for source profiles, weakest-source
selection, Desperate/Dormant distinction, effect delivery and final-recipient
ownership, centralized caps/expiry, coherent-baseline snapshots, Echo hard caps,
one-axis collision suppression, prohibited Echo channels, readable previews, and
player/enemy symmetry. Illustrative Poison/Burn cases are not production content.

For document 34, a future approved implementation plan must cover deliberate
inventory readiness, one inventory action per round, Reconsider lifecycle, item use
timing, source/tool loss, no substitution, state-required ownership, and automatic-
defense separation.

For document 35, a future approved implementation plan must trace `RMG-C-001`
through `RMG-C-012` to deterministic tests for explicit range classifications,
non-stacking maintenance, Preparation negative cases, source-state revalidation,
automatic-defense spatial outcomes, sequential Lead/Reply contest, no implicit
production maintainer/releaser, neutral-fixture quarantine, readable counters, and
player/enemy symmetry.

## 1. Unit tests

### Configuration and definitions

- reject duplicate IDs;
- reject missing body slots;
- reject invalid integrity/cost/reference;
- ensure Grip Strike is not configured as clean-sever capable;
- load all supplied YAML successfully.

### Limb thresholds

- 30/30 is Intact;
- 20/30 is Damaged;
- 10/30 is Critical;
- zero from basic attack becomes Ruined/Disabled, not Clean Severed;
- zero from valid Bone Scissors extraction becomes Severed with Clean Harvest;
- tags do not overwrite primary state incorrectly.

### Acting source

- Damaged source applies 75%;
- Critical source applies 50%;
- unusable source cancels action;
- enemy action cancels if source is disabled by earlier player action.

### Blood

- spend/gain logs before/delta/after/reason;
- insufficient blood action is illegal unless a documented effect allows debt;
- Panic Pulse triggers from damage, bleeding, or voluntary spending crossing below 25;
- Pulse triggers once and caps at 35;
- Blood 0 creates death when no approved prevention resolves;
- Limb for Life removes one seeded usable non-Core limb, restores 12 once, and logs
  that death was prevented;
- no eligible limb or an already-used Limb for Life produces final death.

### Approved wound direction and deferred runtime contract

- config locks Cover It duration to exactly one round while its effect remains
  explicitly runtime-deferred;
- document 31 supplies the approved paper target/source/redirection contract, but no
  runtime test may infer or implement it before a separate approved migration plan;
- ordinary runtime limb damage must not create the newly approved wound-to-Blood
  behavior before a separate implementation gate supplies validated numeric config;
- future wound implementation tests must cover the approved four families, one
  dominant wound per slot, treatment states, repeat-Major Ruin for arms/Legs, repair
  boundaries, sever/harvest separation, symmetry, basic-attack no-Clean behavior, and
  the Ruined-Torso rescue window;
- runtime acceptance additionally requires an approved numeric table for thresholds,
  Blood loss, repair, treatment timing, worsening, and caps.

### Timing

- Focus does not consume main action;
- one Focus per round;
- no Focus with unusable Head;
- damaged Head raises cost;
- critical Head uses injected RNG for incomplete info;
- at most one Fast item per round;
- Fast item occurs before main action;
- consumables persist as consumed across encounters;
- fight-use tools refresh per fight.

### Harvest and tools

- Claim marks and upgrades subsequent valid sever to Clean;
- Claim does not itself sever;
- Bone Scissors Critical valid limb Clean severs;
- Stabilized modifies Bone Scissors attempt and failure creates Hanging/Disabled;
- Hell Saw seeded success/failure paths;
- Hell Saw failure gives Rage exactly once;
- Marked and unmarked salvage distributions use injected RNG;
- Ruined cannot normal emergency graft.

### Grafting

- Clean and Stressed stability tables;
- slot replacement updates available actions;
- Unstable Twitch/Works/Ache/Surge branches;
- Ache queued disable;
- Surge cost reduction or +2 fallback;
- Integrated graft stops normal instability checks.

### Plead/surrender

- generic Plead Pressure increments only from documented triggers;
- basic plead at 2;
- Jeff pleads after both clean-severed arms;
- Jeff incapacity-surrenders after both arms unusable without granting clean quality;
- Anna offer trigger recognizes Unstable/Bleeding/threatened graft.

### Table

- affordability and transformations;
- table loan stores minimal debt record;
- leave unchanged is legal;
- cannot integrate missing/non-grafted arm.

## 2. Integration scenarios

### S1 Jeff Baseline Acquisition

Purpose: intended extraction chain. Scripted or strategy decisions should mark right arm, damage, use saw, disable/extract left, bargain, and emergency graft.

Pass invariants:

- clean right-arm harvest possible;
- blood transactions fully logged;
- new Guard Flesh available after graft;
- final blood above 0;
- seed reproducible.

### S2 Jeff No-Spend Exploit

Purpose: spam free attacks.

Pass invariants:

- Jeff may surrender through incapacity;
- no Clean Harvest from free attacks;
- player cannot gain premium graft without spending through salvage/other valid route.

### S3 Failed Hell Saw Spiral

Purpose: force saw failure, Rage, Bleeding pressure.

Pass invariants:

- failure is explicit;
- projected/actual critical state visible;
- Panic/Limb for Life/death timing correct;
- no hidden rescue.

### S4 Anna Stabilization Path

Purpose: first Unstable graft, Focus/Guard/medical timing, accept treatment.

Pass invariants:

- player can trade limb greed for stabilization;
- fight can end without Anna death;
- Unstable removed and event logged.

### S5 Anna Greed Path

Purpose: reject treatment and pursue Crude Graft Arm.

Pass invariants:

- Stabilized sever penalty visible;
- valid success/failure paths;
- risky extraction remains possible;
- no automatic free arm.

### S6 Mini-Campaign

Purpose: end-to-end source-of-truth loop.

Pass invariants:

- S-001 → Jeff → graft → Anna → table completes;
- at least one body change affects later encounter options;
- final summary describes body, blood, items, decisions, unresolved vulnerability.

### S7 Blood Bag Balance Variants

Purpose: compare current Blood Bag against documented alternative values without changing baseline.

Pass invariants:

- variants are config overlays;
- report use timing and survival/body outcomes;
- implementation does not automatically select a winner.

## 3. Strategy batch

Run default 100 seeds for each:

- balanced;
- blood_hoarder;
- limb_greed;
- survival_first;
- reckless_sever.

Minimum report:

- encounter completion and death rate;
- average/median final blood;
- blood spent/gained;
- Clean/Stressed/Ruined outcomes;
- action frequency;
- graft/stabilization/table paths;
- identical final body rate.

## 4. Acceptance gate

## 4A. Encounter 3 moderated paper-test gate

This is paper evidence only and does not alter simulator implementation acceptance. Run eight valid free-choice human sessions using fixture `E3-PRETABLE-01` and the P01–P08 Known/Unknown × Policy A/B matrix.

A positive signal requires all ten:

1. At least six participants explain one target-damage → weakened/lost Warden-action relationship.
2. At least two strategic families produce a non-death result.
3. No player action is required in every successful session.
4. No Warden action executes from an unusable source.
5. No facilitator invents anatomy or a hidden weak point.
6. Known Threat changes planning without one universal table choice.
7. At least two table options remain defensible in observed play.
8. Logged state and decisions explain failures.
9. No undocumented rescue, immunity, or narrative override occurs.
10. Every participant encounters a meaningful consequence of the table choice.

Revise if Strengthen is nearly mandatory; one policy causes unavoidable death; 40-Blood Leave dominates; Knockdown is not understood; source disabling is trivial/irrelevant; Guard or Repair lacks defensible use; the round cap frequently decides outcomes; moderators need biological judgment; or success relies on an unpublished rule.

A material facilitator deviation contaminates that session and excludes it from aggregate conclusions. Eight valid sessions—not merely eight attempts—are required. Human testing does not authorize runtime implementation or Unity.

### Implementation pass

- all mandatory unit tests pass;
- all seven integration scenarios execute and meet invariants;
- same seed produces identical events/results;
- text and JSON reports contain required fields;
- package has no runtime UI/engine dependencies;
- no undocumented mechanic was introduced.

### Product continue signal

Report a positive simulator signal—not an automatic Unity approval—if:

- no-spend does not reliably produce premium limbs;
- blood-cost actions appear in successful Balanced/Limb Greed runs;
- Unstable increases risk without making most runs unavoidable failures;
- Anna stabilization and greed paths both occur under plausible strategies;
- table choices are not universally identical;
- body changes affect later legal actions/decisions.

### Revise signal

- one action dominates all strategies;
- Blood Hoarder earns equal/better premium bodies;
- Blood Bag is always used immediately and erases risk;
- Hell Saw is always or never rational;
- Anna always kills or is always trivially spared;
- table option is universal;
- most successful runs converge to one body;
- logs cannot explain failures.

### Unity remains blocked

Even passing simulator tests do not automatically approve Unity. Produce a review recommendation first.

## 5. Future Package B paper/runtime obligations

Document 36 adds future acceptance requirements `TAC-B-001` through `TAC-B-015`.
They are obligations for any later approved paper instrument or runtime migration;
they do not alter the current simulator acceptance gate.

At minimum, future evidence must prove:

- separate ownership of treatment, Blood restoration, structural repair, extraction,
  and graft effects;
- explicit origin, timing, exact sources, target, cost/use stage, and ordered effects;
- the one-voluntary-inventory-action limit across Preparation and Main;
- pre-execution cancellation without resource/tool loss and without partial mutation;
- complete atomic success/failure chains after execution begins;
- attachment, wound-state, structural-band, and ceiling checks for repair;
- donor-wound and harvested-object separation with invariant harvest quality;
- contextual access and ownership before salvage or graft;
- no bonus combat action or implicit healing from emergency graft;
- isolated table effects and player/enemy causal symmetry.

The bounded cases are `TAC-B-01` through `TAC-B-14`. No test implementation,
fixture data, configuration, or production content is approved by this section.

## 6. Future Package A catastrophic-survival obligations

Document 37 adds future acceptance requirements `CIS-A-001` through `CIS-A-016`.
They govern any later approved paper harness or runtime migration and do not change
the current simulator acceptance gate.

At minimum, future evidence must prove:

- Blood-0 rescue occurs only after the current atomic chain and Panic Pulse;
- one visible tutorial-scope charge, exact eligible arm/Legs choice, and Accept Death;
- no random sacrifice, Head/Torso/Core eligibility, or hidden objective immunity;
- one atomic severance, Untreated Stump, no-harvest, final-net-12 chain;
- later stump pressure without a duplicate immediate post-reset loss;
- zero Preparation/Main/inventory/readiness/defense/Reply/Lead consumption;
- complete body-source, capability, Attention Slot, Integrity Echo, range, and lock
  recomputation;
- Blood-0 rescue without prevention or delay of catastrophic Torso failure;
- actor-explicit availability with symmetric causality and no generic victory-route
  requirement;
- a complete preview and deterministic fatality-source trace.

The bounded cases are `CIS-A-01` through `CIS-A-16`. No test implementation, fixture
data, configuration, UI, or production content is approved by this section.
