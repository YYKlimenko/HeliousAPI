"""Base Config class to inherent in another classes"""
from abc import ABC
from typing import Protocol


class BaseSQLConfigProtocol(Protocol):
    """The protocol to implement in SQLConfig classes"""
    def get_url_db(self) -> str: ...


class BaseSQLConfig(ABC):
    """Abstract class to keep data for connecting with SQL DB"""
    DIALECT_DB: str
    DRIVER_DB: str
    LOGIN_DB: str
    PASSWORD_DB: str
    HOST_DB: str
    PORT_DB: int
    DB_NAME: str

    def get_url_db(self) -> str:
        """Get url for connecting to DB."""
        return f'{self.LOGIN_DB}:{self.PASSWORD_DB}@{self.HOST_DB}:{self.PORT_DB}/{self.DB_NAME}'
