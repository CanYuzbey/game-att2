"""Shared validation helpers for command-line entry points."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


class CLIInputError(ValueError):
    """A user-correctable command-line input error."""


def positive_int(value: str) -> int:
    """Parse a strictly positive integer for argparse."""
    try:
        parsed = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be an integer") from error
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


def load_json_list(path: Path, *, label: str) -> list[Any]:
    """Read a UTF-8 JSON list and present file/JSON failures as CLI input errors."""
    try:
        raw = path.read_text(encoding="utf-8-sig")
    except OSError as error:
        reason = error.strerror or str(error)
        raise CLIInputError(f"cannot read {label} '{path}': {reason}") from error
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as error:
        raise CLIInputError(
            f"{label} '{path}' is not valid JSON (line {error.lineno}, column {error.colno})"
        ) from error
    if not isinstance(value, list):
        raise CLIInputError(f"{label} must contain a JSON list")
    return value
