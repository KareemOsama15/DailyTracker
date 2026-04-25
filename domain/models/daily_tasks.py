from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class DailyTasks:
    """DailyTasks domain model"""

    id: int
    user_id: int
    project_id: int
    date: str
    task: str
    time_spent: float
    added_to_jira: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
