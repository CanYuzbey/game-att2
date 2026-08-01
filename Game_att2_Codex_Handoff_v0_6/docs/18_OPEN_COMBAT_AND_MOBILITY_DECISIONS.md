# Game att2 — Consolidated Combat and Mobility Decision Queue

Status date: 2026-08-01

Purpose: detailed supporting register of unresolved product questions. Start future
core-gameplay work from `19_CORE_GAMEPLAY_DIRECTION_AND_HANDOFF_2026-08-01.md`; use this
file only to inspect subordinate dependencies. Do not walk every row as an independent
owner interview, and do not implement an item until its blocking macro decision is
approved.

## P0 — Wounds, Blood, and physical viability

| ID | Decision required | Why it blocks runtime | Depends on |
|---|---|---|---|
| W-01 | Name the minimum wound classes represented by the prototype. | Damage cannot create Blood loss without a wound fact. | — |
| W-02 | Map each action/result to a wound class. | Prevents every hit from bleeding identically. | W-01 |
| W-03 | Set immediate and periodic Blood loss for each class. | Blood transactions require configured values. | W-01, W-02 |
| W-04 | Define stabilization, worsening, stacking, and per-round caps. | Determines whether ongoing wounds can be controlled. | W-01–W-03 |
| W-05 | Choose the exact Ruined Torso chain: fatal immediately, rescue window, or conditional fatality. | Torso viability and death remain undefined. | W-01–W-04 |
| W-06 | Define which actions/passives weaken when Torso is Damaged, Critical, or Ruined. | “Physical weakness” needs capability consequences. | W-05 |

## P0 — Movement and main combat model

| ID | Decision required | Why it blocks runtime | Depends on |
|---|---|---|---|
| MOV-01 | Is position represented by no movement, abstract range bands, lanes, or a grid? | Reachability cannot be validated without spatial meaning. | — |
| MOV-02 | Does movement consume the Main action, use separate movement points, or combine with actions? | Defines the real action economy. | MOV-01 |
| MOV-03 | Which leg states reduce movement, dodge, initiative, reach, or stability? | Legs currently affect only Knockdown/Brace. | MOV-01, MOV-02 |
| MOV-04 | Can actors disengage, pursue, block, or escape, and what sources those actions? | Survival and escape motivations need legal affordances. | MOV-01–MOV-03 |
| ACT-01 | Is one Main action plus Focus/Fast the final combat economy or only the survey harness? | The current loop may not represent final combat skill expression. | MOV-02 |
| ACT-02 | Are defense choices proactive stances, reactions, or both? | Brace, Guard Flesh, and Cover It currently mix timing models. | DEF-01–DEF-04 |
| ACT-03 | How are initiative and simultaneous intentions resolved? | Needed when either actor can bargain, move, defend, or attack. | MOV-02, ACT-01 |

## P0 — Defense trade-offs

Cover It duration is already fixed at one round. Brace is manual; Braced Legs is a
separate automatic charge. The unresolved questions are:

| ID | Decision required | Candidate dimensions |
|---|---|---|
| DEF-01 | What exactly does Cover It protect? | One selected limb, marked limb, threatened limb, or a target category |
| DEF-02 | What physical source is required? | Covering arm, any usable arm, torso posture, tool, or no source |
| DEF-03 | What happens to an incoming attack? | Negate, reduce, redirect to covering source, or raise extraction difficulty |
| DEF-04 | What is the Cover It cost/trade-off? | Enemy action, exposed covering limb, reduced offense, Blood, or limited reuse |
| DEF-05 | Why choose manual Brace rather than Guard Flesh or movement? | Knockdown breadth must justify losing a Main action |
| DEF-06 | Why acquire Braced Legs if manual Brace exists? | Passive charge, reliability, action preservation, and limb opportunity cost need comparison |
| DEF-07 | Can Cover It and Brace/Guard stack? | Stacking order and caps must be explicit |

Recommended test hypothesis, not a decision: Cover It may be broader target protection
but expose or occupy a physical covering source; manual Brace may protect only against
Knockdown but be reliable and source-neutral beyond usable Legs.

## P1 — Limb for Life

