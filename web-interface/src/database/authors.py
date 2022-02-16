from dataclasses import asdict
from typing import List
from seqmeta.database.connect import Connect
from seqmeta.objects.author import Author


import sys

class AuthorsTable:


    def __init__(self):
        self.conn = Connect()


    def get_authors(self) -> List[Author]:
        query = "SELECT * FROM authors"
        raw = self.conn.fetchall(query)
        if len(raw) == 0: return []
        return [Author(**item) for item in raw]


    def select_author(self, id_: int) -> Author:
        query = f"SELECT * FROM `authors` WHERE id = {id_}"
        data = self.conn.fetchone(query)
        return Author(**data)


    def save(self, author: Author) -> int:
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
        self.conn.execute_sql(sql, asdict(author))
