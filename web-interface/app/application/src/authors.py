from collections import OrderedDict
from .db.interface import DBInterface
from .db.cursor import Cursor

class Authors(DBInterface):

    display_table_name = "view_authors"
    edit_table_name = "view_authors"
    submit_table_name = "authors"

    clean_keys_string = ["middle_name"]


    @classmethod
    def fetch_select_list(cls) -> list:
        """Returns list of authors formatted for select template."""
        ls = cls.fetch_list_labeled(replace_key="abbreviated_middle_name")
        for item in ls:
            del item["last_name"]
            del item["first_name"]
            del item["middle_name"]
            del item["full_name"]
        return ls



class AuthorGroups(DBInterface):

    display_table_name = "view_authors_in_groups_condensed"
    view_id_key = "group_id"
    submit_table_name = "author_groups"


    @staticmethod
    def create_empty_od():
        group = OrderedDict()
        group["group_id"] = 0
        group["group_name"] = ""
        group["authors"] = []
        return group


    @classmethod
    def fetch_entry_edit(cls, group_id=0):
        where = "WHERE `id` = {:d}".format(group_id)
        group_name = Cursor.select("author_groups", fields=["name"],
                                   clauses=where)
        group = cls.create_empty_od()
        group["group_id"] = group_id
        if len(group_name) != 1:
            return group

        group["group_name"] = group_name[0]["name"]
        where = "WHERE `group_id` = {:d}".format(group_id)
        fields = ["author_id", "abbreviated_middle_name", "order_index"]
        authors_list = Cursor.select("view_authors_in_groups",
                                fields=fields,
                                clauses=where)
        if len(authors_list) == 1 and authors_list[0]["id"] == 0:
            authors_list = []
        group["authors"] = authors_list
        return group


    @classmethod
    def save(cls, group_info, authors_list):
        args = [group_info["id"], group_info["name"], 0]
        res = Cursor.call_procedure("upsert_group", args=args, commit=True)
        group_id = int(res[2])

        for author in authors_list:
            vals = [group_id, author["author_id"], author["order_index"]]
            Cursor.call_procedure("upsert_authors_in_group",
                                  vals, commit=True)
        return group_id


    @classmethod
    def fetch_select_list(cls) -> list:
        return cls.fetch_list_labeled(replace_key="group_name",
                                      replace_id="group_id")
