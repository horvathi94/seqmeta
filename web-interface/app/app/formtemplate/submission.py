from seqmeta.objects.samples.attribute import Attribute
from seqmeta.objects.samples.template import Template
from seqmeta.objects.samples.templates import TemplatesList
from seqmeta.form import submission


def handle(raw: dict) -> None:

    template_name = raw.pop("loaded_template_name")
    new_name = raw.pop("template_name")

    template_data = submission.parse(raw, "template")[0]
    template = Template(name=template_name, **template_data)

    attrs = submission.parse(raw, "attr")
    for a in attrs:
        attr = Attribute(**a)
        template.add_attribute(attr)

    tl = TemplatesList()
    tl.save(template)
