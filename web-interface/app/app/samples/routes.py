from flask import Blueprint, request, jsonify, redirect, url_for
from .view import View
from .editor import Editor

from . import generate
from seqmeta.form import submission
from seqmeta.objects.template import SampleTemplate
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
    elif action == "delete":
        samples = submission.keys()
        print(f"\n\nDeleteing: {samples}")
        for sample_name in samples:
            sample = Sample.load(sample_name, template_name=template_name)
            sample.delete()
        return redirect(url_for("samples_bp.view"))


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



from seqmeta.objects.seqfiles import SeqFile
def sort_files(files: list) -> dict:
    sorted_files = {}
    sorted_files["all"] = \
        [f for f in files.getlist("uploadedfiles") if f.filename]
    for field in files:
        if field == "uploadedfiles": continue
        index = int(field.split("+")[1])
        sorted_files[index] = [f for f in files.getlist(field) if f.filename]
    return sorted_files


def handle_submission(raw: dict, files: list) -> None:

    template_name = raw.pop("template_name")
    template = SampleTemplate.load(template_name)

    sample_data = submission.parse(raw, "sample")
    sorted_files = sort_files(files)


    for index in sample_data:
        name = sample_data[index].pop("sample_name")
        short_description = sample_data[index].pop("short_description")
        sample = Sample(name, short_description, template_name=template_name)
        sample.taxonomy = template.taxonomy
        sample.ena_checklist = template.ena_checklist

        for aname, aval in sample_data[index].items():
            attr = template.get_attribute(aname)
            sample_attr = attr.as_sample_attribute()
            sample_attr.value = aval
            sample.add_attribute(sample_attr)

        sample_files = []
        if len(sorted_files[index]) > 0:
            sample_files = [f for f in sorted_files[index]]
        else:
            for f in sorted_files["all"]:
                fname = f.filename.split(".")[0]
                if fname == sample.name: sample_files.append(f)

        if len(sample_files) > 0:
            for f in sample_files:
                sample.save_file("ena_read_files", f)
        else:
            sample.check_files("ena_read_files")

        sample.save()



@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    page = handle_submission(dict(request.form), request.files)
    return jsonify(dict(request.form))
