from flask import Blueprint, render_template, request, redirect, url_for
from application.src.samples.nametemplates.virusname_gisaid import \
    VirusnameGisaid
from application.src.samples.nametemplates.isolate_ena import \
    IsolateEna
from application.src.forms.form import Form
from application.src import misc
from application.src.defaults import DefaultValues
from application.src.institutions import Institutions
from application.src.authors import AuthorGroups
from .editors import defaults
from application.src.fields import Field
from . import basic_editors
from application.src.defaults import DefaultValues


from .pages.descriptions import LibraryDescription
from .pages.workflows import WorkflowBasic, \
    WorkflowGISAID, WorkflowENA, WorkflowNCBI
from .pages.misc_editor import MiscEditor
from .pages import basic_options as bopt


misc_bp = Blueprint("misc_bp", __name__,
                    template_folder="templates",
                    static_folder="static",
                    static_url_path="/static/misc/");



@misc_bp.route("/descriptions/library")
def descript_library():
    return LibraryDescription.show();



@misc_bp.route("/misc/edit")
def edit():
    """Editor for misc values."""
    return MiscEditor.show();



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



@misc_bp.route("/misc/submit/hosts", methods=["POST"])
def submit_hosts():
    parsed = Form.parse_list(request.form, "hosts")[1:];
    misc.Hosts.save_by_procedure(parsed);
    return redirect(url_for("misc_bp.edit"));



@misc_bp.route("/misc/submit/specimen-sources", methods=["POST"])
def submit_specimen_sources():
    return bopt.SpecimenSourcesEditor.parse_and_save(request.form);

#    parsed = Form.parse_list(request.form, "specimen_sources")[1:];
#    misc.SpecimenSources.save_by_procedure(parsed);
#    return redirect(url_for("misc_bp.edit"));



@misc_bp.route("/misc/submit/assembly-methods", methods=["POST"])
def submit_assembly_methods():
    parsed = Form.parse_list(request.form, "assembly_methods")[1:];
    misc.AssemblyMethods.save_by_procedure(parsed);
    return redirect(url_for("misc_bp.edit"));



@misc_bp.route("/misc/submit/sampling-strategies", methods=["POST"])
def submit_sampling_strategies():
    parsed = Form.parse_list(request.form, "sampling_strategies")[1:];
    misc.SamplingStrategies.save_by_procedure(parsed);
    return redirect(url_for("misc_bp.edit"));



@misc_bp.route("/misc/submit/collection-devices", methods=["POST"])
def submit_collection_devices():
    parsed = Form.parse_list(request.form, "collection_devices")[1:];
    misc.CollectionDevices.save_by_procedure(parsed);
    return redirect(url_for("misc_bp.edit"));



@misc_bp.route("/misc/submit/host-anatomical-materials", methods=["POST"])
def submit_host_anatomical_materials():
    parsed = Form.parse_list(request.form, "host_anatomical_materials")[1:];
    misc.HostAnatomicalMaterials.save_by_procedure(parsed);
    return redirect(url_for("misc_bp.edit"));



@misc_bp.route("/misc/submit/host-body-products", methods=["POST"])
def submit_host_body_products():
    parsed = Form.parse_list(request.form, "host_body_products")[1:];
    misc.HostBodyProducts.save_by_procedure(parsed);
    return redirect(url_for("misc_bp.edit"));



@misc_bp.route("/misc/submit/purposes-of-sampling", methods=["POST"])
def submit_purpose_of_sampling():
    parsed = Form.parse_list(request.form, "purpose_of_sampling")[1:];
    misc.PurposesOfSampling.save_by_procedure(parsed);
    return redirect(url_for("misc_bp.edit"));



@misc_bp.route("/misc/submit/purposes-of-sequencing", methods=["POST"])
def submit_purpose_of_sequencing():
    parsed = Form.parse_list(request.form, "purpose_of_sequencing")[1:];
    misc.PurposesOfSequencing.save_by_procedure(parsed);
    return redirect(url_for("misc_bp.edit"));


@misc_bp.route("/default-values")
def edit_default_values():
    styles = [{"filename": "markers.css"}];
    html = render_template("head.html", styles=styles);
    html+= defaults.Editor.show();
    html+= render_template("footer.html");
    return html;


@misc_bp.route("/default-values/submit", methods=["POST"])
def submit_default_values():
    DefaultValues.save(request.form.to_dict());
    return redirect(url_for("misc_bp.edit_default_values"));




@misc_bp.route("/workflows/basic")
def workflow_basic():
    return WorkflowBasic.show();



@misc_bp.route("/workflows/gisaid")
def workflow_gisaid():
    return WorkflowGISAID.show();


@misc_bp.route("/workflows/ena")
def workflow_ena():
    return WorkflowENA.show();


@misc_bp.route("/workflows/ncbi")
def workflow_ncbi():
    return WorkflowNCBI.show();
