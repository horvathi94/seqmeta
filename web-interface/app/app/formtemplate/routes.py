from flask import Blueprint, request, jsonify
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
    template_name = request.args.get("name");
    page = Editor(template_name=template_name)
    return page.render()


@formtemplate_bp.route("/templates/submit", methods=["POST"])
def submit():
    from . import submission
    submission.handle(dict(request.form))
    return jsonify(dict(request.form))


from seqmeta.objects.samples.template import Template, list_templates
@formtemplate_bp.route("/templates/json")
def json():
    template_name = request.args.get("name")
    template = Template(name=template_name)
    template.load()
    return jsonify(template.asjson())


@formtemplate_bp.route("/templates/names")
def names():
    templates = list_templates()
    return jsonify([t.name for t in templates])
