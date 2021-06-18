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
        values["region"] = values["region"] \
            if values["region"] != None else "";
        values["locality"] = values["locality"] \
            if values["locality"] != None else "";
        return values;

    @classmethod
    def save(cls, submitted):
        cls.clean_submit(submitted);
        for key in submitted:
            Cursor.call_procedure(cls.save_procedure,
                                  args=(key, submitted[key]),
                                  commit=True);


    @classmethod
    def clean_submit(cls, submitted):
        if submitted["geo_loc_latitude"] == "":
            submitted["geo_loc_latitude"] = None;
        if submitted["geo_loc_longitude"] == "":
            submitted["geo_loc_longitude"] = None;
        if submitted["region"] == "":
            submitted["region"] = None;
        if submitted["locality"] == "":
            submitted["locality"] = None;
