from dataclasses import dataclass, field
from typing import List
from .pickle import PickleFile
from .taxonomy import Taxonomy
from .seqfiles import SeqFile
from .attributes.enums import Requirement
from .sample_template import SampleTemplate



@dataclass
class Sample(PickleFile):

    template_name: str
    taxonomy: Taxonomy = Taxonomy()
    attributes: list = field(default_factory=lambda: [])
    extension: str = "sample"
    ena_checklist: str = ""
    _name: str = None


    def get_template(self) -> SampleTemplate:
        return SampleTemplate.load(self.template_name)


    def add_attribute(self, attr: "SampleAttribute") -> None:
        self.attributes.append(attr)


    def get_attribute(self, name: str) -> "SampleAttribute":
        for a in self.attributes:
            if a.general_name == name:
                return a
        return None


    def get_value(self, name: str) -> any:
        attr = self.get_attribute(name)
        if attr is None: return None
        return attr.value


    def set_value(self, name: str, value: any) -> None:
        attr = self.get_attribute(name)
        if attr is None: return
        attr.value = value


    @property
    def name(self) -> str:
        name = self.get_value("sample_name")
        if name is None:
            name = self._name
        return str(name)


    @name.setter
    def name(self, name: str) -> None:
        self._name = name


    def is_ena_complete(self) -> bool:
        for a in self.attributes:
            if a.ena_requirement is not Requirement.MANDATORY: continue
            if not a.has_value():
                return False
        return True


    def is_gisaid_complete(self) -> bool:
        for a in self.attributes:
            if a.gisaid_requirement is not Requirement.MANDATORY: continue
            if not a.has_value():
                return False
        return True


    @classmethod
    def list_names(cls, template_name: str) -> list:
        names = []
        s = Sample(template_name=template_name)
        for f in s.path.iterdir():
            if cls.check_extension(f.name):
                names.append(f.stem)
        return names


    @classmethod
    def load(cls, name: str, template_name: str) -> "Sample":
        s = Sample(template_name=template_name)
        s.name = name
        return cls.load_pickle(s.file)


    def as_json(self) -> dict:
        return {
            "name": self.name,
            "template_name": self.template_name,
            "short_description": str(self.get_value("short_description")),
            "is_ena_complete": self.is_ena_complete(),
            "is_gisaid_complete": self.is_gisaid_complete(),
            "taxonomy": self.taxonomy,
            "attributes": [a.as_json() for a in self.attributes],
            "ena_checklist": self.ena_checklist,
        }


    @classmethod
    def from_sub(cls, template: "SampleTemplate", atts: dict) -> "Sample":
        s = Sample(template.name)
        s.taxonomy = template.taxonomy
        s.ena_checklist = template.ena_checklist
        for aname, aval in atts.items():
            field = template.get_field(aname)
            a = field.as_sample_attribute()
            a.value = aval
            s.add_attribute(a)
        return s


    def save_files(self, files: any) -> None:
        pass


