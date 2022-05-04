import pathlib
from dataclasses import dataclass, field
from typing import List
from .pickle import PickleFile
from .attributes.sampleattr import SampleAttribute
from .taxonomy import Taxonomy


@dataclass
class Sample(PickleFile):

    name: str
    short_description: str = ""
    template_name: str = None
    attributes: List[SampleAttribute] = field(default_factory=lambda: [])
    extension: str = "sample"
    taxonomy: Taxonomy = None
    ena_checklist: str = None


    def add_attribute(self, a: SampleAttribute) -> None:
        self.attributes.append(a)


    def asjson(self) -> dict:
        return {
            "name": self.name,
            "short_description": self.short_description,
            "template_name": self.template_name,
            "attributes": [a.asjson() for a in self.attributes]
        }


    def list_ena(self) -> List[SampleAttribute]:
        return [a for a in self.attributes if a.ena_include()]


    def list_gisaid(self) -> List[SampleAttribute]:
        return [a for a in self.attributes if a.gisaid_include()]


    @classmethod
    def list_names(cls, template_name: str) -> list:
        names = []
        s = Sample(name="", template_name=template_name)
        for f in s.path.iterdir():
            if cls.check_extension(f.name):
                names.append(f.stem)
        return names


    @classmethod
    def load(cls, name: str, template_name: str) -> "Sample":
        s = Sample(name=name, template_name=template_name)
        return cls.load_pickle(s.file)
