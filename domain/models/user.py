from dataclasses import dataclass
from typing import Optional, ClassVar
from datetime import datetime


@dataclass
class User:
    """User domain model"""

    __table_name__: ClassVar[str] = "users"

    id: int
    username: str
    password: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
