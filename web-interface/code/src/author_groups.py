from .cursor import Cursor
from .base import Base
from .authors import AuthorNameTag
from collections import OrderedDict

class AuthorGroups(Base):

    table_name = "author_groups";

    def fetch_display_list(self):

        cursor = Cursor();
        groups_description = \
            cursor.call_procedure("ConcatAuthorsAndGroups")[0];


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
            group["authors_list"] += name_tag.abreviated_middle_name() + ", ";
            group["members_count"] += 1;


        group["authors_list"] = group["authors_list"][:-2]
        groups.append(group);


        cursor.close();
        return groups;


    def fetch_entry(self, group_id=0):

        cursor = Cursor();
        group = cursor.call_procedure("SelectGroup", args=[group_id])[0];
        for author in group:
            name_tag = AuthorNameTag(author);
            author["name_tag"] = name_tag.abreviated_middle_name();
        cursor.close();
        return group;


    def save(self, group_info, authors_list):

        cursor = Cursor();
        args = [group_info["id"], group_info["name"], 0];
        res = cursor.commit_procedure("UpsertGroupNames",
                                           args=args);

        group_id = int(res[2]);
        for author in authors_list:
            update_data = [group_id,
                           author["author_id"],
                           author["order_index"]];
            cursor.commit_procedure("UpdateGroup", update_data);
        cursor.close();
        return group_id;
