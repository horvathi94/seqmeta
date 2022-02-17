from dataclasses import asdict
from typing import List
from seqmeta.database.connect import Connect
from seqmeta.database.authors import AuthorsTable
from seqmeta.objects.group import Group


class GroupsTable:


    @classmethod
    def select(cls, id_: int) -> Group:
        sql = f"SELECT * FROM `author_groups` WHERE `id` = {id_}"
        conn = Connect()
        raw = conn.fetchone(sql)
        group = Group(**raw)

        sql = f"SELECT `author_id`, `order_index` FROM `authors_in_group` " \
            f"WHERE `agroup_id` = {id_}"
        aids = conn.fetchall(sql)
        for aid in aids:
            a = AuthorsTable.select(aid["author_id"])
            group.add_author(a, aid["order_index"])
        return group


    @classmethod
    def select_all(cls) -> List[Group]:
        query = "SELECT `id` FROM `author_groups`"
        conn = Connect()
        raw = conn.fetchall(query)
        if len(raw) == 0: return []
        return [cls.select(r["id"]) for r in raw]


    @classmethod
    def save_group_info(cls, group: Group) -> int:
        conn = Connect()
        values = {"name": group.name}

        if group.id == 0:

            sql = "INSERT INTO `author_groups` (`name`) VALUES (%(name)s)"
            index = conn.execute_sql(sql, values, last_insert=True)

        else:
            sql = f"UPDATE `author_groups` " \
                f"SET `name` = %(name)s "\
                f"WHERE `id` = {group.id}"
            conn.execute_sql(sql, values)
            index = group.id

        return index


    @classmethod
    def save_author(cls, author: "AuthorInGroup", gid: int) -> None:
        sql = f"SELECT `id` FROM `authors_in_group` " \
            f"WHERE `author_id` = {author.author.id} " \
            f"AND `agroup_id` = {gid};"
        conn = Connect()
        id_ = conn.fetchone(sql)

        data = {"author_id": author.author.id, "group_id": gid,
                "order": author.order}

        if id_ is None:

            sql = "INSERT INTO `authors_in_group` " \
                "(`author_id`, `agroup_id`, `order_index`) " \
                "VALUES (%(author_id)s, %(group_id)s, %(order)s)"
        else:

            sql = "UPDATE `authors_in_group` " \
                "SET `order_index` = %(order)s " \
                f"WHERE `agroup_id` = {data['group_id']} " \
                f"AND `author_id` = {data['author_id']}"

        conn.execute_sql(sql, data)


    @classmethod
    def remove_author(cls, author: "AuthorInGroup", gid: int) -> None:

        sql = "DELETE FROM `authors_in_group` " \
            f"WHERE `agroup_id` = {gid} " \
            f"AND `author_id` = {author.author.id}"
        conn = Connect()
        conn.execute_sql(sql, None)


    @classmethod
    def save(cls, group: Group) -> None:
        gid = cls.save_group_info(group)
        for a in group:
            if a.order == 0:
                cls.remove_author(a, gid)
            else:
                cls.save_author(a, gid)
