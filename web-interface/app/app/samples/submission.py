from typing import List
from seqmeta.objects.samples.sample import Sample
from seqmeta.database.samples import SamplesTable
from seqmeta.database.attributes import AttributesTable

import sys


def parse_submission(raw_data: dict, key: str) -> List[dict]:

    cleaned = []

    for rname, rvalue in raw_data.items():
        if rname.split("+")[0] != key: continue
        k, status, index, name = rname.split("+")
        index = int(index)

        item_index = -1
        for i, item in enumerate(cleaned):
            if item["status"] == status and item["id"] == index:
                item_index = i

        if item_index == -1:
            cleaned.append({"status": status, "id": index})

        cleaned[item_index][name] = rvalue

    return cleaned



def handle(raw: dict) -> any:

    template_id = int(raw.pop("template_id"))
    sample_data = parse_submission(raw, "sample")
    for sd in sample_data:
        s = {"template_id": template_id}
        s["id"] = sd.pop("id")
        s["name"] = sd.pop("name")
        s["status"] = sd.pop("status")
        s["short_description"] = sd.pop("short_description")
        sample = Sample(**s)
        for aname, aval in sd.items():
            attr = AttributesTable.select_by_name(aname)
            attr.value = aval
            sample.add_attribute(attr)
        SamplesTable.save(sample)
