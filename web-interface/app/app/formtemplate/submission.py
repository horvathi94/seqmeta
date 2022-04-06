from typing import List
from seqmeta.objects.samples.attribute import Attribute
from seqmeta.objects.samples.template import Template
from seqmeta.database.templates import TemplatesTable


import sys

def parse_list(raw: dict, fkey: str, skip_0: bool=True) -> List[dict]:

    datad = {}
    for key, val in raw.items():
        k, indx, label = key.split("+")
        if k != fkey: continue
        indx = int(indx)
        if skip_0 and indx == 0: continue
        if indx not in datad: datad[indx] = {}
        datad[indx][label] = val
    return list(datad.values())



def handle(raw: dict) -> "html":

    data = parse_list(raw, "attr")
    tdata = parse_list(raw, "template", skip_0=False)[0]
    t = Template(**tdata)
    for d in data:
        a = Attribute(**d)
        t.add_attribute(a)
    try:
        TemplatesTable.save(t)
    except:
        return "<h1>Failed to save the template. Duplicate name.</h1>"
