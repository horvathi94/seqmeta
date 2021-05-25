from .db_interface import DBInterface


class Studies(DBInterface):

    display_table_name = "ena_studies";
    submit_table_name = "ena_studies";
