from seqmeta.database.connect import Connect


class Table:

    table_name = None
    object_class = None


    @classmethod
    def select(cls, id_: int) -> "Object":
        query = f"SELECT * FROM {cls.table_name} WHERE id = {id_}"
        conn = Connect()
        data = conn.fetchone(query)
        return cls.object_class(**data)


    @classmethod
    def select_all(cls) -> list:
        query = f"SELECT `id` FROM `{cls.table_name}`"
        conn = Connect()
        ids = [i["id"] for i in conn.fetchall(query)]
        if len(ids) == 0: return []
        return [cls.select(i) for i in ids]
