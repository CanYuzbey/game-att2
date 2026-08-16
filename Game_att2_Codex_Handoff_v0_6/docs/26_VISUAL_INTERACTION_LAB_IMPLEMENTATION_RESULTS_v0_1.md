# Game att2 - Visual Interaction Lab Implementation Results v0.1

Status date: 2026-08-13

Status: VL-WP1 through VL-WP3 implemented and fidelity-verified. The owner approved
and then deferred VL-WP4 before execution on 2026-08-13. No external-player or
production experience claim is supported by this work.

## 1. Executive result

The owner-approved bounded H1-F0 visual lab now exists as an isolated local research
instrument. It renders Anna's existing Right-Arm Surgical Jab toward the player's
Torso, records signed Block timing, displays one provisional readiness resource, and
shows the resulting damage, recovery, body-source legality, and disclosed source risk.

All ten paired comparisons have deterministic scripted evidence. The full repository
regression remains clean. The campaign, seven scenarios, Combat Rules v0.5, production
configuration, and content catalog were not changed.

## 2. Implemented boundary

Implemented:

- one timed single-input Block family using fixture H1-F0;
- strict research-only YAML configuration with duplicate-key and exact-schema checks;
- pure signed-timing, readiness, recovery, source-legality, and exposure resolution;
- precise and assisted timing profiles through the same consequence pipeline;
- two practice attempts followed by recorded A/B/B/A trials;
- immediate visible causal feedback and four comprehension fields;
- explicit acknowledgement before the disclosed high-risk route becomes usable;
- anonymous local JSON evidence download with no network calls;
- twenty scripted variants covering VL-C1 through VL-C10.

Not implemented:

- wounds, wound-to-Blood mapping, Ruined Torso meaning, movement, Dodge, Parry,
  Counter, active Cover It, broader reflex families, new content, campaign integration,
  production UI, Unity, or an external participant pipeline.

## 3. Implementation map

| Area | Files | Role |
|---|---|---|
| Research configuration | `config/visual_lab_v0_1.yaml` | Provisional fixture, readiness, timing, mitigation, and exposure values |
| Deterministic model | `src/game_att2_sim/visual_lab_config.py`, `visual_lab.py` | Strict loading and pure trial resolution |
| Local surface | `src/game_att2_sim/visual_lab_page.py`, `research/visual_lab/visual_lab.template.html` | Validated configuration injection and interaction fragment |
| Operator interface | `src/game_att2_sim/visual_lab_cli.py`, `research/visual_lab/README.md` | Page generation and scripted replay |
| Scripted evidence | `examples/visual_lab_scripted_comparisons.json` | Twenty controlled variants |
| Verification | `tests/unit/test_visual_lab*.py`, `tests/integration/test_visual_lab*.py`, `tests/integration/test_console_entrypoints.py` | Contracts, negative paths, comparisons, page, CLI, and entry point |

## 4. Requirements traceability

| ID | Result | Evidence |
|---|---|---|
| VL-RQ-001 | PASS | Browser inspection confirmed visible moving telegraph, Torso path, and contact marker. |
| VL-RQ-002 | PASS | Early and late signs are preserved; equal absolute offsets are symmetric. |
| VL-RQ-003 | PASS | The surface exposes one readiness meter and no separate Block meter. |
| VL-RQ-004 | PASS | VL-C1 cost rises from 18 to 34; effective offset rises from 120 ms to 200 ms. |
| VL-RQ-005 | PASS | VL-C2 low Blood changes the existing cost from 26 to 33 and effective offset from 145 ms to 165 ms; Blood delta remains zero. |
| VL-RQ-006 | PASS | VL-C9 exceptional input succeeds with a usable Right Arm and remains illegal when that source is unusable. |
| VL-RQ-007 | PASS | VL-C7 forgoing restores 12 only after resolution; VL-C8 material pressure break restores 35. |
| VL-RQ-008 | PASS | Menu/item negative path restores zero readiness and resolves no threat. |
| VL-RQ-009 | PASS | VL-C10 ordinary miss adds zero Right-Arm exposure. |
| VL-RQ-010 | PASS | VL-C5 precise and assisted variants share legality and mutation logic; only the declared timing band differs. |
| VL-RQ-011 | PASS | Each result displays signed timing, grade, original/mitigated Torso damage, readiness change, Blood change, and Right-Arm exposure. |
| VL-RQ-012 | PASS | Two twenty-variant exports were byte-identical; SHA-256 `b0b37171312cdbb8965311c0d650adec184ddba6f7c97cafadd4fa69007ad9c9`. |
| VL-RQ-013 | PASS | Diff audit found no changes to production rules, content, campaign control, or the seven scenario definitions. |

## 5. Verification record

All commands exited `0` on 2026-08-12.

| Check | Result |
|---|---|
| Focused visual-lab suite | 18 passed |
| Full automated suite | 261 passed |
| Source-only line coverage | 87% |
| Ruff | All checks passed |
| Strict mypy | No issues in 32 source files |
| Seven approved scenarios, seed 42 | All executed; `mini_campaign` ended at 25 Blood |
| Playable campaign replay, seed 42 | Completed at 36 Blood |
| H1 scripted replay | 12 variants, byte-identical |
| Visual-lab scripted replay | 20 variants, byte-identical |
| Browser fidelity pass | Desktop layout readable; controls, practice gate, recorded order, risk acknowledgement, and console checked; no warnings or errors |

The full coverage run reported 91% when tests were included; the comparable source-only
figure remains 87%.

## 6. Scope and hostile review

The review attempted to falsify the lab's safety and causal claims:

- unusable Right Arm plus exceptional timing cannot make Block legal;
- an unacknowledged high-risk attempt is rejected by the pure resolver and disabled in
  the visual surface;
- an ordinary miss cannot damage the blocking source;
- low Blood does not mutate Blood or create an undeclared independent state;
- menus and unrelated items cannot grant readiness recovery;
- practice trials are marked separately from recorded evidence;
- the visual fragment contains no `fetch`, XHR, WebSocket, upload, or participant
  identity path;
- generated output refuses to overwrite an existing file;
- no runtime content, scenario, campaign, combat-rule, or production-config file changed.

No blocking defect remained after the visual pass. Two presentation-fidelity defects
were corrected and retested before this report was written: the high-risk branch
initially lacked an on-screen acknowledgement control, and the Jab initially travelled
past its marked contact point during the impact beat. The corrected Jab tip reaches the
contact line at the input moment, remains there through impact resolution, and advances
a matching timeline cursor.

## 7. Assumptions and limitations

- Every number in `visual_lab_v0_1.yaml` is `PROVISIONAL_VISUAL_LAB_ONLY`.
- Automated and browser checks establish implementation fidelity, not fun, balance,
  accessibility, fairness, control quality, or player comprehension.
- The local visual is a research fragment, not a final UI direction or production
  technology choice.
- Owner self-test data would be contaminated diagnostic evidence and must not be mixed
  with a later external pilot.
- External participants still require a separately approved protocol for consent,
  recruitment, privacy, retention, deletion, and analysis.

## 8. Merge recommendation and current gate

The VL-WP1 through VL-WP3 implementation is suitable to merge after normal branch
review because its acceptance requirements and repository regressions pass and its
rollback boundary is isolated. VL-WP4 was later opened by separate owner approval on
2026-08-13 and then deferred before execution later that day.

The lab has no active human diagnostic gate. At this result's decision point, space
and reach was the first dependency-ordered strategic-combat gate after approval of
the physical-consequence meanings. Documents 28 through 32 now record the later
paper decisions; document 24 owns the current product gate.
