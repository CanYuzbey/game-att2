# Game att2 Post-Table Consequence Probe v0.1

## Executive verdict

**TABLE OPTIONS SHOW SITUATIONAL VALUE, WITH A BLOCKED LEG DIMENSION.** This is a `NON_CANONICAL_VALIDATION_ONLY` simulator probe, not a new encounter, balance change, or fun claim. Integrating an actually Unstable graft removes future Unstable events; Table Loan can avert immediate pressure but creates explicit settlement risk; repairing the torso is observable under torso pressure but its current cost is not justified by this short probe. Strengthen Legs is **not identifiable** because the authoritative rules do not define an unresolved Knockdown consequence.

Unity remains blocked. The baseline configuration and Combat Rules v0.4 were not rebalanced or rewritten.

## Baseline preservation and 37/25 reconciliation

The accepted commit was `6fb2bf8`. The original seed-42 mini-campaign is unchanged and remains deterministic at **25 Blood**. Historical paper evidence of **37 Blood** is retained in the project-state and paper-evidence documents as an unreconciled arithmetic/source-history contradiction, including an unconfigured spare-arm sale. It is not an automated expected value; 25 is not an intended balance target.

## Probe architecture

- Entry point: `--scenario post_table_probe`.
- Marker: `NON_CANONICAL_VALIDATION_ONLY` in code, events, fixture reports, and this report.
- Start state: the accepted seed-42 campaign reproduced through Anna and stopped immediately before the table, then one legal option is applied.
- Pressure is a labeled validation hazard, not a named enemy. It creates no harvest, reward, item, lore, dialogue, map node, or permanent progression.
- Future random choices use `SeededRNG`; paired rows share the same seed per fixture/profile.
- The mixed profile draws four profile selections from the config-backed distribution `[graft_pressure, torso_pressure, knockdown_pressure]`.
- Table Loan retains the existing debt record and settles `owe 30 after next fight` after the probe. Payment and debt failure are separate outcomes.

### Controlled-state matrix

| Fixture | Classification | Natural / synthetic | Purpose |
|---|---|---|---|
| `campaign_pretable` | natural seed-42 pre-table state | natural | exact selected campaign continuation |
| `stable_damaged_comfortable` | controlled diagnostic fixture | synthetic but legal | baseline maintenance state |
| `unstable_damaged_dangerous` | controlled diagnostic fixture | synthetic but legal | graft-risk pressure |
| `stable_critical_dangerous` | controlled diagnostic fixture | synthetic but legal | torso-risk pressure |
| `unstable_healthy_comfortable` | controlled diagnostic fixture | synthetic but legal | isolates arm instability |
| `stable_damaged_braced_low` | controlled diagnostic fixture | synthetic but legal | tests already-braced / low-Blood legality |
| `graft_absent` | controlled diagnostic fixture | synthetic but legal | makes integration illegal |
| `existing_debt` | controlled diagnostic fixture | synthetic but legal | makes a second loan illegal and tests settlement |

## Threat profiles

| Profile | Existing mechanics exercised | Measurements | Status |
|---|---|---|---|
| Graft Pressure | Unstable checks, Guard Flesh, limb damage | Unstable events, right-arm availability, Guard attempts, mitigation, limb degradation | Implemented |
| Torso Pressure | torso damage, Bleeding, Clotting Cream, Panic | Bleeding rounds, Cream use, Blood, critical states, collapse | Implemented |
| Knockdown Pressure | Brace/Knockdown references only | attempts/prevention/unresolved/action loss | **BLOCKED: owner-approved mechanical definition required** |
| Mixed Unknown Pressure | injected RNG chooses the config-backed profile sequence | selected sequence plus all applicable profile metrics | Partially identifiable; any Knockdown draw remains blocked |
| Debt Settlement | existing minimal debt record | payment possible, debt failure, final Blood | Implemented |

No action-loss rule, movement system, initiative system, or new status framework was installed. The validation harness maps unaffordable mandatory Bleeding to an explicit non-canonical collapse event; the baseline engine behavior was not altered.

## Paired-seed evidence

The complete matrix ran **1,000 paired seeds x 5 options x 4 profiles x 8 fixtures**: 160 aggregate rows in 60.18 seconds. Illegal options are retained as `legal_option_rate: 0`, not silently substituted.

Selected 1,000-seed rows (mean final Blood; all listed completion rates are 100% unless stated):

| Fixture / profile | Integrate | Repair torso | Strengthen legs | Loan | Leave | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| natural / Graft | 19 | 16 | 22 | 24 | 34 | graft was already stabilized; Leave preserves Blood |
| unstable-dangerous / Graft | 14, 0 unstable events | 10.4, 4 events | 16.4, 4 events | 10.4, 0 events | 28.2, 4 events | integration buys stability, not immediate Blood |
| natural / Torso | 19.4 | 18.0 | 22.4 | 24.4 | 30.4 | all survive; short pressure does not justify current repair price |
| critical-dangerous / Torso | 12.5 | 7.8, 89% completion | 15.5 | not a spending comparison | 30.4 | repair is price-sensitive and can collapse in this harness |
| graft absent / either | illegal | legal | legal | legal | legal | integration correctly remains unavailable |
| existing debt / Torso | 100% debt failure | 83.6% debt failure, 16.4% collapse | 100% debt failure | illegal | 84.8% debt failure | existing debt dominates decision space |

