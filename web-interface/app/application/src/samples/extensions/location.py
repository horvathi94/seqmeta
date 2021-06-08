from .base import SampleExtension


class Location(SampleExtension):

    submit_table_name = "samples_location";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["geo_loc_latitude"] == "":
            entry["geo_loc_latitude"] = None;
        if entry["geo_loc_longitude"] == "":
            entry["geo_loc_longitude"] = None;
        return entry;
