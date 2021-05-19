from .cursor import Cursor
from .base import Base
from collections import OrderedDict

class AuthorGroups(Base):

    view_table_name = "view_authors_in_groups_condensed";
    submit_table_name = "author_groups";


    @staticmethod
    def create_empty_od():
        group = OrderedDict();
        group["group_id"] = 0;
        group["group_name"] = "";
        group["authors"] = [];
        return group;


    @classmethod
    def fetch_entry(cls, group_id=0):
        where = "WHERE `id` = {:d}".format(group_id);
        group_name = Cursor.select("author_groups", fields=["name"],
                                   clauses=where);
        group = cls.create_empty_od();
        group["group_id"] = group_id;
        if len(group_name) != 1:
            return group;

        group["group_name"] = group_name[0]["name"];
        where = "WHERE `group_id` = {:d}".format(group_id);
        fields = ["author_id", "abbreviated_middle_name", "order_index"];
        group["authors"] = Cursor.select("view_authors_in_groups",
                                fields=fields,
                                clauses=where);
        return group;


    @classmethod
    def save(cls, group_info, authors_list):
        args = [group_info["id"], group_info["name"], 0];
        res = Cursor.call_procedure("UpsertGroup", args=args, commit=True);
        group_id = int(res[2]);

        for author in authors_list:
            vals = [group_id, author["author_id"], author["order_index"]];
            Cursor.call_procedure("UpsertAuthorsInGroup", vals, commit=True);
        return group_id;
