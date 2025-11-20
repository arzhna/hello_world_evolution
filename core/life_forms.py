"""Complex life form hierarchy with multiple inheritance and mixins."""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Callable, Any

T = TypeVar('T')


class DNASequence(Generic[T]):
    """Generic DNA sequence container with monad-like operations."""

    def __init__(self, value: T):
        self._value = value

    def bind(self, func: Callable[[T], 'DNASequence']) -> 'DNASequence':
        """Monadic bind operation."""
        return func(self._value)

    def fmap(self, func: Callable[[T], Any]) -> 'DNASequence':
        """Functor map operation."""
        return DNASequence(func(self._value))

    def get(self) -> T:
        return self._value


class Organism(ABC):
    """Abstract base organism."""

    @abstractmethod
    def evolve(self) -> 'Organism':
        """Evolve to next stage."""
        pass

    @abstractmethod
    def get_genetic_code(self) -> DNASequence:
        """Get genetic information."""
        pass


class AquaticMixin:
    """Mixin for aquatic capabilities."""

    def swim(self) -> str:
        return "swimming in primordial waters"

    def breathe_water(self) -> bool:
        return True


class TerrestrialMixin:
    """Mixin for terrestrial capabilities."""

    def walk(self) -> str:
        return "walking on ancient earth"

    def breathe_air(self) -> bool:
        return True


class CarnivorousMixin:
    """Mixin for carnivorous behavior."""

    def hunt(self) -> str:
        return "hunting for meaning"


class MessageCarrierMixin:
    """Mixin for carrying message fragments."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._message_fragment = ""

    def carry_message(self, fragment: str):
        self._message_fragment = fragment

    def get_message_fragment(self) -> str:
        return self._message_fragment


class LifeForm(Organism, MessageCarrierMixin, ABC):
    """Abstract life form base class."""

    def __init__(self, complexity: int = 1):
        super().__init__()
        self.complexity = complexity
        self._dna = DNASequence(complexity)

    def get_genetic_code(self) -> DNASequence:
        return self._dna

    def mutate(self, mutation_factor: int) -> None:
        """Apply mutation to increase complexity."""
        self.complexity = self._dna.fmap(lambda x: x * mutation_factor).get()
        self._dna = DNASequence(self.complexity)


class Fish(LifeForm, AquaticMixin):
    """Primordial fish - the beginning of our journey."""

    def __init__(self):
        super().__init__(complexity=1)
        self.carry_message("H")

    def evolve(self) -> 'Amphibian':
        """Crawl onto land and become amphibian."""
        self.mutate(2)
        return Amphibian(
            inherited_complexity=self.complexity,
            inherited_message=self.get_message_fragment()
        )


class Amphibian(LifeForm, AquaticMixin, TerrestrialMixin):
    """Amphibian - transitional form."""

    def __init__(
        self,
        inherited_complexity: int = 2,
        inherited_message: str = ""
    ):
        super().__init__(complexity=inherited_complexity)
        self.carry_message(inherited_message + "ello")

    def evolve(self) -> 'Reptile':
        """Fully adapt to land and become reptile."""
        self.mutate(3)
        return Reptile(
            inherited_complexity=self.complexity,
            inherited_message=self.get_message_fragment()
        )


class Reptile(LifeForm, TerrestrialMixin):
    """Reptile - masters of the land."""

    def __init__(
        self,
        inherited_complexity: int = 6,
        inherited_message: str = ""
    ):
        super().__init__(complexity=inherited_complexity)
        self.carry_message(inherited_message + " ")

    def evolve(self) -> 'Dinosaur':
        """Grow to magnificent proportions and become dinosaur."""
        self.mutate(4)
        return Dinosaur(
            inherited_complexity=self.complexity,
            inherited_message=self.get_message_fragment()
        )


class Dinosaur(LifeForm, TerrestrialMixin, CarnivorousMixin):
    """Dinosaur - apex of evolution (in our case)."""

    def __init__(
        self,
        inherited_complexity: int = 24,
        inherited_message: str = ""
    ):
        super().__init__(complexity=inherited_complexity)
        self.carry_message(inherited_message + "World")

    def evolve(self) -> 'MessageBearer':
        """Transcend physical form and become pure message."""
        self.mutate(5)
        return MessageBearer(
            final_message=self.get_message_fragment()
        )

    def roar(self) -> str:
        """Mighty roar that echoes through time."""
        return "ROAR! (carrying message: {})".format(
            self._message_fragment
        )


class MessageBearer:
    """
    Final form - pure message carrier transcending biological evolution.
    """

    def __init__(self, final_message: str):
        self._final_message = final_message

    def reveal(self) -> str:
        """Reveal the message that has been carried through eons."""
        return self._final_message

    def __str__(self) -> str:
        return self.reveal()
