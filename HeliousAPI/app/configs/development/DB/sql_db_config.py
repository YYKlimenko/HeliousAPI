"""SQL Database Config to connect with development database"""


class SQLiteDevConfig:
    """Class for creating config types to connect to DB through SQLAlchemy."""

    DIALECT_DB: str = 'sqlite'
    DB_URL: str = 'sqlite3.db'

    def get_url_db(self) -> str:
        """Get url for connecting to DB."""
        return f'{self.DIALECT_DB:///{self.DB_URL}}'
