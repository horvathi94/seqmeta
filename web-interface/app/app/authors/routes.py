from flask import Blueprint
from .authors import Authors


authors_bp = Blueprint("authors_bp", __name__)


@authors_bp.route("/authors")
@authors_bp.route("/authors/view")
def view():
    page = Authors()
    return page.render()
