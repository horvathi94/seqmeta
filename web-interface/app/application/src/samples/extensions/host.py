from .base import SampleExtension


PATIENT_GENDERS = [
{
    "db_value": "",
    "db_save": None,
    "value": 0,
    "label": "N/A"
},
{
    "db_value": 1,
    "db_save": True,
    "value": 1,
    "label": "Male"
},
{
    "db_value": 0,
    "db_save": False,
    "value": 2,
    "label": "Female"
},
];


class Host(SampleExtension):

    submit_table_name = "samples_host";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["patient_age"] == "":
            entry["patient_age"] = None;
        for genders in PATIENT_GENDERS:
            if genders["value"] == int(entry["patient_gender"]):
                entry["patient_gender"] = genders["db_save"];
                break;
        if entry["host_recent_travel_return_date"] == "":
            entry["host_recent_travel_return_date"] = None;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        for layout in PATIENT_GENDERS:
            if layout["db_value"] == entry["patient_gender"]:
                entry["patient_gender"] = layout["value"];
                break;
        if "host_recent_travel_return_date" in entry:
            if entry["host_recent_travel_return_date"] == None:
                entry["host_recent_travel_return_date"] = "";
        return entry;
