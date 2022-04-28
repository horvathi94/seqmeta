from typing import List
from seqmeta.objects.sample import Sample

from seqmeta.submissions import ena as ena_metadata
from seqmeta.submissions import gisaid as gisaid_metadata



def gisaid(sample_names: List[str]) -> dict:
    samples = Sample.list_all()
    md = gisaid_metadata.Metadata()
    md.add_samples(samples)
    md.write()
    return [s.asjson() for s in samples]


def ena(sample_names: List[str]) -> str:
    samples = Sample.list_all()
    return ena_metadata.sample_set(samples)
