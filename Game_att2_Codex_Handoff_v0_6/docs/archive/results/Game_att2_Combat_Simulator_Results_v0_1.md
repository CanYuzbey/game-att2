# Game att2 Combat Simulator Results v0.1

> **Historical artifact — superseded.** Preserve the results below as historical evidence. The current authoritative simulator evidence is `Game_att2_Combat_Simulator_Results_v0_2.md`, generated after the 2026-07-23 causal-integrity correction.

Generated from deterministic simulator runs. These results validate implementation behavior; they do not prove player fun or market demand.

## Review Gate Addendum (2026-07-16)

The original v0.1 numbers below are preserved as historical output. The review gate corrected a source-compliance defect: Jeff's intended right arm is now a large Hell Saw target and S1 explicitly verifies the saw event. The corrected seed-42 mini-campaign ends at 25 blood, not the former 32. The original 100-seed strategy results are superseded by the 500-seed review evidence in `Game_att2_Simulator_Review_Gate_v0_1.md`; no baseline balance value was changed.

## Required Scenarios

| Scenario | Seed | Result | Final Blood | Clean/Stressed/Ruined | Key Outcome |
|---|---:|---|---:|---|---|
| jeff_baseline | 42 | completed | 57 | 1/0/0 | scenario completed |
| jeff_no_spend | 42 | completed | 85 | 0/0/0 | scenario completed |
| failed_hell_saw | 42 | completed | 29 | 0/0/0 | scenario completed |
| anna_stabilization | 42 | completed | 63 | 0/0/0 | scenario completed |
| anna_greed | 42 | completed | 79 | 1/0/0 | scenario completed |
| mini_campaign | 42 | completed | 32 | 1/0/0 | integrate_arm |
| blood_bag_balance | 42 | completed | 117 | 0/0/0 | baseline: blood 85->100; bleeding recovery 15, variant_b: blood 100->107; bleeding recovery 12, variant_c: blood 107->117; bleeding recovery 15 |

## Batch Metrics

| Strategy | Completion | Collapse | Avg Blood | Median Blood | Table Paths | Identical Body Rate |
|---|---:|---:|---:|---:|---|---:|
| balanced | 100% | 0% | 35.0 | 35.0 | {'integrate_arm': 100} | 64% |
| blood_hoarder | 100% | 0% | 85.0 | 85.0 | {'leave': 100} | 100% |
| limb_greed | 100% | 0% | 39.3 | 39.0 | {'strengthen_legs': 100} | 80% |
| survival_first | 100% | 0% | 32.0 | 32.0 | {'repair_torso': 100} | 100% |
| reckless_sever | 100% | 0% | 26.9 | 27.0 | {'integrate_arm': 100} | 65% |

### Strategy Detail

- **balanced**: actions={'claim_the_cut': 100, 'grip_strike': 400, 'bone_scissors': 100, 'guard_flesh': 100}; Clean/Stressed/Ruined=100/0/0; trade acceptance=100%.
- **blood_hoarder**: actions={'grip_strike': 400}; Clean/Stressed/Ruined=0/0/0; trade acceptance=0%.
- **limb_greed**: actions={'claim_the_cut': 100, 'grip_strike': 600, 'bone_scissors': 200}; Clean/Stressed/Ruined=154/0/0; trade acceptance=0%.
- **survival_first**: actions={'claim_the_cut': 100, 'grip_strike': 400, 'bone_scissors': 100, 'guard_flesh': 100}; Clean/Stressed/Ruined=100/0/0; trade acceptance=100%.
- **reckless_sever**: actions={'claim_the_cut': 100, 'grip_strike': 600, 'hell_saw': 100, 'bone_scissors': 100, 'guard_flesh': 100}; Clean/Stressed/Ruined=100/0/0; trade acceptance=100%.

## Observations

- Free Grip Strike paths produce ruined arms and surrender pressure, not premium clean grafts.
- The reported batch is a deterministic strategy probe, not player behavior evidence.
- Unity remains blocked pending owner review of this simulator evidence and any needed rule revisions.
