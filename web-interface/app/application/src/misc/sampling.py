from application.src.db.interface import DBInterface


class SamplingStrategies(DBInterface):

    display_table_name = "view_sampling_strategies";
    edit_table_name = "view_sampling_strategies";
    submit_table_name = "sampling_strategies";
    save_procedure = "upsert_basic_table";



class SpecimenSources(DBInterface):

    display_table_name = "view_specimen_sources";
    edit_table_name = "view_specimen_sources";
    submit_table_name = "specimen_sources";
    save_procedure = "upsert_basic_table";



class SampleCaptureStatuses(DBInterface):

    display_table_name = "sample_capture_status";



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

