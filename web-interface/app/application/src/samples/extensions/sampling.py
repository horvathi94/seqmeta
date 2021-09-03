from .base import SampleExtension


class Sampling(SampleExtension):

    submit_table_name = "samples_sampling";

    clean_keys_strings = ["strain",
                          "isolation_source_host_associated",
                          "isolation_source_non_host_associated",
                          "serotype",
                          "definition_for_seropositive_sample",
                          "passage_method",
                          "sample_storage_conditions"];

    clean_keys_numbers = ["passage_number"];

    clean_keys_select = ["host_anatomical_material_id",
                         "host_body_product_id",
                         "sampling_strategy_id",
                         "purpose_of_samplig_id",
                         "purpose_of_sequencing_id",
                         "sample_capture_status_id",
                         "specimen_source_id"];
