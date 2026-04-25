from typing import Any, Dict
from domain.models.user import User
from infrastructure.mapper.mapper_interface import MapperInterface


class UserMapper(MapperInterface):
    """UserMapper class for the application"""

    def to_model(self, row: Dict[str, Any]) -> User:
        """Convert a dictionary to a User model"""
        return User(
            id=row.get("id"),
            username=row.get("username"),
            password=row.get("password"),
            created_at=row.get("created_at"),
            updated_at=row.get("updated_at"),
        )

    def to_create(self, instance: User) -> Dict[str, Any]:
        """Convert a User model to a dictionary for creation"""
        return {
            "username": instance.username,
            "password": instance.password,
        }

    def to_update(self, instance: User) -> Dict[str, Any]:
        """Convert a User model to a dictionary for update"""
        return {
            "username": instance.username,
            "password": instance.password,
        }
