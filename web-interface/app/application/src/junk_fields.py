from datetime import datetime
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
        field["field_name"] = str(raw["field_name"].strip());
        field["field_type"] = raw["field_type"].strip();
        field["db_key"] = raw["db_key"];
        field["handle"] = raw["handle"];
        field["edit_all"] = raw["edit_all"];
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
        field["input"]["name_single"] = raw["prefix"] + "+" + raw["db_key"];
        field["input"]["multi_all"] = raw["prefix"]+"-"+raw["db_key"]+"-all";
        field["input"]["multi_template"] = raw["prefix"]+"+0+"+raw["db_key"];
        field["input"]["defaults"] = raw["db_key"];
        field["input"]["class"] = raw["class"];
        field["input"]["onchange"] = "";
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
        if raw["field_type"] == "date":
            date = "";
            if raw["min_date"] != None:
                date = raw["min_date"].strftime("%Y-%m-%d");
            field["input"]["min"] = date;
            date = "";
            if raw["max_date"] != None:
                date = raw["max_date"].strftime("%Y-%m-%d");
            field["input"]["max"] = date;
            field["value"] = "";
        if raw["field_type"] == "seqfile":
            field["input"]["multi_template"] = \
                raw["prefix"]+"+0+"+raw["db_key"];
            field["file_type"] = raw["db_key"];
        field["description"] = str(raw["description"].strip());
        return field;
