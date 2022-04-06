from seqmeta.database.connect import Connect
from seqmeta.objects.samples.sample import Sample

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
            sample.id = conn.execute_sql(sql, (sample.name,sample.template_id))
        print(f"\nSaving: {sample}", file=sys.stderr)
