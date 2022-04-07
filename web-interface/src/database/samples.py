from seqmeta.database.connect import Connect
from seqmeta.objects.samples.sample import Sample

import sys


import sys
class SamplesTable:

    table_name = "samples"


    @classmethod
    def save(cls, sample: Sample) -> None:
        if sample.id is None:
            # Insert
            sql = f"INSERT INTO {cls.table_name} (name, template_id) "\
                f"VALUES (%s, %s)"
            conn = Connect()
            sample.id = conn.execute_sql(sql,
                                         (sample.name,sample.template_id),
                                         last_insert=True)
        for attr in sample.attributes.items():
            cls.save_attribute(sample.id, attr[0], attr[1])


    @classmethod
    def save_attribute(cls, sample_id: int, name: str, val: str) -> None:
        # Insert
        sql = f"INSERT INTO `sample_attributes` "\
            "(sample_id, name, value) VALUES (%s, %s, %s)"
        conn = Connect()
        conn.execute_sql(sql, (sample_id, name, val))


