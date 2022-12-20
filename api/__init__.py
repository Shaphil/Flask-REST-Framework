from flask import Flask

from api.settings import Config


def create_app(test_config=None):
    """The application factory"""

    app = Flask(__name__)

    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    with app.app_context():
        from . import urls

    return app
