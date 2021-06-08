from flask import Blueprint, render_template, request, redirect, url_for, \
    jsonify
from application.src.samples.samples import Samples
from application.src.samples import extensions as sample_exten
from application.src.institutions import Institutions
from application.src.authors import Authors, AuthorGroups
from application.src import misc
from application.src import library as lib

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
    styles = [{"filename": "edit.css", "prefix": "samples"},
              {"filename": "markers.css"}];
    scripts = [{"filename": "edit.js", "prefix": "samples"}];
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    html = render_template("head.html", styles=styles);
    html+= render_template(
        "samples/edit.html",
        sample=Samples.fetch_entry_edit(id=sample_id, id_key="sample_id"),
        authors=Authors.fetch_list_labeled(
            replace_key="abbreviated_middle_name"),
        author_groups=AuthorGroups.fetch_list_labeled(
            replace_key="group_name",
            replace_id="group_id"),
        institutions=Institutions.fetch_list_labeled(),
        hosts=misc.Hosts.fetch_list(),
        sampling_strategies=misc.SamplingStrategies.fetch_list(),
        passage_details=misc.PassageDetails.fetch_list(),
        assembly_methods=misc.AssemblyMethods.fetch_list(),
        sequencing_instruments=misc.SequencingInstruments.fetch_list(),
        patient_statuses=misc.PatientStatuses.fetch_list(),
        specimen_sources=misc.SpecimenSources.fetch_list(),
        countries=misc.Countries.fetch_list(),
        continents=misc.Continents.fetch_list(),
        sample_capture_statuses=misc.SampleCaptureStatuses.fetch_list(),
        host_disease_outcomes=misc.HostDiseaseOutcomes.fetch_list(),
        host_health_states=misc.HostHealthStates.fetch_list(),
        host_habitats=misc.HostHabitats.fetch_list(),
        host_behaviours=misc.HostBehaviours.fetch_list(),
        library_strategies=lib.LibraryStrategies.fetch_list_labeled(
            replace_key="item_key"),
        library_sources=lib.LibrarySources.fetch_list_labeled(
            replace_key="item_key"),
        library_selections=lib.LibrarySelections.fetch_list_labeled(
            replace_key="item_key")
        );
    html+= render_template("footer.html", scripts=scripts);
    return html;


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
