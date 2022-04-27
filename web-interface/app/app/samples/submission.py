from seqmeta.objects.samples.sample import Sample
from seqmeta.objects.samples.templates import SamplesList, TemplatesList
from seqmeta.form import submission

def handle(raw: dict, files: any) -> None:

    raw.update(files)
    template_name = raw.pop("template_name")
    tl = TemplatesList()
    template = tl.load_by_name(template_name)
    sample_data = submission.parse(raw, "sample")
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
        sample.save_files()
        sl.save(sample)
