from .base import SampleExtension


class SampleSequencing(SampleExtension):

    submit_table_name = "samples_sequencing";


    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["coverage"] == "":
            entry["coverage"] = None;
        return entry;
