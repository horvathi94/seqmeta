from application.src.db.interface import DBInterface
from application.src.db.cursor import Cursor

class DefaultValues(DBInterface):

    view_tab = "view_default_values";
    save_procedure = "upsert_deftab";

    clean_keys_strings = ["region", "locality"];
    clean_keys_numbers = ["geo_loc_latitude", "geo_loc_longitude"];

    @classmethod
    def fetch(cls):
        vals = Cursor.select(cls.view_tab)[0];
        vals = cls.clean_entry(vals);
        return vals;


    @classmethod
    def save(cls, submitted):
        cls.clean_submit(submitted);
        for key in submitted:
            Cursor.call_procedure(cls.save_procedure,
                                  args=(key, submitted[key]), commit=True);

