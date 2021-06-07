from flask import current_app as app
from flask import Blueprint, render_template

home_bp = Blueprint("home_bp", __name__,
                    template_folder="templates",
                    static_folder="static");


@home_blueprint.route("/", methods=["GET"])
def home():
    return render_template("index.html");
