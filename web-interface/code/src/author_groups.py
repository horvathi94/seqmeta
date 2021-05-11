from .cursor import Cursor
from .base import Base

class AuthorGroups(Base):

    table_name = "author_groups";

    def fetch_display_list(self):

        groups = self.fetch_list();
        cursor = Cursor();

        for group in groups:
            where_clause = """
                WHERE `author_group_id` = {:d}
                """.format(group["id"]);
            count = cursor.count_entries("authors_in_group",
                                         where_clause=where_clause);

            sql = "SELECT ";
            members = cursor.select();
            group["members_count"] = count;

        cursor.close();

        return groups;
