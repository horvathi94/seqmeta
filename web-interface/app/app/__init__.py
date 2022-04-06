from flask import Flask

def create_app() -> None:

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    with app.app_context():
        from .index import routes as index
        app.register_blueprint(index.index_bp)

        from .authors import routes as authors
        app.register_blueprint(authors.authors_bp)

        from .samples import routes as samples
        app.register_blueprint(samples.samples_bp)

        from .formtemplate import routes as formtemplate
        app.register_blueprint(formtemplate.formtemplate_bp)

    return app
