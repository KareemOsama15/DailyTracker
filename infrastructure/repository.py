from infrastructure.database import Database


class Repository:
    """Repository class for the application"""

    def __init__(self, db_path="app.db"):
        self.database = Database(db_path)
