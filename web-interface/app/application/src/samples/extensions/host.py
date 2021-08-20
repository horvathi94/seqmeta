from .base import SampleExtension
from application.src.misc import Genders


class Host(SampleExtension):

    submit_table_name = "samples_host";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        gend = Genders.get_item_from_value(entry["patient_gender"]);
        entry["patient_gender"] = gend.dbsave;
        if entry["patient_age"] == "":
            entry["patient_age"] = None;
        if entry["host_recent_travel_return_date"] == "":
            entry["host_recent_travel_return_date"] = None;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        gend = Genders.get_item_from_dbvalue(entry["patient_gender"]);
        entry["patient_gender"] = gend.value;
        if "host_recent_travel_return_date" in entry:
            if entry["host_recent_travel_return_date"] == None:
                entry["host_recent_travel_return_date"] = "";
        return entry;
