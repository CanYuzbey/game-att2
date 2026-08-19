# Game att2 — Reflex Interaction Taxonomy and Diagnostic Revision v0.1

Status date: 2026-08-13

Status: owner-resolved attack-led input ownership, timing shape, state pressure, and
shared-readiness boundary after `OWNER-H1-DIAG-004`. This document records why the
fixed one-second terminal diagnostic is insufficient and organizes the remaining
research variables. It does not approve the visual lab, broader reflex runtime
implementation, final controls, timing values, movement, wounds, Unity, or
player-experience claims.

Authority: the owner feedback recorded after `OWNER-H1-DIAG-004`, interpreted under
the H1 owner decisions in `19_CORE_GAMEPLAY_DIRECTION_AND_HANDOFF_2026-08-01.md` and
the causal contract in `11_SYSTEMIC_CAUSAL_DESIGN_SKILL_v0_1_CODEX.md`.

## 1. Owner finding

The completed diagnostic tested whether the owner could estimate a hidden one-second
interval and press Enter. It did not adequately test reflex usage in combat.

The owner requires reflex interactions to be classified and separated. Most readable
physical actions may use a well-timed single input, but other actions should be able
to use directional movement/drag or multiple meaningful inputs when those controls
better represent the physical response. Attack type, telegraph, body state, and other
approved state facts should affect the opportunity and consequence.

The next diagnostic must show what early, ideal, late, incomplete, wrong-direction,
and missed inputs actually do. A raw timing score without immediate state consequence
is not meaningful enough.

### Resolved input-ownership direction — 2026-08-12

The rival's attack normally defines the reflex challenge. Each attack declares its
compatible response/input routes, its expected/default route, and the base difficulty
of those routes. Some attacks are intentionally readable and answerable with an easy
movement; others demand a harder window, direction, sequence, or sustained action.

The player can still direct the input type by explicitly choosing another legal
response route. For example, the same incoming action might permit a timed Block or a
directional Dodge, with different required sources and consequences. The player
cannot select an arbitrary easy input when the attack, body source, reach, or chosen
response does not support it.

This creates a challenge-led, player-directed model:

```text
attack defines the available challenge routes and their baseline difficulty
→ player accepts the expected route or chooses another legal route
→ body state, preparation, intent knowledge, and accessibility tune that route
→ execution changes only the declared state consequence
```

### Resolved timing-shape direction — 2026-08-12

Ordinary timed interactions use a symmetric response curve by default. Inputs equally
early and late receive the same grade and standard state modifier. This provides one
learnable baseline across routine attacks.

A specifically defined harder attack may use an asymmetric curve when its physical
meaning benefits from it. The attack must declare and communicate the difference. For
example, an early Block may redirect the strike, while an equally late Block may
reduce direct damage but fail to prevent a declared secondary effect. Asymmetry is an
action property, not a hidden global penalty and not something invented after input.

## 2. Corrected reflex-event model

The existing H1 model records legality, timing error, grade, and mutation. A broader
proposal needs two additional separations:

```text
incoming physical event and visible telegraph
→ attack-defined compatible routes, expected route, and base difficulty
→ player-directed legal response route
→ selected interaction family
→ action-specific opportunity parameters
→ recorded input dimensions
→ execution grade
→ approved state modifier
→ visible body/Blood/position/capability consequence
```

The incoming attack is the primary challenge definition. The chosen response and its
physical source select one of the attack-compatible routes. This allows attacks to
feel differently demanding without removing player direction or body-derived
alternatives.

## 3. Proposed interaction families

These are reusable interaction grammars, not four independent combat engines.

