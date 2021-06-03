import os
from __main__ import app
from flask import request, \
    render_template, \
    jsonify, \
    redirect, \
    make_response, \
    send_file, \
    url_for, \
    Response
from datetime import datetime

from .src.samples import Samples, \
    SampleLibrary, \
    SampleCollection,\
    SampleLocation, \
    SampleHost, \
    SampleSampling, \
    SampleSequencing, \
    SampleHealthStatus
from .src.authors import Authors
from .src.author_groups import AuthorGroups
from .src.gisaid_submit import GisaidSubmit
from .src.ena import SampleSet as EnaSampleSet, \
        ExperimentSet as EnaExperimentSet
from .src.fast_files import Fasta
from .src.institutions import Institutions
from .src.locations import Continents, Countries
from .src.library import LibraryStrategies, \
    LibrarySources, \
    LibrarySelections
from .src.custom_options import Hosts, \
    SamplingStrategies, \
    PassageDetails, \
    AssemblyMethods, \
    PatientStatuses, \
    SpecimenSources, \
    SampleCaptureStatuses, \
    HostDiseaseOutcomes, \
    HostHealthStates, \
    HostHabitats, \
    HostBehaviours, \
    SequencingInstruments


from .src import funcs


@app.route("/samples/view")
def view_samples():
    samples_list = Samples.fetch_list();
    html = render_template("head.html", styles=["prompt.css", "samples.css"]);
    if len(samples_list) == 0:
        html+= render_template("list_is_empty.html",
                               name_plural="samples",
                               link="edit_samples");
    else:
#        return jsonify(samples_list);
        html+= render_template("samples/list.html", samples=samples_list);

    scripts = ["sample_details.js"];
    html+= render_template("footer.html", scripts=scripts);
    return html;


@app.route("/sample/details")
def sample_details():
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    sample_details = Samples.fetch_details(sample_id=sample_id);
    return jsonify(sample_details);



@app.route("/samples/edit")
def edit_samples():
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    styles = ["samples_edit.css", "markers.css"];
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
        hosts=Hosts.fetch_list(),
        sampling_strategies=SamplingStrategies.fetch_list(),
        passage_details=PassageDetails.fetch_list(),
        assembly_methods=AssemblyMethods.fetch_list(),
        sequencing_instruments=SequencingInstruments.fetch_list(),
        patient_statuses=PatientStatuses.fetch_list(),
        specimen_sources=SpecimenSources.fetch_list(),
        countries=Countries.fetch_list(),
        continents=Continents.fetch_list(),
        sample_capture_statuses=SampleCaptureStatuses.fetch_list(),
        host_disease_outcomes=HostDiseaseOutcomes.fetch_list(),
        host_health_states=HostHealthStates.fetch_list(),
        host_habitats=HostHabitats.fetch_list(),
        host_behaviours=HostBehaviours.fetch_list(),
        library_strategies=LibraryStrategies.fetch_list_labeled(
            replace_key="item_key"),
        library_sources=LibrarySources.fetch_list_labeled(
            replace_key="item_key"),
        library_selections=LibrarySelections.fetch_list_labeled(
            replace_key="item_key")
        );
    html+= render_template("footer.html", scripts=["sample_edit.js"]);
    return html;


@app.route("/samples/submit", methods=["POST"])
def submit_samples():
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


@app.route("/samples/fasta")
def samples_fasta():

    sample_id = 0;
    if "id" in request.args:
        sample_id = int(request.args["id"]);

    samples = Samples();
    sample = samples.fetch_entry(sample_id=sample_id);

    fasta = Fasta(sample["sample_name"]);
    sequences = fasta.read_fasta();

    if not fasta.has_fasta:
        resp_string = "fasta file was not found.";
    else:
        seq = sequences[0].seq;
        resp_string = str(seq);

    response = make_response(resp_string, 200);
    response.mimetype = "text/fasta";
    return response;


@app.route("/samples/generate", methods=["POST"])
def samples_generate():
    sub_types = request.form.getlist("submission_types");
    if len(sub_types) == 0:
        return "No files selected";

    selected = request.form.getlist("selected-samples");
    selected = [int(s) for s in selected];
    if len(selected) == 0:
        return "No files selected;"

    if "gisaid" in sub_types:
        filename = request.form["submission_filename_gisaid"];
        samples = Samples.fetch_entries("view_samples_gisaid",
                                        sample_ids=selected);

        if filename == "": filename = str(datetime.now()) + "_gisaid";
        GisaidSubmit.write_gisaid(samples);
        excel_file = os.path.join(GisaidSubmit.get_temp_filename());
        return send_file(excel_file, attachment_filename=filename+".xls")

    if "ena" in sub_types:
#        test = EnaSampleSet.create_xml(selected);

        test = EnaExperimentSet.create_xml(selected);
        return Response(test, mimetype="text/xml");

    return "Finished";


