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
        if sample.id is None:
            # Insert
            sql = f"INSERT INTO {cls.table_name} "\
                f"(name, template_id, short_description) "\
                f"VALUES (%(name)s, %(template_id)s, %(short_description)s)"
            conn = Connect()
            sample.id = conn.execute_sql(sql, sample.asdict(),
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


