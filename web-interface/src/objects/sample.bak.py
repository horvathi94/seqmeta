import pathlib
from dataclasses import dataclass, field
from typing import List
from .pickle import PickleFile
from .attributes.sampleattr import SampleAttribute
from .taxonomy import Taxonomy
from .seqfiles import SeqFile, SeqFileType

READ_ELEMENTS = ["ena_study", "ena_experiment_name", "platform", "instrument",
         "insert_size", "library_name", "library_source",
         "library_selection", "library_strategy",
         "ena_experiment_description"]

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
            "ena_checklist": self.ena_checklist,
            "attributes": [a.asjson() for a in self.attributes]
        }


    def list_ena(self) -> List[SampleAttribute]:
        attribs = []
        for a in self.attributes:
            if not a.ena_include(): continue
            if not a.ena_name: continue
#            if a.general_name in READ_ELEMENTS: continue
            if a.general_name == "ena_title": continue
            attribs.append(a)
        return attribs


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


    def save_file(self, file: "FileStorage", tp: SeqFileType) -> str:
        seqfile = SeqFile()
        seqfile.path_base = self.path
        seqfile.filedata = file
        seqfile.name = self.name
        seqfile.type_ = tp
        seqfile.save()
        return seqfile


    def save_files(self, sample_file: "SampleFile", files: list) -> None:
        seqfiles = []
        for file in files:
            if file.filename == "": continue
            sf = self.save_file(file, sample_file.filetype)
            seqfiles.append(sf.filename)

        a = SampleAttribute(general_name=sample_file.general_name,
                            value=seqfiles, is_file=True)
        self.add_attribute(a)


    @property
    def file_attributes(self) -> List[SampleAttribute]:
        return [a for a in self.attributes if a.is_file]


    def delete(self) -> None:
        for a in self.file_attributes:
            for f in self.load_files(a.general_name):
                f.delete()
        self.file.unlink()


    def check_files(self, name: str) -> bool:
        for a in self.attributes:
            if a.general_name == name: return True
        seqfile = SeqFile()
        seqfile.path_base = self.path
        seqfile.name = self.name
        seqfile.type_ = SeqFileType.READ
        if not seqfile.check_files(): return False
        a = SampleAttribute(general_name=name,
                            value=str(seqfile.file), is_file=True)
        self.add_attribute(a)
        return True


    def load_files(self, name: str) -> List["file"]:
        seqfiles = []
        for a in self.file_attributes:
            if a.general_name == name:
                seqfile = SeqFile()
                seqfile.path_base = self.path
                seqfile.filename = a.value
                seqfile.type_ = SeqFileType.READ
                seqfiles.append(seqfile)
        return seqfiles


    def list_ena_experiment(self) -> List[dict]:
        items = []
        items.append({"name": "SAMPLE", "value": self.name})
        for e in READ_ELEMENTS:
            attr = self.get_attribute(e)
            items.append({"name": attr.ena_name, "value": attr.value})

        for seqfile in self.load_read_files():
            items.append({"name": "FASTQ", "value": seqfile.filename})
        return items


    def get_attribute(self, name: str) -> SampleAttribute:
        for a in self.attributes:
            if a.general_name == name:
                return a


    def get_attribute_value(self, name: str) -> any:
        attr = self.get_attribute(name)
        return attr.value


    @property
    def ena_title(self) -> str:
        return self.get_attribute_value("ena_title")


    @property
    def gisaid_virusname(self) -> str:
        return self.get_attribute_value("gisaid_virusname")


    @property
    def gisaid_filename(self) -> str:
        return self.get_attribute_value("gisaid_filename")


    def load_gisaid_assembly(self) -> SeqFile:
        vals = self.get_attribute_value("gisaid_assembly")
        seqfile = SeqFile.load(self.path, vals[0], SeqFileType.ASSEMBLY)
        return seqfile


    def load_read_files(self) -> List[SeqFile]:
        vals = self.get_attribute_value("raw_reads")
        return [SeqFile.load(self.path, v, SeqFileType.READ) for v in vals]


    @property
    def library_layout(self) -> str:
        reads = self.load_read_files()
        if len(reads) == 2: return "paired"
        if len(reads) == 1: return "single"
        return None
