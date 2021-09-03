from .cursor import Cursor


import sys

class DBInterface:

    display_table_name = "";
    edit_table_name = "";

    view_table_name = "";
    view_id_key = "id";
    edit_table_name = "";
    submit_table_name = "";

    save_procedure = "";

    clean_keys_strings = [];
    clean_keys_numbers = [];
    clean_keys_select = [];


    def __init__(self):
        pass;


    @classmethod
    def clean_fetched_string(cls, entry: dict, key: str) -> dict:
        """Substitutes emtpy string for NULL values retrieved from database."""
        if key in entry and entry[key] is None:
            entry[key] = "";
        return entry;


    @classmethod
    def clean_submit_string(cls, entry: dict, key: str) -> dict:
        if key in entry and entry[key].strip() == "":
            entry[key] = None;
        else:
            entry[key] = entry[key].strip();
        return entry;


    @classmethod
    def clean_submit_number(cls, entry: dict, key: str) -> dict:
        if key in entry and entry[key] == "":
            entry[key] = None;
        else:
            entry[key] = float(entry[key].strip());
        return entry;


    @classmethod
    def clean_submit_select(cls, entry: dict, key: str) -> dict:
        if key in entry:
            if int(entry[key]) == 0:
                entry[key] = None;
            else:
                entry[key] = int(entry[key]);
        return entry;


    @classmethod
    def clean_fetched_number(cls, entry: dict, key: str) -> dict:
        if key in entry and entry[key] is not None:
            entry[key] = float(entry[key]);
        return entry;


    @classmethod
    def clean_entry(cls, entry: dict) -> dict:
        for key in cls.clean_keys_strings:
            entry = cls.clean_fetched_string(entry, key);
        for key in cls.clean_keys_numbers:
            entry = cls.clean_fetched_number(entry, key);
        return entry;


    @classmethod
    def clean_submit(cls, submitted):
        submitted["id"] = int(submitted["id"]);
        for key in cls.clean_keys_strings:
            submitted = cls.clean_submit_string(submitted, key);
        for key in cls.clean_keys_numbers:
            submitted = cls.clean_submit_number(submitted, key);
        for key in cls.clean_keys_select:
            submitted = cls.clean_submit_select(submitted, key);
        return submitted;


    @classmethod
    def fetch_list(cls) -> list:
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

