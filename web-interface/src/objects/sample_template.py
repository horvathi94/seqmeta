from dataclasses import dataclass, field
from typing import List
from .pickle import PickleFile
from .taxonomy import Taxonomy
from .attributes.attr_field import AttributeField


@dataclass
class SampleTemplate(PickleFile):

    name: str
    description: str = "No description available."
    extension: str = "template"
    fields: List[AttributeField] = field(default_factory=lambda: [])
    taxonomy: Taxonomy = Taxonomy()
    ena_checklist: str = "N/A"
    gisaid_assembly: bool = False
    ena_reads: bool = False


    def add_attribute(self, a: AttributeField) -> None:
        if not isinstance(a, AttributeField):
            raise ValueError("AttributeField required.")
        self.fields.append(a)


    @property
    def attribute_count(self) -> int:
        return len(self.fields)


    @property
    def template_name(self) -> str:
        return self.name


    @template_name.setter
    def template_name(self, name: str) -> None:
        self.name = name


    @classmethod
    def list_names(cls) -> List[str]:
        names = []
        for d in cls.BASE_PATH.iterdir():
            if d.is_dir(): names.append(d.name)
        return names


    @classmethod
    def load(cls, name: str) -> "SampleTemplate":
        t = SampleTemplate(name=name)
        return cls.load_pickle(t.file)
