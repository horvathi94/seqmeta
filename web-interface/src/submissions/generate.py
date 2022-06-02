from seqmeta.objects.sample import Sample
from .gisaid.metadata import Metadata as GisaidMeta


def load_samples(template_name: str, sample_names: list) -> list:
    return [Sample.load(sname, template_name) for sname in sample_names]


def gisaid_submission(template_name: str, sample_names: list) -> any:
    samples = load_samples(template_name, sample_names)
    md = GisaidMeta()
    md.from_samples(samples)
    md.write()
    return [s.as_json() for s in samples]

    return {"succes": True}


def ena_submission(template_name: str, sample_names: list) -> any:
    samples = load_samples(template_name, sample_names)
    pass
