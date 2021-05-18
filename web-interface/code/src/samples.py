from collections import OrderedDict
from .cursor import Cursor
from .base import Base
from .author_groups import AuthorGroups
from datetime import datetime

class Samples(Base):

    view_table_name = "view_samples";
    submit_table_name = "sample_data";
    date_format = "%Y-%m-%d";


    def clean_entry(self, sample):

        sample["collection_date"] = \
            sample["collection_date"].strftime(self.date_format);

        author_group = AuthorGroups();
        author_group = \
            author_group.fetch_entry(group_id=sample["author_group_id"]);

        sample["authors"] = "";
        for author in author_group["authors"]:
            sample["authors"] += author["name_tag"] + ", ";
        sample["authors"] = sample["authors"][:-2];



    def fetch_entry(self, sample_id=0):

        cursor = Cursor();
        where_clause = "WHERE `sample_id` = {:d}".format(sample_id);
        raw_data = cursor.select(self.view_table_name,
                                 where_clause=where_clause);

        if len(raw_data) == 0:
            data = cursor.create_empty_ordereddict(self.view_table_name);
            cursor.close();
            return data;

        cursor.close();

        data = raw_data[0];
        self.clean_entry(data);

        author_group = AuthorGroups();
        author_group = \
            author_group.fetch_entry(group_id=data["author_group_id"]);

        data["authors"] = "";
        for author in author_group["authors"]:
            data["authors"] += author["name_tag"] + ", ";
        data["authors"] = data["authors"][:-2];
        del data["author_group_id"];

        return data;


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



    def clean_submit(self, submitted):

        submitted["name"] = submitted["sample_name"];
        del submitted["sample_name"];

        if submitted["patient_gender"] == "Male":
            submitted["patient_gender"] = True;
        elif submitted["patient_gender"] == "Female":
            submitted["patient_gender"] = False;
        else:
            submitted["patient_gender"] = None;

        submitted["submission_date"] = datetime.today();


