from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy();


def create_app():
    """Create the Flask application."""
    app = Flask(__name__, instance_relative_config=False);
    app.config.from_object("config.Config");

    db.init_app(app);


    with app.app_context():
        from .home import routes as home
        app.register_blueprint(home.home_bp);

        from .authors import routes as authors
        app.register_blueprint(authors.authors_bp);

        from .author_groups import routes as author_groups
        app.register_blueprint(author_groups.author_groups_bp);

        from .institutions import routes as institutions
        app.register_blueprint(institutions.institutions_bp);

        from .misc import routes as misc
        app.register_blueprint(misc.misc_bp);

    return app;


