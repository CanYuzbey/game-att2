# Game att2 - Bounded Visual Interaction Lab Plan v0.1

Status date: 2026-08-13

Status: VL-WP1 through VL-WP3 are implemented and fidelity-verified in document 26.
The owner separately approved and then deferred VL-WP4 before execution on
2026-08-13. This plan is preserved for later research and does not cover production combat, campaign
integration, final controls, content, wounds, movement, Unity, or experience claims.

Authority: the owner-approved shared-readiness direction in the Development Master,
the interaction taxonomy in document 23, the H1 contract/results in documents 20-22,
and the systemic causal design contract in document 11.

## 1. Research question

> Can one visible shared readiness resource make repeated Block pressure readable and
> tactically meaningful while preserving Blood, body source, preparation, intent, and
> the original attack as the decisive state facts?

This plan replaces the inadequate hidden one-second terminal task with a small visual,
replayable interaction lab. It does not attempt to implement the complete combat loop.

## 2. Fixture and scope

Reuse the existing H1-F0 research fixture only:

- post-Jeff player with the current grafted Right Arm;
- Anna's existing Right-Arm-sourced Surgical Jab;
- the current Torso target as a fixture-only target;
- existing Guard Flesh cost and source;
- current precise and assisted profiles as comparison inputs;
- integrity consequences only; wounds, wound-to-Blood mapping, and Ruined Torso
  meaning remain `DEFERRED`.

The lab may use a separate static local visual surface and research-only configuration.
It must not modify the seven scenarios, campaign controller, content YAML, Combat
Rules v0.5, or production dependencies.

## 3. Interaction boundary

Version 0.1 implements one family only: **timed single-input Block**.

It must visually show:

- the incoming attack telegraph and contact point;
- the selected legal response route and required Right-Arm source;
- current Blood band, readiness band, repeated-Block pressure, and preparation state;
- signed early/late input rather than absolute error only;
- immediate grade, original consequence, mitigation, source exposure, and resulting
  capability state.

Directional, meaningful-sequence, and sustained-control families remain classified
but unimplemented. They may receive later isolated plans only after the timed family
proves the shared evidence contract.

## 4. Shared-readiness research contract

The owner-approved direction is represented in the lab as follows:

| Fact | Research handling |
|---|---|
| General readiness | One visible resource with readable Ready / Strained / Exhausted bands |
| Physical response | Uses provisional readiness according to its action family |
| Repeated Block | Applies a stronger temporary family repetition weight |
| Low Blood | Visibly amplifies existing strain; never creates a hidden independent penalty |
| Unusable body source | Makes Block illegal regardless of readiness or timing |
| Empty readiness | Weakens opportunity/effectiveness; does not silently imitate limb loss or death |
| Forgoing Block | Stops Block repetition growth; modest recovery occurs only after the threat resolves |
| Material pressure break | May grant a larger recovery when the attack source or reach state changes explicitly |
| Menu/item selection | Does not restore readiness by itself |

Exact resource values, costs, windows, recovery amounts, and multipliers are
`PROVISIONAL_VISUAL_LAB_ONLY` and must live outside production configuration.

## 5. Timing model

- Routine timed interactions use a symmetric early/late curve.
- A signed offset is recorded for every attempt.
- Equally early and late routine inputs receive the same grade and standard modifier.
- The lab may explain how an attack-defined asymmetric profile would differ, but v0.1
  must not implement a second attack or hidden asymmetric punishment.
- Ordinary misses apply only the original attack consequence.
- Additional Right-Arm exposure occurs only for a previewed and acknowledged high-risk
  response.

## 6. Comparison matrix

All recorded comparisons are paired, repeated, and counterbalanced. Practice attempts
are stored separately and excluded from measured results.

| ID | Pair | Isolates |
|---|---|---|
| VL-C1 | First Block vs repeated Block | Family repetition pressure |
| VL-C2 | Normal Blood vs low Blood at equal repetition | Blood as visible amplifier |
| VL-C3 | Unprepared Block vs Guard Flesh prepared | Strategic preparation |
| VL-C4 | Exact vs vague intent | Information value |
| VL-C5 | Precise vs assisted profile | Accommodation equivalence |
| VL-C6 | Symmetric early vs equally late input | Timing-shape fidelity |
| VL-C7 | Use Block again vs forgo Block through the resolved threat | Modest recovery and consequence trade-off |
| VL-C8 | Continued pressure vs explicit attack-source disruption fixture | Small recovery versus material reset |
| VL-C9 | Usable vs unusable Right Arm | Readiness never bypasses body legality |
| VL-C10 | Ordinary vs disclosed high-risk miss | Commitment-sensitive failure |

The lab must not claim that the player can perform a runtime source-disruption action
that is not approved. VL-C8 uses a controlled before/after state fixture only.

## 7. Human-facing trial structure

1. Show the fixture, response source, original consequence, and current readiness.
2. Provide at least two unrecorded practice attempts for the current profile.
3. Run recorded paired trials in a counterbalanced order.
4. Show immediate before/after state and a plain-language causal explanation.
5. Ask four short questions after each comparison block:
   - What threat was coming?
   - Why was Block available or unavailable?
   - What changed because of timing/readiness/preparation?
   - What new cost or risk exists now?
