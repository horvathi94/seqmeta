from flask import Blueprint
from .ena import Ena
from . import submission

samples_bp = Blueprint("samples_bp", __name__, template_folder="templates")


@samples_bp.route("/samples")
@samples_bp.route("/samples/view")
def view():
    return "Samples"



@samples_bp.route("/ena")
def ena():
    page = Ena()
    return page.render()

@samples_bp.route("/templates/submit", methods=["POST"])
def submit_template():
    from flask import jsonify, request
    submission.handle(dict(request.form))
    return jsonify(request.form)



@samples_bp.route("/samples/single-editor")
def single_editor():
    return "<h1>Single editor</h1>"


@samples_bp.route("/samples/multi-editor")
def multi_editor():
    return "<h1>Multiple editor</h1>"
