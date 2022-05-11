import pathlib
from dataclasses import dataclass
from enum import Enum


class SeqFileType(Enum):

    READ = "read"
    ASSEMBLY = "assembly"


FILE_DIR = {
    SeqFileType.READ: "reads",
    SeqFileType.ASSEMBLY: "assemblies",
}


EXTENSIONS = {
    "fasta": ["fa", "fasta"],
    "bam": ["bam"],
    "fastq": ["fastq"],
}


@dataclass
class SeqFile:

    name: str = ""
    type_: SeqFileType = SeqFileType.READ
    _extension: str = ""
    data: any = None
    path_base: pathlib.Path = None


    @property
    def extension(self) -> str:
        return self._extension


    @extension.setter
    def extension(self, ext: str) -> None:
        for ekey in EXTENSIONS:
            if ext in EXTENSIONS[ekey]:
                self._extension = ekey
                return


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
        chk = pathlib.Path(self.path)
        if not chk.is_dir: chk.mkdir(parents=True, exist_ok=True)
        self.data.save(self.file)


    @property
    def path(self) -> pathlib.Path:
        return pathlib.Path(self.path_base, FILE_DIR[self.type_])
