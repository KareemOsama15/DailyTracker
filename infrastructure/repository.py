from infrastructure.database import Database
from typing import Any


class Repository:
    """Repository class for the application.

    Args:
        model: The model class to use for the repository
        db_path: The path to the database file
    """

    def __init__(self, model: Any, db_path="app.db"):
        self.database = Database(db_path)
        self.model = model

    def create(self, data: Any):
        """Create a new record in the database"""
        pass

    def get(self, id: int):
        """Get a record from the database"""
        pass

    def list(self):
        """List all records from the database"""
        pass

    def update(self, id: int, data: Any):
        """Update a record in the database"""
        pass

    def delete(self, id: int):
        """Delete a record from the database"""
        pass
