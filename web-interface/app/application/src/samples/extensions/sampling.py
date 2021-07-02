from .base import SampleExtension


class Sampling(SampleExtension):

    submit_table_name = "samples_sampling";


    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if "passage_number" in entry:
            if entry["passage_number"] == "":
                entry["passage_number"] = None;
        return entry;
