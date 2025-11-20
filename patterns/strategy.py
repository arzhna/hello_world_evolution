"""Strategy pattern for evolution algorithms."""
import sys
import os
from typing import Dict, Type

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from core.evolution_engine import (
    EvolutionStrategy,
    LinearEvolutionStrategy,
    AcceleratedEvolutionStrategy
)


class EvolutionStrategyFactory:
    """Factory for creating evolution strategies."""

    _strategies: Dict[str, Type[EvolutionStrategy]] = {
        'linear': LinearEvolutionStrategy,
        'accelerated': AcceleratedEvolutionStrategy,
    }

    @classmethod
    def create_strategy(cls, strategy_type: str, **kwargs) -> EvolutionStrategy:
        """Create an evolution strategy."""
        strategy_class = cls._strategies.get(strategy_type.lower())
        if strategy_class is None:
            raise ValueError(f"Unknown strategy type: {strategy_type}")

        if strategy_type.lower() == 'linear':
            return strategy_class()
        else:
            return strategy_class(**kwargs)

    @classmethod
    def register_strategy(cls, name: str, strategy_class: Type[EvolutionStrategy]) -> None:
        """Register a new strategy type."""
        cls._strategies[name.lower()] = strategy_class


class EvolutionContext:
    """Context for strategy pattern."""

    def __init__(self, strategy: EvolutionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: EvolutionStrategy) -> None:
        """Change strategy at runtime."""
        self._strategy = strategy

    def execute_evolution(self, organism):
        """Execute evolution using current strategy."""
        return self._strategy.evolve(organism)
