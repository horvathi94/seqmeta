from dataclasses import dataclass, field
from typing import List
import shutil
from .pickle import PickleFile
from .taxonomy import Taxonomy
from .attributes.attr_field import AttributeField
from .attributes.file_field import FileField, ALL_FIELDS, REPO_FIELDS


@dataclass
class SampleTemplate(PickleFile):

    name: str
    description: str = "No description available."
    extension: str = "template"
    fields: List[AttributeField] = field(default_factory=lambda: [])
    file_fields: List[FileField] = field(default_factory=lambda: ALL_FIELDS)
    taxonomy: Taxonomy = Taxonomy()
    ena_checklist: str = "N/A"


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


    def as_json(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "taxonomy": self.taxonomy,
            "ena_checklist": self.ena_checklist,
            "gisaid_assembly": self.check_file_field("gisaid_assembly"),
            "ena_reads": self.check_file_field("ena_reads"),
            "fields": [f.as_json() for f in self.fields],
            "file_fields": [f.as_json() for f in self.file_fields],
        }


    def set_file_field(self, fname: str) -> None:
        for file_field in self.file_fields:
            if file_field.general_name == REPO_FIELDS[fname]["type"]:
                file_field.add_repo(REPO_FIELDS[fname]["repo"])
                return


    def check_file_field(self, fname: str) -> bool:
        for file_field in self.file_fields:
            if file_field.general_name != REPO_FIELDS[fname]["type"]:
                continue
            if REPO_FIELDS[fname]["repo"] in file_field.repos:
                return True
        return False


    def active_files(self) -> List[FileField]:
        return [f for f in self.file_fields if f.is_active]


    def get_field(self, name: str) -> AttributeField:
        for f in self.fields:
            if f.general_name == name:
                return f


    def delete(self) -> None:
        shutil.rmtree(self.path)
