# Game att2 Encounter 3 Owner Decision and Requirements Reconciliation v0.1

Status: owner-approved requirements for paper testing only. Encounter 3 runtime implementation is blocked. Unity is blocked. Canonical Warden outcomes: none.

## Approved decisions

Encounter 3 is a bounded causal pressure encounter, not pure endurance. The paper-only Warden has three target zones and two offensive action sources. Player actions may weaken or disable those sources, immediately changing legal Warden actions. Multiple state-derived non-collapse paths are permitted; no action is designated “the solution.”

The encounter resolves only through player collapse under existing rules, bounded Warden combat incapacity, or `UNRESOLVED — ROUND CAP` after eight completed rounds. Warden death, harvest, internal anatomy, organs, penetration, surrender, bargaining, escape, personality, generalized AI, runtime implementation, and Unity remain unapproved.

## Fixed fixture: E3-PRETABLE-01

| Field | Approved paper state |
|---|---|
| Blood | 40 |
| Head | Human Head, Intact |
| Torso | Damaged Human Torso, Damaged, not Bleeding |
| Left arm | Human Left Arm, Intact |
| Right arm | Grafted Human Right Arm, Intact; Grafted and Stabilized; not Unstable or Integrated |
| Legs | Weak Human Legs, Intact |
| Core | Human Heart, Intact |
| Fight resources | Panic Pulse unused; Brace unused |
| Inventory | Hell Saw once; Bone Scissors visible but invalid; Claim/Blood Bag/Clotting Cream unavailable |

This fixture is controlled paper-test state, not a claim about every simulator route. Current repository verification treats 25 Blood as the seed-42 result after the 15-Blood integration spend; historical 32 and 37 are not current evidence.

## Table decisions

| Choice | Cost / start Blood | Effect | Test identity |
|---|---:|---|---|
| Integrate grafted arm | 15 / 25 | Remove Stabilized; add Integrated; Guard remains available | secure graft/direct limb pressure; torso and legs unresolved |
| Repair damaged torso | 18 / 22 | Torso becomes Intact | direct attack protection; graft and legs unresolved |
| Strengthen weak legs | 12 / 28 | Replace with Braced Human Legs; gain Anchored | resist Knockdown; torso and graft unresolved |
| Leave unchanged | 0 / 40 | No transformation | preserve Blood and accept vulnerabilities |

Table Loan is excluded because its principal consequence is outside this encounter. It remains part of the broader prototype.

### Paper-only Anchored rule

The first valid Knockdown attempt each fight is automatically prevented. This does not consume Brace. Brace remains available once as a main action and prevents one additional Knockdown attempt during the protected round.

## Evidence and gate

Run eight real, individually moderated, free-choice sessions using `Game_att2_Encounter_3_Session_Record_Pack_v0_1.md`. `SELF-S01` and `SELF-S02` remain contaminated designer diagnostics and never count toward P01–P08. `SELF-S03` and `SELF-S04` are unnecessary before this gate.

Paper-test approval does not authorize simulator code, runtime configuration, production content, or Unity. Full mechanics, policies, conditions, records, and acceptance criteria are in the current Encounter 3 packet referenced by README.
