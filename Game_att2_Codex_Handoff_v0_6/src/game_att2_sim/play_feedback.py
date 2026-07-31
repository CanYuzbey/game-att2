"""Versioned, privacy-conscious local feedback for both playable CLI modes."""

from __future__ import annotations

import json
from collections import Counter
from collections.abc import Mapping
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

from .campaign_play import CAMPAIGN_INTERFACE_VERSION
from .play_session import LOCKED_SCOPE, PLAY_INTERFACE_VERSION, PlaySession, blood_band
from .research_shell import APPROVED_SEQUENCE, InteractiveResearchSession

FEEDBACK_SCHEMA_VERSION = "0.2"
CONSENT_TEXT_VERSION = "0.1"
DEFAULT_FEEDBACK_DIRECTORY = Path("reports/play_feedback")

PlayableSession = PlaySession | InteractiveResearchSession


def _validate_answers(
    ratings: Mapping[str, int | None], collection_status: str
) -> None:
    if collection_status not in {"complete", "partial"}:
        raise ValueError("collection_status must be 'complete' or 'partial'")
    for key, value in ratings.items():
        if value is not None and not 1 <= value <= 5:
            raise ValueError(f"rating {key!r} must be between 1 and 5")


def _phase_one_gameplay(session: PlaySession) -> dict[str, object]:
    event_counts = Counter(event.event_type for event in session.log.events)
    graft = session.graftable_right_arm
    return {
        "outcome": session.outcome.value,
        "rounds": session.log.round_number,
        "final_blood": session.player.blood,
        "final_blood_band": blood_band(session.player.blood, session.rules),
        "blood_spent": session.metrics.blood_spent,
        "blood_gained": session.metrics.blood_gained,
        "panic_pulse_used": session.player.panic_pulse_used,
        "limb_for_life_used": session.player.soft_collapse_used,
        "graftable_right_arm": (
            None
            if graft is None
            else {"limb_name": graft.limb_name, "quality": graft.quality.value}
        ),
        "harvests": [
            {
                "slot": harvest.slot.value,
                "limb_name": harvest.limb_name,
                "quality": harvest.quality.value,
            }
            for harvest in session.harvests
        ],
        "action_counts": dict(sorted(session.metrics.actions.items())),
        "action_trace": [
            {
                "round": report.round_number,
                "actor": report.actor,
                "action": report.action_label,
                "target": report.targeted,
                "changes": list(report.changed),
                "blood_cost": report.blood_cost,
                "gains": list(report.gained),
                "new_risks": list(report.new_risks),
            }
            for report in session.reports
        ],
        "event_type_counts": dict(sorted(event_counts.items())),
        "current_pressure_model": {
            "player_defeat_route": "Blood reaches collapse threshold after rescue checks",
            "jeff_direct_blood_loss": False,
            "jeff_swing_target": "torso_integrity",
            "ruined_torso_defeat_rule": "deferred_owner_decision",
        },
    }


def _campaign_gameplay(session: InteractiveResearchSession) -> dict[str, object]:
    event_counts = Counter(event.event_type for event in session.log.events)
    return {
        "outcome": session.outcome,
        "rounds": session.log.round_number,
        "final_blood": session.player.blood,
        "blood_spent": session.metrics.blood_spent,
        "blood_gained": session.metrics.blood_gained,
        "anna_path": session.anna_path,
        "table_choice": session.metrics.table_choice,
        "final_body": session.export_payload()["final_body"],
        "action_counts": dict(sorted(session.metrics.actions.items())),
        "action_sequence": list(session.action_sequence),
        "decision_points": [asdict(decision) for decision in session.decisions],
        "event_type_counts": dict(sorted(event_counts.items())),
        "current_pressure_model": {
            "player_defeat_route": "Blood reaches collapse threshold after rescue checks",
            "jeff_direct_blood_loss": False,
            "jeff_swing_target": "torso_integrity",
            "declared_enemy_source_revalidated_before_resolution": True,
            "ruined_torso_defeat_rule": "deferred_owner_decision",
            "cover_it_protection": "deferred_owner_decision",
            "brace_conflict": "deferred_owner_decision",
            "jeff_blood_threat": "deferred_owner_decision",
        },
    }


def build_feedback_record(
    session: PlayableSession,
    *,
    ratings: Mapping[str, int | None],
    reflections: Mapping[str, str],
    model_training_consent: bool,
    collection_status: str,
    session_id: str | None = None,
    recorded_at_utc: str | None = None,
) -> dict[str, object]:
    """Build one anonymous local record without including the raw transcript."""
    _validate_answers(ratings, collection_status)
    record_id = session_id or str(uuid4())
    timestamp = recorded_at_utc or datetime.now(UTC).isoformat()
    if isinstance(session, PlaySession):
        record_type = "game_att2_phase_1_playtest_feedback"
        versions = {
            "interface_version": PLAY_INTERFACE_VERSION,
            "rules_version": str(session.rules["rules_version"]),
            "content_version": session.config.content_version,
            "scenario_version": session.config.scenario_version,
        }
        source = {
            "interface": "phase_1_playable_cli",
            "scope": LOCKED_SCOPE,
            "seed": session.seed,
            "evidence_class": "UNCLASSIFIED_HUMAN_PLAY",
            "participant_independence_verified": False,
        }
        gameplay = _phase_one_gameplay(session)
    else:
        record_type = "game_att2_full_campaign_playtest_feedback"
        versions = {
            "interface_version": CAMPAIGN_INTERFACE_VERSION,
            "rules_version": str(session.config.rules["rules_version"]),
            "content_version": session.config.content_version,
            "scenario_version": session.config.scenario_version,
        }
        source = {
            "interface": "full_campaign_playable_cli",
            "scope": APPROVED_SEQUENCE,
            "seed": session.metadata.seed,
            "evidence_class": "UNCLASSIFIED_HUMAN_PLAY",
            "participant_independence_verified": False,
        }
        gameplay = _campaign_gameplay(session)
    return {
        "schema_version": FEEDBACK_SCHEMA_VERSION,
        "record_type": record_type,
        "session_id": record_id,
        "recorded_at_utc": timestamp,
        "collection_status": collection_status,
        "versions": versions,
        "consent": {
            "local_design_research": True,
            "model_training": model_training_consent,
            "consent_text_version": CONSENT_TEXT_VERSION,
        },
        "source": source,
        "gameplay": gameplay,
        "ratings": dict(ratings),
        "reflections": {key: value.strip() for key, value in reflections.items()},
    }


def write_feedback_record(record: Mapping[str, Any], directory: Path) -> Path:
    """Write one record without overwriting an existing session file."""
    session_id = record.get("session_id")
    if not isinstance(session_id, str) or not session_id.strip():
        raise ValueError("feedback record requires a non-empty session_id")
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"play-feedback-{session_id}.json"
    payload = json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
    return path
