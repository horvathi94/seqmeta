from .base import SampleExtension
from application.src.misc.host import Genders


class Host(SampleExtension):

    submit_table_name = "samples_host";


    clean_keys_strings = ["host_subject_id", "ppe",
                          "host_description", "gravidity",
                          "additional_host_info", "host_recent_travel_loc",
                          "host_recent_travel_return_date"];
    clean_keys_numbers = ["patient_age"]
    clean_keys_select = ["host_id",
                         "patient_status_id",
                         "host_habitat_id",
                         "host_behaviour_id",];


    @classmethod
    def extra_clean_submitted(cls, entry: dict) -> dict:
        if not "patient_gender" in entry:
            return entry;
        gend = Genders.get_item_from_value(int(entry["patient_gender"]));
        entry["patient_gender"] = gend.dbsave;
        return entry;


    @classmethod
    def clean_entry(cls, entry: dict) -> dict:
        for key in cls.clean_keys_strings:
            entry = cls.clean_fetched_string(entry, key);
        for key in cls.clean_keys_numbers:
            entry = cls.clean_fetched_number(entry, key);
        if not "patient_gender" in entry:
            return entry;
        gend = Genders.get_item_from_dbvalue(entry["patient_gender"]);
        entry["patient_gender"] = gend.value;
        return entry;
