# Game att2 — H1 Hybrid Combat Specification v0.1

Status date: 2026-08-11

Status: owner-approved, documentation-only H1 contract for implementation planning.
This document defines the smallest testable H1 research slice. Approval permits a
traceable implementation plan; it does not approve runtime implementation, change
Combat Rules v0.5, add content, or provide evidence that the hybrid loop is fun or
accessible.

Authority: the 2026-08-11 owner decisions recorded in the Development Master and
decision ledger, interpreted under `AGENTS.md`, Combat Rules v0.5, and the systemic
causal design contract.

## 1. Research objective

H1 asks one question:

> Can a broadly present but usually modest timing-based Block layer add execution
> ownership to the existing turn strategy, while body source, preparation, Blood,
> intent, and prior mistakes remain decisive?

The smallest proof reuses the post-Jeff player and Anna's existing `Surgical Jab`.
It does not attempt to prove the full combat model.

The Torso target used below is the current research-shell fixture, not a new general
rule for Anna's targeting behavior. H1 must not promote that fixture choice into final
enemy behavior or canon.

## 2. Owner-resolved direction

1. **Strategy-led with bounded clutch recovery.** Strategy normally dominates.
   Reflex skill usually reduces bad consequences or improves good consequences by a
   modest amount. Exceptional execution may occasionally convert an extreme but still
   legally recoverable situation into a costly survivable one.
2. **Broad, tiered reflex presence.** Reflex opportunities should exist in most
   readable physical interactions. Most have small effects; prepared or strongly
   telegraphed interactions may have material effects; life-changing effects are rare.
3. **Commitment-sensitive failure.** Missing an ordinary reflex applies the original
   consequence only. Additional exposure is legal only for a clearly disclosed,
   voluntarily selected high-risk response.
4. **Dual Body-as-Build proof.** Jeff's grafted Right Arm both enables the strongest
   defensive response against Anna and becomes a source the player risks when using
   that response. Damage or loss of the arm weakens or removes the capability.

These decisions do not permit reflexes to restore an unusable source, waive Blood
costs, ignore reach, directly select victory, or repeatedly erase a structurally bad
plan.

## 3. Scope

H1 contains only:

- the existing six-slot player body and Blood model;
- a controlled post-Jeff player state;
- the existing Grafted Human Right Arm and `Guard Flesh` action;
- Anna's existing Right-Arm-sourced `Surgical Jab` against the player's Torso;
- broad, partial, and exact intent states;
- one Preparation choice and one Main action;
- one reflex response family: `Block`;
- prepared, unprepared, and explicitly high-risk Block variants;
- scripted timing inputs for deterministic replay and a human-input boundary for later
  research;
- structured events and comparison metrics.

H1 is a single controlled interaction with comparison fixtures, not a full encounter,
campaign rewrite, or content expansion.

## 4. Explicit non-goals

H1 does not define or implement:

- exact milliseconds, grade thresholds, or mitigation percentages;
- new wound classes, wound-to-Blood mappings, or Ruined Torso lethality;
- active `Cover It`, a final movement model, Dodge, Parry, Counter, or Stamina;
- generalized reflexes for every attack;
- a new enemy, limb, item, reward, anatomy rule, or Anna personality rule;
- generalized mental defeat, full negotiation, or new encounter resolutions;
- final controls, UI, animation, audio, engine, Unity, or accessibility certification;
- Encounter 3 or the Warden in runtime or H1 fixtures.

## 5. Controlled fixture

### H1-F0 — shared prior state

Use a deterministic post-Jeff snapshot with:

- the player alive and able to continue;
- the Grafted Human Right Arm present and usable unless a comparison variant says
  otherwise;
- enough Blood to afford already-approved actions used by the fixture;
- no uncontrolled Unstable roll during the measured interaction;
- Anna alive with a usable Crude Graft Arm;
- Anna declaring `Surgical Jab` from her Right Arm against the player's Torso;
- no invented wound or fatal-Torso consequence.

