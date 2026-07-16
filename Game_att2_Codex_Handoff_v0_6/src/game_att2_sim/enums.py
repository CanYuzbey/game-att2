"""Closed vocabulary for the simulator domain."""

from __future__ import annotations

from enum import Enum


class Slot(str, Enum):
    HEAD = "head"
    TORSO = "torso"
    LEFT_ARM = "left_arm"
    RIGHT_ARM = "right_arm"
    LEGS = "legs"
    CORE = "core"


class LimbState(str, Enum):
    INTACT = "intact"
    DAMAGED = "damaged"
    CRITICAL = "critical"
    DISABLED = "disabled"
    SEVERED = "severed"
    MISSING = "missing"
    RUINED = "ruined"


class LimbTag(str, Enum):
    BLEEDING = "bleeding"
    GRAFTED = "grafted"
    UNSTABLE = "unstable"
    INTEGRATED = "integrated"
    STABILIZED = "stabilized"
    MARKED = "marked"
    HANGING = "hanging"
    PROTECTED = "protected"


class HarvestQuality(str, Enum):
    CLEAN = "clean"
    STRESSED = "stressed"
    RUINED = "ruined"


class Phase(str, Enum):
    START = "start"
    INTENT = "intent"
    FOCUS = "focus"
    FAST = "fast"
    MAIN = "main"
    ENEMY = "enemy"
    END = "end"
    TABLE = "table"


class IntentClarity(str, Enum):
    VAGUE = "vague"
    PARTIAL = "partial"
    EXACT = "exact"


class UnstableResult(str, Enum):
    TWITCH = "twitch"
    WORKS = "works"
    ACHE = "ache"
    SURGE = "surge"
