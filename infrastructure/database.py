import sqlite3
from typing import Any, List, Dict


class Database:
    """Database class for the application"""

    def __init__(self, db_path: str, table_name: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.table_name = table_name

    def create_record(self, data: Dict[str, Any]) -> int:
        """Create a new record for a table in the database"""
        self.cursor.execute(
            f"INSERT INTO {self.table_name} ({', '.join(data.keys())}) VALUES ({', '.join(data.values())})"
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_record(self, id: int) -> Dict[str, Any] | None:
        """Get a record from a table in the database"""
        self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id = {id}")
        return self.cursor.fetchone()

    def list_records(self) -> List[Dict[str, Any]] | None:
        """List all records from a table in the database"""
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.cursor.fetchall()

    def update_record(self, id: int, data: Dict[str, Any]) -> None:
        """Update a record in a table in the database"""
        self.cursor.execute(
            f"UPDATE {self.table_name} SET {', '.join([f'{key} = {value}' for key, value in data.items()])} WHERE id = {id}"
        )
        self.conn.commit()

    def delete_record(self, id: int) -> None:
        """Delete a record from a table in the database"""
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = {id}")
        self.conn.commit()

    def close(self) -> None:
        """Close the connection to the database"""
        self.conn.close()
