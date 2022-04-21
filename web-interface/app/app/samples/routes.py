from flask import Blueprint, request, jsonify
from . import submission
from .view import View
from .editor import Editor

from .generate import generate_upload
from seqmeta.database.samples import SamplesTable

samples_bp = Blueprint("samples_bp", __name__, template_folder="templates")


@samples_bp.route("/samples")
@samples_bp.route("/samples/view")
def view():
    page = View()
    return page.render()


@samples_bp.route("/samples/edit", methods=["POST"])
def edit():
    submission = dict(request.form)
    template_id = int(submission.pop("template_id"))
    action = submission.pop("action")
    if action == "Edit samples":
        samples = [int(k) for k in submission.keys()]
        page = Editor(template_id=template_id, samples=samples)
    elif action == "Generate":
        data = generate_upload([int(k) for k in submission.keys()])
        return jsonify(data)
    else:
        page = Editor(template_id=template_id)
    return page.render()


@samples_bp.route("/samples/json")
def json():
    sample_id = int(request.args.get("id"))
    sample = SamplesTable.select(sample_id)
    return jsonify(sample.asjson())


@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    page = submission.handle(dict(request.form))
    return jsonify(dict(request.form))
