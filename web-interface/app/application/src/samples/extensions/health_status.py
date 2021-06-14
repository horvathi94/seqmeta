from .base import SampleExtension

HOSPITALISATIONS = [
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
    "label": "Yes"
},
{
    "db_value": 0,
    "db_save": False,
    "value": 2,
    "label": "No"
},
];


class HealthStatus(SampleExtension):

    submit_table_name = "samples_health_status";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        for hosp in HOSPITALISATIONS:
            if hosp["value"] == int(entry["hospitalization"]):
                entry["hospitalization"] = hosp["db_save"];
                break;
        if entry["ilness_duration"] == "":
            entry["ilness_duration"] = None;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        for hosp in HOSPITALISATIONS:
            if hosp["db_value"] == entry["hospitalization"]:
                entry["hospitalization"] = hosp["value"];
                break;
        return entry;
