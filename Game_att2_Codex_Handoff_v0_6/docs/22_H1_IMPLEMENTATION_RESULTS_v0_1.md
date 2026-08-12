# Game att2 — H1 Hybrid-Combat Implementation Results v0.1

Status date: 2026-08-12

Status: the bounded H1 implementation-fidelity gate passed. This result does not
establish fun, balance, comprehension, accessibility, market value, or readiness for
production or Unity.

Authority: `20_H1_HYBRID_COMBAT_SPEC_v0_1.md` and the owner-approved execution plan
`21_H1_IMPLEMENTATION_PLAN_v0_1.md`.

## 1. Executive result

The implementation provides one isolated deterministic research runner that:

- reuses the current post-Jeff body, graft, Anna, Surgical Jab, Guard Flesh, Blood,
  limb-integrity, and structured-event rules;
- validates the Block's body source before grading and again before consequence;
- compares prepared/unprepared, usable/unusable source, ordinary/high-risk failure,
  intent clarity, precise/assisted input, and normal/threshold pressure;
- routes target damage and disclosed Right-Arm exposure through the existing rule
  engine;
- leaves the seven approved scenarios and playable campaign unchanged by default.

Merge recommendation: merge the bounded H1 research implementation. Do not treat this
as approval for another response family, wound rules, content, Encounter 3 runtime, or
Unity.

## 2. Deterministic comparison result

All numeric values below are `PROVISIONAL_H1_RESEARCH_ONLY`.

| Comparison | Variant A | Variant B | Fidelity observation |
|---|---|---|---|
| H1-C1 | Unprepared: Limited, 7 Torso damage | Guard-prepared: Strong, 2 Torso damage | Preparation changes both grade context and consequence; Guard reduction is consumed once. |
| H1-C2 | Usable arm: Exceptional, 4 damage | Disabled arm: denied, original 8 damage | Exceptional timing cannot bypass an unusable body source. |
| H1-C3 | Ordinary miss: 8 Torso, 0 arm | High-risk miss: 8 Torso, 30 arm | Ordinary failure adds nothing; selected disclosed risk can ruin the source. |
| H1-C4 | Vague intent: Miss, 8 damage | Exact intent: Limited, 7 damage | Information changes grade without changing legality or body state. |
| H1-C5 | Precise: Limited, 7 damage | Assisted: Strong, 6 damage | Both profiles share one legality/consequence pipeline. |
| H1-C6 | Normal: 4 Torso, 4 arm | Threshold: 0 Torso, 4 arm | Rare exceptional legal input preserves known integrity while retaining a body cost; downstream survival/wound meaning remains deferred. |

These automated comparisons establish only that the configured causal distinctions are
reachable, logged, and repeatable. They do not establish that the values feel correct.

## 3. Requirements traceability

| Requirement | Implementation | Primary evidence | Result |
|---|---|---|---|
| H1-RQ-001 | `reflex.py`, `h1_research.py` | H1-C1 and H1-C4 integration tests | Pass |
| H1-RQ-002 | `h1_reflex_v0_1.yaml`, `h1_config.py` | tier/profile validation and grade-boundary tests | Pass |
| H1-RQ-003 | pure availability plus rule-engine revalidation | missing, disabled, incompatible, and post-offer invalidation tests | Pass |
| H1-RQ-004 | current Guard Flesh plus prepared grade context | H1-C1 and single-consumption regression | Pass |
| H1-RQ-005 | ordinary exposure map fixed at zero | H1-C3 ordinary-miss assertions | Pass |
| H1-RQ-006 | acknowledged `HIGH_RISK` attempt and source exposure | preview ordering and Right-Arm-only H1-C3 assertions | Pass |
| H1-RQ-007 | `AttackModifier` contains only state modifiers | grade events and absence-of-outcome assertions | Pass |
| H1-RQ-008 | fixture graft plus capability recomputation | H1-C2/H1-C3 capability retained/lost assertions | Pass |
| H1-RQ-009 | legality precedes grade and is revalidated | exceptional input against unusable/invalidated source | Pass |
| H1-RQ-010 | precise and assisted timing profiles | H1-C5 shared-pipeline assertions | Pass |
| H1-RQ-011 | script, structured events, JSON/Markdown CLI | identical payload and CLI replay tests | Pass |
| H1-RQ-012 | isolated loader and prohibited-key validation | zero measured Blood delta and prohibited-category tests | Pass |

## 4. Authored implementation surface

- `config/h1_reflex_v0_1.yaml`: isolated provisional values and fixture identifiers.
- `h1_config.py`: strict duplicate, schema, range, reference, status, and prohibited-key
  validation.
- `reflex.py`: immutable contexts, attempts, grades, risks, availability, and pure
  modifier resolution.
- `h1_research.py`: current-definition fixture, paired comparisons, metrics, events,
  and exports.
