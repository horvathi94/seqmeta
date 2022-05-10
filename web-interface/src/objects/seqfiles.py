import pathlib
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
    data: any = None
    path: pathlib.Path = None


    @property
    def filename(self) -> str:
        return self.name + "." + self.extension


    @filename.setter
    def filename(self, filename: str) -> None:
        self.name, self.extension = filename.split(".")


    @property
    def filedata(self) -> "FileStorage":
        return data


    @filedata.setter
    def filedata(self, fdata: "FileStorage") -> None:
        self.data = fdata
        self.filename = fdata.filename


    @property
    def file(self) -> pathlib.Path:
        return pathlib.Path(self.path, self.filename)


    def save(self) -> None:
        self.data.save(self.filename)
