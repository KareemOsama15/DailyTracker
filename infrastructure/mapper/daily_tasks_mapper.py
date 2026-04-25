from typing import Any, Dict
from domain.models.daily_tasks import DailyTasks
from infrastructure.mapper.mapper_interface import MapperInterface


class DailyTasksMapper(MapperInterface):
    """DailyTasksMapper class for the application"""

    def to_model(self, row: Dict[str, Any]) -> DailyTasks:
        """Convert a dictionary to a DailyTasks model"""
        return DailyTasks(
            id=row.get("id"),
            user_id=row.get("user_id"),
            project_id=row.get("project_id"),
            date=row.get("date"),
            task=row.get("task"),
            time_spent=row.get("time_spent"),
            added_to_jira=row.get("added_to_jira"),
            created_at=row.get("created_at"),
            updated_at=row.get("updated_at"),
        )

    def to_create(self, instance: DailyTasks) -> Dict[str, Any]:
        """Convert a DailyTasks model to a dictionary for creation"""
        return {
            "user_id": instance.user_id,
            "project_id": instance.project_id,
            "date": instance.date,
            "task": instance.task,
            "time_spent": instance.time_spent,
            "added_to_jira": instance.added_to_jira,
        }

    def to_update(self, instance: DailyTasks) -> Dict[str, Any]:
        """Convert a DailyTasks model to a dictionary for update"""
        return {
            "user_id": instance.user_id,
            "project_id": instance.project_id,
            "date": instance.date,
            "task": instance.task,
            "time_spent": instance.time_spent,
            "added_to_jira": instance.added_to_jira,
        }
