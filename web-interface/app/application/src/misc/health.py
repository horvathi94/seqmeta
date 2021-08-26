from application.src.db.interface import DBInterface
from application.src.fields.radio import RadioValue, RadioList


class ReceivedTreatment(RadioList):

    items = [
        RadioValue(),
        RadioValue("Yes", 1, 1, True),
        RadioValue("No", 2, 0, False),
    ];



class PriorInfection(RadioList):

    items = [
        RadioValue(),
        RadioValue("Yes", 1, 1, True),
        RadioValue("No", 2, 0, False),
    ];



class Hospitalisation(RadioList):

    items = [
        RadioValue(),
        RadioValue("Yes", 1, 1, True),
        RadioValue("No", 2, 0, False),
    ];



class PatientStatuses(DBInterface):

    display_table_name = "view_patient_statuses";
    edit_table_name = "view_patient_statuses";
    submit_table_name = "patient_statuses";
    save_procedure = "upsert_basic_table";



class HostDiseaseOutcomes(DBInterface):

    display_table_name = "host_disease_outcome";



class HostHealthStates(DBInterface):

    display_table_name = "host_health_states";



class HasVaccine(DBInterface):

    display_table_name = "has_received_vaccine";
