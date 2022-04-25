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


    @classmethod
    def select_by_name(cls, name: str) -> Attribute:
        query = f"SELECT `id` FROM {cls.table_name} "\
            f"WHERE `general_name` = '{name}'"
        conn = Connect()
        i = conn.fetchone(query)
        return cls.select(i["id"])


    @classmethod
    def save(cls, attr: Attribute) -> None:
        conn = Connect()
        conn.call_procedure("upsert_attribute", attr.upsert_values)
