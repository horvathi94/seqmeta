from .cursor import Cursor
from .base import Base
from .authors import AuthorNameTag
from collections import OrderedDict

class AuthorGroups(Base):

    view_table_name = "view_authors_in_groups";
    submit_table_name = "author_groups";

    def fetch_display_list(self):

        cursor = Cursor();

        groups_count = cursor.count_entries("author_groups");
        if groups_count == 0:
            return [];

        groups_description = cursor.select_all(self.view_table_name);

        reg_group_ids = [];
        groups = [];
        for i, entry in enumerate(groups_description):

            group_id = entry["group_id"];
            if group_id not in reg_group_ids:

                if i > 0:
                    group["authors_list"] = group["authors_list"][:-2]
                    groups.append(group);

                group = OrderedDict();
                group["group_id"] = group_id;
                group["group_name"] = entry["group_name"];
                group["authors_list"] = "";
                group["members_count"] = 0;
                reg_group_ids.append(group_id);


            name_tag = AuthorNameTag(entry);
            if name_tag.check_if_exists():
                group["authors_list"] += name_tag.abreviated_middle_name() + ", ";
                group["members_count"] += 1;


        group["authors_list"] = group["authors_list"][:-2]
        groups.append(group);


        cursor.close();
        return groups;


    def create_empty_group(self):

        group = OrderedDict();
        group["group_id"] = 0;
        group["group_name"] = "";
        group["authors"] = [];
        return group;


    def fetch_entry(self, group_id=0):

        cursor = Cursor();
        where_clause = "WHERE `group_id` = {:d}".format(group_id);
        raw_group = cursor.select_all(self.view_table_name, extra=where_clause);

        group = self.create_empty_group();
        if len(raw_group) == 0:
            return group;

        group["group_id"] = raw_group[0]["group_id"];
        group["group_name"] = raw_group[0]["group_name"];

        for author in raw_group:
            name_tag = AuthorNameTag(author);
            if name_tag.check_if_exists():
                author["name_tag"] = name_tag.abreviated_middle_name();
                group["authors"].append(author);

        cursor.close();
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
