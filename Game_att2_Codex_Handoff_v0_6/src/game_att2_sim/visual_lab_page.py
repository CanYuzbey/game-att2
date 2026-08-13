"""Render the local visual-lab HTML fragment from validated research configuration."""

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import fields, is_dataclass
from pathlib import Path
from typing import Any

from .visual_lab_config import VisualLabConfig, load_visual_lab_config


def default_visual_lab_template_path() -> Path:
    return (
        Path(__file__).resolve().parents[2]
        / "research"
        / "visual_lab"
        / "visual_lab.template.html"
    )


def _json_value(value: object) -> Any:
    if is_dataclass(value) and not isinstance(value, type):
        return {field.name: _json_value(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, Mapping):
        return {str(key): _json_value(child) for key, child in value.items()}
    if isinstance(value, (tuple, list)):
        return [_json_value(child) for child in value]
    return value


def render_visual_lab_fragment(config: VisualLabConfig | None = None) -> str:
    lab = config or load_visual_lab_config()
    template = default_visual_lab_template_path().read_text(encoding="utf-8")
    marker = "__VISUAL_LAB_CONFIG__"
    if template.count(marker) != 1:
        raise ValueError("visual-lab template must contain exactly one configuration marker")
    payload = json.dumps(_json_value(lab), sort_keys=True, separators=(",", ":"))
    return template.replace(marker, payload)
