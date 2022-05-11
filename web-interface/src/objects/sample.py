import pathlib
from dataclasses import dataclass, field
from typing import List
from .pickle import PickleFile
from .attributes.sampleattr import SampleAttribute
from .taxonomy import Taxonomy
from .seqfiles import SeqFile, SeqFileType


@dataclass
class Sample(PickleFile):

    name: str
    short_description: str = ""
    template_name: str = None
    attributes: List[SampleAttribute] = field(default_factory=lambda: [])
    extension: str = "sample"
    taxonomy: Taxonomy = None
    ena_checklist: str = None


    def __getstate__(self):
        return {
            "name": self.name,
            "short_description": self.short_description,
            "template_name": self.template_name,
            "taxonomy": self.taxonomy,
            "attributes": self.attributes,
        }


    def __setstate__(self, state):
        self.name = state["name"]
        self.short_description = state["short_description"]
        self.template_name = state["template_name"]
        self.taxonomy = state["taxonomy"]
        self.attributes = []
        for a in state["attributes"]:
            self.add_attribute(a)
        self.files = []


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


    def save_file(self, name: str, file: "FileStorage") -> None:
        if file.filename == "": return
        seqfile = SeqFile()
        seqfile.path_base = self.path
        seqfile.filedata = file
        seqfile.name = self.name
        seqfile.type_ = SeqFileType.READ
        a = SampleAttribute(general_name=name,
                            value=seqfile.filename, is_file=True)
        self.add_attribute(a)
        seqfile.save()


    def load_files(self, name: str) -> List["file"]:
        pass
