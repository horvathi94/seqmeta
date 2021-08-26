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
    return send_from_directory("static/assets",
                               'favicon.ico', mimetype='image/x-icon');

