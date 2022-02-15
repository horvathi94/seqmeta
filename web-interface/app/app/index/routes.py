from flask import Blueprint, send_from_directory
from .index import Index


index_bp = Blueprint("index_bp", __name__)


@index_bp.route("/")
def index():
    page = Index()
    return page.render()


@index_bp.route("/favicon.ico")
def favicon():
    return send_from_directory("/static/assets", "favicon.ico",
                               mimetype="image/x-icon")
