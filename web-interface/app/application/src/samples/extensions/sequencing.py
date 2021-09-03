from .base import SampleExtension


class Sequencing(SampleExtension):

    submit_table_name = "samples_sequencing";

    clean_keys_numbers = ["coverage"];
    clean_keys_select = ["sequencing_lab_id",
                         "sequencing_instrument_id"];
