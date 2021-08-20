from .base import SampleExtension
from application.src.misc import ReceivedTreatment, PriorInfection


class PatientTreatment(SampleExtension):

    submit_table_name = "samples_patient_treatment";


    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        treat = ReceivedTreatment.get_item_from_value(
            entry["prior_sars_cov_2_antiviral_treat"]);
        entry["prior_sars_cov_2_antiviral_treat"] = treat.dbvalue;
        infect = PriorInfection.get_item_from_value(
            entry["prior_sars_cov_2_infection"]);
        entry["prior_sars_cov_2_infection"] = infect.dbvalue;
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
        treat = ReceivedTreatment.get_item_from_dbvalue(
            entry["prior_sars_cov_2_antiviral_treat"]);
        entry["prior_sars_cov_2_antiviral_treat"] = treat.value;
        infect = PriorInfection.get_item_from_dbvalue(
            entry["prior_sars_cov_2_infection"]);
        entry["prior_sars_cov_2_infection"] = infect.value;
        if entry["date_of_prior_antiviral_treat"] == None:
           entry["date_of_prior_antiviral_treat"] = "";
        if entry["date_of_prior_sars_cov_2_infection"] == None:
           entry["date_of_prior_sars_cov_2_infection"] = "";
        if entry["date_of_prior_sars_cov_2_vaccination"] == None:
           entry["date_of_prior_sars_cov_2_vaccination"] = "";
        return entry;
