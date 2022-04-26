from typing import List
from seqmeta.objects.samples.sample import Sample
from seqmeta.objects.samples.templates import SamplesList
from seqmeta.database.samples import SamplesTable

from seqmeta.submissions import ena as ena_metadata
from seqmeta.submissions import gisaid as gisaid_metadata



def gisaid(sample_names: List[str]) -> dict:
    sl = SamplesList()
    samples = [sl.load_by_name(sname) for sname in sample_names]
    md = gisaid_metadata.Metadata()
    md.add_samples(samples)
    md.write()
    return [s.asjson() for s in samples]


def ena(sample_names: List[str]) -> str:
    sl = SamplesList()
    samples = [sl.load_by_name(sname) for sname in sample_names]
    return ena_metadata.sample_set(samples)
