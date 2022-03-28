from config import Config
from db.databaseProvider import DatabaseProvider
from dependencies.cors import CORS

config = Config()
databaseProvider = DatabaseProvider(config)
cors = CORS(config)
