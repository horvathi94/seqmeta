from flask import Blueprint, request, jsonify, redirect, url_for
from .editor import Editor
from .view import View
from seqmeta.objects.template import SampleTemplate
from seqmeta.form import submission
from seqmeta.objects.attributes.attribute import Attribute



formtemplate_bp = Blueprint("formtemplate_bp", __name__,
                            template_folder="templates")



@formtemplate_bp.route("/templates")
@formtemplate_bp.route("/templates/view")
def view():
    page = View()
    return page.render()


@formtemplate_bp.route("/templates/edit")
def edit():
    template_name = request.args.get("name")
    template = None
    if template_name:
        template = SampleTemplate.load(template_name)
    page = Editor(template=template)
    return page.render()



def handle_submission(raw: dict) -> None:
    template_name = raw.pop("template_name")
    template = SampleTemplate(template_name)
    taxonomy = submission.parse(raw, "taxonomy")[0]
    template.taxonomy.update(taxonomy)
    ena_checklist = submission.parse(raw, "ena_checklist")[0]
    template.ena_checklist = ena_checklist["ena_checklist"]
    template_data = submission.parse(raw, "template")[0]
    template.short_description = template_data["short_description"]
    files = submission.parse(raw, "submission_files")[0]
    template.set_files_from_submission(files)
    attrs = submission.parse(raw, "attr")
    for a in list(attrs.values()):
        template.add_attribute(Attribute(**a))
    template.save(create_path=True)


@formtemplate_bp.route("/templates/submit", methods=["POST"])
def submit():
    handle_submission(dict(request.form))
    return jsonify(dict(request.form))
    return redirect(url_for("formtemplate_bp.view"))


@formtemplate_bp.route("/templates/json")
def json():
    template_name = request.args.get("name")
    template = SampleTemplate.load(template_name)
    if template is None: return jsonify({})
    return jsonify(template.asjson())


@formtemplate_bp.route("/templates/names")
def names():
    return jsonify(SampleTemplate.list_names())
