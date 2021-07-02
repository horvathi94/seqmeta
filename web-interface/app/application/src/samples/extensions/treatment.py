from .base import SampleExtension

ANTIVIRAL_TREAT = [
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

PRIOR_INFECTION = [
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


class PatientTreatment(SampleExtension):

    submit_table_name = "samples_patient_treatment";


    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        for item in ANTIVIRAL_TREAT:
            if item["value"] == int(entry["prior_sars_cov_2_antiviral_treat"]):
                entry["prior_sars_cov_2_antiviral_treat"] = item["db_save"];
                break;
        for item in PRIOR_INFECTION:
            if item["value"] == int(entry["prior_sars_cov_2_infection"]):
                entry["prior_sars_cov_2_infection"] = item["db_save"];
                break;
        if "date_of_prior_antiviral_treat" in entry:
            if entry["date_of_prior_antiviral_treat"] == "":
                entry["date_of_prior_antiviral_treat"] = None;
        if "date_of_prior_sars_cov_2_infection" in entry:
            if entry["date_of_prior_sars_cov_2_infection"] == "":
                entry["date_of_prior_sars_cov_2_infection"] = None;
        if "date_of_prior_sars_cov_2_vaccination" in entry:
            if entry["date_of_prior_sars_cov_2_vaccination"] == "":
                entry["date_of_prior_sars_cov_2_vaccination"] = None;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        for item in ANTIVIRAL_TREAT:
            if item["db_value"] == entry["prior_sars_cov_2_antiviral_treat"]:
                entry["prior_sars_cov_2_antiviral_treat"] = item["value"];
                break;
        for item in PRIOR_INFECTION:
            if item["db_value"] == entry["prior_sars_cov_2_infection"]:
                entry["prior_sars_cov_2_infection"] = item["value"];
                break;
        if entry["date_of_prior_antiviral_treat"] == None:
           entry["date_of_prior_antiviral_treat"] = "";
        if entry["date_of_prior_sars_cov_2_infection"] == None:
           entry["date_of_prior_sars_cov_2_infection"] = "";
        if entry["date_of_prior_sars_cov_2_vaccination"] == None:
           entry["date_of_prior_sars_cov_2_vaccination"] = "";
        return entry;
