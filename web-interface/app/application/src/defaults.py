from .db.interface import DBInterface
from .db.cursor import Cursor


class DefaultValues:

    view_tab = "view_default_values";
    save_procedure = "upsert_deftab";

    @classmethod
    def fetch(cls):
        values = Cursor.select(cls.view_tab)[0];
        values["geo_loc_latitude"] = float(values["geo_loc_latitude"]) \
            if values["geo_loc_latitude"] != None else None;
        values["geo_loc_longitude"] = float(values["geo_loc_longitude"]) \
            if values["geo_loc_longitude"] != None else None;
        return values;

    @classmethod
    def save(cls, submitted):
        for key in submitted:
            Cursor.call_procedure(cls.save_procedure,
                                  args=(key, submitted[key]),
                                  commit=True);
