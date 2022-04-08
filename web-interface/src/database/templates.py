import mysql.connector
from seqmeta.database.connect import Connect
from seqmeta.database.table import Table
from seqmeta.database.attributes import AttributesTable
from seqmeta.objects.samples.template import Template



class TemplatesTable(Table):


    table_name = "templates"


    @classmethod
    def select(cls, id_: int):
        query = f"SELECT * FROM `{cls.table_name}` WHERE id = {id_}"
        conn = Connect()
        data = conn.fetchone(query)
        t = Template(**data)
        attrs = AttributesTable.select_all_in_template(id_)
        for a in attrs:
            t.add_attribute(a)
        return t


    @classmethod
    def save(cls, t: Template) -> None:
        conn = Connect()
        if t.id is None:
            sql = f"INSERT INTO `{cls.table_name}` (name) VALUES (%s)"

        try:
            tid = conn.execute_sql(sql, (t.name,), last_insert=True)
        except mysql.connector.IntegrityError as e:
            raise Exception("Failed to save, duplicate template name.")

        for a in t.attributes:
            a.template_id = tid
            AttributesTable.save(a)
