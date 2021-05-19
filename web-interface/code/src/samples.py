from collections import OrderedDict
from .cursor import Cursor
from .base import Base
from .author_groups import AuthorGroups
from datetime import datetime

class Samples(Base):

    view_table_name = "view_samples_list_display";
    submit_table_name = "sample_data";
    date_format = "%Y-%m-%d";


    @classmethod
    def clean_entry(cls, entry):
        entry["collection_date"] = \
            entry["collection_date"].strftime(cls.date_format);
        return entry;

    @classmethod
    def fetch_details(cls, sample_id):
        where = "WHERE `sample_id` = {:d}".format(sample_id);
        details = Cursor.select("view_samples_details", clauses=where);
        if len(details) != 1:
            return;
        return details[0];


    @classmethod
    def fetch_entry(cls, sample_id=0):
        where = "WHERE `sample_id` = {:d}".format(sample_id);
        sample = Cursor.select("view_samples_for_edit", clauses=where);
        if len(sample) != 1:
            return Cursor.create_empty_ordereddict("view_samples_for_edit")[0];
        sample = cls.clean_entry(sample[0]);
        return sample;


    def fetch_entries(self, sample_ids=[]):

        if len(sample_ids) == 0:
            return [];


        cursor = Cursor()
        list_sql = "";
        for sample_id in sample_ids:
            list_sql+= "{:d}, ".format(sample_id);
        list_sql = list_sql[:-2];

        where_clause = "WHERE `sample_id` IN ({:s})".format(list_sql);
        raw_data = cursor.select_all(self.view_table_name, where_clause);

        cursor.close();

        for rd in raw_data:
            self.clean_entry(rd);

        return raw_data;


    @classmethod
    def clean_submit(cls, submitted):
        submitted["id"] = int(submitted["id"]);
        submitted["name"] = submitted["sample_name"];
        del submitted["sample_name"];
        if submitted["patient_gender"] == "Male":
            submitted["patient_gender"] = True;
        elif submitted["patient_gender"] == "Female":
            submitted["patient_gender"] = False;
        else:
            submitted["patient_gender"] = None;
        submitted["submission_date"] = datetime.today();
        return submitted;

