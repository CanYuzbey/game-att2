# Bounded Visual Interaction Lab v0.1

Status: fidelity-verified local instrument preserved for later research. The owner
deferred VL-WP4 before execution on 2026-08-13. This lab reuses H1-F0 only and is not
production combat, a campaign rule, final UI, or external-player evidence. Results are recorded in
`docs/26_VISUAL_INTERACTION_LAB_IMPLEMENTATION_RESULTS_v0_1.md`.

## What it tests

- a visible Anna Surgical Jab telegraph and contact point;
- signed early/late Block input;
- one visible Ready / Strained / Exhausted resource;
- stronger repeated-Block strain and visible low-Blood amplification;
- Guard preparation, intent information, precise/assisted timing, and body-source
  legality;
- threat-resolution and explicit pressure-break recovery;
- ordinary versus acknowledged high-risk failure.

The ten deterministic comparison pairs are VL-C1 through VL-C10 in
`docs/25_BOUNDED_VISUAL_INTERACTION_LAB_PLAN_v0_1.md`. Directional, sequence, and
sustained input families remain unimplemented.

## Build the local page

From the package root:

```powershell
python -m game_att2_sim.visual_lab_cli `
  --page `
  --output tmp/game-att2-readiness-lab.html
```

The generated file is an HTML fragment with embedded validated research
configuration and no network request. It refuses to overwrite an existing file.
Generated `tmp/` output is ignored by Git.

The page requires two practice attempts before four recorded A/B/B/A trials. Practice
attempts remain labeled and excluded from measured evidence. VL-WP4 is deferred, so
the page must not be used for evidence collection until a later owner gate reopens it.

## Deterministic replay

```powershell
python -m game_att2_sim.visual_lab_cli `
  --script examples/visual_lab_scripted_comparisons.json `
  --all-comparisons `
  --format json
```

The scripted runner resolves all twenty variants through the Python research
contract. It establishes configuration, causality, isolation, and byte-replay
fidelity only. It cannot establish fun, comprehension, accessibility, fairness,
balance, fatigue, preference, or production readiness.

## Evidence and contamination boundary

- `AUTOMATED_REGRESSION`: deterministic signed inputs; fidelity evidence only.
- `OWNER_DIAGNOSTIC`: separately approved local owner session; diagnostic evidence.
- External participants: blocked until a separate consent, privacy, recruitment,
  retention, deletion, and session protocol is approved.

Do not commit generated diagnostic evidence unless its evidence class, consent,
fixture/config version, deviations, and contamination disposition are recorded.
