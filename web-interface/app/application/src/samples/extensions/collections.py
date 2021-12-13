from .base import SampleExtension


class Collection(SampleExtension):

    submit_table_name = "samples_collection"

    clean_keys_ints = ["collection_year",
                          "collection_month",
                          "collection_day",]
    clean_keys_strings = ["originating_lab_sample_name",
                          "submitting_lab_sample_name"]
    clean_keys_select = ["collector_id",
                         "collection_device_id",
                         "originating_lab_id",
                         "submitting_lab_id",
                         "author_group_id"]


