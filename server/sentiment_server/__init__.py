"""
Main app module
"""

import logging
from server.sentiment_server.common.settings import LOGGING_FILE, LOGGING_FORMAT, DATA_FMT
from flask import Flask
from flask_cors import CORS
from server.sentiment_server.routes.status_routes import status_routes
from server.sentiment_server.routes.api_routes import api_routes

logging.basicConfig(filename=LOGGING_FILE,
                    filemode='a',
                    format=LOGGING_FORMAT,
                    level=logging.DEBUG,
                    datefmt=DATA_FMT)


def create_app():
    """Creates flask instance"""
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(status_routes)
    app.register_blueprint(api_routes)

    return app
