from collections import OrderedDict
from datetime import datetime
from .cursor import Cursor
from .db_interface import DBInterface


class SampleLibrary(DBInterface):

    submit_table_name = "samples_library";


    @classmethod
    def clean_submit(cls, entry):
        if entry["layout_paired"] == "":
            entry["layout_paired"] = None;
        elif entry["layout_paired"]:
            entry["layout_paired"] = True;
        else:
            entry["layout_paired"] = False;
        return entry;



class SampleCollection(DBInterface):

    submit_table_name = "samples_collection";





class Samples(DBInterface):

    display_table_name = "view_samples_display";
    edit_table_name = "view_samples_base";
    view_id_key = "sample_id";
    submit_table_name = "samples";
    date_format = "%Y-%m-%d";


    @classmethod
    def clean_entry(cls, entry):
        if "link_library_id" in entry:
            if entry["link_library_id"] == "":
                entry["link_library_id"] = 0;

        if "link_collection_id" in entry:
            if entry["link_collection_id"] == "":
                entry["link_collection_id"] = 0;


        if "patient_gender" in entry:
            if entry["patient_gender"] == "b''":
                entry["patient_gender"] = "unknown";

        if "hospitalization" in entry:
            if entry["hospitalization"] == "b''":
                entry["hospitalization"] = "N/A";

        if "library_layout" in entry:
            if entry["library_layout"] == "b''":
                entry["library_layout"] = "";

        return entry;


    @classmethod
    def fetch_details(cls, sample_id):
        where = "WHERE `sample_id` = {:d}".format(sample_id);
        details = Cursor.select("view_samples_details", clauses=where);
        if len(details) != 1:
            return;
        return details[0];


    @classmethod
    def fetch_entries(cls, table_name, sample_ids=[]):
        if len(sample_ids) == 0:
            return [];

        list_sql = ", ".join(str(sid) for sid in sample_ids);
        where_clause = "WHERE `sample_id` IN ({:s})".format(list_sql);
        entries = Cursor.select(table_name, clauses=where_clause);
        for entry in entries:
            entry = cls.clean_entry(entry);
        return entries;


    @classmethod
    def clean_submit(cls, submitted):
        submitted["id"] = int(submitted["sample_id"]);
        del submitted["sample_id"];
        submitted["name"] = submitted["sample_name"];
        del submitted["sample_name"];
#        if submitted["patient_gender"] == "Male":
#            submitted["patient_gender"] = True;
#        elif submitted["patient_gender"] == "Female":
#            submitted["patient_gender"] = False;
#        else:
#            submitted["patient_gender"] = None;
#
#        if submitted["hospitalization"] == "Yes":
#            submitted["hospitalization"] = True;
#        elif submitted["hospitalization"] == "No":
#            submitted["hospitalization"] = False;
#        else:
#            submitted["hospitalization"] = None;

        return submitted;


    @classmethod
    def save(cls, submitted):
        pass;


