import sqlite3
from typing import Any


class Database:
    """Database class for the application"""

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
