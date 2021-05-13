from collections import OrderedDict
from .cursor import Cursor
from .base import Base
from .author_groups import AuthorGroups

class Samples(Base):

    table_name = "view_samples";
    date_format = "%Y-%m-%d";


    def fetch_entry(self, sample_id=0):

        cursor = Cursor()
        where_clause = "WHERE `sample_id` = {:d}".format(sample_id);
        raw_data = cursor.select_all(self.table_name, where_clause);
        cursor.close();

        if len(raw_data) == 0:
            return [];

        data = raw_data[0];
        data["collection_date"] = \
            data["collection_date"].strftime(self.date_format);

        author_group = AuthorGroups();
        author_group = \
            author_group.fetch_entry(group_id=data["author_group_id"]);

        data["authors"] = "";
        for author in author_group["authors"]:
            data["authors"] += author["name_tag"] + ", ";
        data["authors"] = data["authors"][:-2];
        del data["author_group_id"];

        return data;
