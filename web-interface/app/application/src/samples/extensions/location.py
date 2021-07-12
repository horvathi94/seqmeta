from .base import SampleExtension


class Location(SampleExtension):

    submit_table_name = "samples_location";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if "geo_loc_latitude" in entry:
            if entry["geo_loc_latitude"] == "":
                entry["geo_loc_latitude"] = None;
        if "geo_loc_longitude" in entry:
            if entry["geo_loc_longitude"] == "":
                entry["geo_loc_longitude"] = None;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        if "geo-loc-latitude" in entry:
            if entry["geo-loc-latitude"] == None:
                entry["geo-loc-latitude"] = "";
            else:
                entry["geo-loc-latitude"] = float(entry["geo-loc-latitude"])
        if "geo-loc-longitude" in entry:
            if entry["geo-loc-longitude"] == None:
                entry["geo-loc-longitude"] = "";
            else:
                entry["geo-loc-longitude"] = float(entry["geo-loc-longitude"])
        return entry;
