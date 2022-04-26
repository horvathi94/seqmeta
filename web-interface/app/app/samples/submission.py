from typing import List
from seqmeta.objects.samples.sample import Sample
#from seqmeta.database.samples import SamplesTable
#from seqmeta.database.attributes import AttributesTable
from seqmeta.objects.samples.templates import SamplesList, TemplatesList

import sys


def old_parse_submission(raw_data: dict, key: str) -> List[dict]:

    cleaned = []

    for rname, rvalue in raw_data.items():
        if rname.split("+")[0] != key: continue
        k, status, id_, name = rname.split("+")

        item_name = None
        for i, item in enumerate(cleaned):
            if item["status"] == status and item["name"] == id_:
                item_index = i

        if item_index == -1:
            cleaned.append({"status": status, "name": id_})

        cleaned[item_index][name] = rvalue

    return cleaned



def parse_submission(raw: dict, main_key: str) -> any:
    cleaned = {}
    for item, value in raw.items():
        mk, index, attr_name = item.split("+")
        if mk != main_key: continue
        if index not in cleaned: cleaned[index] = {}
        cleaned[index][attr_name] = value
    return list(cleaned.values())


def handle(raw: dict) -> any:

    template_name = raw.pop("template_name")
    tl = TemplatesList()
    template = tl.load_by_name(template_name)
    sample_data = parse_submission(raw, "sample")
    sl = SamplesList()

    for sd in sample_data:
        s = {"template_name": template_name}
        s["name"] = sd.pop("name")
        s["short_description"] = sd.pop("short_description")
        sample = Sample(**s)

        for aname, aval in sd.items():
            attr = template.get_attribute(aname)
            attr.value = aval
            sample.add_attribute(attr)
        sl.save(sample)