If the fixture retains an Unstable tag for fidelity, its roll must be scripted and
identical across paired comparisons. H1 must not mistake graft randomness for a reflex
effect.

### Required paired comparisons

| ID | Changed condition | What it isolates |
|---|---|---|
| H1-C1 | Unprepared Block versus prepared `Guard Flesh` | Value of strategic preparation |
| H1-C2 | Usable grafted Right Arm versus unusable/missing Right Arm | Body-derived capability gain and loss |
| H1-C3 | Ordinary Block versus disclosed high-risk Block | Commitment-sensitive failure |
| H1-C4 | Broad/partial versus exact intent | Information and prediction value |
| H1-C5 | Precise timing profile versus assisted/non-precise profile | Whether the causal decision survives input accommodation |
| H1-C6 | Normal versus threshold-pressure Torso state | Bounded clutch recovery without inventing lethality |

Paired fixtures must differ only in their named condition.

## 6. H1 interaction sequence

```text
1. State
   Show public body state, Blood band, legal source status, and current intent clarity.

2. Preparation
   Player chooses one allowed preparation, such as Focus or Fast treatment.

3. Commitment
   Player chooses one Main action. Guard Flesh is the prepared-Block comparison;
   another legal Main action leaves Block unprepared.

4. Revalidation
   Recheck Anna's attacking source, the player's blocking source, target, Blood cost,
   action commitments, and intent requirements. Reject or cancel invalid actions.

5. Reflex opportunity
   If Surgical Jab and the selected response remain legal, expose the configured
   Block opportunity and record its timing profile and risk class.

6. Execution grade
   Convert the recorded input into a grade. The grade selects only an approved state
   modifier; it never selects victory or narrative outcome.

7. Consequence
   Resolve original Torso pressure, mitigation, any declared Right-Arm exposure, and
   limb-state changes. Do not infer Blood loss from ordinary limb damage.

8. Recompute
   Recompute Guard/Block availability from the resulting Right-Arm state and record
   whether the body-derived capability remains available.
```

## 7. Reflex tiers

The product direction uses three tiers. H1 implements or simulates only enough of each
tier to validate the shared contract.

| Tier | Eligibility | Intended effect scale | H1 representation |
|---|---|---|---|
| Routine | Readable, blockable physical action with a legal response source | Small reduction of a bad consequence or small improvement of a good one | Unprepared Block against normal Surgical Jab pressure |
| Significant | Prepared defense, strong telegraph, or meaningfully committed attack | Material mitigation, secondary-effect prevention, or source exposure change | Guard Flesh-prepared Block |
| Critical | Extreme state, legal source, clear high-risk commitment, exceptional execution | Rare conversion of a severe approved consequence into a costly survivable state | Threshold-pressure comparison only; downstream wound/death claims remain deferred |

The Critical tier is not permission to invent a rescue from Blood-0 death, Ruined
Torso, or an unusable source. H1 may show that a legal exceptional Block preserves a
known integrity threshold; it must label any unapproved downstream consequence
`DEFERRED`.

## 8. Block contract

A Block opportunity is legal only when all are true:

- the incoming action exists, remains legal, and is marked blockable for H1;
- the attacking source remains usable;
- the player has received the minimum required telegraph;
- the selected blocking source exists, is usable, and can reach the attack path;
- the source is not incompatibly committed to another action;
- required Blood or item costs are affordable;
- the actor is not blocked by Downed or another approved condition.

### Unprepared Block

- Uses a legal available source without prior Guard preparation.
- Uses the routine timing profile and routine result floor.
- A miss resolves the original Surgical Jab consequence only.
- Exceptional input may improve the approved state modifier, but cannot overcome a
  missing, disabled, unreachable, or incompatibly committed source.

### Prepared Block through Guard Flesh

- Guard Flesh remains a Blood-cost Main action sourced by the grafted Right Arm.
- Preparation must improve at least one measurable dimension: opportunity tolerance,
  result floor, mitigation ceiling, secondary-effect control, or exposure safety.
