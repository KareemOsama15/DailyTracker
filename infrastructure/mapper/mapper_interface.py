from typing import Any, Dict
from abc import ABC, abstractmethod


class MapperInterface(ABC):
    """MapperInterface class for the application"""

    @abstractmethod
    def to_model(self, row: Dict[str, Any]) -> Any:
        """Convert a dictionary to a model"""
        raise NotImplementedError

    @abstractmethod
    def to_create(self, instance: Any) -> Dict[str, Any]:
        """Convert a model to a dictionary for creation"""
        raise NotImplementedError

    @abstractmethod
    def to_update(self, instance: Any) -> Dict[str, Any]:
        """Convert a model to a dictionary for update"""
        raise NotImplementedError
