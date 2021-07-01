import os
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, \
    jsonify, send_file, Response
from application.src.samples.samples import Samples
from application.src.samples.extensions.collections import Collection
from application.src.samples.extensions.host import Host,\
    PATIENT_GENDERS
from application.src.samples.extensions.health_status import HealthStatus,\
    HOSPITALISATIONS
from application.src.samples.extensions.library import Library,\
    LIBRARY_LAYOUTS
from application.src.samples.extensions.location import Location
from application.src.samples.extensions.sampling import Sampling
from application.src.samples.extensions.sequencing import Sequencing
from application.src.institutions import Institutions
from application.src.authors import Authors, AuthorGroups
from application.src import misc
from application.src import library as lib
from application.src.forms.form import Form
from application.src.metatemplates.gisaid.main import GisaidMeta
from application.src.metatemplates.ena.main import EnaMeta
from application.src.seqfiles.db import SeqFileTypes, SeqFile
from application.src.seqfiles.seqfiles import SeqFilesBunch
from .save import save
from application.src.defaults import DefaultValues
from application.src.samples.nametemplates.virusname_gisaid import \
    VirusnameGisaid
from application.src.samples.nametemplates.isolate_ena import \
    IsolateEna



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
        sample["virusname_gisaid"] = \
            VirusnameGisaid.format_name(sample["sample_id"]);
        sample["isolate_ena"] = \
            IsolateEna.format_name(sample["sample_id"]);
    html = render_template("head.html", styles=styles);
    if len(samples_list) == 0:
        html+= render_template("empty_list.html",
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
    scripts = [{"filename": "validate-sample-name.js", "prefix": "samples"},
               {"filename": "edit-sample.js", "prefix": "samples"}];
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    seqfiles=SeqFilesBunch(sample_id);
    sample=Samples.fetch_entry_edit(id=sample_id, id_key="sample_id");
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
            replace_key="item_key"),
        library_layouts=LIBRARY_LAYOUTS,
        genders=PATIENT_GENDERS,
        hospitalisations=HOSPITALISATIONS,
        default_vals=DefaultValues.fetch(),
        );
    html+= render_template("footer.html", scripts=scripts);
    return html;


@samples_bp.route("/samples/add-multiple", methods=["GET"])
def add_multiple():
    styles = [{"filename": "add-multiple.css", "prefix": "samples"},
              {"filename": "markers.css"},
              {"filename": "tooltips.css"}];
    scripts = [{"filename": "edit-multiple.js", "prefix": "samples"},
               {"filename": "validate-samples.js", "prefix": "samples"}];
    html = render_template("head.html", styles=styles);
    html+= render_template("samples/add_multiple.html",
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
            replace_key="item_key"),
        library_layouts=LIBRARY_LAYOUTS,
        genders=PATIENT_GENDERS,
        hospitalisations=HOSPITALISATIONS,
        default_vals=DefaultValues.fetch(),
        );
    html+= render_template("footer.html", scripts=scripts);
    return html;


@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    save_data = {};
    save_data["sample"] = Form.parse_simple(request.form, "sample");
    save_data["location"] = Form.parse_simple(request.form, "location");
    save_data["collection"] = Form.parse_simple(request.form, "collection");
    save_data["library"] = Form.parse_simple(request.form, "library");
    save_data["host"] = Form.parse_simple(request.form, "host");
    save_data["sampling"] = Form.parse_simple(request.form, "sampling");
    save_data["health"] = Form.parse_simple(request.form, "health");
    save_data["sequencing"] = Form.parse_simple(request.form, "sequencing");
    sample_ids = save([save_data]);
    sample_id = sample_ids[0];

    assembly_file = request.files["assembly-file"];
    if assembly_file.filename != "":
        file_data = {"sample_id": sample_id,
                     "file_type_id": request.form["assembly-file-type"],
                     "is_assembly": True,
                     "is_forward_read": None};
        SeqFile.save(file_data);
        filename = SeqFile.fetch_filename(sample_id, ftype="assembly");
        assembly_file.save(os.path.join("/uploads/samples/assemblies",
                                        filename));

    fwread_file = request.files["forward-read-file"];
    if fwread_file.filename != "":
        file_data = {"sample_id": sample_id,
                     "file_type_id": request.form["forward-read-file-type"],
                     "is_assembly": False,
                     "is_forward_read": True};
        SeqFile.save(file_data);
        filename = SeqFile.fetch_filename(sample_id, ftype="fwread");
        fwread_file.save(os.path.join("/uploads/samples/raw", filename));

    rvread_file = request.files["reverse-read-file"];
    if rvread_file.filename != "":
        file_data = {"sample_id": sample_id,
                     "file_type_id": request.form["reverse-read-file-type"],
                     "is_assembly": False,
                     "is_forward_read": False};
        SeqFile.save(file_data);
        filename = SeqFile.fetch_filename(sample_id, ftype="rvread");
        rvread_file.save(os.path.join("/uploads/samples/raw", filename));

    return redirect(url_for('samples_bp.show'));


@samples_bp.route("/samples/submit-multiple", methods=["POST"])
def submit_multiple():
    sample_data = Form.parse_list(request.form, "sample")[1:];
    collection = Form.parse_list(request.form, "collection")[1:];
    location = Form.parse_list(request.form, "location")[1:];
    host = Form.parse_list(request.form, "host")[1:];
    health = Form.parse_list(request.form, "health")[1:];
    sequencing = Form.parse_list(request.form, "sequencing")[1:];
    sampling = Form.parse_list(request.form, "sampling")[1:];
    library = Form.parse_list(request.form, "library")[1:];
    samples = [];
    for i, sd in enumerate(sample_data):
        save_data = {};
        save_data["sample"] = sd;
        save_data["sample"]["sample_id"] = 0;
        save_data["location"] = location[i];
        save_data["collection"] = collection[i];
        save_data["host"] = host[i];
        save_data["health"] = health[i];
        save_data["sequencing"] = sequencing[i];
        save_data["sampling"] = sampling[i];
        save_data["library"] = library[i];
        samples.append(save_data);
    save(samples);
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


