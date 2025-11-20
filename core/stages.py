"""Evolution stage definitions with functional composition."""
from enum import Enum, auto
from functools import reduce
from typing import Callable, List


class EvolutionStage(Enum):
    """Enumeration of evolution stages."""
    PRIMORDIAL_SOUP = auto()
    AQUATIC = auto()
    AMPHIBIOUS = auto()
    TERRESTRIAL = auto()
    APEX_PREDATOR = auto()
    TRANSCENDENT = auto()


class StageTransition:
    """Represents a transition between evolution stages."""

    def __init__(
        self,
        from_stage: EvolutionStage,
        to_stage: EvolutionStage,
        transformation: Callable
    ):
        self.from_stage = from_stage
        self.to_stage = to_stage
        self.transformation = transformation

    def execute(self, organism):
        """Execute the transformation."""
        return self.transformation(organism)


class EvolutionPipeline:
    """Functional pipeline for evolution stages."""

    def __init__(self):
        self._stages: List[Callable] = []

    def add_stage(self, stage_func: Callable) -> 'EvolutionPipeline':
        """Add a stage to the pipeline (fluent interface)."""
        self._stages.append(stage_func)
        return self

    def execute(self, initial_organism):
        """Execute the full pipeline using reduce."""
        return reduce(
            lambda org, stage: stage(org),
            self._stages,
            initial_organism
        )


def compose(*functions: Callable) -> Callable:
    """Compose functions from right to left."""
    def inner(arg):
        return reduce(
            lambda result, func: func(result),
            reversed(functions),
            arg
        )
    return inner


def curry(func: Callable) -> Callable:
    """Simple currying implementation."""
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(
            *(args + more_args),
            **(kwargs | more_kwargs)
        )
    return curried
