from typing import List
from seqmeta.database.table import Table
from seqmeta.database.attributes import AttributesTable
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
        sample = Sample(**data)
        attributes = cls.select_attributes(id_)
        for a in attributes:
            sample.add_attribute(a)
        return sample


    @classmethod
    def select_attributes(cls, id_: int) -> dict:
        query = f"SELECT * FROM `sample_attributes` WHERE `sample_id` = {id_}"
        conn = Connect()
        satts = conn.fetchall(query)
        attributes = []
        for sa in satts:
            a = AttributesTable.select_by_name(sa["name"])
            a.value = sa["value"]
            attributes.append(a)
        return attributes


    @classmethod
    def save(cls, sample: Sample) -> None:
        args = (sample.id, sample.template_id, sample.name,
                sample.short_description, sample.status, 0)
        conn = Connect()

#        try:
        res = conn.call_procedure("upsert_sample", args)
        sample.id = int(list(res.values())[-1])
#        except:
#            raise Exception("Failed to save.");

        for attr in sample.attributes:
            args = (sample.id, attr.general_name, attr.value, sample.status)
            conn.call_procedure("upsert_sample_attribute", args)
