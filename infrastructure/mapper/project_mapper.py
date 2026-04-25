from typing import Any, Dict
from domain.models.project import Project
from infrastructure.mapper.mapper_interface import MapperInterface


class ProjectMapper(MapperInterface):
    """ProjectMapper class for the application"""

    def to_model(self, row: Dict[str, Any]) -> Project:
        """Convert a dictionary to a Project model"""
        return Project(
            id=row.get("id"),
            name=row.get("name"),
            description=row.get("description"),
            created_at=row.get("created_at"),
            updated_at=row.get("updated_at"),
        )

    def to_create(self, instance: Project) -> Dict[str, Any]:
        """Convert a Project model to a dictionary for creation"""
        return {
            "name": instance.name,
            "description": instance.description or None,
        }

    def to_update(self, instance: Project) -> Dict[str, Any]:
        """Convert a Project model to a dictionary for update"""
        return {
            "name": instance.name,
            "description": instance.description or None,
        }
