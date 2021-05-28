from __main__ import app
from flask import request, \
    render_template, \
    jsonify, \
    redirect, \
    make_response, \
    send_file, \
    url_for

from .src.samples import Samples, \
    SampleLibrary, \
    SampleCollection
from .src.authors import Authors
from .src.author_groups import AuthorGroups
from .src.base.excel_generator import ExcelGenerator
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

    library = funcs.parse_form_simple(request.form, "library");
    library["id"] = int(request.form.to_dict()["link_library_id"]);
    sample_data["link_library_id"] = SampleLibrary.save_entry(library);

    collection = funcs.parse_form_simple(request.form, "collection");
    collection["id"] = int(request.form.to_dict()["link_collection_id"]);
    sample_data["link_collection_id"] = \
        SampleCollection.save_entry(collection);


    sample_id = Samples.save_entry(sample_data);
    return jsonify(sample_id);

    collection = funcs.parse_form_simple(request.form, "collection");
    location = funcs.parse_form_simple(request.form, "location");
    return jsonify(location);
    return jsonify(request.form.to_dict());
    Samples.save_entry(request.form.to_dict());
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
        ExcelGenerator.write_gisaid(samples);
        excel_file = os.path.join(ExcelGenerator.get_temp_filename("gisaid"));
        return send_file(excel_file, attachment_filename=filename+".xls")


    return "Finished";


