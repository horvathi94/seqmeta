from dataclasses import dataclass
from enum import Enum


class SeqFileType:

    READ = "read"
    ASSEMBLY = "assembly"



@dataclass
class SeqFile:

    name: str = ""
    type_: SeqFileType = SeqFileType.READ
    extension: str = ""
    file_data: any = None


    @property
    def filename(self) -> str:
        return self.name + "." + self.extension


