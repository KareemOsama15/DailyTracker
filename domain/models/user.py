from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class User:
    """User domain model"""

    id: int
    username: str
    password: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
