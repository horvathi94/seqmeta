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
        query = f"SELECT * FROM `{cls.table_name}`"
        conn = Connect()
        raw = conn.fetchall(query)
        if len(raw) == 0: return []
        return [cls.object_class(**item) for item in raw]