- The same arm may perform the reflex because Guard Flesh explicitly prepares it for
  that job; this is not an incompatible double commitment.
- If the arm becomes unusable before execution, the Block is canceled and no hidden
  substitute source appears.

### High-risk Block

- Must be explicitly selected and labeled before timing input.
- Must disclose the additional failure exposure and its affected source.
- A miss resolves the original Surgical Jab plus only that disclosed exposure.
- It cannot add unrelated damage, Blood loss, status, or narrative punishment.
- It exists to test rare clutch recovery, not to make ordinary Block attempts punitive.

## 9. Execution grades

H1 uses qualitative grades whose thresholds and numeric state modifiers remain
configurable:

| Grade | Ordinary response | High-risk response |
|---|---|---|
| Miss | Original consequence | Original consequence plus disclosed source exposure |
| Limited | Small approved mitigation | Small mitigation; declared commitment remains relevant |
| Strong | Material approved mitigation or secondary-effect control | Material mitigation with explicit source consequence if configured |
| Exceptional | Best legal state modifier for this opportunity | May preserve an approved threshold in a rare crisis; never directly selects survival or victory |

The grade vocabulary is a prototype default. H1 must log the raw/scripted input,
profile, derived grade, state modifier, and final mutation separately.

## 10. Body-as-Build causal proof

H1 must demonstrate this exact dependency:

```text
Jeff's Right Arm acquired and grafted
→ Guard Flesh and arm-sourced Block become legal
→ Anna's Surgical Jab creates a reason to use them
→ using the arm may commit or expose it
→ resulting arm integrity/state is mutated explicitly
→ Guard/Block capability is recomputed
→ an unusable arm removes the strongest defensive response
```

Passing a timing input without the arm must not reproduce the arm-enabled result.
Conversely, owning the arm without using it must not grant automatic perfect defense.

## 11. Requirements

| ID | Requirement | Acceptance evidence |
|---|---|---|
| H1-RQ-001 | Strategy remains relevant to every reflex result. | Prepared/unprepared and intent comparisons produce explainable differences. |
| H1-RQ-002 | Reflexes use a tiered effect scale. | Routine, significant, and bounded critical profiles are distinct in logs/config. |
| H1-RQ-003 | Every Block names and validates its physical source. | Missing/disabled/committed-source negative fixtures reject or cancel Block. |
| H1-RQ-004 | Guard Flesh materially improves prepared Block. | H1-C1 changes at least one declared opportunity/outcome dimension. |
| H1-RQ-005 | Ordinary misses add no extra punishment. | Ordinary miss equals the original attack consequence. |
| H1-RQ-006 | Extra failure exposure requires explicit high-risk commitment. | H1-C3 preview and event log identify the chosen risk and affected source. |
| H1-RQ-007 | Execution grades mutate state, not resolution. | No grade writes victory, survival, bargain, or narrative outcome directly. |
| H1-RQ-008 | The grafted arm is both capability and liability. | H1-C2 and post-mutation capability recomputation show gain/loss. |
| H1-RQ-009 | Exceptional skill cannot bypass illegality. | Exceptional scripted input still fails with an unusable or incompatible source. |
| H1-RQ-010 | H1 supports precise and assisted/non-precise input profiles. | Both profiles use identical legality and causal-resolution rules. |
| H1-RQ-011 | H1 evidence is replayable and inspectable. | Scripted timing inputs reproduce identical grades, mutations, and events. |
| H1-RQ-012 | Deferred physical rules remain deferred. | No new wound-to-Blood or Ruined Torso result appears in spec/runtime/config. |

## 12. Structured evidence

Every H1 attempt must record:

