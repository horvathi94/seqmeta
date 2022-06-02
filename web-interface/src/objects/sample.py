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
        for i, a in enumerate(self.attributes):
            if a == attr:
                self.attributes[i] = a
                return
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
        loaded = cls.load_pickle(s.file)
        if loaded is None:
            return s
        return loaded


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


    def update_attributes(self, atts: List["SampleAttribute"]) -> None:
        attr_names = [a.general_name for a in atts]
        for a in self.attributes:
            if a.is_file() or a.general_name in attr_names: continue
            self.attributes.remove(a)
        for a in atts:
            self.add_attribute(a)


    def list_text_attributes(self) -> List["SampleAttribute"]:
        return [a for a in self.attributes if not a.is_file()]


    def list_file_attributes(self) -> List["SampleAttribute"]:
        return [a for a in self.attributes if a.is_file()]


    def clear_files(self, a: "SampleAttribute") -> None:
        print(f"\nClearing files: {a.value}")
        for seqfile in a.value:
            seqfile.delete()


    def save_files(self, a: "SampleAttribute", files: list) -> None:
        a.value = []
        for f in files:
            seqfile = SeqFile(self.path)
            seqfile.filename = f.filename
            seqfile.sample_name = self.name
            seqfile.file_type = a.seqfile_type
            seqfile.save_data(f)
            a.value.append(seqfile)


    def update_file(self, new_a: "SampleAttribute", files: list) -> None:
        a = self.get_attribute(new_a.general_name)

        if a is None:
            # New attribute is not in sample attributes
            self.save_files(new_a, files)
        elif len(files) > 0:
            # There were files submitted
            self.clear_files(a)
            self.save_files(new_a, files)
        else:
            # There were no files submitted
            new_a.value = a.value
        self.add_attribute(new_a)



    def update_files(self, atts: List["SampleAttribute"], files: dict) -> None:
        attr_names = [a.general_name for a in atts]
        for a in self.list_file_attributes():
            if a.general_name not in attr_names:
                self.attributes.remove(a)

        for new_a in atts:
            self.update_file(new_a, files[new_a.general_name])


    def delete(self) -> None:
        for a in self.list_file_attributes():
            self.clear_files(a)
        self.file.unlink()


    def list_gisaid_attributes(self) -> List["SampleAttribute"]:
        return [a for a in self.attributes if a.gisaid_include()]


    def list_ena_sample_attributes(self) -> List["SampleAttribute"]:
        return [a for a in self.attributes if a.ena_include()]
