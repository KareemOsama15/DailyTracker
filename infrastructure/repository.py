from infrastructure.database import Database
from typing import Any, List, Dict


class Repository:
    """Repository class for the application.

    Args:
        model: The model class to use for the repository
        db_path: The path to the database file
    """

    def __init__(self, model: Any, db_path="app.db"):
        self.table_name = self.__resolve_table_name(model)
        self.database = Database(db_path, self.table_name)

    def create(self, data: Dict[str, Any]) -> None:
        """Create a new record in the database"""
        return self.database.create_record(data=data)

    def get(self, id: int) -> Dict[str, Any] | None:
        """Get a record from the database"""
        return self.database.get_record(id=id)

    def list(self) -> List[Dict[str, Any]] | None:
        """List all records from the database"""
        return self.database.list_records()

    def update(self, id: int, data: Dict[str, Any]) -> None:
        """Update a record in the database"""
        self.database.update_record(id=id, data=data)

    def delete(self, id: int) -> None:
        """Delete a record from the database"""
        self.database.delete_record(id=id)

    def __resolve_table_name(self, model: Any) -> str:
        """Resolve the table name for the model"""
        if hasattr(model, "__table_name__"):
            return model.__table_name__
        else:
            return f"{model.__name__.lower()}s"
