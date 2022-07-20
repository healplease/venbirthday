import os


class Config():
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    SERVER_NAME = os.environ.get("FLASK_SERVER_NAME")

    MONGODB_USERNAME = os.environ.get("FLASK_MONGODB_USER")
    MONGODB_PASSWORD = os.environ.get("FLASK_MONGODB_PASSWORD")
    MONGODB_HOST = os.environ.get("FLASK_MONGODB_HOST")
    MONGODB_PORT = os.environ.get("FLASK_MONGODB_PORT")
    MONGODB_DB = "venjendiyfull"
    MONGODB_PROTOCOL = "mongodb+srv"
    MONGODB_ARGUMENTS = {"retryWrites": "true", "w": "majority"}

    ADMIN_USERNAME = os.environ.get("FLASK_VENJENDIYFULL_USERNAME")
    ADMIN_PASSWORD_HASH = os.environ.get("FLASK_VENJENDIYFULL_PASSWORD_HASH")


class LocalConfig(Config):
    DEBUG = True


class HerokuConfig():
    pass


class DevelopmentConfig(HerokuConfig, Config):
    MONGODB_DB = "venjendiyfull_dev"


class ProductionConfig(HerokuConfig, Config):
    MONGODB_DB = "venjendiyfull_prod"


environment_configs = {
    "local": LocalConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
