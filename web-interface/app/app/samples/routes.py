from flask import Blueprint, request
from . import submission
from .view import View
from .editor import Editor

samples_bp = Blueprint("samples_bp", __name__, template_folder="templates")


@samples_bp.route("/samples")
@samples_bp.route("/samples/view")
def view():
    page = View()
    return page.render()


@samples_bp.route("/samples/edit", methods=["POST"])
def edit():
    template_id = int(request.form.get("template_id"))
    page = Editor(template_id=template_id)
    return page.render()


@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    from flask import jsonify
    page = submission.handle(dict(request.form))
    return jsonify(dict(request.form))
