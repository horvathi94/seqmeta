from seqmeta.form import submission
from seqmeta.objects.template import SampleTemplate
from seqmeta.objects.sample import Sample



def handle(raw: dict, files: any) -> None:

    raw.update(files)
    template_name = raw.pop("template_name")
    template = SampleTemplate.load(template_name)

    sample_data = submission.parse(raw, "sample")

    for sd in sample_data:
        name = sd.pop("name")
        short_description = sd.pop("short_description")
        sample = Sample(name, short_description, template_name=template_name)

        for aname, aval in sd.items():
            attr = template.get_attribute(aname)
            sample_attr = attr.as_sample_attribute()
            sample.add_attribute(sample_attr)

        sample.save()
