import os
from flask import Blueprint, send_from_directory
from .pages.home import Home


home_bp = Blueprint("home_bp", __name__,
                    template_folder="templates",
                    static_folder="static");



@home_bp.route("/", methods=["GET"])
@home_bp.route("/index.html", methods=["GET"])
@home_bp.route("/home.html", methods=["GET"])
def home():
    return Home.render();



@home_bp.route("/favicon.ico")
def favicon():
    path = os.path.join(app.root_path, 'static', 'assets');
    return send_from_directory(path, 'favicon.ico', mimetype='image/x-icon');

