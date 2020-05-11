from flask import Flask
from flask_pymongo import PyMongo

# Instantiate Flask extensions
mongo = PyMongo()


# Initialize Flask Application
def create_app():
    """Create a Flask application.
    """
    # Instantiate Flask
    app = Flask(__name__)

    # Load settings
    app.config.from_object('settings.api')

    # Setup MongoDB
    mongo.init_app(app)

    # Register blueprints
    from .blueprints import register_blueprints
    register_blueprints(app)
    return app
