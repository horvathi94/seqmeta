import pathlib
from dataclasses import dataclass, field, asdict
from typing import List
from seqmeta.database.templates import TemplatesTable
from seqmeta.objects.samples.attribute import Attribute, Requirement
from .attribute import FieldType



@dataclass
class Sample:

    name: str = None
    template_name: str = None
    attributes: List[Attribute] = field(default_factory=lambda: [])
    short_description: str = None
    status: str = None


    def __post_init__(self):
        if self.status == "new": self.id = 0


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
        json["attributes"] = {a.general_name: a.value for a in self.attributes}
        return json


    @property
    def ena_list(self) -> list:
        atts = []
        for a in self.attributes:
            if a.ena_requirement is Requirement.EXCLUDE: continue
            if a.value is None or a.value == "": continue
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
