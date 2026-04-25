from dataclasses import dataclass
from typing import Optional, ClassVar
from datetime import datetime


@dataclass
class Project:
    """Project domain model"""

    __table_name__: ClassVar[str] = "projects"

    id: int
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