@samples_bp.route("/samples/registered/sample-names", methods=["GET"])
def reg_sample_names():
    sample_names = [s["sample_name"] for s in Samples.fetch_list()];
    return jsonify(sample_names);


@samples_bp.route("/samples/registered/library-names", methods=["GET"])
def reg_library_names():
    lib_ids = [l["library_id"] for l in Library.fetch_list()
               if l["library_id"] != ""];
    return jsonify(lib_ids);



from .editor import Editor
from application.src.samples.extensions.treatment import ANTIVIRAL_TREAT

from application.src.fields import Field


@samples_bp.route("/test")
def tester():

    sample_id = 1;
    editor = Editor(sample_id);


#    return jsonify(Field.fetch("date_of_prior_antiviral_treat"));

    styles = [{"filename": "edit.css", "prefix": "samples"},
              {"filename": "markers.css"}];
    scripts = [{"filename": "validate-sample-name.js", "prefix": "samples"},
               {"filename": "edit-sample.js", "prefix": "samples"}];
    html = render_template("head.html", styles=styles);
    html+= render_template("samples/form/single/head.html",
                           sample_id=sample_id);


    html+= editor.single("sample_name");
    html+= editor.single("sample_comment");
    html+= editor.single("sample_title");
    html+= editor.single("sample_description");

    html+= editor.single("collection_year");
    html+= editor.single("collection_month");
    html+= editor.single("collection_day");
    html+= editor.single("collector_name",
                         dlist=Authors.fetch_list_labeled(
                             replace_key="abbreviated_middle_name"));


    html+= editor.single("location_continent",
                         dlist=misc.Continents.fetch_list());
    html+= editor.single("location_country",
                         dlist=misc.Countries.fetch_list());

    html+= editor.single("location_region");
    html+= editor.single("location_locality");
    html+= editor.single("additional_location_info");
    html+= editor.single("geo_loc_latitude");
    html+= editor.single("geo_loc_longitude");

    html+= editor.single("host", dlist=misc.Hosts.fetch_list());
    html+= editor.single("host_subject_id");
    html+= editor.single("additional_host_info");
    html+= editor.single("patient_gender", dlist=PATIENT_GENDERS);
    html+= editor.single("patient_age");
    html+= editor.single("patient_status",
                         dlist=misc.PatientStatuses.fetch_list());
    html+= editor.single("ppe");
    html+= editor.single("host_habitat",
                         dlist=misc.HostHabitats.fetch_list());
    html+= editor.single("host_behaviour",
                         dlist=misc.HostBehaviours.fetch_list());
    html+= editor.single("host_description");
    html+= editor.single("host_gravidity");

    html+= editor.single("prior_sars_cov_2_antiviral_treat",
                         dlist=ANTIVIRAL_TREAT);
    html+= editor.single("date_of_prior_antiviral_treat");


    html+= render_template("samples/form/single/tail.html");
    return html;



@samples_bp.route("/test/submit", methods=["POST"])
def tester_submit():

#    return jsonify(request.form);
    save_data = {};
    save_data["sample"] = Form.parse_simple(request.form, "sample");
    save_data["collection"] = Form.parse_simple(request.form, "collection");
    save_data["location"] = Form.parse_simple(request.form, "location");
    save_data["host"] = Form.parse_simple(request.form, "host");
    sample_ids = save([save_data]);

    return jsonify(save_data);
    save_data["library"] = Form.parse_simple(request.form, "library");
    save_data["sampling"] = Form.parse_simple(request.form, "sampling");
    save_data["health"] = Form.parse_simple(request.form, "health");
    save_data["sequencing"] = Form.parse_simple(request.form, "sequencing");
    sample_ids = save([save_data]);
    sample_id = sample_ids[0];

    assembly_file = request.files["assembly-file"];
    if assembly_file.filename != "":
        file_data = {"sample_id": sample_id,
                     "file_type_id": request.form["assembly-file-type"],
                     "is_assembly": True,
                     "is_forward_read": None};
        SeqFile.save(file_data);
        filename = SeqFile.fetch_filename(sample_id, ftype="assembly");
        assembly_file.save(os.path.join("/uploads/samples/assemblies",
                                        filename));

    fwread_file = request.files["forward-read-file"];
    if fwread_file.filename != "":
        file_data = {"sample_id": sample_id,
                     "file_type_id": request.form["forward-read-file-type"],
                     "is_assembly": False,
                     "is_forward_read": True};
        SeqFile.save(file_data);
        filename = SeqFile.fetch_filename(sample_id, ftype="fwread");
        fwread_file.save(os.path.join("/uploads/samples/raw", filename));

    rvread_file = request.files["reverse-read-file"];
    if rvread_file.filename != "":
        file_data = {"sample_id": sample_id,
                     "file_type_id": request.form["reverse-read-file-type"],
                     "is_assembly": False,
                     "is_forward_read": False};
        SeqFile.save(file_data);
        filename = SeqFile.fetch_filename(sample_id, ftype="rvread");
        rvread_file.save(os.path.join("/uploads/samples/raw", filename));

    return redirect(url_for('samples_bp.show'));

