from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize extensions here

    # Attach blueprints here

    # Attach shell context processors here

    # Attach request context processors here

    # Attach error handlers here

    # Attach before and after request handlers here
    
    return app
