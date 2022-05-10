from flask import Blueprint, request, jsonify
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
def handle_submission(raw: dict, files: list) -> None:

    template_name = raw.pop("template_name")
    template = SampleTemplate.load(template_name)

    sample_data = submission.parse(raw, "sample")

    seqfiles = []
    for f in files:
        seqfile = SeqFile()
        seqfile.path = template.path
        seqfile.filedata = f
        seqfiles.append(seqfile)


    for sd in sample_data:
        name = sd.pop("sample_name")
        short_description = sd.pop("short_description")
        sample = Sample(name, short_description, template_name=template_name)
        sample.taxonomy = template.taxonomy
        sample.ena_checklist = template.ena_checklist

        for aname, aval in sd.items():
            attr = template.get_attribute(aname)
            sample_attr = attr.as_sample_attribute()
            sample_attr.value = aval
            sample.add_attribute(sample_attr)

        for sf in seqfiles:
            print(f"\n{sf.name} == {sample.name}\n")
            if sf.name == sample.name:
                print(f"\nAdding {sf}\n")
                sample.add_file(sf)
        print(sample)
#        sample.save()



@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    files = request.files.getlist("uploadedfiles")
    page = handle_submission(dict(request.form), files)
    return jsonify(dict(request.form))
