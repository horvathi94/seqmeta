from flask import Flask

def create_app() -> None:

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    with app.app_context():
        from .index import routes as index
        app.register_blueprint(index.index_bp)

        from .samples import routes as samples
        app.register_blueprint(samples.samples_bp)

        from .sample_template import routes as sample_template
        app.register_blueprint(sample_template.sample_template_bp)

    return app
