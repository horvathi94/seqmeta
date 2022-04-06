from seqmeta.database.connect import Connect
from seqmeta.objects.samples.attribute import Attribute


class AttributesTable:

    @staticmethod
    def select_all():
        pass


    @staticmethod
    def select():
        pass


    @staticmethod
    def save(attr: Attribute) -> None:
        sql = """INSERT INTO `attributes`
            (name, template_id, type_, has_options, description)
            VALUES
            (%(name)s, %(template_id)s, %(type_)s,
            %(has_options)s, %(description)s)"""
        conn = Connect()
        conn.execute_sql(sql, attr.asdict())
