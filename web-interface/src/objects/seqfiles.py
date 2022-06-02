import hashlib
import pathlib
from dataclasses import dataclass
from .attributes.file_types import FILE_TYPES, SeqFileType


DIRNAMES = {
    SeqFileType.READ: "reads",
    SeqFileType.ASSEMBLY: "assemblies",
    SeqFileType.CONTIGS: "contigs",
    SeqFileType.SCAFFOLDS: "scaffolds"
}


class SeqFile:

    def __init__(self, path_base: str):
        self.sample_name = ""
        self.order = 0
        self._extension = ""
        self.path_base = path_base
        self._filetype = None


    def set_from_filename(self, name: str) -> None:
        split = name.split("_")
        if len(split) > 1:
            name = split[0]
            self.order = int(split[1])
        self.sample_name = name


    @property
    def extension(self) -> str:
        return self._extension


    @extension.setter
    def extension(self, ext: str) -> None:
        for ft in FILE_TYPES:
            if ft.is_valid_extension(ext):
                self._extension = ft.main_extension


    @property
    def filename(self) -> str:
        if self.order == 0:
            return self.sample_name + "." + self.extension
        return self.sample_name + "_" + str(self.order) + "." + self.extension


    @filename.setter
    def filename(self, fname: str) -> None:
        for ft in FILE_TYPES:
            for ext in ft.extensions:
                if fname.endswith(ext):
                    self.extension = ext
                    self.set_from_filename(fname.split(ext)[0].replace(".",""))
                    return


    @property
    def path(self) -> pathlib.Path:
        return pathlib.Path(self.path_base, DIRNAMES[self.file_type])


    @property
    def file(self) -> pathlib.Path:
        return pathlib.Path(self.path, self.filename)


    @property
    def file_type(self) -> SeqFileType:
        return SeqFileType(self._filetype)


    @file_type.setter
    def file_type(self, ftype: any) -> None:
        if isinstance(ftype, SeqFileType):
            ftype = ftype.value
        self._filetype = ftype


    def md5_checksum(self) -> str:
        hash_md5 = hashlib.md5()
        with open(self.file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


    def save_data(self, fdata: "FileStorage") -> None:
        chk = pathlib.Path(self.path)
        if not chk.is_dir(): chk.mkdir(parents=True, exist_ok=True)
        fdata.save(self.file)


    def as_json(self) -> str:
        return self.filename


    def delete(self) -> None:
        if self.file.is_file():
            self.file.unlink()
