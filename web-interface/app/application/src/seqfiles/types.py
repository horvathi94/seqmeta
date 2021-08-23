import os
from enum import Enum
from dataclasses import dataclass


class AssemblyLevels(Enum):

    CONSENSUS = 1;
    CONTIGS = 2;
    SCAFFOLDS = 3;



class SeqFileTypes(Enum):

    CONSENSUS_FILE = "assembly_file";
    CONTIGS_FILE = "contigs_file";
    SCAFFOLDS_FILE = "scaffolds_file";

    FWREAD_FILE = "fwread_file";
    RVREAD_FILE = "rvread_file";

    @classmethod
    def list_assemblies(cls) -> list:
        """Returns list of assembly file types."""
        return [cls.CONSENSUS_FILE, cls.CONTIGS_FILE, cls.SCAFFOLDS_FILE];


    @classmethod
    def list_reads(cls) -> list:
        """Returns list of raw reads file types."""
        return [cls.FWREAD_FILE, cls.RVREAD_FILE];


    @classmethod
    def list_values(cls) -> list:
        return [item.value for item in cls];




@dataclass
class SeqFile:

    sample_id: int = 0;
    file_type: SeqFileTypes = None;
    file_type_id: int = 0;
    is_assembly: bool = True;
    assembly_level: str = None;
    is_forward_read: bool = None;
    filedata: "flask.fileStorage" = None;
    filename: str = "";


    def __post_init__(self):
        if self.file_type is not None:
            self.is_assembly = self.get_is_assembly(self.file_type);
            self.assembly_level = self.get_assembly_level(self.file_type);
            self.is_forward_read = self.get_is_forward_read(self.file_type);


    @staticmethod
    def get_assembly_level(e: SeqFileTypes) -> str:
        if e not in SeqFileTypes.list_assemblies():
            return None;
        if e == SeqFileTypes.CONSENSUS_FILE:
            return AssemblyLevels.CONSENSUS;
        if e == SeqFileTypes.CONTIGS_FILE:
            return AssemblyLevels.CONTIGS;
        if e == SeqFileTypes.SCAFFOLDS_FILE:
            return AssemblyLevesl.SCAFFOLDS;


    @staticmethod
    def get_is_assembly(e: SeqFileTypes) -> bool:
        if e in SeqFileTypes.list_assemblies():
            return True;
        return False;


    @staticmethod
    def get_is_forward_read(e: SeqFileTypes) -> bool:
        if e not in SeqFileTypes.list_reads():
            return None;
        if e == SeqFileTypes.FW_READ_FILE:
            return True;
        return False;


    def get_where_clause(self) -> str:
        if self.sample_id == 0: return "";
        where_clause = f"WHERE sample_id = {self.sample_id}";
        where_clause+= f" AND is_assembly IS {str(self.is_assembly)}";
        if self.file_type in SeqFileTypes.list_assemblies():
            where_clause+= \
                f" AND assembly_level = {self.assembly_level.value}";
        if self.file_type in SeqFileTypes.list_reads():
            where_clause+= f" AND is_forward_read IS {self.is_forward_read}";
        return where_clause;


    def get_path(self) -> "os.path":
        if self.file_type in SeqFileTypes.list_assemblies():
            return "/uploads/samples/assemblies/";
        if self.file_type in SeqFileTypes.list_reads():
            return "/uploads/samples/raw";
        return None;


    def save_file(self) -> None:
        path = self.get_path();
        if path is None: return;
        if self.filename is None: return;
        self.filedata.save(os.path.join(path, self.filename));
