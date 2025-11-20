"""Design patterns module."""
from .singleton import *  # noqa: F401, F403
from .factory import *  # noqa: F401, F403
from .observer import *  # noqa: F401, F403
from .strategy import *  # noqa: F401, F403

__all__ = [
    'Singleton',
    'LifeFormFactory',
    'EvolutionLogger',
    'EvolutionStrategyFactory'
]
