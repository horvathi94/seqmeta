from collections import OrderedDict
from datetime import datetime
from application.src.db.cursor import Cursor
from application.src.db.interface import DBInterface
from .extensions.library import Library
from .extensions.host import Host
from .extensions.health_status import HealthStatus
from .extensions.treatment import PatientTreatment
from .extensions.location import Location

class Samples(DBInterface):

    display_table_name = "view_samples_display";
    edit_table_name = "view_samples_base";
    view_id_key = "sample_id";
    submit_table_name = "samples";
    date_format = "%Y-%m-%d";


    @classmethod
    def clean_entry(cls, entry: dict) -> dict:
        """Clean data fetched from the database."""
        if "hospitalization" in entry:
            entry = HealthStatus.clean_entry(entry);
        if "patient_gender" in entry:
            entry = Host.clean_entry(entry);
        if "library_layout_paired" in entry:
            entry = Library.clean_entry(entry);
        if "prior_sars_cov_2_antiviral_treat" in entry:
            entry = PatientTreatment.clean_entry(entry);
        if "geo-loc-longitude" in entry:
            entry = Location.clean_entry(entry);
        return entry;


    @classmethod
    def fetch_details(cls, sample_id: int) -> dict:
        """Fetch sample details about sample with sample_id"""
        where = "WHERE `sample_id` = {:d}".format(sample_id);
        details = Cursor.select("view_samples_details", clauses=where);
        if len(details) != 1:
            return;
        return details[0];


    @classmethod
    def fetch_entries(cls, table_name: str, sample_ids: list=[]):
        """Fetch samples with ids in the sample_ids list."""
        if len(sample_ids) == 0:
            return [];

        list_sql = ", ".join(str(sid) for sid in sample_ids);
        where_clause = "WHERE `sample_id` IN ({:s})".format(list_sql);
        entries = Cursor.select(table_name, clauses=where_clause);
        for entry in entries:
            entry = cls.clean_entry(entry);
        return entries;


    @classmethod
    def clean_submit(cls, submitted: dict) -> dict:
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
    def fetch_name(cls, sample_id: int) -> str:
        where_clause = f"WHERE `sample_id` = {sample_id}";
        fields = ["sample_name"];
        sample_name ,= Cursor.select(cls.edit_table_name, fields=fields,
                                     clauses=where_clause);
        return sample_name;


    @classmethod
    def fetch(cls, table_name: str, sample_id: int=0) -> dict:
        """Fetch sample with sample_id from the database."""
        where_clause = f"WHERE `sample_id` = {sample_id}";
        entry, = Cursor.select(table_name, clauses=where_clause);
        entry = cls.clean_entry(entry);
        return entry;


    @classmethod
    def delete(cls, sample_id: int) -> None:
        """Detele the sample with sample_id from the database."""
        args = (sample_id,);
        Cursor.call_procedure("delete_sample", args=args, commit=True);
        return;


    @classmethod
    def update_virusname(cls, sample_id: int, virusname: str) -> None:
        """Update the virusname of sample with id sample_id."""
        where_clause = f"WHERE id = {sample_id}";
        values = {"gisaid_virusname": virusname};
        Cursor.update_row("samples", where_clause, values);


    @classmethod
    def update_isolatename(cls, sample_id: int, isolate: str) -> None:
        """Update the virusname of sample with id sample_id."""
        where_clause = f"WHERE id = {sample_id}";
        values = {"isolate": isolate};
        Cursor.update_row("samples", where_clause, values);

