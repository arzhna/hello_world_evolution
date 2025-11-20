"""Singleton pattern implementation with metaclass."""
from typing import Any, Dict
import threading


class SingletonMeta(type):
    """Thread-safe singleton metaclass."""

    _instances: Dict[type, Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]

    @classmethod
    def clear_instances(mcs):
        """Clear all singleton instances (useful for testing/debugging)."""
        with mcs._lock:
            mcs._instances.clear()


class Singleton(metaclass=SingletonMeta):
    """Base singleton class."""
    pass


def singleton(cls):
    """Singleton decorator alternative."""
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
