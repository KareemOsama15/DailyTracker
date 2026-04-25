from infrastructure.database import Database
from typing import Any, List, Dict, Type, Generic, TypeVar
from infrastructure.mapper.mapper_interface import MapperInterface


T = TypeVar("T", bound=Any)

class BaseRepository(Generic[T]):
    """Repository class for the application.

    Args:
        model: The model class to use for the repository
    """

    def __init__(self, model: Type[T], mapper: MapperInterface):
        self.table_name = self.__resolve_table_name(model)
        self.database = Database(table_name=self.table_name)
        self.mapper = mapper

    def create(self, instance: T) -> T:
        """Create a new record in the database"""
        data = self.mapper.to_create(instance=instance)
        id = self.database.create_record(data=data)
        if id:
            return self.mapper.to_model(id=id)
        raise ValueError(f"Failed to create record for {self.model.__name__}")

    def get(self, id: int) -> T | None:
        """Get a record from the database"""
        row = self.database.get_record(id=id)
        if row:
            return self.mapper.to_model(row=row)
        return None

    def list(self) -> List[T] | None:
        """List all records from the database"""
        rows = self.database.list_records()
        if rows:
            return [self.mapper.to_model(row=row) for row in rows]
        return None

    def update(self, id: int, instance: T) -> None:
        """Update a record in the database"""
        data = self.mapper.to_update(instance=instance)
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
