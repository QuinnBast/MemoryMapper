import os


class Config:
    port = os.getenv("MM_PORT", 8000)
    database_mode = os.getenv("MM_DATABASE_MODE", "Database")
    db_string = os.getenv("MM_DBAPI_STRING", "sqlite+pysqlite:///:memory:")
    env = os.getenv("MM_ENV", "dev")

    def __init__(self):
        config = {
            "port": self.port,
            "database_mode": self.database_mode,
            "db_string": self.db_string,
            "env": self.env,
        }
        print(config)
