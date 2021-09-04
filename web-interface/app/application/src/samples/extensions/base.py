from application.src.db.cursor import Cursor
from application.src.db.interface import DBInterface

import sys


class SampleExtension(DBInterface):


    @classmethod
    def save_entry(cls, submitted):
        submitted = cls.clean_submit(submitted);
        where = f"WHERE sample_id = {int(submitted['sample_id'])}";
        row_id = Cursor.select(cls.submit_table_name, fields=["sample_id"],
          clauses=where)[0]["sample_id"];

        if row_id == "":
            Cursor.insert_row(cls.submit_table_name, submitted);
        else:
            where = "WHERE `sample_id` = {:d}".format(row_id);
            Cursor.update_row(cls.submit_table_name,
                              where, submitted, id_col="sample_id");


    @classmethod
    def extra_clean_submitted(cls, entry: dict) -> dict:
        return entry;


    @classmethod
    def clean_submit(cls, submitted):
        submitted["sample_id"] = int(submitted["sample_id"]);
        for key in cls.clean_keys_strings:
            submitted = cls.clean_submit_string(submitted, key);
        for key in cls.clean_keys_floats:
            submitted = cls.clean_submit_number(submitted, key);
        for key in cls.clean_keys_ints:
            submitted = cls.clean_submit_number(submitted, key, type="int");
        for key in cls.clean_keys_select:
            submitted = cls.clean_submit_select(submitted, key);
        submitted = cls.extra_clean_submitted(submitted);
        return submitted;
