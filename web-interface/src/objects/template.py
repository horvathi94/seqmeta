import pathlib
import shutil
from dataclasses import dataclass, field
from typing import List
from .pickle import PickleFile
from .taxonomy import Taxonomy
from .attributes.attribute import Attribute
from .attributes.enums import FieldType


SAMPLE_NAME_ATTR = Attribute("sample_name", "Sample name",
    description="Sample name for easier identification "\
                "(will not be submitted).",
    is_fixed = True)

SAMPLE_DESCRIPTION_ATTR = Attribute("short_description", "Short description",
    description="Sample short description for easier identification "\
                "(will not be submitted).",
    is_fixed = True)

SAMPLE_ENA_READ_FILES = Attribute("ena_read_files", "ENA read files",
    type_ = FieldType.FILE,
    description="Cleaned and prepared read files to upload.",
    is_fixed = True)



@dataclass
class SampleTemplate(PickleFile):

    name: str
    short_description: str = ""
    taxonomy: Taxonomy = Taxonomy()
    attributes: List[Attribute] = field(default_factory=lambda: [])
    extension: str = "template"
    gisaid_assembly: bool = False
    ena_reads: bool = False
    ena_scaffold: bool = False
    ena_contig: bool = False


    def __post_init__(self):
        self.add_attribute(SAMPLE_NAME_ATTR)
        self.add_attribute(SAMPLE_DESCRIPTION_ATTR)
        self.add_attribute(SAMPLE_ENA_READ_FILES)


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


    def list_attributes_for_json(self) -> List[Attribute]:
        return [a.asjson() for a in self.attributes if not a.is_invisible]


    def asjson(self) -> dict:
        return {
            "name": self.name,
            "short_description": self.short_description,
            "taxonomy": self.taxonomy,
            "ena_checklist": self.ena_checklist,
            "attributes": self.list_attributes_for_json()
        }


    @property
    def ena_checklist(self) -> str:
        for a in self.attributes:
            if a.general_name == "ena_checklist": return a.value
        return None


    @ena_checklist.setter
    def ena_checklist(self, ena_checklist: str) -> None:
        a = Attribute("ena_checklist", "ENA Checklist", is_invisible=True,
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


    def delete(self) -> None:
        shutil.rmtree(self.path)


    def files_from_list(self, files: List[str]) -> None:
        for f in files:
            setattr(self, f, True)
#        if "ena_reads" in raw: self.ena_reads = True
#        if "ena_scaffold" in raw: self.ena_scaffold = True
#        if "ena_contig" in raw: self.ena_contig = True
#        if "gisaid_assembly" in raw: self.gisaid_assembly = True
