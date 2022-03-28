from config import Config


class CORS:
    def __init__(self, config: Config):
        if config.env == "dev":
            self.origins = [
                "http://localhost",
                "http://localhost:8080",
                "http://localhost:8000",
            ]
        else:
            self.origins = []
