from .base import SampleExtension


class Collection(SampleExtension):

    submit_table_name = "samples_collection";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["year"] == "":
            entry["year"] = None;
        if entry["month"] == "":
            entry["month"] = None;
        if entry["day"] == "":
            entry["day"] = None;
        if entry["collector_id"] == "":
            entry["collector_id"] = None;
        return entry;
