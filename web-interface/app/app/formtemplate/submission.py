from seqmeta.form import submission
from seqmeta.objects.template import SampleTemplate
from seqmeta.objects.attributes.attribute import Attribute


def handle(raw: dict) -> None:

    loaded_name = raw.pop("loaded_template_name")
    if loaded_name == "": loaded_name = None
    new_name = raw.pop("template_name")

    template = SampleTemplate(new_name)
    taxonomy = submission.parse(raw, "taxonomy")[0]
    template.taxonomy.update(taxonomy)

    ena_checklist = submission.parse(raw, "ena_checklist")[0]
    template.ena_checklist = ena_checklist["ena_checklist"]

    template_data = submission.parse(raw, "template")[0]
    template.short_description = template_data["short_description"]

    attrs = submission.parse(raw, "attr")
    for a in attrs:
        template.add_attribute(Attribute(**a))

    template.save(overwrite=loaded_name)
