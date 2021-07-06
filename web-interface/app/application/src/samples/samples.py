from collections import OrderedDict
from datetime import datetime
from application.src.db.cursor import Cursor
from application.src.db.interface import DBInterface
from .extensions.library import Library
from .extensions.host import Host
from .extensions.health_status import HealthStatus
from .extensions.treatment import PatientTreatment

class Samples(DBInterface):

    display_table_name = "view_samples_display";
    edit_table_name = "view_samples_base";
    view_id_key = "sample_id";
    submit_table_name = "samples";
    date_format = "%Y-%m-%d";


    @classmethod
    def clean_entry(cls, entry):
        if "hospitalization" in entry:
            entry = HealthStatus.clean_entry(entry);
        if "patient_gender" in entry:
            entry = Host.clean_entry(entry);
        if "library_layout_paired" in entry:
            entry = Library.clean_entry(entry);
        if "prior_sars_cov_2_antiviral_treat" in entry:
            entry = PatientTreatment.clean_entry(entry);
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
        if "sample_id" in submitted:
            submitted["id"] = int(submitted["sample_id"]);
            del submitted["sample_id"];
        if "sample_name" in submitted:
            submitted["name"] = submitted["sample_name"];
            del submitted["sample_name"];
        if "sample_comment" in submitted:
            submitted["comment"] = submitted["sample_comment"];
            del submitted["sample_comment"];
        if "sample_title" in submitted:
            submitted["title"] = submitted["sample_title"];
            del submitted["sample_title"];
        if "sample_description" in submitted:
            submitted["description"] = submitted["sample_description"];
            del submitted["sample_description"];
        return submitted;


    @classmethod
    def save(cls, submitted):
        pass;


    @classmethod
    def fetch(cls, table_name, sample_id=0):
        where_clause = "WHERE `sample_id` = {:d}".format(sample_id);
        entry, = Cursor.select(table_name, clauses=where_clause);
        entry = cls.clean_entry(entry);
        return entry;
