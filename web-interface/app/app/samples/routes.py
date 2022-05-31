from flask import Blueprint, request, jsonify, redirect, url_for
from .view import View
from .editor import Editor

from . import generate
from seqmeta.form import submission
from seqmeta.objects.template import SampleTemplate
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
    return jsonify(sample.asjson())


@samples_bp.route("/samples/names")
def names():
    template_name = request.args.get("template_name")
    names = Sample.list_names(template_name)
    return jsonify(names)



def handle_submission(raw: dict, files: dict) -> None:

#    template_name = raw.pop("template_name")
    template_name = raw["template_name"]
    template = SampleTemplate.load(template_name)

    sample_data = submission.parse(raw, "sample")
    sample_names = {index:sample_data[index]["sample_name"] \
                    for index in sample_data}

    cleaned_files = submission.files_to_dict(files)

    for index in sample_data:
        sample = Sample(template_name)
        sample.taxonomy = template.taxonomy
        sample.ena_checklist = template.ena_checklist

        for aname, aval in sample_data[index].items():
            field = template.get_field(aname)
            attr = field.as_sample_attribute()
            attr.value = aval
            sample.add_attribute(attr)

        for field in template.active_files():
            files = submission.fetch_files(cleaned_files, field.general_name,
                                           sample.name, index)
            attr = field.as_sample_attribute()
            seqfiles = []
            for f in files:
                if not f.filename: continue
                seqfile = SeqFile(sample.path)
                seqfile.file_type = attr.seqfile_type
                seqfile.filename = f.filename
                seqfile.name = sample.name
                seqfile.save_data(f)
                seqfiles.append(seqfile)
            attr.value = seqfiles
            sample.add_attribute(attr)
        sample.save()


@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    page = handle_submission(dict(request.form), request.files)
    return jsonify(dict(request.form))
