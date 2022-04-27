import pathlib
from dataclasses import dataclass, field, asdict
from typing import List
from seqmeta.objects.samples.attribute import Attribute, Requirement, FieldType
from seqmeta.objects.samples.templates import TemplatesList


@dataclass
class Sample:

    name: str = None
    template_name: str = None
    attributes: List[Attribute] = field(default_factory=lambda: [])
    short_description: str = None
    template: "Template" = None


    def __post_init__(self):
        self._load_template()


    def _load_template(self) -> None:
        if self.template_name is None: return
        tl = TemplatesList()
        self.template = tl.load_by_name(self.template_name)


    @property
    def taxonomy_id(self) -> str:
        return self.template.taxonomy_id


    @property
    def scientific_name(self) -> str:
        return self.template.scientific_name


    @property
    def common_name(self) -> str:
        return self.template.common_name


    @property
    def ena_checklist(self) -> str:
        return self.template.ena_checklist


    def add_attribute(self, a: Attribute) -> None:
        self.attributes.append(a)


    def asdict(self) -> dict:
        return {
            "name": self.name,
            "template_name": self.template_name,
            "short_description": self.short_description
        }


    def asjson(self) -> dict:
        json = self.asdict()
        json["attributes"] = {a.general_name: a.json_value \
                              for a in self.attributes}
        return json


    @property
    def ena_list(self) -> list:
        atts = []
        for a in self.attributes:
            if a.ena_requirement is Requirement.EXCLUDE: continue
            if a.value is None or a.value == "": continue
            if a.type_ is FieldType.FILE: continue
            atts.append({"tag": a.ena_name, "value": a.value,
                         "units": a.units})
        return atts


    @property
    def gisaid_attributes(self) -> List[dict]:
        atts = []
        i = 0
        for a in self.attributes:
            if a.gisaid_requirement is Requirement.EXCLUDE: continue
            atts.append({"tag": a.gisaid_name, "value": a.value, "index": i,
                         "header": a.gisaid_header})
            i += 1
        return atts


    def save_files(self) -> None:
        for a in self.attributes:
            if a.type_ is FieldType.FILE:
                ext = a.value.filename.split(".")[-1]
                file = pathlib.Path("/home/seqmeta/uploads/samples",
                        self.name + "." + ext)
                a.value.save(file)
                a.value = file
