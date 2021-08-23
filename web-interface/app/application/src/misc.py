from dataclasses import dataclass
from .db.cursor import Cursor
from .db.interface import DBInterface
from .fields.radio import RadioValue, RadioList


class Genders(RadioList):

    items = [
        RadioValue(),
        RadioValue("Male", 1, 1, True),
        RadioValue("Female", 2, 0, False),
    ];


class ReceivedTreatment(RadioList):

    items = [
        RadioValue(),
        RadioValue("Yes", 1, 1, True),
        RadioValue("No", 2, 0, False),
    ];


class PriorInfection(RadioList):

    items = [
        RadioValue(),
        RadioValue("Yes", 1, 1, True),
        RadioValue("No", 2, 0, False),
    ];


class Hospitalisation(RadioList):

    items = [
        RadioValue(),
        RadioValue("Yes", 1, 1, True),
        RadioValue("No", 2, 0, False),
    ];


class LibraryLayouts(RadioList):

    items = [
        RadioValue(),
        RadioValue("Paired-end", 1, 1, True),
        RadioValue("Single", 2, 0, False),
    ];



class Countries(DBInterface):
    display_table_name = "countries";


class Continents(DBInterface):
    display_table_name = "continents";



class Hosts(DBInterface):

    display_table_name = "view_hosts";
    edit_table_name = "view_hosts";
    submit_table_name = "hosts";
    save_procedure = "upsert_hosts";

    @classmethod
    def save_by_procedure(cls, items):
        for item in items:
            args = (str(item["label"]),
                    str(item["latin"]),
                    int(item["indx"]));
            Cursor.call_procedure(cls.save_procedure, args=args, commit=True);



class SamplingStrategies(DBInterface):

    display_table_name = "view_sampling_strategies";
    edit_table_name = "view_sampling_strategies";
    submit_table_name = "sampling_strategies";
    save_procedure = "upsert_basic_table";



class PassageDetails(DBInterface):

    display_table_name = "view_passage_details";
    edit_table_name = "view_passage_details";
    submit_table_name = "passage_details";
    save_procedure = "upsert_basic_table";



class AssemblyMethods(DBInterface):

    display_table_name = "view_assembly_methods";
    edit_table_name = "view_assembly_methods";
    submit_table_name = "assembly_methods";
    save_procedure = "upsert_basic_table";



class PatientStatuses(DBInterface):

    display_table_name = "view_patient_statuses";
    edit_table_name = "view_patient_statuses";
    submit_table_name = "patient_statuses";
    save_procedure = "upsert_basic_table";



class SpecimenSources(DBInterface):

    display_table_name = "view_specimen_sources";
    edit_table_name = "view_specimen_sources";
    submit_table_name = "specimen_sources";
    save_procedure = "upsert_basic_table";


class SampleCaptureStatuses(DBInterface):

    display_table_name = "sample_capture_status";


class HostDiseaseOutcomes(DBInterface):

    display_table_name = "host_disease_outcome";


class HostHealthStates(DBInterface):

    display_table_name = "host_health_states";


class HostHabitats(DBInterface):

    display_table_name = "host_habitats";


class HostBehaviours(DBInterface):

    display_table_name = "host_behaviours";


class SequencingInstruments(DBInterface):

    display_table_name = "sequencing_instruments";


class HasVaccine(DBInterface):
    display_table_name = "has_received_vaccine";


class SarsCovGenes(DBInterface):
    display_table_name = "sars_cov_2_genes";


class HostAnatomicalMaterials(DBInterface):
    display_table_name = "view_host_anatomical_materials";
    edit_table_name = "view_host_anatomical_materials";
    submit_table_name = "host_anatomical_materials";
    save_procedure = "upsert_basic_table";


class HostBodyProducts(DBInterface):
    display_table_name = "view_host_body_products";
    edit_table_name = "view_host_body_products";
    submit_table_name = "host_body_products";
    save_procedure = "upsert_basic_table";


class PurposesOfSampling(DBInterface):
    display_table_name = "purposes_of_sampling";
    edit_table_name = "view_purposes_of_sampling";
    submit_table_name = "purposes_of_sampling";
    save_procedure = "upsert_basic_table";


class PurposesOfSequencing(DBInterface):
    display_table_name = "purposes_of_sequencing";
    edit_table_name = "view_purposes_of_sequencing";
    submit_table_name = "purposes_of_sequencing";
    save_procedure = "upsert_basic_table";


class CollectionDevices(DBInterface):
    display_table_name = "view_collection_devices";
    edit_table_name = "view_collection_devices";
    submit_table_name = "collection_devices";
    save_procedure = "upsert_basic_table";

