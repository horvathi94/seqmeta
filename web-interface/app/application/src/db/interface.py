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
    def fetch_entry_edit(cls, id=0, id_key="id"):
        entry = Cursor.select(cls.edit_table_name,
                              clauses="WHERE `{:s}` = {:d}"
                                .format(id_key, id));
        if len(entry) != 1:
            return [];
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
            last_id = Cursor.insert_row(cls.submit_table_name, submitted);
        else:
            where = "WHERE `id` = {:d}".format(submitted["id"]);
            last_id = Cursor.update_row(cls.submit_table_name,
                                        where, submitted);
        return last_id




    @staticmethod
    def clean_submit(submitted):
        submitted["id"] = int(submitted["id"]);
        return submitted;


    @classmethod
    def save_by_procedure(cls, items):
        """
            Good for basic tables with columns: | label | indx |
        """
        for item in items:
            args = (cls.submit_table_name,
                    str(item["label"]),
                    int(item["indx"]));
            Cursor.call_procedure("upsert_basic_table",
                                  args=args, commit=True);


    @classmethod
    def fetch_list_labeled(cls, replace_key="name", replace_id="id"):
        items = cls.fetch_list();
        for item in items:
            item["id"] = item.pop(replace_id);
            item["label"] = item.pop(replace_key);
        return items;

