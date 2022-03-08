from seqmeta.objects.samples.attribute import Attribute
from seqmeta.objects.samples.template import Template


import sys

KEYS = ["keep", "name", "importance", "default", "description"]

def create_keys(index):
    return [f"inpfield+{index}+{k}" for k in KEYS]



def handle(data: dict):

    indices = list(set([int(k.strip().split("+")[1]) for k in data.keys()]))
    template = Template()
    for index in indices:
        keys = create_keys(index)
        keep_key = keys.pop(0)
        if not int(data[keep_key]): continue
        curr = {k.strip().split("+")[-1]: data[k] for k in keys}
        attr = Attribute(**curr)
        template.add_attribute(attr)
    print(f"Template: {template.attributes}", file=sys.stderr)
