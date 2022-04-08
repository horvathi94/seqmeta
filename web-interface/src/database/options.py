from seqmeta.database.connect import Connect
from seqmeta.database.table import Table


class OptionsTable(Table):

    table_name = "options"


    @classmethod
    def save(cls, attr_id: int, option: str) -> None:
        sql = f"""INSERT INTO `{cls.table_name}`
            (attribute_id, option) VALUES (%s, %s)"""
        conn = Connect()
        conn.execute_sql(sql, (attr_id, option))
