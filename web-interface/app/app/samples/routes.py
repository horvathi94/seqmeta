from flask import Blueprint, request, jsonify, redirect, url_for
from .view import View
from .editor import Editor

from . import generate
from seqmeta.form import submission
from seqmeta.objects.sample_template import SampleTemplate
from seqmeta.objects.sample import Sample
from seqmeta.objects.seqfiles import SeqFile


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

    if action == "edit":
        samples = submission.keys()
        page = Editor(template_name=template_name, samples=samples)
    elif action == "delete":
        samples = submission.keys()
        for sample_name in samples:
            sample = Sample.load(sample_name, template_name=template_name)
            sample.delete()
        return redirect(url_for("samples_bp.view"))
    elif action == "ena-generate":
        data = generate.ena(template_name, submission.keys())
        return Response(data, mimetype="application/xml")
    elif action == "ena-submit":
        data = generate.submit_to_ena(template_name, submission.keys())
        return str(data)
        return data, 200, {'Content-Type': 'application/xml', }
#        return Response(data, mimetype="application/xml")
    elif action == "gisaid":
        data = generate.gisaid(template_name, submission.keys())
        return jsonify(data)
    else:
        page = Editor(template_name=template_name)
    return page.render()


@samples_bp.route("/samples/json")
def json():
    template_name = request.args.get("template_name")
    sample_name = request.args.get("name")
    sample = Sample.load(sample_name, template_name)
    return jsonify(sample.as_json())


@samples_bp.route("/samples/names")
def names():
    template_name = request.args.get("template_name")
    names = Sample.list_names(template_name)
    return jsonify(names)



def handle_submission(raw: dict, files: dict) -> None:

    template_name = raw.pop("template_name")
    template = SampleTemplate.load(template_name)

    sample_data = submission.parse(raw, "sample")
    sample_names = {index:sample_data[index]["sample_name"] \
                    for index in sample_data}

    cleaned_files = submission.files_to_dict(files)


    for index in sample_data:

        sample = Sample.load(sample_names[index], template_name)
        sample.taxonomy = template.taxonomy
        sample.ena_checklist = template.ena_checklist

        new_atts = []
        for aname, aval in sample_data[index].items():
            field = template.get_field(aname)
            a = field.as_sample_attribute()
            a.value = aval
            new_atts.append(a)
        sample.update_attributes(new_atts)


        new_file_atts = []
        save_files = {}
        for field in template.active_files():
            files = submission.fetch_files(cleaned_files, field.general_name,
                                           sample.name, index)
            attr = field.as_sample_attribute()
            new_file_atts.append(attr)
            save_files[attr.general_name] = files
        sample.update_files(new_file_atts, save_files)

    sample.save()



@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    page = handle_submission(dict(request.form), request.files)
    return jsonify(dict(request.form))
