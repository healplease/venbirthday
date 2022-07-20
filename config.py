import os


class Config():
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    SERVER_NAME = os.environ.get("FLASK_SERVER_NAME")


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
