from typing import List
from seqmeta.objects.sample import Sample

from seqmeta.submissions import ena as ena_metadata
from seqmeta.submissions import gisaid as gisaid_metadata



def gisaid(template_name: str, sample_names: List[str]) -> dict:
    samples = [Sample.load(name, template_name) for name in sample_names]
    md = gisaid_metadata.Metadata()
    md.add_samples(samples)
    md.write()
    return [s.asjson() for s in samples]


def ena(template_name: str, sample_names: List[str]) -> str:
    samples = [Sample.load(name, template_name) for name in sample_names]
    return ena_metadata.sample_set(samples)
