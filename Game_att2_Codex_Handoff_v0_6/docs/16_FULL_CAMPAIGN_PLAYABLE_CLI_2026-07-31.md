# Game att2 — Full Campaign Playable CLI Implementation Report

Date: 2026-07-31

Status: implemented within approved digital scope; identity-rule decisions remain
blocked as listed below.

## Delivered player path

The default terminal interface now exposes the approved sequence:

```text
S-001 → Jeff → harvest → emergency graft → Anna → Grafting Table
```

It reuses `InteractiveResearchSession` for orchestration and `RuleEngine` for rule
resolution. Presentation does not duplicate combat, Blood, harvest, graft, Anna, or
table rules. The earlier Jeff-only playable loop is retained with `--phase-1`.

## Player-facing contract

- State shows Blood, both bodies, scene objective, public enemy intent, and statuses.
- Combat choices are layered as action → target; unavailable actions remain visible
  with their reason.
- Target lines identify limbs that source Jeff's Desperate Swing or Anna's Surgical
  Jab.
- A declared enemy source is checked again immediately before resolution. If the
  player made that exact source unusable, the action is cancelled; it cannot fall
  back to another limb in the same phase.
- Each resolved action answers the five Pillar 5 questions: target, state change,
  Blood cost, gain, and new risk.
- Irreversible graft, trade, table, and end-session choices require confirmation in
  interactive play.

## Feedback evidence boundary

After interactive play, the participant may opt into a local questionnaire. The
record includes interface/rule/content/scenario versions, deterministic gameplay
facts, ratings, and optional reflections. It excludes the raw terminal transcript,
does not upload automatically, never overwrites an existing record, and keeps model
training consent separate from local design-research consent.

Records are labeled `UNCLASSIFIED_HUMAN_PLAY` and
`participant_independence_verified: false`. Collection alone therefore does not prove
external-pilot validity, fun, balance, comprehension, or production readiness.

## Deterministic smoke path

```powershell
python -m game_att2_sim.play_cli `
  --seed 42 `
  --script examples/play_cli_full_campaign_sequence.json
```

The recorded sequence reaches every approved phase and ends `COMPLETED` with 25
Blood through the Anna stabilization trade and `integrate_arm` table choice.

## Verification

```text
pytest: 163 passed
coverage: 87%
ruff: all checks passed
mypy: success, no issues in 22 source files
mini_campaign seed 42: completed, 25 Blood
```

## Owner decisions still required

The implementation deliberately does not invent answers for:

1. How Jeff directly threatens Blood, if he should do so at all.
2. What a Ruined player Torso means for viability, defeat, and recovery.
3. The magnitude, duration, and target semantics of Jeff's `Cover It` protection.
4. Which Brace authority wins: manual Weak-Legs Brace in the Development
   Master/config, or automatic Braced-Legs Brace in Combat Rules and the later owner
   decision.

Until those decisions are made, the CLI reports the current configured behavior and
marks the gaps in feedback evidence instead of silently creating product rules.
