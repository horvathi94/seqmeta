from flask import Blueprint, request, jsonify, redirect, url_for
from .view import View
from .editor import Editor

from seqmeta.objects.sample_template import SampleTemplate
from seqmeta.objects.attributes.attr_field import AttributeField
from seqmeta.objects.attributes.list_attrs import list_fields
from seqmeta.form import submission



sample_template_bp = Blueprint("sample_template_bp", __name__,
                               template_folder="templates")



@sample_template_bp.route("/templates")
@sample_template_bp.route("/templates/view")
def view():
    page = View()
    return page.render()


@sample_template_bp.route("/templates/edit")
def edit():
    template_name = request.args.get("name")
    template = SampleTemplate.load(template_name) if template_name else None
    page = Editor(template=template)
    return page.render()


@sample_template_bp.route("/templates/delete")
def delete():
    template_name = request.args.get("name")
    template = SampleTemplate.load(template_name)
    template.delete()
    return redirect(url_for("sample_template_bp.view"))


def handle_submission(raw: dict) -> None:
    template_name = raw.pop("template_name")
    template = SampleTemplate(template_name)
    taxonomy = submission.parse(raw, "taxonomy")[0]
    template.taxonomy.update(taxonomy)
    ena_checklist = submission.parse(raw, "ena_checklist")[0]
    template.ena_checklist = ena_checklist["ena_checklist"]
    template_data = submission.parse(raw, "template")[0]
    template.description = template_data["short_description"]

    files = submission.parse(raw, "submission_files")
    if files:
        print(f"Files:\n{files}")
        for f in files[0].keys():
            template.set_file_field(f)

    attrs = submission.parse(raw, "attr")
    for a in list(attrs.values()):
        print(f" - {a}")
        attr = AttributeField.from_dict(a)
        template.add_attribute(attr)
    template.save(create_path=True)


@sample_template_bp.route("/templates/submit", methods=["POST"])
def submit():
    handle_submission(dict(request.form))
    return redirect(url_for("sample_template_bp.view"))


@sample_template_bp.route("/templates/json")
def json():
    template_name = request.args.get("name")
    use = request.args.get("use")
    template = SampleTemplate.load(template_name)
    return jsonify(template.as_json())
    if template is None: return jsonify({})
    if use == "sample_editor":
        return jsonify(template.sample_editor_json())
    return jsonify(template.asjson())


@sample_template_bp.route("/templates/names")
def names():
    return jsonify(SampleTemplate.list_names())



@sample_template_bp.route("/templates/attributes")
def attributes():
    which = request.args.get("for")
    return jsonify([f.as_json() for f in list_fields(which)])