| Family | Player input | Best physical meaning | Recorded dimensions | Example state effect |
|---|---|---|---|---|
| Timed single input | Press/click once around visible contact | Intercept, basic Block, catch, short tool activation | Signed early/late offset, valid source, cue visibility | Reduce or redirect an incoming consequence |
| Directional response | Drag/move toward a displayed direction or safe region | Dodge, step, redirect, choose which body side receives pressure | Start time, direction error, distance, completion time | Change reach/position/target or convert a direct hit into a glancing one |
| Meaningful sequence | Two or more ordered clicks/presses at readable checkpoints | Multi-stage treatment, extraction, complex counter, maintaining a chained technique | Correct order, per-step timing, completed steps, abandonment | Partial completion, quality, cost, or source exposure changes by completed stage |
| Sustained control | Hold, track, or hold-and-release through a visible interval | Bracing against continuing force, maintaining alignment, resisting displacement | Entry timing, stability, duration, release timing | Preserve posture/source control or reduce an ongoing consequence |

Rapid button mashing is not the default meaning of “multiple click.” Mashing mostly
tests speed and endurance and creates an accessibility risk. It should be used only if
the represented action genuinely depends on repeated force, and it must have an
equivalent assisted input profile.

## 4. What different click times should mean

For a timed single-input response, the diagnostic should expose a visible telegraph
with a defined contact point. It must record a signed offset rather than only absolute
error.

| Input region | Meaning | Ordinary response consequence |
|---|---|---|
| Far too early | Player commits before the attack can be intercepted | Original legal consequence; no extra punishment |
| Early edge | Guard arrives early but still catches part of the action | Limited mitigation or a glancing redirection |
| Effective window | Response meets the readable attack | Strong action-specific mitigation |
| Exceptional core | Response meets the best legal contact point | Best legal state modifier; rare crisis preservation only where the prior state permits it |
| Late edge | Response catches follow-through after initial contact | Limited mitigation, normally weaker or different from an early-edge result when the action supports asymmetry |
| Far too late | Original action has already resolved | Original legal consequence; no extra punishment |

Early and late are mirror images for the ordinary default curve. A harder attack may
override that default: for example, an early Block may redirect an attack but give up
counterpressure, while a late Block may reduce damage without preventing a secondary
effect. Any such asymmetry must be declared by the action definition and visible in
the telegraph and feedback; it cannot be invented after input.

An explicitly selected high-risk response remains different: its preview may state
that a mistimed attempt also exposes the named source. That added exposure is never a
hidden property of an ordinary early or late input.

## 5. Current H1 numbers and their actual meaning

The current research-only implementation does not yet use the signed regions above.
It measures absolute distance from a fixed one-second target:

| Profile | Exceptional | Strong | Limited | Miss |
|---|---:|---:|---:|---:|
| Precise | 0–40 ms | 41–90 ms | 91–160 ms | More than 160 ms |
| Assisted | 0–80 ms | 81–160 ms | 161–300 ms | More than 300 ms |

Before grading, current H1 subtracts 40 ms for prepared Guard, adds 0/40/80 ms for
exact/partial/vague intent, and gives prepared Guard a minimum `Limited` grade while
its source remains legal.

The grade then selects provisional mitigation:

| Opportunity tier | Miss | Limited | Strong | Exceptional |
|---|---:|---:|---:|---:|
| Routine | 0% | 15% | 30% | 50% |
| Significant | 0% | 25% | 50% | 75% |
| Critical | 0% | 25% | 55% | 100% |

Ordinary attempts add zero source damage at every grade. The current disclosed
high-risk fixture applies 30/15/8/4 Right-Arm integrity damage for
Miss/Limited/Strong/Exceptional respectively. These are provisional simulator values,
not validated game balance.

This explains the earlier diagnostic outcomes, but it also exposes the instrument's
weakness: it cannot tell early from late, shows no attack motion, tests only one input
family, and gives only one attempt per comparison condition.

## 6. How state should tune an interaction

To preserve strategy and readability, each factor should have a clear job:

| Factor | Recommended influence |
|---|---|
| Incoming attack | Defines compatible/default interaction routes, their baseline difficulty, telegraph/contact pattern, and original consequence |
| Chosen response | Accepts the expected route or selects another attack-compatible family, required source, and consequence trade-off |
| Intent knowledge/preparation | Improves cue clarity, widens or shifts the useful region, or improves a legal result floor |
| Required source condition | Determines legality, possible grade ceiling, effectiveness, and whether later capability survives |
| Recent/repeated Block use | Primary dynamic pressure on later Block windows; repeated reliance makes the same defensive route harder |
| Player Blood/health pressure | Raises consequence stakes and visibly amplifies Block-window pressure, but is not the primary shrinkage source by itself |
| Explicit impairment/status | May change input tolerance or grade ceiling only when disclosed and causally sourced |
| Accessibility profile | Changes tolerance, pace, or input form while preserving the same strategic choice and consequence ownership |

