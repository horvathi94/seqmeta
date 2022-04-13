from typing import List
from seqmeta.database.table import Table
from seqmeta.database.connect import Connect
from seqmeta.objects.samples.sample import Sample

import sys


class SamplesTable(Table):

    table_name = "samples"


    @classmethod
    def select(cls, id_: int) -> Sample:
        query = f"SELECT * FROM {cls.table_name} WHERE `id` = {id_}"
        conn = Connect()
        data = conn.fetchone(query)
        return Sample(**data)


    @classmethod
    def save(cls, sample: Sample) -> None:
        if sample.status == "new":
            # Insert
            sql = f"INSERT INTO {cls.table_name} "\
                f"(name, template_id, short_description) "\
                f"VALUES (%(name)s, %(template_id)s, %(short_description)s)"
            conn = Connect()
            sample.id = conn.execute_sql(sql, sample.asdict(),
                                         last_insert=True)
        for attr_name, attr_value in sample.attributes.items():
            cls.save_attribute(sample.id, attr_name, attr_value)


    @classmethod
    def save_attribute(cls, sample_id: int, name: str, val: str) -> None:
       sql = f"INSERT INTO `sample_attributes` "\
           "(sample_id, name, value) VALUES (%s, %s, %s)"
       conn = Connect()
       conn.execute_sql(sql, (sample_id, name, val))


