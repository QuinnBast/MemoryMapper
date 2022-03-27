import os


class Config:
    port = os.getenv("MM_PORT", 8000)
    database_mode = os.getenv("MM_DATABASE_MODE", "Database")
    database_type = os.getenv("MM_DATABASE_TYPE", "SQLITE")
    db_string = os.getenv("MM_DBAPI_STRING", "sqlite+pysqlite:///:memory:")