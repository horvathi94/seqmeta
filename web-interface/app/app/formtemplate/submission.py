from seqmeta.objects.samples.attribute import Attribute
from seqmeta.objects.samples.template import Template
from seqmeta.objects.samples.templates import TemplatesList
from seqmeta.form import submission


def handle(raw: dict) -> None:

    template_name = raw.pop("loaded_template_name")
    template_short_description = raw.pop("template_short_description")
    template = Template(name=template_name,
                        short_description=template_short_description)
    new_name = raw.pop("template_name")
    attrs = submission.parse(raw, "attr")

    for a in attrs:
        attr = Attribute(**a)
        template.add_attribute(attr)

    tl = TemplatesList()
    tl.save(template)
