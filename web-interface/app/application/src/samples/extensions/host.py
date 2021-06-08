from .base import SampleExtension


class Host(SampleExtension):

    submit_table_name = "samples_host";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["patient_age"] == "":
            entry["patient_age"] = None;
        if entry["patient_gender"] == "":
            entry["patient_gender"] = None;
        elif int(entry["patient_gender"]) == 1:
            entry["patient_gender"] = True;
        elif int(entry["patient_gender"]) == 0:
            entry["patient_gender"] = False;
        return entry;
