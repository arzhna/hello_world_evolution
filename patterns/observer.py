"""Observer pattern for evolution monitoring."""
import os
import sys
from typing import Any

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from core.stages import EvolutionStage  # noqa: E402
from .singleton import Singleton  # noqa: E402


class EvolutionLogger(Singleton):
    """Singleton observer that logs evolution events."""

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._log_entries = []
            self._initialized = True

    def on_evolution_step(
        self,
        organism: Any,
        stage: EvolutionStage
    ) -> None:
        """Log evolution step."""
        entry = (
            f"Evolution stage: {stage.name} - "
            f"Organism: {type(organism).__name__}"
        )
        self._log_entries.append(entry)

    def get_logs(self) -> list:
        """Retrieve all log entries."""
        return self._log_entries.copy()

    def clear_logs(self) -> None:
        """Clear all log entries."""
        self._log_entries.clear()


class SilentObserver:
    """Observer that does nothing (null object pattern)."""

    def on_evolution_step(
        self,
        organism: Any,
        stage: EvolutionStage
    ) -> None:
        """Silently observe without action."""
        pass
