from flask import Flask

def create_app():
    """Create the Flask application."""
    app = Flask(__name__, instance_relative_config=False);
    app.config.from_object("config.Config");

    with app.app_context():
        from .home import routes as home
        app.register_blueprint(home.home_bp);

    return app;

