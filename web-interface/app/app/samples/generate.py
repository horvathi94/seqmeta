from typing import List
from seqmeta.objects.samples.sample import Sample
from seqmeta.database.samples import SamplesTable

from seqmeta.submissions import ena
from seqmeta.submissions import gisaid



def generate_upload(sample_ids: List[int]) -> dict:

    samples = [SamplesTable.select(sid) for sid in sample_ids]
    md = gisaid.Metadata()
    md.add_samples(samples)
    md.write()
    return samples
#    test = ena.sample_set(samples)
#    return test
