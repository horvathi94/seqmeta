import pathlib
from dataclasses import dataclass
from .attributes.samplefile import SampleFile, SeqFileType



FILE_DIR = {
    SeqFileType.READ: "reads",
    SeqFileType.ASSEMBLY: "assemblies",
    SeqFileType.CONTIGS: "contigs",
    SeqFileType.SCAFFOLDS: "scaffolds"
}



@dataclass
class SeqFile:

    _name: str = ""
    type_: SeqFileType = SeqFileType.READ
    _extension: str = ""
    data: any = None
    path_base: pathlib.Path = None
    order: int = 0


    def __lt__(self, other):
        return self.order < other.order


    def __gt__(self, other):
        return self.order > other.order


    def __eq__(self, other):
        return self.order == other.order


    @property
    def name(self) -> str:
        return self._name


    @name.setter
    def name(self, name: str) -> None:
        if len(name.split("_")) == 1:
            self._name = name
        else:
            self._name = name.split("_")[0]
            self.order = int(name.split("_")[1])


    @property
    def extension(self) -> str:
        return self._extension


    @extension.setter
    def extension(self, ext: str) -> None:
        self._extension = SampleFile.valid_extension(ext)


    @property
    def filename(self) -> str:
        if self.order == 0:
            return self.name + "." + self.extension
        return self.name + "_" + str(self.order) + "." + self.extension


    @filename.setter
    def filename(self, filename: str) -> None:
        for ext in SampleFile.all_extensions():
            if filename.endswith(ext):
                self.extension = ext
                self.name = filename.split(ext)[0].replace(".", "")
                return


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


    def delete(self) -> None:
        self.file.unlink()


    def save(self) -> None:
        chk = pathlib.Path(self.path)
        if not chk.is_dir(): chk.mkdir(parents=True, exist_ok=True)
        self.data.save(self.file)


    @classmethod
    def load(cls, path: pathlib.Path, fname: str, tp: SeqFileType) -> "SeqFile":
        seqfile = SeqFile()
        seqfile.path_base = path
        seqfile.filename = fname
        seqfile.type_ = tp
        return seqfile


    def check_files(self) -> bool:
        for f in self.path.iterdir():
            if f.stem == self.name:
                self.filename = f
                return True
        return False


    @property
    def path(self) -> pathlib.Path:
        return pathlib.Path(self.path_base, FILE_DIR[self.type_])

