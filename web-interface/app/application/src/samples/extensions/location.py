from .base import SampleExtension


class Location(SampleExtension):

    submit_table_name = "samples_location";

    clean_keys_numbers = ["geo_loc_latitude",
                          "geo_loc_longitude"];
    clean_keys_strings = ["region", "locality",
                          "additional_location_info"];
    clean_keys_select = ["continent_id",
                         "country_id",
                         "geo_loc_exposure_id"];


