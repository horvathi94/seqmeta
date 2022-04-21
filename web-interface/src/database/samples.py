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
        sample.id = 1 if sample.name == "S01" else 4
        sample.status = "registered"
        args = (sample.id, sample.template_id, sample.name,
                sample.short_description, sample.status, 0)
        conn = Connect()

#        try:
        res = conn.call_procedure("upsert_sample", args)
        sample.id = int(list(res.values())[-1])
#        except:
#            raise Exception("Failed to save.");

        print(f"\n\nSaved: {sample}", file=sys.stderr)


        for attr_name, attr_value in sample.attributes.items():
            args = (sample.id, attr_name, attr_value, sample.status)
            conn.call_procedure("upsert_sample_attribute", args)
