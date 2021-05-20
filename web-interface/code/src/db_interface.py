from .cursor import Cursor

class DBInterface:

    display_table_name = "";
    edit_table_name = "";

    view_table_name = "";
    view_id_key = "id";
    edit_table_name = "";
    submit_table_name = "";

    save_procedure = "";


    def __init__(self):
        pass;


    @staticmethod
    def clean_entry(entry):
        return entry;


    @classmethod
    def fetch_list(cls):
        entries = Cursor.select_all(cls.display_table_name);
        for entry in entries:
            entry = cls.clean_entry(entry);
        if len(entries) == 1 and entries[0][cls.view_id_key] == 0:
            return [];
        return entries;


    @classmethod
    def fetch_entry_edit(cls, id=0):
        entry = Cursor.select(cls.edit_table_name,
                              clauses="WHERE `id` = {:d}".format(id));
        entry = cls.clean_entry(entry[0]);
        return entry;


    @classmethod
    def fetch_entry(cls, id=0):
        entry = Cursor.select(cls.edit_table_name,
                              clauses="WHERE `id` = {:d}".format(id));
        entry = cls.clean_entry(entry[0]);
        return entry;


    @classmethod
    def save_entry(cls, submitted):
        submitted = cls.clean_submit(submitted);
        if submitted["id"] == 0:
            Cursor.insert_row(cls.submit_table_name, submitted);
        else:
            where = "WHERE `id` = {:d}".format(submitted["id"]);
            Cursor.update_row(cls.submit_table_name, where, submitted);



    @staticmethod
    def clean_submit(submitted):
        submitted["id"] = int(submitted["id"]);
        return submitted;


    @classmethod
    def save_by_procedure(cls, items):
        """
            Good for basic tables with columns: | id | label |
        """
        if cls.save_procedure == "":
            return;

        for item in items:
            args = (int(item["id"]), str(item["label"]));
            Cursor.call_procedure(cls.save_procedure, args=args, commit=True);
