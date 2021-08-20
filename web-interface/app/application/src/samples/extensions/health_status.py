from .base import SampleExtension
from application.src.misc import Hospitalisation

HOSPITALISATIONS = [
{
    "db_value": None,
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
        hosp = Hospitalisation.get_item_from_value(entry["hospitalization"]);
        entry["hospitalization"] = hosp.dbsave;
        if entry["ilness_duration"] == "":
            entry["ilness_duration"] = None;
        if "sars_cov_2_diag_pcr_ct_value_1" in entry:
            if entry["sars_cov_2_diag_pcr_ct_value_1"] == "":
                entry["sars_cov_2_diag_pcr_ct_value_1"] = None;
        if "sars_cov_2_diag_pcr_ct_value_2" in entry:
            if entry["sars_cov_2_diag_pcr_ct_value_2"] == "":
                entry["sars_cov_2_diag_pcr_ct_value_2"] = None;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        hosp = Hospitalisation.get_item_from_dbvalue(entry["hospitalization"]);
        entry["hospitalization"] = hosp.value;
        return entry;
