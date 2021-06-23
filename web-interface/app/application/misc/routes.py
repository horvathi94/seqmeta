from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from application.src.library import LibraryStrategies, \
    LibrarySelections, \
    LibrarySources
from application.src.samples.extensions.library import Library,\
    LIBRARY_LAYOUTS
from application.src.samples.nametemplates.virusname_gisaid import \
    VirusnameGisaid
from application.src.samples.nametemplates.isolate_ena import \
    IsolateEna
from application.src.forms.form import Form
from application.src import misc
from application.src.defaults import DefaultValues
from application.src.institutions import Institutions
from application.src.authors import AuthorGroups

misc_bp = Blueprint("misc_bp", __name__,
                    template_folder="templates",
                    static_folder="static",
                    static_url_path="/static/misc/");


@misc_bp.route("/descriptions/library")
def descript_library():
    styles=[{"filename":"library.css", "prefix":"misc"}];
    html = render_template("head.html", styles=styles);
    html+= render_template("descriptions/library.html",
                           lib_strategies=LibraryStrategies.fetch_list(),
                           lib_sources=LibrarySources.fetch_list(),
                           lib_selections=LibrarySelections.fetch_list());
    html+= render_template("footer.html");
    return html;


@misc_bp.route("/misc/edit")
def edit():
    html = render_template("head.html");
    html+= render_template("misc/specimen_sources.html",
                           items=misc.SpecimenSources.fetch_list());
    html+= render_template("misc/assembly_methods.html",
                           items=misc.AssemblyMethods.fetch_list());
    html+= render_template("misc/virusname.html",
                virusname_format=VirusnameGisaid.fetch_format_string(),
                available_db_keys=VirusnameGisaid.available_db_keys());
    html+= render_template("misc/isolate_ena.html",
                virusname_format=IsolateEna.fetch_format_string(),
                available_db_keys=IsolateEna.available_db_keys());
    html+= render_template("footer.html");
    return html;


@misc_bp.route("/misc/submit/virusname", methods=["POST"])
def submit_virusname():
    virusname = request.form.to_dict()["virusname"];
    VirusnameGisaid.call_save_procedure(virusname);
    return redirect(url_for("misc_bp.edit"));


@misc_bp.route("/misc/submit/isolate-ena", methods=["POST"])
def submit_isolate_ena():
    virusname = request.form.to_dict()["virusname"];
    IsolateEna.call_save_procedure(virusname);
    return redirect(url_for("misc_bp.edit"));


@misc_bp.route("/misc/submit/specimen-sources", methods=["POST"])
def submit_specimen_sources():
    parsed = Form.parse_list(request.form, "specimen_source")[1:];
    misc.SpecimenSources.save_by_procedure(parsed);
    return redirect(url_for("misc_bp.edit"));


@misc_bp.route("/misc/submit/assembly-methods", methods=["POST"])
def submit_assembly_methods():
    parsed = Form.parse_list(request.form, "assembly_methods")[1:];
    misc.AssemblyMethods.save_by_procedure(parsed);
    return redirect(url_for("misc_bp.edit"));


@misc_bp.route("/default-values")
def edit_default_values():
    html = render_template("head.html");
    html+= render_template("defaults/edit.html",
        default_vals=DefaultValues.fetch(),
        continents=misc.Continents.fetch_list(),
        countries=misc.Countries.fetch_list(),
        hosts=misc.Hosts.fetch_list(),
        sampling_strategies=misc.SamplingStrategies.fetch_list(),
        passage_details=misc.PassageDetails.fetch_list(),
        assembly_methods=misc.AssemblyMethods.fetch_list(),
        sequencing_instruments=misc.SequencingInstruments.fetch_list(),
        patient_statuses=misc.PatientStatuses.fetch_list(),
        specimen_sources=misc.SpecimenSources.fetch_list(),
        sample_capture_statuses=misc.SampleCaptureStatuses.fetch_list(),
        host_health_states=misc.HostHealthStates.fetch_list(),
        library_strategies=LibraryStrategies.fetch_list_labeled(
            replace_key="item_key"),
        library_sources=LibrarySources.fetch_list_labeled(
            replace_key="item_key"),
        library_selections=LibrarySelections.fetch_list_labeled(
            replace_key="item_key"),
        library_layouts=LIBRARY_LAYOUTS,
        author_groups=AuthorGroups.fetch_list_labeled(
            replace_key="group_name",
            replace_id="group_id"),
        institutions=Institutions.fetch_list_labeled(),
    );
    html+= render_template("footer.html");
    return html


@misc_bp.route("/default-values/submit", methods=["POST"])
def submit_default_values():
    DefaultValues.save(request.form.to_dict());
    return redirect(url_for("misc_bp.edit_default_values"));
