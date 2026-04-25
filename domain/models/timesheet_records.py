from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class TimeSheetRecord:
    """TimeSheetRecord domain model"""

    id: int
    user_id: int
    project_id: int
    date: str
    start_time: float
    end_time: float
    actual_duration: float
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
