from seqmeta.objects.samples.attribute import Attribute
from seqmeta.objects.samples.template import Template
from seqmeta.objects.samples.templates import TemplatesList
from seqmeta.form import submission


def handle(raw: dict) -> None:

    loaded_name = raw.pop("loaded_template_name")
    new_name = raw.pop("template_name")
    template_data = submission.parse(raw, "template")[0]
    tl = TemplatesList()

    if loaded_name == "":
        template = Template(name=new_name, **template_data)
    else:
        template = tl.load_by_name(loaded_name)
        template.short_description = template_data["short_description"]
        template.taxonomy_id = template_data["taxonomy_id"]
        template.scientific_name = template_data["scientific_name"]
        template.common_name = template_data["common_name"]
        template.name = new_name

    attrs = submission.parse(raw, "attr")
    for a in attrs:
        attr = Attribute(**a)
        template.add_attribute(attr)

    tl.save(template)
