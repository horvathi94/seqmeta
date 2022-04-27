import pathlib
import pickle
from dataclasses import dataclass, field, asdict
from typing import List
from .attribute import Attribute


@dataclass
class Template:

    path: pathlib.Path = pathlib.Path("/home/seqmeta/uploads/samples/")
    name: str = None
    attributes: List[Attribute] = field(default_factory=lambda: [])
    short_description: str = None
    ena_checklist: str = None
    taxonomy_id: int = None
    scientific_name: str = None
    common_name: str = None


    def get_attribute(self, name: str) -> Attribute:
        for a in self.attributes:
            if a.general_name == name: return a
        return None


    def clear_attributes(self) -> None:
        self.attributes = []


    def add_attribute(self, new_attr: Attribute) -> None:
        for i, attr in enumerate(self.attributes):
            if attr.general_name == new_attr.general_name:
                self.attributes[i] = new_attr
                return
        self.attributes.append(new_attr)


    def asdict(self) -> dict:
        return asdict(self)


    def asjson(self) -> dict:
        return {
            "name": self.name,
            "short_description": self.short_description,
            "ena_checklist": self.ena_checklist,
            "taxonomy_id": self.taxonomy_id,
            "scientific_name": self.scientific_name,
            "common_name": self.common_name,
            "attributes": [a.asjson() for a in self.attributes]
        }

    @property
    def attribute_count(self) -> int:
        return len(self.attributes)
