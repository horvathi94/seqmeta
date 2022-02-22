from flask import Blueprint
from .ena import Ena


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
    return jsonify(request.form)
