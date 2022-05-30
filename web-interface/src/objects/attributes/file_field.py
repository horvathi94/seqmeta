from dataclasses import dataclass, field
from typing import List
from .enums import FieldType
from .attr_field import AttributeField
from .file_types import FILE_TYPES, SeqFileType



@dataclass
class FileField(AttributeField):

    type_: FieldType = FieldType.FILE
    repos: List[str] = field(default_factory=lambda: [])
    _seqfile_type: str = None


    @property
    def file_type(self) -> SeqFileType:
        return SeqFileType(self._seqfile_type)


    @file_type.setter
    def file_type(self, sftype: SeqFileType) -> None:
        if isinstance(sftype, SeqFileType):
            sftype = sftype.name
        self._seqfile_type = sftype


    def valid_extensions(self) -> List[str]:
        valid = []
        for ftype in FILE_TYPES:
            if ftype.is_valid_for(self.file_type):
                valid.append(ftype.extensions)
        return valid


    def add_repo(self, r: str) -> None:
        for repo in self.repos:
            if repo == r: return
        self.repos.append(r)


    @property
    def is_active(self) -> bool:
        if len(self.repos) == 0: return False
        return True


    def as_json(self) -> dict:
        return {
            "general_name": self.general_name,
            "label": self.label,
            "type_": self.type_.value,
            "description": self.description,
            "options": self.valid_extensions()
        }


ALL_FIELDS = [
    FileField("assembly_file", "Assembly file",
              description="Upload assembled sequence files.",
              _seqfile_type="assembly"),
    FileField("read_files", "Sequencing read files",
              description="Upload prepared sequencing files.",
              _seqfile_type="read"),
]

REPO_FIELDS = {
    "gisaid_assembly": {"type": "assembly_file", "repo": "gisaid"},
    "ena_reads": {"type": "read_files", "repo": "ena"},
    "ena_contigs": {"type": "contigs_file", "repo": "ena"},
    "ena_scaffolds": {"type": "scaffolds_file", "repo": "ena"},
}
