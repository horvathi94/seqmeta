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


    def get_attribute(self, name: str) -> Attribute:
        for a in self.attributes:
            if a.general_name == name: return a
        return None


    def add_attribute(self, a: Attribute) -> None:
        self.attributes.append(a)


    def asdict(self) -> dict:
        return asdict(self)


    def asjson(self) -> dict:
        return {
            "name": self.name,
            "short_description": self.short_description,
            "ena_checklist": self.ena_checklist,
            "attributes": [a.asjson() for a in self.attributes]
        }

    @property
    def attribute_count(self) -> int:
        return len(self.attributes)
