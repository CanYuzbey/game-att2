# Game att2 — Decisions, Risks, and Open Questions v0.6

## Locked identity/product decisions

- single-player PC target;
- mostly silent self-insert;
- hell-loop limb-grafting duel roguelike/roguelite;
- dark/disturbing tone with satirical relief;
- Buckshot Roulette is atmosphere influence, not copied mechanics;
- limbs are the main build engine;
- blood is health/currency/fuel for prototype;
- six slots for first demo;
- table decision view + side/body action presentation later;
- emergency grafting and safer table grafting;
- missing-limb builds are rare/special;
- small demo first.

## Approved for simulator, still reversible

- acting-limb impairment;
- clean-sever gating;
- Harvest Quality;
- Focus pre-action;
- Fast medical timing;
- Plead Pressure;
- Unstable v0.4;
- tutorial soft-collapse/low-blood valve;
- Jeff first and Anna second;
- Grafting Table v0.2;
- scripted deterministic sequence.

## Open product decisions — Codex must not decide

- final title;
- final engine;
- final art style;
- complete run/map structure;
- meta progression;
- long-term enemy/limb roster;
- dialogue system;
- store/release strategy;
- final debt economy;
- final save/load format;
- whether soft collapse survives past prototype.

## Implementation questions Codex may resolve reversibly

- exact internal class/module names;
- YAML loader versus documented migration to another checked-in data format;
- integer rounding rule, if tested and documented;
- CLI library (standard argparse preferred);
- report formatting details;
- test-fixture organization.

## Active risks

| Risk | Probability | Impact | Simulator warning sign | Control |
|---|---:|---:|---|---|
| Blood hoarding | Medium | Very high | premium body without meaningful spend | no-free-clean-sever scenarios |
| Blood Bag dominance | High | Medium | immediate use nearly universal | variant/config report |
| Death spiral | Medium | Very high | one failed roll makes later actions irrelevant | Panic, Fast items, soft-loss metrics |
| Limb system becomes stats | Medium | Very high | body changes do not change legal actions | final body/action summary |
| Table has one answer | High | Medium | integrate selected almost universally | strategy/batch table rates |
| Unstable hated/ignored | Medium | High | always stabilize or never graft | path and collapse metrics |
| Anna path one-sided | Medium | Medium | offer always accepted/rejected | two integration scenarios |
| Simulator overbuild | Medium | High | frameworks/content unrelated to tests | AGENTS scope gate |
| Rule/config drift | Medium | High | prose and code values diverge | config validation and report versioning |
| Premature Unity | High | Very high | engine work before results review | explicit blocked gate |

## Revisit triggers

- Simulator results show a dominant exploit.
- A rule requires repeated special-case code.
- The same mechanic produces contradictory desired outcomes.
- Test logs cannot explain why a run failed.
- External/blind player behavior conflicts with internal simulations.
- Unity architecture would be constrained by a simulator-only convenience.