- `h1_cli.py`: scripted replay and local owner-diagnostic boundary.
- `examples/h1_scripted_comparisons.json`: versioned deterministic input.
- H1 unit/integration tests and the narrow neutral modifier regression in
  `test_causal_integrity.py`.

The only shared runtime change is an optional default-neutral `AttackModifier` at
`RuleEngine.enemy_attack`. Existing callers omit it and retain their prior event and
state behavior.

## 5. Verification

Run from the package root on 2026-08-12:

| Command | Exit | Result |
|---|---:|---|
| `python -m pytest -q` | 0 | 242 passed |
| `python -m pytest --cov=game_att2_sim --cov-report=term-missing -q` | 0 | 242 passed; 87% line coverage |
| `python -m ruff check src tests` | 0 | All checks passed |
| `python -m mypy src` | 0 | No issues in 28 source files |
| `python -m game_att2_sim --all-scenarios --seed 42 --format markdown` | 0 | Seven approved results unchanged; mini-campaign ends at 25 Blood |
| `python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_full_campaign_sequence.json` | 0 | Completed at 36 Blood; 38 events |
| H1 all-comparison JSON command, repeated | 0 | Output matched byte for byte |

H1-focused verification after diagnostic-boundary corrections: 73 tests passed.

## 6. Causal and scope audit

The measured interaction records:

```text
post-Jeff body and Anna source state
→ action/source/telegraph/commitment validation
→ recorded timing input and configured grade
→ existing Guard reduction at most once
→ configured state modifier
→ existing limb-integrity mutation
→ disclosed Right-Arm exposure when selected
→ Guard/Block capability recomputation
→ structured evidence
```

No normal limb damage produces Blood loss. No execution grade writes victory,
survival, bargain, encounter resolution, or narrative outcome. The threshold fixture
stops at known Torso integrity and marks wound class, wound-to-Blood mapping, and
Ruined Torso downstream meaning `DEFERRED`.

No content/scenario YAML, Encounter 3 file, playable campaign controller, Unity work,
movement, active Cover It, generalized reflex family, wound system, new enemy, item,
limb, reward, runtime dependency, or external service was added.

## 7. Hostile review

P0/P1 findings: none remaining.

Controls verified:

- invalid or lost Block sources cannot apply mitigation or exposure;
- invalid modifiers fail before attack mutation;
- Guard Flesh reduction appears exactly once;
- ordinary misses equal the original consequence;
- high-risk exposure is previewed before input and affects only the declared arm;
- assisted input changes thresholds, not legality or consequence ownership;
- normal scenario and campaign paths remain unchanged;
- output labels its evidence class and claim boundary.

## 8. Known limitations and open evidence

- Exact timing, mitigation, and exposure values are provisional and have not received
  sensitivity or human-validation approval.
- Automated timing errors are fixtures, not evidence of human motor performance.
- The local terminal timing capture is an owner diagnostic, not a final control scheme.
- No valid external participant has tested comprehension, fatigue, prompt frequency,
  accessibility, or enjoyment.
- H1 contains Block only and cannot support conclusions about Dodge, Parry, Counter,
  movement, or a complete combat model.
- Fixture-only Torso targeting does not change Anna's canonical/general behavior.

## 9. Gate position

H1 implementation fidelity passes. The next product gate remains closed: evidence must
be reviewed before changing provisional values, generalizing reflexes, defining wound
consequences, or considering production-engine work.

## 10. Owner diagnostic status — 2026-08-12

Owner diagnostic `OWNER-H1-DIAG-004` completed H1-C1, H1-C3, and H1-C5 with six
consented local timing captures. The raw record passed structural validation, but it
does not support timing or experience decisions:

- prepared/unprepared raw inputs differed too much to isolate preparation;
- ordinary and high-risk misses exercised the intended consequence distinction;
- precise and assisted profiles both graded Miss;
- the terminal instrument collected no subjective fairness, risk, clarity, or control
  answers.

The full result and contamination record are in
`../research/h1/OWNER-H1-DIAG-004-summary.md`. Disposition: revise the diagnostic
instrument before making player-experience claims or changing provisional values.

## 11. Owner interpretation and revised design path — 2026-08-12

The owner confirmed that the one-second terminal task does not validate the intended
reflex layer. It tests only a single timed input without representative attack motion,
does not distinguish early from late, does not cover directional or multi-input
adaptations, and does not make the state outcomes of different inputs sufficiently
clear.

This strengthens the existing `REVISE INSTRUMENT BEFORE EXPERIENCE CLAIMS`
disposition. The H1 deterministic resolver remains useful as a fidelity fixture, but
the next human-facing diagnostic requires an interaction taxonomy, visible telegraph,
signed and family-specific input measurements, repeated counterbalanced trials, and
immediate consequence feedback. The proposal and optimized owner-question order are
in `23_REFLEX_INTERACTION_TAXONOMY_AND_DIAGNOSTIC_REVISION_v0_1.md`. No new runtime
gate is opened.
