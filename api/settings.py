"""The settings module"""

from secrets import token_hex


class Config(object):
    # Application settings
    DEVELOPMENT = True
    TESTING = False
    SECRET_KEY = token_hex()
