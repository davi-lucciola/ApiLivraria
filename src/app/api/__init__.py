from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, 
        instance_relative_config=False, 
        template_folder='./client/templates',
        static_folder='./client/templates',
    )
    app.config.from_object("api.config.Config")

    with app.app_context():
        from . import books_routes 
        return app
