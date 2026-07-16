"""Domain-specific errors surfaced by the CLI and asserted by tests."""


class SimulatorError(Exception):
    """Base class for expected simulator failures."""


class ConfigValidationError(SimulatorError):
    """Configuration is syntactically valid YAML but invalid game data."""


class IllegalActionError(SimulatorError):
    """An action cannot be performed in the current state or phase."""


class InvalidTargetError(SimulatorError):
    """The selected target does not satisfy an action's requirements."""


class InsufficientBloodError(SimulatorError):
    """A blood cost cannot be paid."""


class InvalidStateTransitionError(SimulatorError):
    """A rule attempted an invalid state transition."""


class ScenarioDefinitionError(SimulatorError):
    """A requested scenario or strategy is unknown."""