### Resolved state-pressure direction — 2026-08-12

Low Blood contributes to a shorter Block opportunity because the actor is near death,
but Blood is not the primary cause by itself. The stronger influence is how repeatedly
the player has relied on Block. Repeated Block use narrows later Block opportunities;
low Blood amplifies that pressure.

The desired dynamic is to prevent a no-progress loop in which the player repeatedly
blocks attacks but cannot create significant counterpressure. The player should be
encouraged to change response, alter the rival's attack source, or accept another
meaningful risk rather than maintain indefinite defense.

The pressure must be visible before execution and derived from recorded state. It
must not use an unexplained hidden penalty. The original minimal proposal used a small
Block-repetition state rather than a universal resource. The owner has now approved
one visible shared-readiness resource as the visual-lab research direction, with
repeated Block represented as stronger family-specific strain. This is research
planning authority, not runtime or lab-implementation approval. Exact accumulation,
maximum shrinkage, floor, recovery, and terminology remain open.

Explicit body impairments separately affect response legality, possible grade ceiling,
or effectiveness. A disabled source still removes its response rather than merely
making its timing harder.

### Lightweight shared-readiness direction — 2026-08-12

The owner approves investigating a small, visible readiness system because repeated
Block pressure is not unique to Block. Repeated physical actions should lose
effectiveness, while repeated Blocks should be affected more strongly. Blood remains
health, currency, and ability fuel; readiness represents short-term physical capacity
and must not become a second health bar, a death trigger, or a competing universal
payment system.

The recommended research model uses **one general Stamina value plus a derived
repetition multiplier**, not a separate Stamina bar and a separate permanent
Block-fatigue bar:

| State/input | Effect in the proposed model |
|---|---|
| General Stamina | All physical response families draw from and are weakened by the same visible readiness pool |
| Action family | Defines the base exertion of a Block, attack, Dodge, sequence, or sustained response |
| Consecutive/recent use of the same family | Raises that family's exertion/penalty temporarily; repeated Block rises faster than most other actions |
| Low Blood | Does not independently collapse the controls; it visibly amplifies existing exertion/Block strain and makes failure more costly |
| Not using Block | Stops adding Block strain and restores a small amount of readiness after the threat resolves; the player accepts the non-Block consequence or uses another legal response |
| Genuine break in pressure | Larger recovery when range changes, the rival's attack source is disrupted, or the opponent cannot maintain offense for a state-derived reason |

Under this model, choosing a Fast item, observation, or another Main action does not
magically restore Stamina. If the player then forgoes Block against an incoming threat,
the modest recovery comes from breaking the defensive pattern, not from the item
itself. Only an explicitly defined restorative action or item could restore additional
Stamina.

Illustrative flow only—no values are approved:

```text
First Block:        normal Stamina cost, normal attack-defined window
Second Block:       lower general Stamina + larger repeated-Block modifier
Third Block at low Blood:
                    same repeated-Block modifier amplified; window is visibly tighter
Forgo Block:        take the original legal consequence or use another response
                    → repeated-Block modifier stops growing; small recovery follows
Disrupt attack arm: attack source/range changes
                    → larger recovery because the pressure state changed materially
```

At empty Stamina, ordinary actions should normally become weak or difficult rather
than silently impossible. A required disabled limb remains an independent legality
failure. This preserves the difference between exhaustion, which asks for a tactical
change, and body loss, which removes a capability.

The boundary decision is **yes** for the visual-lab hypothesis: this one-resource
model replaces the standalone Block-pressure state, and repeated Block is a specially
weighted use of general readiness. Exact values and recovery behavior remain
reversible variables in `25_VISUAL_INTERACTION_LAB_RECORD_v0_1.md`. Production
combat remains unchanged unless later evidence supports a separately approved gate.

