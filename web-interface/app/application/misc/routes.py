from flask import Blueprint, request
from .pages.descriptions import LibraryDescription
from .pages.workflows import WorkflowBasic, \
    WorkflowGISAID, WorkflowENA, WorkflowNCBI
from .pages.misc_editor import MiscEditor
from .pages import basic_options as bopt
from .pages import virusname_templates as vnt
from .pages.defaults import DefaultsEditor


misc_bp = Blueprint("misc_bp", __name__,
                    template_folder="templates",
                    static_folder="static",
                    static_url_path="/static/misc/");



@misc_bp.route("/descriptions/library")
def descript_library():
    return LibraryDescription.render();


@misc_bp.route("/misc/edit")
def edit():
    return MiscEditor.render();


@misc_bp.route("/misc/submit/hosts", methods=["POST"])
def submit_hosts():
    return bopt.HostsEditor.parse_and_save(request.form);


@misc_bp.route("/misc/submit/assembly-methods", methods=["POST"])
def submit_assembly_methods():
    return bopt.AssemblyMethodsEditor.parse_and_save(request.form);


@misc_bp.route("/misc/submit/sampling-strategies", methods=["POST"])
def submit_sampling_strategies():
    return bopt.SamplingStrategies.save_by_procedure(request.form);


@misc_bp.route("/misc/submit/specimen-sources", methods=["POST"])
def submit_specimen_sources():
    return bopt.SpecimenSourcesEditor.parse_and_save(request.form);


@misc_bp.route("/misc/submit/collection-devices", methods=["POST"])
def submit_collection_devices():
    return bopt.CollectionDevicesEditor.parse_and_save(request.form);


@misc_bp.route("/misc/submit/host-anatomical-materials", methods=["POST"])
def submit_host_anatomical_materials():
    return bopt.HostAnatomicalMaterialsEditor.parse_and_save(request.form);


@misc_bp.route("/misc/submit/host-body-products", methods=["POST"])
def submit_host_body_products():
    return bopt.HostBodyProductsEditor.parse_and_save(request.form);


@misc_bp.route("/misc/submit/purposes-of-sampling", methods=["POST"])
def submit_purpose_of_sampling():
    return bopt.PurposesOfSamplingEditor.parse_and_save(request.form);


@misc_bp.route("/misc/submit/purposes-of-sequencing", methods=["POST"])
def submit_purpose_of_sequencing():
    return bopt.PurposesOfSequencingEditor.parse_and_save(request.form);



@misc_bp.route("/misc/submit/virusname", methods=["POST"])
def submit_virusname():
    virusname = request.form.to_dict()["virusname"];
    return vnt.GisaidVirusnameEditor.save_and_redirect(virusname);


@misc_bp.route("/misc/submit/isolate-ena", methods=["POST"])
def submit_isolate_ena():
    virusname = request.form.to_dict()["virusname"];
    return vnt.EnaVirusnameEditor.save_and_redirect(virusname);




@misc_bp.route("/default-values")
def edit_default_values():
    return DefaultsEditor.render();


@misc_bp.route("/default-values/submit", methods=["POST"])
def submit_default_values():
    return DefaultsEditor.save(submitted=request.form);



@misc_bp.route("/workflows/basic")
def workflow_basic():
    return WorkflowBasic.render();



@misc_bp.route("/workflows/gisaid")
def workflow_gisaid():
    return WorkflowGISAID.render();


@misc_bp.route("/workflows/ena")
def workflow_ena():
    return WorkflowENA.render();


@misc_bp.route("/workflows/ncbi")
def workflow_ncbi():
    return WorkflowNCBI.render();
