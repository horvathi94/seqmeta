from typing import List
from seqmeta.objects.samples.sample import Sample
from seqmeta.database.samples import SamplesTable

import sys



def parse(raw: dict) -> List[dict]:

    samples = {}
    for key, val in raw.items():
        k, sts = key.split("+")[:2]
        if k != "sample": continue

        k, sts, index, attr_name = key.split("+")
        index = int(index)
        if index not in samples:
            samples[index] = {"sample_status": sts}
        samples[index][attr_name] = val
    return samples


def handle(raw: dict) -> any:

    template_id = int(raw.pop("template_id"))
    sample_data = parse(raw)


    for index, data in sample_data.items():
        sample_name = data.pop("name")
        short_description = data.pop("short_description")
        status = data.pop("sample_status")
        sample = Sample(name=sample_name,
                        template_id=template_id,
                        short_description=short_description,
                        status=status)
        if status == "registered":
            sample.id = index

        for attr_name, attr_value in data.items():
            sample.add_attribute(attr_name, attr_value)

        SamplesTable.save(sample)
