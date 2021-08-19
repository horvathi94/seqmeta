import os
from flask import current_app as app
from flask import Blueprint, render_template, send_from_directory


home_bp = Blueprint("home_bp", __name__,
                    template_folder="templates",
                    static_folder="static");



@home_bp.route("/", methods=["GET"])
@home_bp.route("/index.html", methods=["GET"])
@home_bp.route("/home.html", methods=["GET"])
def home():
    """ Homepage """
    html = render_template("head.html");
    html+= render_template("index.html");
    html+= render_template("footer.html");
    return html;



@home_bp.route("/favicon.ico")
def favicon():
    path = os.path.join(app.root_path, 'static', 'assets');
    return send_from_directory(path, 'favicon.ico', mimetype='image/x-icon');

