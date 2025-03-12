"""The settings module"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    # Application settings
    DEVELOPMENT = True
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    # Application settings
    DEVELOPMENT = False
