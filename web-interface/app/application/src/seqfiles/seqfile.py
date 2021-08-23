import os
from Bio import SeqIO
from dataclasses import dataclass
from application.src.seqfiles import db
from .types import AssemblyLevels, SeqFileTypes


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
    exists: bool = None;
    extension: str = "fasta";


    def __post_init__(self):
        if self.file_type is not None:
            self.is_assembly = self.get_is_assembly(self.file_type);
            self.assembly_level = self.get_assembly_level(self.file_type);
            self.is_forward_read = self.get_is_forward_read(self.file_type);


    def fetch_filename(self):
        return db.DBSeqFile.fetch_filename_new(self);


    def get_file(self):
        path = self.get_path();
        if path is None: return;
        if self.filename is None: return;
        return os.path.join(self.get_path(), self.filename);


    def check_if_exists(self):
        if self.filename == "": return False;
        if self.get_path() is None: return False;
        return os.path.isfile(self.get_file());


    @staticmethod
    def get_assembly_level(e: SeqFileTypes) -> str:
        if e not in SeqFileTypes.list_assemblies():
            return None;
        if e == SeqFileTypes.CONSENSUS_FILE:
            return AssemblyLevels.CONSENSUS;
        if e == SeqFileTypes.CONTIGS_FILE:
            return AssemblyLevels.CONTIGS;
        if e == SeqFileTypes.SCAFFOLDS_FILE:
            return AssemblyLevels.SCAFFOLDS;


    @staticmethod
    def get_is_assembly(e: SeqFileTypes) -> bool:
        if e in SeqFileTypes.list_assemblies():
            return True;
        return False;


    @staticmethod
    def get_is_forward_read(e: SeqFileTypes) -> bool:
        if e not in SeqFileTypes.list_reads():
            return None;
        if e == SeqFileTypes.FWREAD_FILE:
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
        self.filedata.save(self.get_file());


    def get_sequence(self, header: str="") -> str:
        if self.file_type not in SeqFileTypes.list_assemblies():
            raise Exception("Trying to get sequence of reads file.");
        if self.get_file() is None:
            return f"Missing sequence.";
        seq = f"> {header}";
        seq+= SeqIO.read(self.get_file(), self.extension);
        return seq.seq;

