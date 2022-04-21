from typing import List
from seqmeta.objects.samples.sample import Sample
from seqmeta.database.samples import SamplesTable


def generate_upload(sample_ids: List[int]) -> dict:

    samples = [SamplesTable.select(sid) for sid in sample_ids]
    return samples
