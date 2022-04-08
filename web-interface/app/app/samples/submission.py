from typing import List
from seqmeta.objects.samples.sample import Sample
from seqmeta.database.samples import SamplesTable

import sys



def parse(raw: dict, skip_0: bool=True) -> List[dict]:

    samples = {}
    for key, val in raw.items():
        k, sts = key.split("+")[:2]
        if k != "sample": continue
        if sts == "editall": continue

        k, sts, index, attr_name = key.split("+")
        index = int(index)
        if skip_0 and index == 0: continue
        if index not in samples:
            samples[index] = {"sample_status": sts}
        samples[index][attr_name] = val
    return samples


def handle(raw: dict) -> any:

    template_id = int(raw.pop("template_id"))
    sample_data = parse(raw)

    for index in sample_data.keys():
        s = sample_data[index]
        sample_status = s.pop("sample_status")
        id_ = None if sample_status == "new" else int(index)
        sample_name = s.pop("name")
        short_description = s.pop("short_description")
        sample = Sample(id=id_,
                        name=sample_name,
                        template_id=template_id,
                        short_description=short_description)
        for attr in s:
            sample.add_attribute(attr, s[attr])
        SamplesTable.save(sample)
        print(f"Sample: {sample}", file=sys.stderr)