- fixture and comparison ID;
- prior player and Anna body/source states;
- Blood before and after approved transactions;
- public intent clarity and telegraph profile;
- Preparation and Main commitments;
- incoming action, target, and source;
- selected Block source and risk class;
- legality/revalidation results and disabled reasons;
- timing profile plus raw or scripted input;
- execution grade and selected state modifier;
- original consequence, mitigation, declared exposure, and final mutations;
- recomputed Guard/Block availability;
- any causal link marked `DEFERRED`.

Minimum comparison metrics:

- opportunity offered/denied/canceled counts and reasons;
- grade distribution by prepared state and timing profile;
- target damage or other approved pressure prevented;
- blocking-source integrity/state change;
- capability retained/lost after resolution;
- ordinary versus high-risk miss consequences;
- cases where exceptional input was rejected by source illegality;
- comprehension answers for threat, source, preparation benefit, cost, and new risk.

## 13. Evidence card

```text
Question or hypothesis:
Does broadly available, usually modest Block execution reinforce turn planning and
Body as Build while permitting rare legal clutch recovery?

Mechanic/config variants:
Prepared/unprepared; usable/unusable grafted arm; intent clarity; ordinary/high-risk;
precise/assisted profile; normal/threshold pressure.

Expected runtime dynamic:
Preparation improves Block, body-source loss removes it, ordinary misses do not add
punishment, and exceptional input changes only a legal state consequence.

Desired player experience:
"My planning created this chance, my execution affected the result, and my body state
decided what was possible."

Instrumentation:
Structured attempt, input, grade, mutation, capability, and comprehension records.

Continue criteria:
Both planning and timing produce measurable, explainable value; the grafted arm is a
real capability and liability; assisted input preserves the same causal decision.

Revise criteria:
Routine prompts are noisy; Guard preparation is irrelevant; high-risk labeling is
unclear; timing dominates body/Blood; or failure lacks a readable recovery state.

Kill/pivot criteria:
Block remains enjoyable or functional only after removing body-source, Blood,
telegraph, or strategic-preparation constraints.

Evidence class and contamination risks:
Automated/scripted evidence can prove rules and reproducibility only. Owner/designer
play is diagnostic. Experience and accessibility claims require valid human sessions.

Decision owner:
Can Yüzbey.
```

## 14. H1 acceptance gate

H1 passes implementation fidelity only if all are true:

1. All H1-RQ-001 through H1-RQ-012 have traceable tests or structured paper/scripted
   evidence.
2. Prepared Guard and unprepared Block differ materially without making preparation
   mandatory for every legal response.
3. A missing, disabled, or incompatibly committed Right Arm cannot produce the
   arm-enabled Block result, even with exceptional timing input.
4. Ordinary Block misses apply no additional penalty.
5. High-risk miss exposure is previewed, selected, source-derived, and logged.
6. Damage or loss of the grafted arm changes later Guard/Block availability.
7. Exact timing values and state modifiers are configurable comparison variables, not
   hidden rules.
8. Precise and assisted profiles share the same legality and consequence pipeline.
9. Logs distinguish strategy, reflex input, execution grade, mutation, and capability
   recomputation.
10. No wound/Blood rule, Ruined Torso result, new content, Encounter 3 runtime work,
    or Unity work is introduced.

A fidelity pass does not prove fun, balance, comprehension, accessibility, market
value, or readiness for production.

## 15. Implementation gate and next boundary

This specification was owner-approved on 2026-08-11 as the contract for an H1
implementation plan. The owner approved execution of that bounded plan on 2026-08-11;
the implementation passed its automated fidelity gate on 2026-08-12.

The approved execution plan is `21_H1_IMPLEMENTATION_PLAN_v0_1.md`.
The verified implementation report is `22_H1_IMPLEMENTATION_RESULTS_v0_1.md`.

After H1 evidence, revisit only the dependency packages that the results make timely:

1. wound classes and Ruined Torso consequences after cadence is observable;
2. broader movement/action economy only if Block cannot express enough physical choice;
3. wider defense balance only after prepared/unprepared Block has evidence;
4. mental defeat and negotiation after physical continuation states are reliable.
