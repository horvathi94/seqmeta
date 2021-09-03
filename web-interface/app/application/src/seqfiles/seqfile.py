import os
from Bio import SeqIO
from dataclasses import dataclass
from application.src.seqfiles import db
from application.src.samples.samples import Samples
from .types import AssemblyLevels, SeqFileTypes



@dataclass
class SeqFile:

    seqtype: SeqFileTypes;
    sample_id: int = 0;
    sample_name: str = None;
    is_assembly: bool = None;
    assembly_level: str = None;
    is_forward_read: bool = None;
    file_type_id: int = None;
    file_type: str = None;
    extension_id: int = None;
    extension: str = None;
    assembly_method_id: int = None;
    assembly_method: str = None;
    filedata: "flask.fileStorage" = None;
    to_save: bool = False;
    exists: bool = None;


    def __post_init__(self):
        self.is_assembly = self._is_assembly();
        self.assembly_level = self._assembly_level();
        self.is_forward_read = self._is_forward_read();


    def _is_assembly(self) -> bool:
        if self.seqtype in SeqFileTypes.list_assemblies():
            return True;
        return False;


    def _is_forward_read(self) -> bool:
        if self.seqtype not in SeqFileTypes.list_reads():
            return None;
        if self.seqtype == SeqFileTypes.FWREAD_FILE:
            return True;
        if self.seqtype == SeqFileTypes.RVREAD_FILE:
            return False;
        return None;


    def _assembly_level(self) -> str:
        if self.seqtype not in SeqFileTypes.list_assemblies():
            return None;
        if self.seqtype == SeqFileTypes.CONSENSUS_FILE:
            return AssemblyLevels.CONSENSUS;
        if self.seqtype == SeqFileTypes.CONTIGS_FILE:
            return AssemblyLevels.CONTIGS;
        if self.seqtype == SeqFileTypes.SCAFFOLDS_FILE:
            return AssemblyLevels.SCAFFOLDS;


    def get_filename(self) -> str:
        if self.sample_name is None:
            raise Exception("Error generating file name.");
        if self.sample_name == "": return "";

        fname = f"{self.sample_name}_";
        if self.is_assembly:
            if self.assembly_level is None: return "";
            fname+= f"{self.assembly_level.name.lower()}";
        else:
            if self.is_forward_read is None: return "";
            fname+= "fw_read" if self.is_forward_read else "rv_read";
        fname+= f".{self.extension}";
        return fname;


    @classmethod
    def create_path(cls, path: "os.path") -> None:
        if os.path.exists(path): return;

        try:
            os.makedirs(path);
        except Exception as e:
            raise Exception(f"Failed to create dir: {e}");


    def get_path(self) -> "os.path":
        if self.seqtype in SeqFileTypes.list_assemblies():
            return "/uploads/samples/assemblies/";
        if self.seqtype in SeqFileTypes.list_reads():
            return "/uploads/samples/raw";
        raise Exception("Error generating path.");


    def get_file(self):
        return os.path.join(self.get_path(), self.get_filename());


    def check_if_exists(self):
        return os.path.isfile(self.get_file());


    def save_file(self) -> None:
        self.create_path(self.get_path());
        self.filedata.save(self.get_file());


    def get_sequence(self, header: str="") -> str:
        if self.file_type not in SeqFileTypes.list_assemblies():
            raise Exception("Trying to get sequence of reads file.");
        if self.get_file() is None:
            return f"Missing sequence.";
        seq = f"> {header}";
        seq+= SeqIO.read(self.get_file(), self.extension);
        return seq.seq;


    def get_display_details(self) -> dict:
        d = {};
        d["seqtype"] = self.seqtype.value;
        d["filename"] = self.get_filename();
        d["is_assembly"] = self.is_assembly;
        d["file_type"] = self.file_type;
        if self.is_assembly:
            d["assembly_method"] = self.assembly_method;
        else:
            d["is_forward_read"] = self.is_forward_read;
        return d;

