import pathlib
from dataclasses import dataclass, field
from typing import List
from .pickle import PickleFile
from .taxonomy import Taxonomy
from .attributes.attribute import Attribute


SAMPLE_NAME_ATTR = Attribute("sample_name", "Sample name",
    description="Sample name for easier identification "\
                "(will not be submitted).",
    is_fixed = True)

SAMPLE_DESCRIPTION_ATTR = Attribute("short_description", "Short description",
    description="Sample short description for easier identification "\
                "(will not be submitted).",
    is_fixed = True)



@dataclass
class SampleTemplate(PickleFile):

    name: str
    short_description: str = ""
    taxonomy: Taxonomy = Taxonomy()
    attributes: List[Attribute] = field(default_factory=lambda: [])
    extension: str = "template"


    def __post_init__(self):
        self.add_attribute(SAMPLE_NAME_ATTR)
        self.add_attribute(SAMPLE_DESCRIPTION_ATTR)


    @property
    def template_name(self) -> str:
        return self.name


    def add_attribute(self, new_a: Attribute) -> None:
        for i, a in enumerate(self.attributes):
            if a == new_a:
                self.attributes[i] = new_a
                return
        self.attributes.append(new_a)


    def get_attribute(self, aname: str) -> Attribute:
        for a in self.attributes:
            if a.general_name == aname: return a
        return None


    @property
    def attribute_count(self) -> int:
        return len(self.editor_attributes())


    def asjson(self) -> dict:
        return {
            "name": self.name,
            "short_description": self.short_description,
            "taxonomy": self.taxonomy,
            "ena_checklist": self.ena_checklist,
            "attributes": [a.asjson() for a in self.attributes]
        }


    @property
    def ena_checklist(self) -> str:
        for a in self.attributes:
            if a.general_name == "ena_checklist": return a.value
        return None


    @ena_checklist.setter
    def ena_checklist(self, ena_checklist: str) -> None:
        a = Attribute("ena_checklist", "ENA Checklist", is_fixed=True,
                      value=ena_checklist)
        self.add_attribute(a)


    @classmethod
    def list_names(cls) -> list:
        names = []
        for d in cls.BASE_PATH.iterdir():
            if d.is_dir(): names.append(d.name)
        return names


    @classmethod
    def load(cls, name: str) -> "SampleTemplate":
        t = SampleTemplate(name=name)
        return cls.load_pickle(t.file)
