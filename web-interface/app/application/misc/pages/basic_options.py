from flask import render_template, redirect, url_for
from dataclasses import dataclass
from application.src import misc
from application.src.forms.form import Form


@dataclass
class BasicOptionEditor:

    name: str = "";
    id: str = "";
    link: str = "";
    description: str = "";
    redirect_after_save = "misc_bp.edit";


    @classmethod
    def get_values(cls) -> list:
        """Get values stored in the database."""
        pass;


    @classmethod
    def render(cls):
        """Render basic options form for the object."""
        return render_template("misc/basic_options.html",
                               info=cls, vals=cls.get_values());


    @classmethod
    def save(cls, data: list) -> None:
        """Save to database"""
        pass;


    @classmethod
    def parse_and_save(cls, form_data: list) -> "flask.redirect":
        """Parse the submitted form data and save to the database."""
        parsed = Form.parse_list(form_data, cls.id)[1:];
        cls.save(parsed);
        return redirect(url_for(cls.redirect_after_save));




@dataclass
class AssemblyMethodsEditor(BasicOptionEditor):

    name = "Assembly methods";
    id = "assembly_methods";
    link = "misc_bp.submit_assembly_methods";
    description = "Programs with which the assembly " \
        "of the sequences was performed.";

    @classmethod
    def get_values(cls) -> list:
        return misc.AssemblyMethods.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        misc.AssemblyMethods.save_by_procedure(data);



@dataclass
class SamplingStrategiesEditor(BasicOptionEditor):

    name = "Sampling strategies";
    id = "sampling_strategies";
    link = "misc_bp.submit_sampling_strategies";
    description = "The sampling strategy used to select the sample.";

    @classmethod
    def get_values(cls) -> list:
        return misc.SamplingStrategies.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        misc.SamplingMethods.save_by_procedure(data);



@dataclass
class SpecimenSourcesEditor(BasicOptionEditor):

    name = "Specimen sources";
    id = "specimen_sources";
    link = "misc_bp.submit_specimen_sources";
    description = "Source of the specimen.";

    @classmethod
    def get_values(cls) -> list:
        return misc.SpecimenSources.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        misc.SpecimenSources.save_by_procedure(data);



@dataclass
class CollectionDevicesEditor(BasicOptionEditor):

    name = "Collection devices";
    id = "collection_devices";
    link = "misc_bp.submit_collection_devices";
    description = "Instrument or container used to collect sample" \
        "<em>e.g. swab.</em>";

    @classmethod
    def get_values(cls) -> list:
        return misc.CollectionDevices.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        misc.CollectionDevices.save_by_procedure(data);



@dataclass
class HostAnatomicalMaterialsEditor(BasicOptionEditor):

    name = "Host anatomical materials";
    id = "host_anatomical_materials";
    link = "misc_bp.submit_host_anatomical_materials";
    description = "Host anatomical material or substance produced by the " \
        "body where the sample was obtained "\
        "<em>e.g., stool, mucus, saliva</em>";

    @classmethod
    def get_values(cls) -> list:
        return misc.HostAnatomicalMaterials.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        misc.HostAnatomicalMaterials.save_by_procedure(data);



@dataclass
class HostBodyProductsEditor(BasicOptionEditor):

    name = "Host body products";
    id = "host_body_products";
    link = "misc_bp.submit_host_body_products";
    description = "Substance produced by the host" \
        "<em>e.g. stool mucus</em>, where the sample was obtained from."

    @classmethod
    def get_values(cls) -> list:
        return misc.HostBodyProducts.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        misc.HostBodyProducts.save_by_procedure(data);



@dataclass
class PurposesOfSamplingEditor(BasicOptionEditor):

    name = "Purpose of sampling";
    id = "purpose_of_sampling";
    link = "misc_bp.submit_purpose_of_sampling";
    description = "The reason the sample was collected " \
        "<em>e.g. diagnostic testing</em>";

    @classmethod
    def get_values(cls) -> list:
        return misc.PurposesOfSampling.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        misc.PurposesOfSampling.save_by_procedure(data);



@dataclass
class PurposesOfSequencingEditor(BasicOptionEditor):

    name = "Purpose of sequencing";
    id = "purpose_of_sequencing";
    link = "misc_bp.submit_purpose_of_sequencing";
    description = "The reason the sample was sequenced " \
        "<em>e.g. baseline surveillance (random sampling)</em>";

    @classmethod
    def get_values(cls) -> list:
        return misc.PurposesOfSequencing.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        misc.PurposesOfSequencing.save_by_procedure(data);



@dataclass
class HostsEditor(BasicOptionEditor):

    id: str = "hosts";

    @classmethod
    def get_values(cls) -> list:
        return misc.Hosts.fetch_list();


    @classmethod
    def render(cls):
        """Render basic options form for the object."""
        return render_template("misc/hosts.html", hosts=cls.get_values());


    @classmethod
    def save(cls, data: list) -> None:
        misc.Hosts.save_by_procedure(data);
