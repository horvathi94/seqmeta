from application.src.db.interface import DBInterface
from application.src.db.cursor import Cursor


class Field(DBInterface):

    display_table_name = "fields";


    @staticmethod
    def parse_req(raw, key):
        if raw[key] == None:
            return None;
        level = "";
        if raw[key] == 3:
            level = "mandatory";
        elif raw[key] == 2:
            level = "recommended";
        elif raw[key] == 1:
            level = "optional";
        return {
            "type": key,
            "level": level};


    @classmethod
    def fetch(cls, handle):
        where_clause = "WHERE handle = '{:s}'".format(handle);
        raw ,= Cursor.select(cls.display_table_name,
                      clauses=where_clause);
        field = {};
        field["field_name"] = raw["field_name"].strip();
        field["field_type"] = raw["field_type"].strip();
        field["requirement"] = [];
        gisaid = cls.parse_req(raw, "gisaid");
        if gisaid != None:
            field["requirement"].append(gisaid);
        ena = cls.parse_req(raw, "ena");
        if ena != None:
            field["requirement"].append(ena);
        ncbi = cls.parse_req(raw, "ncbi");
        if ncbi != None:
            field["requirement"].append(ncbi);
        field["input"] = {};
        field["input"]["name_single"] = raw["prefix"] + "+" + raw["name"];
        field["input"]["class"] = raw["class"];
        if raw["field_type"] == "text":
            field["input"]["maxlength"] = raw["max_val"] \
                if raw["max_val"] != None else 0;
            field["value"] = "";
        if raw["field_type"] == "number":
            field["input"]["min"] = float(raw["min_val"]) \
                if raw["min_val"] != None else "";
            field["input"]["max"] = float(raw["max_val"]) \
                if raw["max_val"] != None else "";
            field["input"]["step"] = float(raw["step"]) \
                if raw["step"] != None else 1;
            field["value"] = "";
        field["description"] = str(raw["description"].strip());
        return field;
