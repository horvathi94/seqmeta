from dataclasses import dataclass, field
from typing import List
from .pickle import PickleFile
from .taxonomy import Taxonomy


@dataclass
class Sample(PickleFile):

    template_name: str
    taxonomy: Taxonomy = Taxonomy()
    attributes: list = field(default_factory=lambda: [])
    extension: str = "sample"
    ena_checklist: str = ""


    def add_attribute(self, attr: "SampleAttribute") -> None:
        self.attributes.append(attr)


    def get_attribute(self, name: str) -> "SampleAttribute":
        for a in self.attributes:
            if a.general_name == name:
                return a


    def get_value(self, name: str) -> any:
        attr = self.get_attribute(name)
        return attr.value


    def set_value(self, name: str, value: any) -> None:
        attr = self.get_attribute(name)
        attr.value = value


    @property
    def name(self) -> str:
        return str(self.get_value("sample_name"))


    def save_files(self, files: list) -> None:
        pass
