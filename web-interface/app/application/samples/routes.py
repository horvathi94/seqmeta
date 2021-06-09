import os
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, \
    jsonify, send_file, Response
from application.src.samples.samples import Samples
from application.src.samples.extensions.collections import Collection
from application.src.samples.extensions.host import Host
from application.src.samples.extensions.health_status import HealthStatus
from application.src.samples.extensions.library import Library
from application.src.samples.extensions.location import Location
from application.src.samples.extensions.sampling import Sampling
from application.src.samples.extensions.sequencing import Sequencing
from application.src.institutions import Institutions
from application.src.authors import Authors, AuthorGroups
from application.src import misc
from application.src import library as lib
from application.src.forms.form import Form
from application.src.metatemplates.gisaid import GisaidMeta
from application.src.metatemplates.ena import EnaMeta
from application.src.seqfiles.db import SeqFileTypes, SeqFile
from application.src.seqfiles.seqfiles import SeqFilesBunch

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
    for sample in samples_list:
        seqbunch = SeqFilesBunch(sample["sample_id"]);
        sample["seqfiles"] = seqbunch.todict();
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
    seqfiles=SeqFilesBunch(sample_id);
    html = render_template("head.html", styles=styles);
    html+= render_template(
        "samples/edit.html",
        sample=Samples.fetch_entry_edit(id=sample_id, id_key="sample_id"),
        seqfiles=seqfiles.todict(),
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
            replace_key="item_key"),
        seqfile_types=SeqFileTypes.fetch_list_labeled(
            replace_key="item_key")
        );
    html+= render_template("footer.html", scripts=scripts);
    return html;


@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    sample_data = Form.parse_simple(request.form, "sample");
    sample_id = Samples.save_entry(sample_data);
    location = Form.parse_simple(request.form, "location");
    location["sample_id"] = sample_id;
    Location.save_entry(location);
    collection = Form.parse_simple(request.form, "collection");
    collection["sample_id"] = sample_id;
    Collection.save_entry(collection);
    library = Form.parse_simple(request.form, "library");
    library["sample_id"] = sample_id;
    Library.save_entry(library);
    host = Form.parse_simple(request.form, "host");
    host["sample_id"] = sample_id;
    Host.save_entry(host);
    sampling = Form.parse_simple(request.form, "sampling");
    sampling["sample_id"] = sample_id;
    Sampling.save_entry(sampling);
    health = Form.parse_simple(request.form, "health");
    health["sample_id"] = sample_id;
    HealthStatus.save_entry(health);
    sequencing = Form.parse_simple(request.form, "sequencing");
    sequencing["sample_id"] = sample_id;
    Sequencing.save_entry(sequencing);

    assembly_file = request.files["assembly-file"];
    if assembly_file.filename != "":
        file_data = {"sample_id": sample_id,
                     "file_type_id": request.form["assembly-file-type"],
                     "is_assembly": True,
                     "is_forward_read": None};
        SeqFile.save(file_data);
        seqfile, = SeqFile.fetch_entries_by_sample_id(sample_id);
        filename = seqfile["filename"];
        assembly_file.save(os.path.join("/uploads/samples/assemblies",
                                        filename));
    return redirect(url_for('samples_bp.show'));


@samples_bp.route("/samples/details")
def sample_details():
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    sample_details = Samples.fetch_details(sample_id=sample_id);
    return jsonify(sample_details);


@samples_bp.route("/samples/generate")
def generate():
    return "Generate"



@samples_bp.route("/samples/generate/gisaid", methods=["POST"])
def gen_gisaid_meta():
    selected = [int(i) for i in request.form.getlist("selected-samples")];
    if len(selected) == 0:
        return "Nothing selected";
    GisaidMeta.write_zip(selected);
    filename = GisaidMeta.get_attachment_filename();
    zip_file = GisaidMeta.get_tempfile();
    return send_file(zip_file, attachment_filename=filename);


@samples_bp.route("/samples/generate/ncbi", methods=["POST"])
def gen_ncbi_meta():
    selected = [int(i) for i in request.form.getlist("selected-samples")];
    if len(selected) == 0:
        return "Nothing selected";
    test = Samples.fetch_entries("view_samples_ncbi_sra",
                                 sample_ids=selected);
    return jsonify(test);


@samples_bp.route("/samples/generate/ena", methods=["POST"])
def gen_ena_meta():
    selected = [int(i) for i in request.form.getlist("selected-samples")];
    if len(selected) == 0: return "Nothing selected";
    EnaMeta.write_zip(selected);
    ena_zip = EnaMeta.get_tempfile();
    filename = EnaMeta.get_attachment_filename();
    return send_file(ena_zip, attachment_filename=filename);


@samples_bp.route("/samples/generate/concat-assemblies", methods=["POST"])
def gen_concat_assemblies():
    selected = [int(i) for i in request.form.getlist("selected-samples")];
    if len(selected) == 0: return "Nothing selected";
    ret = "";
    for sid in selected:
        seqbunch = SeqFilesBunch(sid);
        ret+= str(seqbunch.get_assembly());
    return ret;


