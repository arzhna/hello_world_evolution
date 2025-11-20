#!/usr/bin/env python3
"""
The Ultimate Over-Engineered Hello World Program
==================================================

A masterpiece of unnecessary complexity that demonstrates:
- Object-Oriented Programming with multiple inheritance
- Design Patterns (Observer, Strategy, Factory, Singleton, Builder)
- Functional Programming (Monads, Functors, Currying, Composition)
- Metaprogramming with metaclasses
- Evolutionary algorithms
- Pipeline architecture
- Lazy evaluation
- Thread-safe singletons
- Decorator chains
- Type hints with Protocols and Generics

All to print: "Hello World"
"""

import sys
import argparse
from typing import Callable
from functools import reduce

# Import core evolution system
from core.life_forms import Fish, MessageBearer
from core.evolution_engine import EvolutionEngine, LinearEvolutionStrategy
from core.stages import EvolutionPipeline, compose

# Import design patterns
from patterns.observer import EvolutionLogger, SilentObserver
from patterns.factory import ConcreteLifeFormFactory, LifeFormBuilder
from patterns.strategy import EvolutionStrategyFactory, EvolutionContext
from patterns.singleton import SingletonMeta

# Import utilities and generators
from utils.decorators import (
    timeit, log_call, retry,
    chain_decorators, DecoratorFactory
)
from generators.message_generator import (
    MessageGenerator, MessageTransformer,
    LazyMessage, DynamicMessageClass
)

# Global debug flag
DEBUG = False


class HelloWorldOrchestrator(metaclass=SingletonMeta):
    """
    Master orchestrator that coordinates all components.
    Singleton to ensure only one instance manages the complexity.
    """

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._engine = None
            self._generator = MessageGenerator()
            self._transformer = MessageTransformer()
            self._factory = ConcreteLifeFormFactory()
            self._initialized = True
            if DEBUG:
                print("[DEBUG] HelloWorldOrchestrator initialized (Singleton)")

    def set_debug(self, debug: bool) -> None:
        """Enable or disable debug mode."""
        global DEBUG
        DEBUG = debug

    def initialize_engine(self) -> EvolutionEngine:
        """Initialize the evolution engine with observers and strategy."""
        if DEBUG:
            print("[DEBUG] Initializing Evolution Engine...")

        # Create strategy using factory
        strategy = EvolutionStrategyFactory.create_strategy('linear')
        if DEBUG:
            print(f"[DEBUG] Strategy: {type(strategy).__name__}")

        # Create engine with strategy and debug flag
        engine = EvolutionEngine(strategy=strategy, debug=DEBUG)

        # Attach observers (using singleton logger)
        logger = EvolutionLogger()
        engine.attach_observer(logger)
        engine.attach_observer(SilentObserver())

        if DEBUG:
            print("[DEBUG] Observers attached: EvolutionLogger, SilentObserver")

        return engine

    def create_initial_organism(self) -> Fish:
        """Create the primordial organism using factory."""
        if DEBUG:
            print("[DEBUG] Creating initial organism: Fish")
        fish = self._factory.create_life_form('fish')
        if DEBUG:
            print(f"[DEBUG] Fish created with message: '{fish.get_message_fragment()}'")
        return fish

    def run_evolution_pipeline(self, initial_organism: Fish) -> MessageBearer:
        """Execute the complete evolution through pipeline."""
        if self._engine is None:
            self._engine = self.initialize_engine()

        if DEBUG:
            print("\n[DEBUG] Starting evolution pipeline...")
            print("=" * 60)

        # Run evolution and get final form
        final_form = self._engine.run_evolution(initial_organism)

        if DEBUG:
            print("=" * 60)
            print(f"[DEBUG] Evolution complete! Final form: {type(final_form).__name__}")

        return final_form

    def extract_message(self, message_bearer: MessageBearer) -> str:
        """Extract and process the message through transformation pipeline."""
        if DEBUG:
            print("\n[DEBUG] Extracting message from MessageBearer...")

        # Extract raw message
        raw_message = self._generator.generate(message_bearer, strategy='composed')
        if DEBUG:
            print(f"[DEBUG] Raw message: '{raw_message}'")

        # Apply transformation pipeline (identity in this case, but complex!)
        transformed = self._transformer.apply_pipeline(
            raw_message,
            self._transformer.identity
        )

        if DEBUG:
            print(f"[DEBUG] Transformed message: '{transformed}'")

        return transformed

    def create_lazy_output(self, message: str) -> LazyMessage:
        """Create a lazy-evaluated output message."""
        return LazyMessage(lambda: message)


class ComplexityWrapper:
    """
    Additional layer of indirection for maximum complexity.
    Wraps the orchestrator with functional composition.
    """

    def __init__(self):
        self._orchestrator = HelloWorldOrchestrator()

    @staticmethod
    def compose_operations(*operations: Callable) -> Callable:
        """Compose multiple operations into single function."""
        return compose(*operations)

    def pipeline_execute(self) -> str:
        """Execute through functional pipeline."""
        # Define pipeline stages
        stage1 = lambda orch: orch.create_initial_organism()  # noqa: E731
        stage2 = lambda org: (  # noqa: E731
            self._orchestrator.run_evolution_pipeline(org)
        )
        stage3 = lambda bearer: (  # noqa: E731
            self._orchestrator.extract_message(bearer)
        )
        stage4 = lambda msg: (  # noqa: E731
            self._orchestrator.create_lazy_output(msg)
        )
        stage5 = lambda lazy: lazy.force()  # noqa: E731

        # Compose and execute
        initial = self._orchestrator
        organism = stage1(initial)
        bearer = stage2(organism)
        message = stage3(bearer)
        lazy = stage4(message)
        result = stage5(lazy)

        return result


