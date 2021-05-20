from .db_interface import DBInterface

class Authors(DBInterface):

    display_table_name = "view_authors";
    edit_table_name = "view_authors";
    submit_table_name = "authors";


    @staticmethod
    def clean_entry(entry):

        if entry["middle_name"] == None:
            entry["middle_name"] = "";
        return entry;

