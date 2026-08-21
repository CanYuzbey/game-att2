# Game att2 — Bounded Visual Interaction Lab Record v0.1

Status date: 2026-08-13

Status: VL-WP1 through VL-WP3 completed and fidelity-verified. VL-WP4 was approved
and then deferred by the owner before execution on 2026-08-13. This document
consolidates the executed lab plan and implementation result.

Authority: the shared-readiness direction in the Development Master, the interaction
taxonomy in document 23, the H1 contract and record in documents 20 and 21, and the
systemic causal contract in document 11.

## 1. Research question and boundary

The lab asks whether one visible shared readiness resource can make repeated Block
pressure readable and tactically meaningful while keeping Blood, body source,
preparation, intent, and the original attack decisive.

It reuses H1-F0 only: the post-Jeff grafted Right Arm, Anna's Right-Arm-sourced
Surgical Jab, the fixture-only Torso target, Guard Flesh, and precise/assisted
profiles. Version 0.1 implements one interaction family: timed single-input Block.

It does not implement production combat, campaign integration, wounds, movement,
Dodge, Parry, Counter, active Cover It, final controls, Unity, or experience claims.

## 2. Shared-readiness contract

| Fact | Research handling |
|---|---|
| General readiness | One visible Ready / Strained / Exhausted resource |
| Repeated Block | Stronger temporary family-specific strain |
| Low Blood | Visible amplifier of existing strain, never a hidden independent penalty |
| Body source | An unusable source makes Block illegal regardless of timing/readiness |
| Forgoing Block | Stops repetition growth; modest recovery follows resolved threat |
| Material pressure break | May grant larger recovery after an explicit source/reach change |
| Menu/item selection | Does not restore readiness by itself |

All exact values remain `PROVISIONAL_VISUAL_LAB_ONLY` in
`config/visual_lab_v0_1.yaml`.

## 3. Delivered implementation

| Area | Files | Role |
|---|---|---|
| Research configuration | `config/visual_lab_v0_1.yaml` | Fixture, readiness, timing, mitigation, and exposure values |
| Deterministic model | `src/game_att2_sim/visual_lab_config.py`, `visual_lab.py` | Strict loading and pure trial resolution |
| Local surface | `src/game_att2_sim/visual_lab_page.py`, `research/visual_lab/visual_lab.template.html` | Validated configuration injection and interaction fragment |
| Operator interface | `src/game_att2_sim/visual_lab_cli.py`, `research/visual_lab/README.md` | Page generation and scripted replay |
| Scripted evidence | `examples/visual_lab_scripted_comparisons.json` | Twenty controlled variants |
| Verification | Visual-lab unit/integration tests | Contracts, negative paths, comparisons, page, CLI, and isolation |

The local surface displays telegraph/contact, signed early/late input, readiness,
repetition, Blood band, preparation, legality, grade, damage, recovery, source
exposure, and resulting capability. It makes no network request.

## 4. Comparison matrix and result

| ID | Pair | Verified distinction |
|---|---|---|
| VL-C1 | First vs repeated Block | Repetition raises cost and effective timing pressure |
| VL-C2 | Normal vs low Blood | Low Blood amplifies existing strain; Blood delta remains zero |
| VL-C3 | Unprepared vs Guard-prepared | Strategic preparation changes the visible response |
| VL-C4 | Exact vs vague intent | Information changes timing pressure |
| VL-C5 | Precise vs assisted | Same legality/mutation route, different declared tolerance |
| VL-C6 | Equally early vs late | Symmetric routine timing is preserved |
| VL-C7 | Block again vs forgo | Recovery follows resolved threat, not menu use |
| VL-C8 | Continued pressure vs source disruption fixture | Material pressure break grants the larger recovery |
| VL-C9 | Usable vs unusable Right Arm | Exceptional input cannot bypass body legality |
| VL-C10 | Ordinary vs disclosed high-risk miss | Ordinary miss adds no source exposure |

VL-RQ-001 through VL-RQ-013 passed implementation-fidelity checks. The twenty
scripted variants reproduced byte-identical evidence at the recorded merge point.

## 5. Preserved diagnostic protocol

If a later owner gate reopens VL-WP4, the local protocol is:

1. show fixture, original consequence, source, Blood, and readiness;
2. run at least two unrecorded practice attempts;
3. use counterbalanced A/B/B/A recorded trials;
4. show immediate before/after causal feedback;
5. ask what threat was coming, why Block was legal, what changed, and what risk now
   exists;
6. retain evidence class, consent, deviations, and contamination status.

Owner sessions remain `OWNER_DIAGNOSTIC`. External participants require a separate
approved consent, privacy, recruitment, retention, deletion, and analysis protocol.

## 6. Historical verification record

Recorded on 2026-08-12:

| Check | Result |
|---|---|
| Focused visual-lab suite | 18 passed |
| Full automated suite | 261 passed |
| Source-only line coverage | 87% |
| Ruff / strict mypy | Passed |
| Seven scenarios, seed 42 | Passed; mini-campaign ended at 25 Blood |
| Playable campaign replay | Completed at 36 Blood |
| H1 / visual-lab replay | Byte-identical; visual lab covered 20 variants |
| Browser fidelity | Passed with no console warnings/errors |

These are historical implementation results. Current factual metrics must come from
fresh verification or the current lead brief.

## 7. Scope and current gate

The hostile review found no remaining P0/P1 implementation-fidelity defect. It
confirmed source illegality, risk acknowledgement, ordinary-miss neutrality,
local-only evidence, no free recovery, practice labeling, and isolation from campaign
rules/content.

VL-WP4 remains deferred before execution. The instrument cannot establish fun,
balance, accessibility, fairness, fatigue, preference, comprehension, or production
readiness. No external pilot or broader reflex/runtime gate is open.
