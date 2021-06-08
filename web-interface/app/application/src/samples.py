from collections import OrderedDict
from datetime import datetime
from .db.cursor import Cursor
from .db.interface import DBInterface
#from .fast_files import Fasta


class SampleExtended(DBInterface):

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



class SampleLibrary(SampleExtended):

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



class SampleCollection(SampleExtended):

    submit_table_name = "samples_collection";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["year"] == "":
            entry["year"] = None;
        if entry["month"] == "":
            entry["month"] = None;
        if entry["day"] == "":
            entry["day"] = None;
        if entry["collector_id"] == "":
            entry["collector_id"] = None;
        return entry;


class SampleLocation(SampleExtended):

    submit_table_name = "samples_location";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["geo_loc_latitude"] == "":
            entry["geo_loc_latitude"] = None;
        if entry["geo_loc_longitude"] == "":
            entry["geo_loc_longitude"] = None;
        return entry;



class SampleHost(SampleExtended):

    submit_table_name = "samples_host";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["patient_age"] == "":
            entry["patient_age"] = None;
        if entry["patient_gender"] == "":
            entry["patient_gender"] = None;
        elif int(entry["patient_gender"]) == 1:
            entry["patient_gender"] = True;
        elif int(entry["patient_gender"]) == 0:
            entry["patient_gender"] = False;
        return entry;



class SampleSampling(SampleExtended):

    submit_table_name = "samples_sampling";


class SampleHealthStatus(SampleExtended):

    submit_table_name = "samples_health_status";

    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["hospitalization"] == "":
            entry["hospitalization"] = None;
        elif int(entry["hospitalization"]) == 1:
            entry["hospitalization"] = True;
        elif int(entry["hospitalization"]) == 0:
            entry["hospitalization"] = False;
        if entry["ilness_duration"] == "":
            entry["ilness_duration"] = None;
        return entry;


class SampleSequencing(SampleExtended):

    submit_table_name = "samples_sequencing";


    @classmethod
    def clean_submit(cls, entry):
        entry["sample_id"] = int(entry["sample_id"]);
        if entry["coverage"] == "":
            entry["coverage"] = None;
        return entry;



class Samples(DBInterface):

    display_table_name = "view_samples_display";
    edit_table_name = "view_samples_base";
    view_id_key = "sample_id";
    submit_table_name = "samples";
    date_format = "%Y-%m-%d";


    @classmethod
    def clean_entry(cls, entry):

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
        return submitted;


    @classmethod
    def save(cls, submitted):
        pass;

