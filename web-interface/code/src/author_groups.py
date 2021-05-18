from .cursor import Cursor
from .base import Base
from .authors import AuthorNameTag
from collections import OrderedDict

class AuthorGroups(Base):

    view_table_name = "view_authors_in_groups_condensed";
    submit_table_name = "author_groups";


    def create_empty_group(self):

        group = OrderedDict();
        group["group_id"] = 0;
        group["group_name"] = "";
        group["authors"] = [];
        return group;


    def fetch_entry(self, group_id=0):

        cursor = Cursor();
        where_clause = "WHERE `id` = {:d}".format(group_id);
        group_name = cursor.select("author_groups", fields=["name"],
                                      where_clause=where_clause);

        group = self.create_empty_group();
        group["group_id"] = group_id;
        if len(group_name) != 1:
            cursor.close();
            return group;

        group["group_name"] = group_name[0]["name"];

        where_clause = "WHERE `group_id` = {:d}".format(group_id);
        authors = cursor.select("view_authors_in_groups",
                                fields=["abbreviated_middle_name"],
                                where_clause=where_clause);

        cursor.close();
        group["authors"] = authors;
        return group;



    def save(self, group_info, authors_list):

        cursor = Cursor();
        args = [group_info["id"], group_info["name"], 0];
        res = cursor.call_procedure("UpsertGroup", args=args, commit=True);
        group_id = int(res[2]);

        for author in authors_list:
            update_data = [group_id,
                           author["author_id"],
                           author["order_index"]];
            cursor.call_procedure("UpsertAuthorsInGroup",
                                  update_data,
                                  commit=True);
        cursor.close();
        return group_id;
