from .base import SampleExtension


class HealthStatus(SampleExtension):

    submit_table_name = "samples_health_status";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["hospitalization"] == "":
            entry["hospitalization"] = None;
        elif int(entry["hospitalization"]) == 1:
            entry["hospitalization"] = True;
        elif int(entry["hospitalization"]) == 0:
            entry["hospitalization"] = False;
        if entry["ilness_duration"] == "":
            entry["ilness_duration"] = None;
        return entry;
