from application.src.db.cursor import Cursor
from application.src.db.interface import DBInterface

class SampleExtension(DBInterface):

    @classmethod
    def save_entry(cls, submitted):
        submitted = cls.clean_submit(submitted);
        where_clause = "WHERE sample_id = {:d}".format(
            int(submitted["sample_id"]));
        row_id = Cursor.select(cls.submit_table_name, fields=["sample_id"],
          clauses=where_clause)[0]["sample_id"];

        if row_id == "":
            Cursor.insert_row(cls.submit_table_name, submitted);
        else:
            where = "WHERE `sample_id` = {:d}".format(row_id);
            Cursor.update_row(cls.submit_table_name,
                              where, submitted, id_col="sample_id");


    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        return entry;

