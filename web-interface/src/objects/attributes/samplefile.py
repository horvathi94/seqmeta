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



@dataclass
class SampleFile:

    general_name: str
    label: str
    filetype: SeqFileType = SeqFileType.READ
    short_description: str = ""
    is_active: bool = False
    repos: List[str] = field(default_factory=lambda: [])


    def add_repo(self, repo: str) -> None:
        for r in self.repos:
            if r == repo: return
        self.repos.append(repo)


    def switch_on(self, repo: str) -> None:
        self.add_repo(repo)
        self.is_active = True


    def asjson(self) -> dict:
        return {
            "general_name": self.general_name,
            "label": self.label,
            "short_description": self.short_description,
            "is_active": self.is_active,
            "filetype": self.filetype.value,
            "repos": self.repos
        }


    def as_attribute(self) -> Attribute:
        return Attribute(self.general_name, self.label, type_=FieldType.FILE,
                    description=self.short_description)


    @classmethod
    def valid_extension(cls, ext: str) -> str:
        EXTENSIONS = {
            "fasta": ["fa", "fasta"],
            "bam": ["bam"],
            "fastq": ["fastq"],
        }
        return EXTENSIONS[ext]


    @classmethod
    def create_full_list(cls) -> List["SampleFile"]:
        gisaid_assembly = SampleFile(
            general_name="gisaid_assembly",
            label="GISAID assembly",
            filetype=SeqFileType.ASSEMBLY,
            short_description=\
                "Assembled sequence for upload to GISAID database.")
        raw_reads = SampleFile(
            general_name="raw_reads",
            label="Raw reads",
            filetype=SeqFileType.READ,
            short_description=\
                "Raw reads for uploading to SRA database.")
        scaffolds_file = SampleFile(
            general_name="scaffolds_file",
            label="Scaffolds file",
            filetype=SeqFileType.ASSEMBLY,
            short_description=\
                "Scaffolds file.")
        contigs_file = SampleFile(
            general_name="contigs_file",
            label="Contigs file",
            filetype=SeqFileType.ASSEMBLY,
            short_description=\
                "Contigs file.")

        return [gisaid_assembly, raw_reads, scaffolds_file, contigs_file]