| ID | Decision required | Current prototype |
|---|---|---|
| LIFE-01 | Does the player choose the sacrificed limb or does seeded randomness remain final? | Seeded-random usable non-Core limb |
| LIFE-02 | May the player refuse sacrifice and accept death? | Not represented |
| LIFE-03 | Are grafted, integrated, critical, or objective-critical limbs eligible? | Any usable non-Core limb |
| LIFE-04 | Is Limb for Life always available once, granted by an item/body part, or earned during a run? | Tutorial-scope once-per-run rule |
| LIFE-05 | Which specific victory-route predicates require sacrifice? | `C04` permits it as an intermediate requirement; no current route requires it yet |

## P1 — Mental defeat, surrender, and mercy

| ID | Decision required | Why needed |
|---|---|---|
| MENT-01 | Define the minimum defeat-acceptance inputs and their representation. | Motivation alone cannot decide surrender. |
| MENT-02 | Define how objective impossibility, offensive incapacity, recovery hope, fear, honor, and desperation combine. | Prevents universal rationality and bespoke endings. |
| MENT-03 | Define which traits are generic and which are character-specific. | Needed for reusable opponents and bosses. |
| MENT-04 | Define the warning threshold before the player loses the final attack source. | Supports informed voluntary surrender. |
| MENT-05 | Define when surrender can be refused and whether an irrational last stand is legal. | Opponent motivation must constrain the answer. |
| MENT-06 | Define mercy as personality, strategy, relationship, or a weighted combination. | Same outward act may have different causes. |

## P1 — Negotiation minigame

| ID | Decision required | Why needed |
|---|---|---|
| NEG-01 | Maximum exchanges and how negotiation ends. | Prevents endless loops. |
| NEG-02 | Whether an exchange consumes combat time and whether Bleeding continues. | Determines the physical cost of talking. |
| NEG-03 | Offer vocabulary: Blood, items, limbs, release, debt, information, future obligation. | Defines legal offer construction. |
| NEG-04 | Opponent evaluation inputs and acceptable uncertainty. | Needed for deterministic, inspectable responses. |
| NEG-05 | Counter-offer construction and concession behavior. | Defines the actual minigame. |
| NEG-06 | Whether either side may attack during negotiation. | Needed for trust and exit behavior. |
| NEG-07 | What memory a rejected offer creates without numerical buffs/debuffs. | Combat resumes unchanged physically but behavior may remember. |
| NEG-08 | How invalid promises or unavailable assets are prevented. | Required causal validation. |

The current Jeff one-click exchange remains a survey shortcut until NEG-01–NEG-08 are
approved.

## P1 — Victory and encounter outcome

| ID | Open question |
|---|---|
| VIC-01 | Is Blood death an available route in every encounter or filtered by motivation/content rating? |
| VIC-02 | When is offensive incapacity partial success, full success, or only negotiation leverage? |
| VIC-03 | When does surrender satisfy the player's actual objective? |
| VIC-04 | How is escape scored for each actor? |
| VIC-05 | How are mutual and multi-route outcomes presented without a binary win screen? |
| VIC-06 | How do boss-specific predicates compose with general routes without hard-coded endings? |
| VIC-07 | Which consequences persist into the next encounter or run? |

## P2 — Motivation, information, and evidence

| ID | Open question |
|---|---|
| MOT-01 | Are Restoration, Survival, Control, and Elimination sufficient as primary classes? |
| MOT-02 | May actors hold primary and secondary motivations simultaneously? |
| MOT-03 | Which state changes may replace or reprioritize a motivation? |
| MOT-04 | What are the final 3–4 reusable ordinary-enemy profiles? |
| INFO-01 | How much motivation is public, inferred, or revealed by Focus? |
| INFO-02 | Is negotiation explicitly offered or discovered through behavior? |
| INFO-03 | Which victory routes are explained before an encounter? |
| TEST-01 | What human-test threshold validates motivation comprehension? |
| TEST-02 | What threshold validates perceived solution breadth and natural resolution? |
| CANON-01 | Is reciprocal-repair Jeff final canon or only the survey instrument? |

## Recommended decision order

```text
Wound classes and Ruined Torso
→ movement representation and action economy
→ defense sources/effects/trade-offs
→ Limb for Life player control
→ mental defeat model
→ negotiation timing and offer evaluation
→ victory persistence and presentation
→ motivation profiles and human-test thresholds
```