## 7. Revised diagnostic requirements

The next instrument should not begin as a full combat implementation. It should be a
small visual interaction lab that can compare the families without changing the
approved campaign.

Minimum requirements:

- use a visible attack telegraph and contact point rather than a hidden one-second
  estimate;
- give practice attempts before recorded attempts;
- record signed early/late timing for single inputs;
- record direction, distance, order, completion, or stability when relevant to the
  selected family;
- show immediate grade and concrete before/after state consequence after every trial;
- repeat and counterbalance conditions instead of comparing one attempt with one
  attempt;
- compare attacks intended to have easy and hard responses while making their
  difficulty readable rather than hidden;
- compare the expected attack-selected route with a player-directed alternative when
  both are legal;
- expose general Stamina, repeated-action pressure, and the Blood contribution before
  each trial;
- compare first-use Block, repeated Block, and a non-Block recovery choice at normal
  and low Blood without changing unrelated state;
- compare precise and assisted inputs through the same legality and consequence path;
- ask whether the threat, valid response, timing result, and resulting state change
  were understandable;
- retain consent, local-only evidence, contamination notes, and the owner-diagnostic
  evidence boundary.

The lab can establish whether controls and consequences are understandable enough to
iterate. It cannot establish fun, accessibility, or balance from owner self-testing.

## 8. Optimized owner-question order

The questions are ordered by how many later decisions depend on them:

1. **Input ownership — resolved:** The rival's attack normally defines compatible
   routes, the expected input family, and baseline difficulty. The player may direct
   the input type by selecting another legal response route.
2. **Timing shape — resolved:** Ordinary attacks use a symmetric response curve.
   Specifically defined harder attacks may give equally early and late inputs
   different visible consequences.
3. **State pressure — resolved:** Repeated Block use is the primary cause of a shorter
   later Block window; low Blood visibly amplifies that pressure. Explicit body
   impairment separately changes legality or effectiveness.
4. **Shared-readiness boundary — resolved for research:** One visible general
   readiness resource replaces the standalone Block-pressure state in the lab
   hypothesis, with repeated Block receiving stronger family-specific strain.
5. **Recovery variables — bounded by the proposed lab plan:** Small recovery follows
   threat resolution or a defensively meaningful choice; larger recovery requires a
   genuine state-derived pressure break. Menus and ordinary item use do not create
   free recovery. Exact values remain provisional.
6. **Multiple-input meaning:** Should multi-input actions use ordered meaningful
   checkpoints by default, reserving rapid repetition for rare force/struggle actions?
7. **Family coverage:** Which first three concrete responses should represent timed,
   directional, and sequential input in the lab without opening deferred runtime
   systems?
8. **Cadence:** How often can small reflex moments occur before they distract from
   reading body state, choosing targets, and managing Blood?
9. **Accommodation equivalence:** Which changes may assisted input make to timing,
   pace, and gesture while preserving the same strategic decision?

Questions 1 through 4 are resolved at the research-direction level. Question 5 has a
reversible default and anti-loop boundary in the proposed lab plan; it is not an
approved final rule. Questions 6 through 9 remain downstream research questions and
must not expand the first Block-only lab.

## 9. Scope and gate

No broader response family is approved for runtime by this proposal. Movement, active
Cover It, wounds, new content, Encounter 3 runtime, and Unity remain blocked. The
current H1 code remains a valid deterministic fidelity fixture but is not an adequate
human reflex instrument.

The shared-readiness direction is resolved, but no implementation gate opens from
that decision alone. `25_VISUAL_INTERACTION_LAB_RECORD_v0_1.md` preserves the
Block-only scope, provisional recovery behavior, explicit comparisons, evidence
fields, rollback, and non-claims. VL-WP1 through VL-WP3 are complete, and VL-WP4 was
owner-approved and then deferred before execution on 2026-08-13. Reflex work is
preserved for a later gate after the strategic-combat packages are coherent.
