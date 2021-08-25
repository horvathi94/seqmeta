import os
from Bio import SeqIO
from dataclasses import dataclass
from application.src.seqfiles import db
from application.src.samples.samples import Samples
from .types import AssemblyLevels, SeqFileTypes


@dataclass
class SeqFileNew:

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
    found_in_db: bool = None;
    to_save: bool = False;


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


    def get_path(self) -> "os.path":
        if self.file_type in SeqFileTypes.list_assemblies():
            return "/uploads/samples/assemblies/";
        if self.file_type in SeqFileTypes.list_reads():
            return "/uploads/samples/raw";
        raise Expcetion("Error generating path.");


    def get_file(self):
        return os.path.join(self.get_path(), self.get_filename());


    def check_if_exists(self):
        return os.path.isfile(self.get_file());


    def save_file(self) -> None:
        if not self.to_save: return;
        if self.get_filename() == "": return;
        self.filedata.save(self.get_file());


    def get_sequence(self, header: str="") -> str:
        if self.file_type not in SeqFileTypes.list_assemblies():
            raise Exception("Trying to get sequence of reads file.");
        if self.get_file() is None:
            return f"Missing sequence.";
        seq = f"> {header}";
        seq+= SeqIO.read(self.get_file(), self.extension);
        return seq.seq;


@dataclass
class SeqFile:

    sample_id: int = 0;
    sample_name: str = "";
    file_type: SeqFileTypes = None;
    file_type_id: int = 0;
    is_assembly: bool = True;
    assembly_level: str = None;
    is_forward_read: bool = None;
    filedata: "flask.fileStorage" = None;
    filename: str = "";
    exists: bool = None;
    extension_id: int = None;
    extension: str = None;
    assembly_method_id: int = None;
    assembly_method: str = None;


    def __post_init__(self):
        if self.file_type is not None:
            self.is_assembly = self.get_is_assembly(self.file_type);
            self.assembly_level = self.get_assembly_level(self.file_type);
            self.is_forward_read = self.get_is_forward_read(self.file_type);
            if self.sample_id != 0:
                self._fetch_extension();
                if self.file_type in SeqFileTypes.list_assemblies():
                    self._set_assembly_method();


    def _set_assembly_method(self):
        d = db.DBSeqFile.fetch_assembly_method(self);
        self.assembly_method_id = d["assembly_method_id"];
        self.assembly_method = d["assembly_method"];


    def _fetch_extension(self):
        d = db.DBSeqFile.fetch_extension(self);
        self.extension_id = d["file_extension_id"];
        self.extension = d["file_extension"];


    def _generate_filename(self):
        sample_name = Samples.fetch_name(self.sample_id);
        fname = sample_name;
        if self.is_assembly:
           pass;



    def fetch_filename(self):
        return db.DBSeqFile.fetch_filename(self);


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

