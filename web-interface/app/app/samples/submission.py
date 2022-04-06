from typing import List
from seqmeta.objects.samples.sample import Sample

import sys



def parse(raw: dict, skip_0: bool=True) -> List[dict]:

    samples = {}
    for key, val in raw.items():
        k, sts, index, attr_name = key.split("+")
        if k != "sample": continue
        index = int(index)
        if skip_0 and index == 0: continue
        if index not in samples:
            samples[index] = {"sample_status": sts}
        samples[index][attr_name] = val
    return samples


def handle(raw: dict) -> any:

    sample_data = parse(raw)
    template_id = 6

    for index in sample_data.keys():
        s = sample_data[index]
        sample_status = s.pop("sample_status")
        id_ = None if sample_status == "new" else int(index)
        sample_name = s.pop("name")
        sample = Sample(id=id_, name=sample_name, template_id=template_id)
        for attr in s:
            sample.add_attribute(attr, s[attr])
        print(f"Received: {sample}", file=sys.stderr)
