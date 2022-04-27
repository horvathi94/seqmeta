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


from seqmeta.objects.samples.templates import TemplatesList
@formtemplate_bp.route("/templates/edit")
def edit():
    template_name = request.args.get("name")
    tl = TemplatesList()
    template = tl.load_by_name(template_name)
    page = Editor(template=template)
    return page.render()


@formtemplate_bp.route("/templates/submit", methods=["POST"])
def submit():
    from . import submission
    submission.handle(dict(request.form))
    return jsonify(dict(request.form))


from seqmeta.objects.samples.templates import TemplatesList
@formtemplate_bp.route("/templates/json")
def json():
    template_name = request.args.get("name")
    tl = TemplatesList()
    template = tl.load_by_name(template_name)
    return jsonify(template.asjson())


@formtemplate_bp.route("/templates/names")
def names():
    tl = TemplateList()
    return jsonify(tl.load_names())
