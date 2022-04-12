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
    def save(cls, attr: Attribute) -> None:
        sql = f"INSERT INTO `{cls.table_name}` "\
            "(general_name, label, template_id, type_, "\
            "options, template, pattern, `default`, description, "\
            "ena_name, ena_requirement, gisaid_name, gisaid_requirement) "\
            "VALUES "\
            "(%(general_name)s, %(label)s, %(template_id)s, %(type_)s, "\
            "%(options)s, %(template)s, %(pattern)s, %(default)s, "\
            "%(description)s, %(ena_name)s, %(ena_requirement)s, "\
            "%(gisaid_name)s, %(gisaid_requirement)s) "
        conn = Connect()
        conn.execute_sql(sql, attr.asdict())
