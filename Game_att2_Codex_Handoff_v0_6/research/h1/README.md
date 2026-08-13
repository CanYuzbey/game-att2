# H1 Hybrid-Combat Research Operations

Status: deterministic fidelity fixture implemented and verified on 2026-08-12. Its
fixed terminal timing task is retained for reproducibility but is not an adequate
human-facing diagnostic. The replacement visual lab is implemented and
fidelity-verified; its owner diagnostic remains separately gated.

H1 tests one controlled post-Jeff interaction against Anna's existing Surgical Jab.
It is not an eighth approved scenario, a full encounter rewrite, or production combat.

## Evidence classes

- `AUTOMATED_REGRESSION`: versioned scripted timing input. It may establish rule
  fidelity, reachability, causal traceability, and deterministic replay.
- `OWNER_DIAGNOSTIC`: local timing capture by the owner/designer. It may identify
  control or comprehension problems but is not external-player evidence.

Neither class establishes fun, balance, accessibility, fairness, market demand, or
production readiness. External participants require a separately approved consent and
session protocol; H1 performs no upload and stores no participant identity.

Read `docs/23_REFLEX_INTERACTION_TAXONOMY_AND_DIAGNOSTIC_REVISION_v0_1.md` for the
diagnostic finding and `docs/25_BOUNDED_VISUAL_INTERACTION_LAB_PLAN_v0_1.md` for the
approved bounded plan. Its results and current owner-diagnostic gate are in
`docs/26_VISUAL_INTERACTION_LAB_IMPLEMENTATION_RESULTS_v0_1.md`. Do not extend this
runner or the visual lab beyond that authority.

## Deterministic replay

From the package root:

```powershell
python -m game_att2_sim.h1_cli `
  --all-comparisons `
  --script examples/h1_scripted_comparisons.json `
  --format json
```

Use `--format markdown` for the compact comparison table. Use
`--comparison H1-C1` through `H1-C6` to run one pair. The scripted file records raw
integer timing error separately from the derived grade.

## Owner diagnostic

Omit `--script` and select one comparison:

```powershell
python -m game_att2_sim.h1_cli `
  --comparison H1-C1 `
  --comparison H1-C3 `
  --comparison H1-C5 `
  --session-id OWNER-H1-DIAG-001 `
  --consent-confirmed `
  --evidence-class OWNER_DIAGNOSTIC `
  --profile precise `
  --format json `
  --output research/h1/OWNER-H1-DIAG-001.json
```

The terminal boundary records elapsed integer milliseconds relative to the diagnostic
target. The pure resolver never reads the operating-system clock. Diagnostic prompts
use the terminal error stream, leaving the saved JSON machine-readable. Existing
evidence files are never overwritten.

## Evidence schema

Each run records:

- fixture, comparison, variant, spec, and configuration versions;
- evidence class and the named changed condition;
- prior player/Anna body state, Blood, intent clarity, preparation, and source state;
- opportunity legality and one disabled reason;
- raw and effective timing error, profile, grade, and state modifier;
- target and disclosed source mutations;
- recomputed Guard Flesh capability;
- structured event sequence and explicitly deferred physical rules.

Exact timing bands, mitigation basis points, and exposure damage are labeled
`PROVISIONAL_H1_RESEARCH_ONLY` in `config/h1_reflex_v0_1.yaml`.

## Contamination controls

- Do not reinterpret scripted output as player behavior.
- Do not pool owner diagnostics with external sessions.
- Preserve configuration, script, and code versions beside any exported result.
- Record facilitator deviations for future human protocols.
- Do not promote the fixture-only Torso target into Anna's general behavior.
