from flask import Blueprint, request, jsonify
from . import submission
from .view import View
from .editor import Editor

from . import generate
from seqmeta.database.samples import SamplesTable

samples_bp = Blueprint("samples_bp", __name__, template_folder="templates")


@samples_bp.route("/samples")
@samples_bp.route("/samples/view")
def view():
    page = View()
    return page.render()


from flask import Response
@samples_bp.route("/samples/edit", methods=["POST"])
def edit():
    submission = dict(request.form)
    template_name = submission.pop("template_name")
    action = submission.pop("action")
    if action == "Edit samples":
        samples = submission.keys()
        page = Editor(template_name=template_name, samples=samples)
    elif action == "Generate ENA":
        data = generate.ena(submission.keys())
        return Response(data, mimetype="application/xml")
    elif action == "Generate GISAID":
        data = generate.gisaid(submission.keys())
        return jsonify(data)
    else:
        page = Editor(template_name=template_name)
    return page.render()


from seqmeta.objects.samples.templates import SamplesList
@samples_bp.route("/samples/json")
def json():
    sample_name = request.args.get("name")
    sl = SamplesList()
    sample = sl.load_by_name(sample_name)
    return jsonify(sample.asjson())


@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    page = submission.handle(dict(request.form), dict(request.files))
    return jsonify(dict(request.form))
