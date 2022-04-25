from typing import List
from seqmeta.objects.samples.attribute import Attribute
from seqmeta.objects.samples.template import Template
from seqmeta.database.templates import TemplatesTable


import sys



def parse_submission(raw_data: dict, key: str) -> List[dict]:

    cleaned = []
    current = {"id": None, "status": None}
    keep = False

    for rname, rvalue in raw_data.items():
        if rname.split("+")[0] != key: continue
        k, status, index, name = rname.split("+")
        index = int(index)
        if current["status"] != status or current["id"] != index:
            cleaned.append(current)
            current = {"status": status, "id": index}
        current[name] = rvalue
    cleaned = cleaned[1:]
    cleaned.append(current)
    return cleaned



def handle(raw: dict) -> "html":

#    template_id = raw.pop("template_id")
    template_name = raw.pop("template_name")
    template = Template(name=template_name)
    attrs = parse_submission(raw, "attr")
    for a in attrs:
        attr = Attribute(**a)
        template.add_attribute(attr)

    template.save()
#    TemplatesTable.save(template)
