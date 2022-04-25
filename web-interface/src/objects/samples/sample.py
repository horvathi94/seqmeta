from dataclasses import dataclass, field, asdict
from typing import List
from seqmeta.database.templates import TemplatesTable
from seqmeta.objects.samples.attribute import Attribute, Requirement




@dataclass
class Sample:

    id: int = None
    name: str = None
    template_id: int = None
    attributes: List[Attribute] = field(default_factory=lambda: [])
    short_description: str = None
    status: str = None


    def __post_init__(self):
        if self.status == "new": self.id = 0


    def add_attribute(self, a: Attribute) -> None:
        self.attributes.append(a)


    @property
    def template_name(self) -> str:
        return TemplatesTable.select(self.template_id).name


    def asdict(self) -> dict:
        return {
            "name": self.name,
            "template_id": self.template_id,
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
            atts.append({"tag": a.ena_name, "value": a.value})
        return atts


    @property
    def gisaid_attributes(self) -> List[dict]:
        atts = []
        i = 0
        for a in self.attributes:
            if a.gisaid_requirement is Requirement.EXCLUDE: continue
            atts.append({"tag": a.gisaid_name, "value": a.value, "index": i})
            i += 1
        return atts
