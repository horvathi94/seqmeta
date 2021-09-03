from .base import SampleExtension
from application.src.misc.health import Hospitalisation


class HealthStatus(SampleExtension):

    submit_table_name = "samples_health_status";

    clean_keys_strings = ["subject_exposure",
                          "subject_exposure_duration",
                          "type_exposure",
                          "outbreak",
                          "ilness_symptoms",
                          "ilness_duration",];
    clean_keys_numbers = ["sars_cov_2_diag_pcr_ct_value_1",
                          "sars_cov_2_diag_pcr_ct_value_2"];
    clean_keys_select = ["host_health_state_id",
                         "host_disease_outcome_id",
                         "sars_cov_2_diag_gene_name_1_id",
                         "sars_cov_2_diag_gene_name_2_id"];


    @classmethod
    def extra_clean_submitted(cls, entry: dict) -> dict:
        hosp = Hospitalisation.get_item_from_value(entry["hospitalization"]);
        entry["hospitalization"] = hosp.dbsave;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        for key in cls.clean_keys_strings:
            entry = cls.clean_fetched_string(entry, key);
        for key in cls.clean_keys_numbers:
            entry = cls.clean_fetched_number(entry, key);
        if not "hospitalization" in entry:
            return entry;
        hosp = Hospitalisation.get_item_from_dbvalue(entry["hospitalization"]);
        entry["hospitalization"] = hosp.value;
        return entry;
