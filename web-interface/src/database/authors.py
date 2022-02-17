from dataclasses import asdict
from typing import List
from seqmeta.database.connect import Connect
from seqmeta.objects.author import Author


class AuthorsTable:


    @staticmethod
    def select_all() -> List[Author]:
        conn = Connect()
        query = "SELECT * FROM authors"
        raw = conn.fetchall(query)
        if len(raw) == 0: return []
        return [Author(**item) for item in raw]


    @staticmethod
    def select(id_: int) -> Author:
        conn = Connect()
        query = f"SELECT * FROM `authors` WHERE id = {id_}"
        data = conn.fetchone(query)
        return Author(**data)


    @staticmethod
    def save(author: Author) -> None:
        conn = Connect()
        if author.id == 0:
            sql = """INSERT INTO `authors`
                   (first_name, last_name, middle_name)
                   VALUES (%(first_name)s, %(last_name)s, %(middle_name)s)"""
        else:
            sql = f"""UPDATE `authors`
                SET `first_name` = %(first_name)s,
                    `middle_name` = %(middle_name)s,
                    `last_name` = %(last_name)s
                WHERE `id` = {author.id}"""
        conn.execute_sql(sql, asdict(author))
