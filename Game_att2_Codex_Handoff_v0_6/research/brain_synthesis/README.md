# Brain Synthesis Structural Diagnostic

Status: **ISOLATED RESEARCH FIXTURE THAT INFORMED THE 2026-08-25 OWNER DIRECTION. NOT
PRODUCTION GAMEPLAY, RUNTIME CONFIGURATION, BALANCE APPROVAL, OR HUMAN-PLAY EVIDENCE.**

This fixture compares three card/Brain ownership structures using neutral card
records and deterministic seeded sessions:

1. the owner-original body pool, weighted Attention, paired Brain Part, and Readied
   Item Card;
2. the later player-authored active deck, ordinary draw, hand modifier, and direct
   inventory access;
3. the synthesis direction: mandatory Body Core, selected Technique Cards, Persistent
   Attention Draw, paired Brain Part, and Readied Item Card.

It exists to answer structural questions before any production implementation:

- Can each round expose a legal Main commitment?
- How often does the hand produce too few meaningful choices?
- What happens when an exact action source is lost?
- Does one Readied Item Card cause dangerous action-slot pressure?
- Does a Commitment-capable slot duty correct that pressure?
- How strongly does an Access Brain Part distort category availability?
- Does a paired Execution Brain remain net-positive when its nerf is ignored?
- Do action and inventory limits remain intact?

The fixture cannot establish fun, balance against real enemies, comprehension,
accessibility, emotional effect, final deck size, final hand size, production card
content, or replay value. Its numeric card values and Brain magnitudes are diagnostic
only.

## Run

From this directory:

```powershell
python -m unittest -v test_fixture.py
python -m unittest -v test_player_like_analysis.py
python run_analysis.py --runs 5000 --format markdown
python run_analysis.py --runs 5000 --format json
python player_like_analysis.py --package-runs 250 --persona-runs 100 --fuzz-cases 5000
```

Repeat the same command and compare bytes when determinism matters.

## Fixture boundaries

- Six neutral Body Core cards.
- Six neutral Technique Cards with balanced, aggressive, and defensive selections.
- Two neutral Item Card records, with exactly one deliberately readied at encounter
  start and no automatic in-encounter replacement.
- Source loss: Right Arm becomes unavailable after round three.
- Six Decision Refresh observations per deterministic session.
- Three, four, and five total Attention Slot comparisons.
- Synthesis is tested with and without the owner-original Commitment-capable duty.
- Access and Execution Brain Parts each have one buff and one nerf fixture.
- The optimized candidate keeps four ordinary Attention Slots and one separate,
  deliberately Readied Item Card lane with no automatic replacement.
- Procedural-persona policies, exhaustive small Technique-package enumeration, and
  generated state-machine cases remain synthetic diagnostics rather than humans.

No file under `src/`, `config/`, `tests/`, `examples/`, or the production catalogue is
imported or changed by this research package.

The v0.2 and v0.3 proposal records are retained in this directory as research
provenance. Current paper authority is `../../docs/DECK_BRAIN_AND_ACTIONS.md`.
