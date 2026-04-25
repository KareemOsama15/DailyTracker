from typing import Any, Dict
from domain.models.timesheet_records import TimeSheetRecord
from infrastructure.mapper.mapper_interface import MapperInterface


class TimeSheetRecordsMapper(MapperInterface):

    def to_model(self, row: Dict[str, Any]) -> TimeSheetRecord:
        """Convert a dictionary to a TimeSheetRecord model"""
        return TimeSheetRecord(
            id=row.get("id"),
            user_id=row.get("user_id"),
            project_id=row.get("project_id"),
            date=row.get("date"),
            start_time=row.get("start_time"),
            end_time=row.get("end_time"),
            actual_duration=row.get("actual_duration"),
            created_at=row.get("created_at"),
            updated_at=row.get("updated_at"),
        )

    def to_create(self, instance: TimeSheetRecord) -> Dict[str, Any]:
        """Convert a TimeSheetRecord model to a dictionary for creation"""
        return {
            "user_id": instance.user_id,
            "project_id": instance.project_id,
            "date": instance.date,
            "start_time": instance.start_time,
            "end_time": instance.end_time,
            "actual_duration": instance.actual_duration,
        }

    def to_update(self, instance: TimeSheetRecord) -> Dict[str, Any]:
        """Convert a TimeSheetRecord model to a dictionary for update"""
        return {
            "user_id": instance.user_id,
            "project_id": instance.project_id,
            "date": instance.date,
            "start_time": instance.start_time,
            "end_time": instance.end_time,
            "actual_duration": instance.actual_duration,
        }