6. End with a structured fairness, clarity, control, fatigue, and preference debrief.

Owner diagnostics remain `OWNER_DIAGNOSTIC`. External participants require a separate
approved protocol, consent, recruitment, privacy, retention, and deletion plan.

## 8. Requirements and acceptance evidence

| ID | Requirement | Acceptance evidence |
|---|---|---|
| VL-RQ-001 | The telegraph and contact point are visible. | Visual-state and recorded-cue checks |
| VL-RQ-002 | Inputs preserve signed early/late offset. | Exact paired replay tests |
| VL-RQ-003 | One visible readiness resource replaces a second Block meter. | State schema and UI audit |
| VL-RQ-004 | Repeated Block is a stronger family-specific use of readiness. | VL-C1 deterministic comparison |
| VL-RQ-005 | Low Blood only amplifies existing strain visibly. | VL-C2 and no-hidden-penalty test |
| VL-RQ-006 | Body source legality remains independent. | VL-C9 exceptional-input negative test |
| VL-RQ-007 | Recovery follows resolved threat or material pressure change. | VL-C7/VL-C8 state traces |
| VL-RQ-008 | Menus and unrelated items do not create free recovery. | Negative tests |
| VL-RQ-009 | Ordinary misses add no punishment. | VL-C10 ordinary path |
| VL-RQ-010 | Assisted input uses the same legality/consequence pipeline. | VL-C5 trace equivalence |
| VL-RQ-011 | Every result shows its concrete state consequence. | Feedback and comprehension record |
| VL-RQ-012 | Scripted trials reproduce byte-identical evidence. | Repeated export comparison |
| VL-RQ-013 | No production content or rules are changed. | Diff and configuration isolation audit |

## 9. Evidence card

```text
Question or hypothesis:
Does one visible readiness system make Block repetition and recovery understandable
without weakening Blood or Body as Build?

Mechanic/config variants:
First/repeated Block; normal/low Blood; prepared/unprepared; precise/assisted;
Block/forgo; pressure maintained/broken; usable/unusable source; ordinary/high-risk.

Expected runtime dynamic:
Repeated Block becomes visibly harder, low Blood amplifies rather than originates the
pressure, changing response creates limited recovery, material pressure breaks create
more recovery, and body-source loss remains an absolute legality boundary.

Desired player experience:
"I can see why this response is harder now, what would restore readiness, and why my
body and earlier choices still decide what is possible."

Instrumentation:
Signed input, telegraph, readiness facts, repetition, Blood band, preparation,
legality, grade, mutation, capability recomputation, and comprehension answers.

Continue criteria:
Players can explain readiness, repetition, Blood amplification, recovery, and source
legality; assisted input preserves the same decision; strategy remains relevant.

Revise criteria:
Readiness feels like a second health bar; recovery is gameable; Block remains the
default answer; feedback cannot explain early/late or source consequences.

Kill criteria:
The shared resource adds cognitive load without improving the narrower visible
Block-pressure state, or it makes Blood/body consequences decorative.

Evidence class and contamination risks:
Automation proves fidelity only. Owner self-test is diagnostic. External experience
claims require a separate valid pilot.

Decision owner:
Can Yüzbey.
```

## 10. Work packages

1. **VL-WP0 - plan approval: COMPLETE.** The owner approved this plan on 2026-08-12.
2. **VL-WP1 - isolated contracts: COMPLETE.** Research-only definitions,
   configuration, and strict validation are isolated from production configuration.
3. **VL-WP2 - static visual surface: COMPLETE.** The local fragment provides the
   telegraph, signed input capture, immediate state feedback, assisted profile, and
   explicit high-risk acknowledgement with zero network use.
4. **VL-WP3 - deterministic evidence: COMPLETE.** Scripted replay, negative tests,
   local export, and current-campaign regressions pass; see document 26.
5. **VL-WP4 - owner diagnostic: DEFERRED BY OWNER 2026-08-13.** No local trial or
   evidence capture is active. Preserve the counterbalanced protocol for a later
   owner gate.

Each work package has a stop gate. VL-WP4 was opened and then deferred before
execution on 2026-08-13; it does not open any later gate.

## 11. Stop and rollback conditions

Stop and return for owner review if the lab requires:

- a wound/Blood or Ruined Torso rule;
- movement, Dodge, Parry, Counter, active Cover It, or a new response family;
- a new enemy, character, limb, item, reward, or encounter outcome;
- campaign or production configuration changes;
- a network service, participant identity, or external data transfer;
- readiness to make an action legal when its body source is unusable;
- hidden low-Blood penalties or automatic narrative resolution.

Rollback is removal of the isolated lab surface, its research configuration, tests,
and generated evidence. The current simulator, H1 fixture, campaign, and rules remain
unchanged.

## 12. Current gate

The bounded local implementation-fidelity work passed, but VL-WP4 is deferred before
execution. The active product path now returns to dependency-ordered strategic-combat
decisions. No decision in this document approves an external pilot, future paper
content set, or final game-design document.