class MetaHelloWorld(type):
    """Metaclass that adds hello world capabilities to any class."""

    def __new__(mcs, name: str, bases: tuple, namespace: dict):
        """Inject hello world functionality."""

        def say_hello(self) -> str:
            """The ultimate hello world method."""
            wrapper = ComplexityWrapper()
            return wrapper.pipeline_execute()

        namespace['say_hello'] = say_hello
        return super().__new__(mcs, name, bases, namespace)


class Application(metaclass=MetaHelloWorld):
    """Main application class with metaclass-injected functionality."""

    def __init__(self):
        self._orchestrator = HelloWorldOrchestrator()
        self._execution_count = 0

    @timeit
    def execute(self) -> str:
        """Execute the hello world program with decorators."""
        self._execution_count += 1
        return self.say_hello()

    def run(self) -> None:
        """Main entry point with error handling."""
        try:
            # Execute through all the complexity
            result = self.execute()

            # Final output
            print(result)

        except Exception as e:
            print(f"Error in evolution: {e}", file=sys.stderr)
            raise


class HigherOrderHelloWorld:
    """
    Even more abstraction using higher-order functions.
    Because why not?
    """

    @staticmethod
    def create_hello_world_factory() -> Callable[[], str]:
        """Factory that creates hello world generators."""
        def factory() -> str:
            app = Application()
            return app.execute()
        return factory

    @staticmethod
    def apply_with_context(func: Callable[[], str]) -> str:
        """Apply function with context management."""
        # Simulate context management
        setup = True
        try:
            result = func()
            return result
        finally:
            cleanup = True

    @classmethod
    def run(cls) -> str:
        """Run with higher-order function composition."""
        factory = cls.create_hello_world_factory()
        return cls.apply_with_context(factory)


def create_evolution_pipeline() -> EvolutionPipeline:
    """
    Create a functional pipeline for evolution (alternative approach).
    """
    pipeline = EvolutionPipeline()

    # Helper functions for pipeline stages
    init_stage = lambda org: (  # noqa: E731
        org if isinstance(org, Fish) else Fish()
    )
    evolve_stage = lambda org: (  # noqa: E731
        org.evolve() if hasattr(org, 'evolve') else org
    )

    # Add stages to pipeline
    return (
        pipeline
        .add_stage(init_stage)
        .add_stage(evolve_stage)
        .add_stage(evolve_stage)
        .add_stage(evolve_stage)
        .add_stage(evolve_stage)
    )


@retry(max_attempts=3)
@log_call(prefix="MAIN: ")
def alternative_main() -> None:
    """Alternative main using direct pipeline execution."""
    pipeline = create_evolution_pipeline()
    initial = Fish()
    result = pipeline.execute(initial)

    generator = MessageGenerator()
    message = generator.generate(result, strategy='composed')
    print(message)


def functional_approach() -> str:
    """Pure functional approach to hello world."""
    # Create computation chain
    operations = [
        lambda: Fish(),
        lambda fish: fish.evolve(),
        lambda amp: amp.evolve(),
        lambda rep: rep.evolve(),
        lambda dino: dino.evolve(),
        lambda bearer: bearer.reveal()
    ]

    # Execute chain
    result = reduce(lambda acc, op: op() if acc is None else op(acc),
                   operations, None)
    return result


def builder_approach() -> str:
    """Using builder pattern to construct and evolve."""
    # Build initial organism with builder
    builder = LifeFormBuilder()
    organism = builder.of_type('fish').build()

    # Evolve through chain
    evolved = organism.evolve().evolve().evolve().evolve()

    return evolved.reveal()


def metaclass_approach() -> str:
    """Using metaclass-generated message."""
    instance = DynamicMessageClass()
    return instance.compose()


def main(debug: bool = False) -> None:
    """
    Main entry point that demonstrates the ultimate over-engineered solution.

    Args:
        debug: Enable debug output to see evolution process

    We have multiple approaches available:
    1. Object-oriented with design patterns (Application class)
    2. Higher-order functions (HigherOrderHelloWorld)
    3. Pipeline-based (alternative_main)
    4. Pure functional (functional_approach)
    5. Builder pattern (builder_approach)
    6. Metaclass generation (metaclass_approach)

    We'll use approach #1 as it demonstrates the most complexity.
    """
    global DEBUG
    DEBUG = debug

    # Clear singleton instances to ensure fresh state with DEBUG flag
    SingletonMeta.clear_instances()

    if DEBUG:
        print("=" * 60)
        print("HELLO WORLD EVOLUTION - DEBUG MODE")
        print("=" * 60)

    # The most complex path through all design patterns
    app = Application()
    app.run()

    if DEBUG:
        print("\n" + "=" * 60)
        print("EVOLUTION COMPLETE")
        print("=" * 60)

    # Uncomment to see alternative approaches:
    # print(HigherOrderHelloWorld.run())
    # alternative_main()
    # print(functional_approach())
    # print(builder_approach())
    # print(metaclass_approach())


if __name__ == "__main__":
    """
    Entry point when run as script.
    After all this complexity, we finally print "Hello World"
    """
    parser = argparse.ArgumentParser(
        description="The Ultimate Over-Engineered Hello World Program",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py              # Normal output
  python main.py --debug      # Debug mode with evolution details
        """
    )
    parser.add_argument(
        '--debug', '-d',
        action='store_true',
        help='Enable debug mode to see the evolution process'
    )

    args = parser.parse_args()
    main(debug=args.debug)
