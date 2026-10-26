# Research method and limits

Primary references checked 2026-09-06. This is a project-specific synthesis, not a
validated universal method or a claim of scientific optimization.

| Foundation | Supported method | Game att2 application | Limit |
|---|---|---|---|
| [Hunicke, LeBlanc, Zubek: MDA](https://www.cs.northwestern.edu/~hunicke/MDA.pdf) | Separate mechanics, runtime dynamics, and desired experience; iterate in both directions | Link limb mutation -> changed plan -> reported rebuilding experience | Does not prove fun or supply numerical balance |
| [NIST: Introduction to Combinatorial Testing](https://csrc.nist.gov/pubs/book/2013/06/introduction-to-combinatorial-testing/final) | Test interactions between factors with explicit coverage | Exhaust critical source/exchange cases; pairwise ordinary factors and named high-risk triples | Coverage strength is not exhaustive behavioral correctness |
| [Microsoft XAG 107](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107) | Input alternatives must address speed and complexity as well as remapping | Digital card selection, tap/hold alternatives and separately tested assistance | Guidelines do not certify this game accessible |
| [Microsoft XAG 116](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/116) | Allow sufficient time for non-core UI interaction | Pause reading, bargain, and commitment previews | This guideline explicitly excludes core gameplay time limits; it does not derive Parry windows |
| [Unity time handling](https://docs.unity3d.com/6000.0/Documentation/Manual/time-handling-variations.html) | Frame update and fixed simulation timing differ | After engine approval, separate replayable rule events from rendered defense timing and record input timestamps | FixedUpdate alone is not cross-machine deterministic combat |

## Inquiry loop

1. Name the uncertain causal link and what decision it blocks.
2. Record current authority separately from external evidence.
3. Compare the existing baseline with meaningfully different alternatives. For a new
   card/graft, vary one source-bound causal property, the choice it changes, and the
   experienced drawback; do not multiply adjectives or substitute a stat-only upgrade.
4. Predict a discriminating result and an adversarial failure case before testing.
5. Use the cheapest adequate instrument: arithmetic for costs; state transitions for
   legality; interaction prototype for input/readability; people for comprehension/appeal.
6. Hold unrelated factors fixed when comparing. Record seed/model version, parameter
   range, policy, accessibility setting, ordering/learning effects, and exclusions.
7. Report uncertainty and counterevidence; retain/revise/reject a bounded hypothesis.
   Do not search indefinitely after the next decision has sufficient evidence.

The creative constraint matrix is our design heuristic: source x consequence x lost
alternative x later pressure. It is not attributed to an experimental result.
Reject proposals that introduce more state than the player can inspect or test.
Compare plausible parameter ranges; if the recommendation flips, expose that sensitivity.

## Evidence card

Question / decision ID:
Current source and status:
Candidates and baseline:
Predicted dynamic:
Desired experience:
Negative example / alternative explanation:
Method, fixture version, seeds or human protocol:
Observed result and uncertainty:
Continue / revise / stop interpretation declared before evidence:
Decision owner and reopen trigger:

Automation can falsify a legality or economy claim. It cannot certify human enjoyment.
No synthetic persona or LLM answer counts as a participant. Owner self-play is internal;
friend play is convenience evidence. Record consent, prior exposure/relationship,
facilitator help, raw behavior, and session duration; owner sets sample and interpretation
before an acceptance session. Do not treat zero observed failures as zero risk.
