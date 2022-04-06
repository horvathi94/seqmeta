from flask import Blueprint, request
from .editor import Editor
from .view import View

formtemplate_bp = Blueprint("formtemplate_bp", __name__,
                            template_folder="templates")


@formtemplate_bp.route("/templates")
@formtemplate_bp.route("/templates/view")
def view():
    page = View()
    return page.render()


@formtemplate_bp.route("/templates/edit")
def edit():
    page = Editor()
    return page.render()


@formtemplate_bp.route("/templates/submit", methods=["POST"])
def submit():
    from flask import jsonify
    from . import submission
    submission.handle(dict(request.form))
    return jsonify(dict(request.form))
