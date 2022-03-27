from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import StaticPool

Base = declarative_base()


class DatabaseProvider:

    def __init__(self, config):
        self.engine = create_engine(
            config.db_string,
            echo=True,
            future=True,
            poolclass=StaticPool,
            connect_args={"check_same_thread": False}
        )
        self.sessionBuilder = sessionmaker(bind=self.engine)
        print("Connected to database: " + config.db_string)

    def get_session(self):
        return self.sessionBuilder()

    def create_tables(self):
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        print("Tables created.")
