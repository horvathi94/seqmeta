from typing import List
from seqmeta.objects.samples.attribute import Attribute
from seqmeta.objects.samples.template import Template


import sys

def parse_list(raw: dict, fkey: str) -> List[dict]:

    datad = {}
    for key, val in raw.items():
        k, indx, label = key.split("+")
        if k != fkey: continue
        indx = int(indx)
        if indx == 0: continue
        if indx not in datad: datad[indx] = {}
        datad[indx][label] = val
    return list(datad.values())



def handle(raw: dict) -> None:

    data = parse_list(raw, "attr")
    t = Template()
    for d in data:
        a = Attribute(**d)
        t.add_attribute(a)
    print(f"Template: {t}", file=sys.stderr)
