from flask import Blueprint, request, jsonify
from . import submission
from .view import View
from .editor import Editor

from . import generate
from seqmeta.objects.sample import Sample

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
    print(f"\n\nSub: {submission}\n");
    template_name = submission.pop("template_name")
    action = submission.pop("action")
    if action == "edit":
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


@samples_bp.route("/samples/json")
def json():
    template_name = request.args.get("template_name")
    sample_name = request.args.get("name")
    sample = Sample.load(sample_name, template_name)
    return jsonify(sample.asjson())


@samples_bp.route("/samples/names")
def names():
    template_name = request.args.get("template_name")
    names = Sample.list_names(template_name)
    return jsonify(names)


@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    page = submission.handle(dict(request.form), dict(request.files))
    return jsonify(dict(request.form))
