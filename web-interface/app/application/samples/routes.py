from flask import Blueprint, render_template, request, redirect, url_for, \
    jsonify
from application.src.samples import Samples

samples_bp = Blueprint("samples_bp", __name__,
                       template_folder="templates",
                       static_folder="static",
                       static_url_path="/static/samples/");



@samples_bp.route("/samples/view")
def show():
    styles = [{"filename":"prompt.css"},
              {"filename": "samples.css", "prefix":"samples"}];
    scripts = [{"filename": "details.js", "prefix":"samples"}];
    samples_list = Samples.fetch_list();
    html = render_template("head.html", styles=styles);
    if len(samples_list) == 0:
        html+= render_template("list_is_empty.html",
                               name_plural="samples",
                               link="samples_bp.edit");
    else:
        html+= render_template("samples/list.html", samples=samples_list);

    html+= render_template("footer.html", scripts=scripts);
    return html;


@samples_bp.route("/samples/edit")
def edit():
    return "Edit";

@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    sample_data = funcs.parse_form_simple(request.form, "sample");
    sample_id = Samples.save_entry(sample_data);
    location = funcs.parse_form_simple(request.form, "location");
    location["sample_id"] = sample_id;
    SampleLocation.save_entry(location);
    collection = funcs.parse_form_simple(request.form, "collection");
    collection["sample_id"] = sample_id;
    SampleCollection.save_entry(collection);
    library = funcs.parse_form_simple(request.form, "library");
    library["sample_id"] = sample_id;
    SampleLibrary.save_entry(library);
    host = funcs.parse_form_simple(request.form, "host");
    host["sample_id"] = sample_id;
    SampleHost.save_entry(host);
    sampling = funcs.parse_form_simple(request.form, "sampling");
    sampling["sample_id"] = sample_id;
    SampleSampling.save_entry(sampling);
    health = funcs.parse_form_simple(request.form, "health");
    health["sample_id"] = sample_id;
    SampleHealthStatus.save_entry(health);
    sequencing = funcs.parse_form_simple(request.form, "sequencing");
    sequencing["sample_id"] = sample_id;
    SampleSequencing.save_entry(sequencing);
    if "fasta-file" in request.files:
        fasta = request.files["fasta-file"];
        fasta.save(os.path.join(
            app.config["UPLOAD_FOLDER"], "fasta",
                sample_data["name"] + ".fasta"));
    return redirect(url_for('view_samples'));


@samples_bp.route("/samples/details")
def sample_details():
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    sample_details = Samples.fetch_details(sample_id=sample_id);
    return jsonify(sample_details);

@samples_bp.route("/samples/generate")
def generate():
    return "Generate"
