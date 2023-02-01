from flask import Flask
import os


ACTUAL_DIR = os.getcwd()
TEMPLATES_DIR = os.path.join(ACTUAL_DIR, 'app', 'client', 'templates')
STATIC_DIR = os.path.join(ACTUAL_DIR, 'app', 'client', 'static')


def create_app():
    """Construct the core application."""

    app = Flask(__name__, 
        instance_relative_config=False, 
        template_folder=TEMPLATES_DIR,
        static_folder=STATIC_DIR,
    )
    app.config.from_object("app.api.config.Config")

    with app.app_context():
        from . import books_routes 
        from . import library_routes
        
        return app
