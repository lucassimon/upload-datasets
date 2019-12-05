# -*- coding: utf-8 -*-
# Python
from datetime import timedelta
from os import getenv
import os


class Config:
    SECRET_KEY = getenv("SECRET_KEY") or "hard to guess string"
    APP_PORT = getenv("APP_PORT")
    DEBUG = getenv("DEBUG") or False
    SENTRY_DSN = getenv("SENTRY_DSN")
    MONGODB_HOST = getenv("MONGODB_URI")
    MONGODB_HOST_TEST = getenv("MONGODB_HOST_TEST")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SENTRY_DSN = getenv("SENTRY_DSN") or ""
    SSL_REDIRECT = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=int(getenv("JWT_ACCESS_TOKEN_EXPIRES", 20))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(getenv("JWT_REFRESH_TOKEN_EXPIRES", 30))
    )
    PROJECT_HOME = os.path.dirname(__file__)
    UPLOAD_FOLDER = os.path.join(PROJECT_HOME, "../uploads/")


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True


class TestingConfig(Config):
    FLASK_ENV = "testing"
    TESTING = True
    MONGODB_HOST = getenv("MONGODB_HOST_TEST")
    SSL_REDIRECT = False


class ProductionConfig(Config):
    DEBUG = False


class HerokuConfig(ProductionConfig):
    SSL_REDIRECT = True if getenv("DYNO") else False


class DockerConfig(ProductionConfig):
    pass


class UnixConfig(ProductionConfig):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "heroku": HerokuConfig,
    "docker": DockerConfig,
    "unix": UnixConfig,
    "default": DevelopmentConfig,
}
