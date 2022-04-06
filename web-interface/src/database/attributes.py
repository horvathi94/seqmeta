from typing import List
from seqmeta.database.connect import Connect
from seqmeta.database.table import Table
from seqmeta.objects.samples.attribute import Attribute


class AttributesTable(Table):

    table_name = "attributes"
    object_class = Attribute


    @classmethod
    def select_all_in_template(cls, template_id: int) -> List[Attribute]:
        query = f"SELECT id FROM {cls.table_name} "\
            f"WHERE template_id = {template_id}"
        conn = Connect()
        ids = conn.fetchall(query)
        return [cls.select(i["id"]) for i in ids]


    @staticmethod
    def save(attr: Attribute) -> None:
        sql = f"""INSERT INTO `{table_name}`
            (name, template_id, type_, has_options, description)
            VALUES
            (%(name)s, %(template_id)s, %(type_)s,
            %(has_options)s, %(description)s)"""
        conn = Connect()
        conn.execute_sql(sql, attr.asdict())
