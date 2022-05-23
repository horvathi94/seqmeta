from dataclasses import dataclass, field
from typing import List
from enum import Enum
from .attribute import Attribute
from .enums import FieldType


class SeqFileType(Enum):

    READ = "read"
    ASSEMBLY = "assembly"
    CONTIGS = "contigs"
    SCAFFOLDS = "scaffolds"


VALID_EXTENSIONS = {
    "fasta": {
        "accepted_by": [SeqFileType.ASSEMBLY, SeqFileType.CONTIGS, SeqFileType.SCAFFOLDS],
        "same_as": ["fa", "fasta", "fna"],
    },
    "bam": {
        "accepted_by": [SeqFileType.ASSEMBLY, SeqFileType.CONTIGS, SeqFileType.SCAFFOLDS],
        "same_as": ["bam"],
    },
    "fastq.gz": {
        "accepted_by": [SeqFileType.READ],
        "same_as": ["fastq.gz"],
    },
}


@dataclass
class SampleFile:

    general_name: str
    label: str
    filetype: SeqFileType = SeqFileType.READ
    short_description: str = ""
    is_active: bool = False
    repos: List[str] = field(default_factory=lambda: [])


    @classmethod
    def all_extensions(cls) -> List[str]:
        exts = []
        for ext_dict in VALID_EXTENSIONS.values():
            exts += ext_dict["same_as"]
        return exts


    @property
    def accepted_extensions(self) -> List[str]:
        for ext in VALID_EXTENSIONS.values():
            if self.filetype in ext["accepted_by"]:
                return ext["same_as"]


    def add_repo(self, repo: str) -> None:
        for r in self.repos:
            if r == repo: return
        self.repos.append(repo)


    def switch_on(self, repo: str) -> None:
        self.add_repo(repo)
        self.is_active = True


    def asjson(self) -> dict:
        d =  {
            "general_name": self.general_name,
            "label": self.label,
            "short_description": self.short_description,
            "is_active": self.is_active,
            "filetype": self.filetype.value,
            "repos": self.repos,
            "accepted_extensions": self.accepted_extensions
        }
        print(f"\n\nSampleFile as json: {d}")
        return {
            "general_name": self.general_name,
            "label": self.label,
            "short_description": self.short_description,
            "is_active": self.is_active,
            "filetype": self.filetype.value,
            "repos": self.repos,
            "accepted_extensions": self.accepted_extensions
        }


    def as_attribute(self) -> Attribute:
        return Attribute(self.general_name, self.label, type_=FieldType.FILE,
                    description=self.short_description,
                    options=self.accepted_extensions)


    @classmethod
    def valid_extension(cls, ext: str) -> str:
        for valid_ext in VALID_EXTENSIONS:
            if ext in VALID_EXTENSIONS[valid_ext]["same_as"]:
                return valid_ext


    @classmethod
    def create_full_list(cls) -> List["SampleFile"]:
        return FILE_FIELDS



FILE_FIELDS = [
    SampleFile(
        general_name="gisaid_assembly", label="GISAID assembly",
        filetype=SeqFileType.ASSEMBLY,
        short_description="Assembled sequence for upload to GISAID database."),
    SampleFile(
        general_name="raw_reads", label="Raw reads",
        filetype=SeqFileType.READ,
        short_description="Raw reads for uploading to SRA database."),
    SampleFile(
        general_name="scaffolds_file", label="Scaffolds file",
        filetype=SeqFileType.ASSEMBLY,
        short_description="Scaffolds file."),
    SampleFile(
        general_name="contigs_file",
        label="Contigs file",
        filetype=SeqFileType.ASSEMBLY,short_description="Contigs file.")
]
