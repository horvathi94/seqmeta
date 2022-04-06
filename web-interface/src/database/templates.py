import mysql.connector
from seqmeta.database.connect import Connect
from seqmeta.database.attributes import AttributesTable
from seqmeta.objects.samples.template import Template


import sys


class TemplatesTable:


    @staticmethod
    def select_all():
        pass


    @staticmethod
    def select():
        pass


    @staticmethod
    def save(t: Template) -> None:
        print(f"\nSaving template: {t}", file=sys.stderr)
        conn = Connect()
        if t.id is None:
            sql = "INSERT INTO `templates` (name) VALUES (%s)"

#        try:
#            tid = conn.execute_sql(sql, (t.name,), last_insert=True)
#        except mysql.connector.IntegrityError as e:
#            raise Exception("Failed to save, duplicate template name.")

        tid = 6

        for a in t.attributes:
            a.template_id = tid
            AttributesTable.save(a)
