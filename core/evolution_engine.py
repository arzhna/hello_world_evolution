"""Evolution engine with observer pattern and strategy pattern."""
from typing import List, Protocol, Any

from .life_forms import LifeForm, Fish, MessageBearer
from .stages import EvolutionStage, EvolutionPipeline


class EvolutionObserver(Protocol):
    """Observer protocol for evolution events."""

    def on_evolution_step(
        self,
        organism: Any,
        stage: EvolutionStage
    ) -> None:
        """Called when evolution step occurs."""
        ...


class EvolutionStrategy(Protocol):
    """Strategy protocol for evolution algorithms."""

    def evolve(self, organism: LifeForm) -> Any:
        """Execute evolution strategy."""
        ...


class LinearEvolutionStrategy:
    """Simple linear evolution strategy."""

    def evolve(self, organism: LifeForm) -> Any:
        """Evolve through linear progression."""
        return organism.evolve()


class AcceleratedEvolutionStrategy:
    """Accelerated evolution with multiple iterations."""

    def __init__(self, acceleration_factor: int = 2):
        self.acceleration_factor = acceleration_factor

    def evolve(self, organism: LifeForm) -> Any:
        """Evolve with acceleration."""
        result = organism
        for _ in range(self.acceleration_factor):
            if hasattr(result, 'evolve'):
                result = result.evolve()
            else:
                break
        return result


class EvolutionEngine:
    """Main evolution engine orchestrating the entire process."""

    def __init__(
        self,
        strategy: EvolutionStrategy = None,
        debug: bool = False
    ):
        self._observers: List[EvolutionObserver] = []
        self._strategy = strategy or LinearEvolutionStrategy()
        self._pipeline = EvolutionPipeline()
        self._debug = debug

    def attach_observer(self, observer: EvolutionObserver) -> None:
        """Attach an observer to evolution events."""
        self._observers.append(observer)

    def detach_observer(self, observer: EvolutionObserver) -> None:
        """Detach an observer."""
        self._observers.remove(observer)

    def notify_observers(
        self,
        organism: Any,
        stage: EvolutionStage
    ) -> None:
        """Notify all observers of evolution event."""
        for observer in self._observers:
            observer.on_evolution_step(organism, stage)

    def set_strategy(self, strategy: EvolutionStrategy) -> None:
        """Set evolution strategy."""
        self._strategy = strategy

    def run_evolution(self, initial_organism: LifeForm = None) -> MessageBearer:
        """Run the complete evolution simulation."""
        if initial_organism is None:
            initial_organism = Fish()

        current = initial_organism
        stages = [
            EvolutionStage.AQUATIC,
            EvolutionStage.AMPHIBIOUS,
            EvolutionStage.TERRESTRIAL,
            EvolutionStage.APEX_PREDATOR,
            EvolutionStage.TRANSCENDENT
        ]

        for stage in stages:
            self.notify_observers(current, stage)

            if self._debug:
                organism_type = type(current).__name__
                complexity = getattr(current, 'complexity', 'N/A')
                message = getattr(
                    current,
                    '_message_fragment',
                    current.reveal() if hasattr(current, 'reveal') else 'N/A'
                )
                complexity_str = (
                    str(complexity) if complexity != 'N/A' else 'N/A'
                )
                print(
                    f"[EVOLUTION] Stage: {stage.name:20s} | "
                    f"Organism: {organism_type:15s} | "
                    f"Complexity: {complexity_str:>4s} | "
                    f"Message: '{message}'"
                )

            if hasattr(current, 'evolve'):
                next_form = current.evolve()

                if self._debug and next_form != current:
                    next_type = type(next_form).__name__
                    next_message = getattr(
                        next_form,
                        '_message_fragment',
                        (next_form.reveal()
                         if hasattr(next_form, 'reveal')
                         else 'N/A')
                    )
                    print(
                        f"            → Evolved to: {next_type:15s} | "
                        f"Message: '{next_message}'"
                    )

                current = next_form
            else:
                break

        return current

    def build_pipeline(self) -> EvolutionPipeline:
        """Build evolution pipeline with functional composition."""
        evolve_stage = lambda org: (  # noqa: E731
            org.evolve() if hasattr(org, 'evolve') else org
        )
        return (
            self._pipeline
            .add_stage(evolve_stage)
            .add_stage(evolve_stage)
            .add_stage(evolve_stage)
            .add_stage(evolve_stage)
        )
