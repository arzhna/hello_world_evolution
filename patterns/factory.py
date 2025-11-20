"""Factory pattern for creating life forms."""
from abc import ABC, abstractmethod
from typing import Type, Dict, Any
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from core.life_forms import LifeForm, Fish, Amphibian, Reptile, Dinosaur


class LifeFormFactory(ABC):
    """Abstract factory for creating life forms."""

    @abstractmethod
    def create_life_form(self, species_type: str, **kwargs) -> LifeForm:
        """Create a life form of specified type."""
        pass


class ConcreteLifeFormFactory(LifeFormFactory):
    """Concrete factory implementation with registry."""

    def __init__(self):
        self._registry: Dict[str, Type[LifeForm]] = {
            'fish': Fish,
            'amphibian': Amphibian,
            'reptile': Reptile,
            'dinosaur': Dinosaur,
        }

    def register(self, species_type: str, life_form_class: Type[LifeForm]) -> None:
        """Register a new life form type."""
        self._registry[species_type.lower()] = life_form_class

    def create_life_form(self, species_type: str, **kwargs) -> LifeForm:
        """Create a life form using the registry."""
        life_form_class = self._registry.get(species_type.lower())
        if life_form_class is None:
            raise ValueError(f"Unknown species type: {species_type}")

        # Handle different constructor signatures
        if species_type.lower() == 'fish':
            return life_form_class()
        else:
            return life_form_class(**kwargs)


class LifeFormBuilder:
    """Builder pattern for complex life form construction."""

    def __init__(self):
        self._complexity = 1
        self._message = ""
        self._type = "fish"

    def with_complexity(self, complexity: int) -> 'LifeFormBuilder':
        """Set complexity (fluent interface)."""
        self._complexity = complexity
        return self

    def with_message(self, message: str) -> 'LifeFormBuilder':
        """Set message fragment (fluent interface)."""
        self._message = message
        return self

    def of_type(self, life_form_type: str) -> 'LifeFormBuilder':
        """Set life form type (fluent interface)."""
        self._type = life_form_type
        return self

    def build(self) -> LifeForm:
        """Build the life form."""
        factory = ConcreteLifeFormFactory()
        if self._type.lower() == 'fish':
            return factory.create_life_form(self._type)
        else:
            return factory.create_life_form(
                self._type,
                inherited_complexity=self._complexity,
                inherited_message=self._message
            )
