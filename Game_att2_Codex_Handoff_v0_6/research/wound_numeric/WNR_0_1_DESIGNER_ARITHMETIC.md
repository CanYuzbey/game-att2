# WNR-0.1 Designer Arithmetic Ledger

Status date: 2026-08-14

Evidence class: **DESIGNER_ARITHMETIC - NOT HUMAN PLAYTEST EVIDENCE**

Current summary: `docs/COMBAT_BODY_AND_BLOOD.md`
Historical package: `docs/archive/design_history_2026-08-21/30_WOUND_BLOOD_REPAIR_NUMERIC_OWNER_REVIEW_v0_1.md`

## Evidence card

| Field | Record |
|---|---|
| Question | Do WNR-0.1 values produce distinct short-term Control, long-term Stabilize, bounded repair, visible self-risk, and one actionable Torso rescue window? |
| Variant | Open 3/5, Major 8/8, clean Stump 10/8, violent Stump 15/12, cap 20; Control 8/two ticks; Stabilize 12/encounter; Field 10/+25%/70% cap; Reconstruct 18/to 35%; Wound Stress 2/4 |
| Expected dynamic | Open pressure is manageable; Major/Stump treatment is urgent; Control leads for two ticks and Stabilize for longer horizons; repair cannot erase Ruin; Torso demands an explicit rescue commitment |
| Desired experience | Readable triage under pressure without automatic treatment, hidden deterioration, or a separate action-point system |
| Instrumentation | Hand arithmetic using current 25-45 integrity fixtures and 0/20/25/35/50/70/85 Blood landmarks |
| Continue criteria | Arithmetic is internally consistent, cap aggregates once, treatments have different horizons, repair ceilings preserve damage, and rescue never grants unsupported capability |
| Contamination | Designer-authored values and interpretation; no external participant, comprehension, fairness, fun, or balance evidence |
| Decision owner | Can Yüzbey |

## Deterministic Blood comparisons

Starting Blood: `85`.

| Wound | After creation | Untreated after 2 ticks | Control cost paid, 2 ticks suppressed | Third tick after Control | Stabilize cost paid |
|---|---:|---:|---:|---:|---:|
| Open | 82 | 72 | 74 | 69 | 70 |
| Major | 77 | 61 | 69 | 61 | 65 |
| Clean Stump | 75 | 59 | 67 | 59 | 63 |
| Violent Stump | 70 | 46 | 62 | 50 | 58 |

Checks:

- Open Control saves `10` periodic Blood for cost `8`: net `+2` across two ticks.
- Major/clean-Stump Control saves `16` for cost `8`: net `+8`.
- Violent-Stump Control saves `24` for cost `8`: net `+16`.
- Stabilize costs `4` more than Control but becomes better when the third periodic
  tick would occur.
- Open `5` + Major `8` + violent Stump `12` = `25`, clamped once to `20`.

## Current-start checks

| Case | Arithmetic | Result |
|---|---|---|
| Jeff-like `70` Blood + violent Stump + two ticks | `70 - 15 - 12 - 12` | `31`, Dangerous but not automatically dead |
| Player `85` Blood + Major + two ticks | `85 - 8 - 8 - 8` | `61`, remains Normal |
| Three wounds at `85`, one capped tick | `85 - 3 - 8 - 15 - 20` | `39`, Dangerous after extreme accumulated injury |
| Blood Bag at `40` while Open is Untreated | `40 + 15` | `55` |
| Control then Blood Bag from `40` | `40 - 8 + 25` | `57`, two more Blood plus suppressed ticks |

## Panic and Torso checks

| Case | Arithmetic | Result |
|---|---|---|
| `30` Blood + Major creation | `30 - 8 = 22`, Panic `+10` | `32` |
| Stabilize after that one-use Panic | `32 - 12` | `20`, alive and Critical |
| `25` Blood + Ruined-Torso Major | `25 - 8 = 17`, Panic `+10` | `27` |
| Representative Torso rescue | `27 - 12` | `15`, rescued but Critical |

Torso's own first periodic contribution is deferred until the rescue deadline. Other
wounds and paid costs continue normally. Refusal permits one existing legal Main, then
catastrophic death; it does not grant another action.

## Threshold and free-attack checks

### 20-integrity arm, Grip Strike 10

```text
20 -> 10: exactly 50% damage; state Damaged; no >50% wound trigger
10 -> 0: Ruin; one Major Wound; immediate Blood -8; never Clean
```

### 30-integrity arm, Grip Strike 10

```text
30 -> 20: Damaged; no threshold wound
20 -> 10: enters Critical; Closed Trauma; Blood 0
10 -> 0: Ruin; escalates to Major; immediate Blood -8; never Clean
```

No duplicate wound record or repeated immediate Major transaction is created by a
single hit satisfying more than one trigger.

## Repair arithmetic

| Maximum | Field delta | Field ceiling | Reconstruct to |
|---:|---:|---:|---:|
| 25 | 6 | 17 | 8 |
| 30 | 8 | 21 | 10 |
| 35 | 9 | 24 | 12 |
| 45 | 11 | 31 | 15 |

For a 30-integrity arm:

```text
Critical 10 + Field 8 -> 18 Damaged
Ruined 0 + Field -> rejected atomically
Ruined 0 + Reconstruct -> 10 Critical
10 + later Field 8 -> 18 Damaged
second Reconstruct in same encounter -> rejected atomically
Severed/Missing + either repair -> rejected atomically
```

Repair changes neither Blood nor treatment state in these checks.

## Wound-stress checks

| Source state | Marked action consequence |
|---|---|
| Untreated Open | Action resolves, then Blood `-2` |
| Untreated Major | Action resolves, then Blood `-4` |
| Controlled Open | Action resolves, Blood `-2`, Control clears, Untreated returns |
| Controlled Major | Action resolves, Blood `-4`, Control clears, Untreated returns |
| Stabilized Open/Major | No wound surcharge unless the card explicitly breaks Stabilization |
| Ordinary unmarked limb card | No wound surcharge in every treatment state |

## Arithmetic verdict

**CONTINUE TO OWNER REVIEW.** The values are internally coherent enough for a first
paper baseline. This verdict does not approve the package or support implementation.

Highest-risk variables:

1. violent Stump `15 immediate / 12 periodic`;
2. two suppressed ticks for Control;
3. representative Stabilize cost `12`;
4. allowing a final Main when Torso rescue is refused.

No human session has tested whether these choices are understandable, fair, tense, or
enjoyable.