The `random_legal` policy was not used as player evidence. The state-aware diagnostic chooser is intentionally not promoted as a player model: known-next-threat may prefer avoiding an Unstable arm when its future cost matters; unknown-next-threat preserves Blood unless a visible instability or torso condition provides a specific reason to spend.

## Dominance and regret

Outcome dimensions are reported separately: survival/completion, final body integrity, final Blood, future Unstable events, and debt settlement. There is no opaque scalar.

| State/profile | Integrate | Repair | Strengthen | Loan | Leave |
|---|---|---|---|---|---|
| stable graft / Graft | strictly dominated in tested condition | strictly dominated in tested condition | weak but defensible only pending Knockdown | situational emergency | competitive |
| unstable graft / Graft | situational | weak but defensible | not identifiable for leg value | situational emergency | competitive but carries 4 unstable checks |
| critical torso / Torso | weak but defensible | weak but defensible; price-sensitive | not identifiable for leg value | situational emergency | competitive in this narrow profile |
| any / Knockdown | not identifiable | not identifiable | **not identifiable** | not identifiable | not identifiable |
| graft absent | illegal | situational | not identifiable | situational | competitive |
| existing debt | weak but defensible | weak but defensible | not identifiable | illegal | situational; settlement dominates |

Regret matrix, using transparent dimensions rather than a weighted score:

| Chosen option | Threat | Best observed dimension | Regret versus best |
|---|---|---|---|
| Integrate | stable Graft | Leave: +15 Blood | loses Blood; no instability benefit exists |
| Leave | unstable Graft | Integrate: 0 future Unstable events | retains four instability checks despite +14.2 mean Blood |
| Repair | critical Torso | Leave: +22.6 mean Blood and +11 points completion | cost and short-profile repair effect do not compete |
| Strengthen | any tested profile | none available | leg consequence is undefined |
| Loan | existing debt | none | second loan illegal; settlement failure dominates |

## Cost sensitivity

An isolated symmetric `-3 / baseline / +3` overlay was sampled at 100 paired seeds for unstable-Graft and critical-Torso fixtures. The larger 1,000-seed baseline matrix completed; a 1,000-seed sensitivity grid was stopped at the 120-second command limit, so the smaller grid is explicitly diagnostic.

| Profile | Option | -3 mean Blood | Baseline | +3 | Finding |
|---|---|---:|---:|---:|---|
| unstable Graft | Integrate | 17.0 | 14.0 | 11.0 | direct price sensitivity; stability benefit remains |
| unstable Graft | Repair | 13.4 | 10.4 | 7.5 | weak under unrelated pressure |
| unstable Graft | Strengthen | 19.4 | 16.4 | 13.4 | Blood-only difference; leg value not tested |
| critical Torso | Integrate | 15.5 | 12.5 | 9.6 | unrelated to torso pressure |
| critical Torso | Repair | 10.7 | 7.8 | 5.1 | 89% completion at baseline and +3 |
| critical Torso | Strengthen | 18.5 | 15.5 | 12.5 | no leg-pressure conclusion |

No candidate cost change is recommended. The current result says that a numerical change alone cannot validate the leg choice or make the torso choice compelling without a more representative, owner-approved threat definition.

## Hostile review

| Priority | Finding | Disposition |
|---|---|---|
| P1 | Authoritative rules lack an unresolved Knockdown consequence; Strengthen Legs cannot be evaluated honestly. | Blocked; owner decision required. |
| P1 | Baseline start-of-round Bleeding cannot spend the final available Blood before raising an affordability error. | Probe-only explicit collapse mapping; do not change baseline without approval. |
| P2 | Repair Torso restores current integrity but has only a short, synthetic pressure test. | Evidence is weak; no rebalance. |
| P2 | Mixed Unknown becomes partially non-identifiable whenever it draws Knockdown. | Reported, not hidden. |
| P3 | The diagnostic chooser is not human-player modeling. | Explicitly limited and not used for product claims. |

## Conclusion and owner decisions

The probe establishes conditional downstream observability for graft instability and debt, but not adequate competition across all table choices. Needed owner decisions:

1. Define the minimal unresolved Knockdown consequence and Brace timing, or declare legs intentionally deferred.
2. Decide whether a post-table torso threat should make repair a survival/body-integrity choice rather than a Blood-loss choice.
3. Define the historical spare-arm sale/bargain transaction only if it remains part of intended product rules.
4. Decide what evidence threshold, beyond this non-canonical probe, is required before an encounter is designed.

No production stage begins from this report.

## Sprint 0.6.1 addendum

The prior blocked leg result is superseded by the owner-approved Tempo Loss rule. The non-canonical rerun now uses canonical Downed, Stand, and encounter-scoped Brace semantics. Strengthen Legs shows situational tempo protection; see `Game_att2_Knockdown_Brace_Validation_v0_1.md`. Unity remains blocked.
