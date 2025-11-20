"""Dynamic message generation using metaclasses and metaprogramming."""
from typing import Any, Dict, Callable
import sys


class MessageMeta(type):
    """Metaclass for dynamic message generation."""

    def __new__(mcs, name: str, bases: tuple, namespace: Dict[str, Any]):
        """Create new class with dynamically generated methods."""

        def generate_message_method(message: str) -> Callable:
            """Generate a method that returns a specific message."""
            def method(self) -> str:
                return message
            return method

        # Add dynamic methods for message parts
        namespace['get_greeting'] = generate_message_method('Hello')
        namespace['get_target'] = generate_message_method('World')
        namespace['get_separator'] = generate_message_method(' ')

        # Add composition method
        def compose_message(self) -> str:
            """Compose the full message."""
            return self.get_greeting() + self.get_separator() + self.get_target()

        namespace['compose'] = compose_message

        return super().__new__(mcs, name, bases, namespace)


class DynamicMessageClass(metaclass=MessageMeta):
    """Dynamically generated message class."""
    pass


def create_message_class(class_name: str = "RuntimeMessage") -> type:
    """Create a message class at runtime."""

    def __init__(self, prefix: str = "", suffix: str = ""):
        self._prefix = prefix
        self._suffix = suffix

    def render(self) -> str:
        """Render the message."""
        core_message = "Hello World"
        return f"{self._prefix}{core_message}{self._suffix}".strip()

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return f"<{class_name}: {self.render()}>"

    # Dynamically create class with methods
    attrs = {
        '__init__': __init__,
        'render': render,
        '__str__': __str__,
        '__repr__': __repr__,
    }

    return type(class_name, (), attrs)


class MessageGenerator:
    """Complex message generator with multiple generation strategies."""

    def __init__(self):
        self._strategies = {
            'simple': self._simple_generation,
            'dynamic': self._dynamic_generation,
            'meta': self._meta_generation,
            'composed': self._composed_generation,
        }

    def _simple_generation(self, source: Any) -> str:
        """Simple string conversion."""
        return str(source)

    def _dynamic_generation(self, source: Any) -> str:
        """Dynamic class generation."""
        MessageClass = create_message_class("DynamicHelloWorld")
        instance = MessageClass()
        return instance.render()

    def _meta_generation(self, source: Any) -> str:
        """Metaclass-based generation."""
        instance = DynamicMessageClass()
        return instance.compose()

    def _composed_generation(self, source: Any) -> str:
        """Composed generation from source."""
        if hasattr(source, 'reveal'):
            return source.reveal()
        return str(source)

    def generate(self, source: Any, strategy: str = 'composed') -> str:
        """Generate message using specified strategy."""
        generation_func = self._strategies.get(strategy, self._simple_generation)
        return generation_func(source)


class MessageTransformer:
    """Transforms messages through various operations."""

    @staticmethod
    def identity(message: str) -> str:
        """Identity transformation."""
        return message

    @staticmethod
    def uppercase(message: str) -> str:
        """Convert to uppercase."""
        return message.upper()

    @staticmethod
    def lowercase(message: str) -> str:
        """Convert to lowercase."""
        return message.lower()

    @staticmethod
    def reverse(message: str) -> str:
        """Reverse the message."""
        return message[::-1]

    def apply_pipeline(self, message: str, *transformations: Callable[[str], str]) -> str:
        """Apply a pipeline of transformations."""
        result = message
        for transform in transformations:
            result = transform(result)
        return result


def message_property(func: Callable) -> property:
    """Decorator to create a message property."""
    return property(lambda self: func(self))


class LazyMessage:
    """Lazy evaluation of message."""

    def __init__(self, generator: Callable[[], str]):
        self._generator = generator
        self._cached_value = None

    def __str__(self) -> str:
        if self._cached_value is None:
            self._cached_value = self._generator()
        return self._cached_value

    def force(self) -> str:
        """Force evaluation."""
        return str(self)
