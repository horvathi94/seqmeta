from .base import SampleExtension


class Collection(SampleExtension):

    submit_table_name = "samples_collection";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["collection_year"] == "":
            entry["collection_year"] = None;
        if entry["collection_month"] == "":
            entry["collection_month"] = None;
        if entry["collection_day"] == "":
            entry["collection_day"] = None;
        if entry["collector_id"] == "":
            entry["collector_id"] = None;
        return entry;
