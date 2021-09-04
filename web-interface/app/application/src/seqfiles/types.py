import os
from enum import Enum


class AssemblyLevels(Enum):

    CONTIGS = 1;
    SCAFFOLDS = 2;
    CONSENSUS = 3;




class SeqFileTypes(Enum):

#    CONSENSUS_FILE = "assembly_file";
#    CONTIGS_FILE = "contigs_file";
#    SCAFFOLDS_FILE = "scaffolds_file";

    CONSENSUS = "assembly_file";
    CONTIGS = "contigs_file";
    SCAFFOLDS = "scaffolds_file";

#    FWREAD_FILE = "fwread_file";
#    RVREAD_FILE = "rvread_file";

    FWREAD = "fwread_file";
    RVREAD = "rvread_file";

    @classmethod
    def list_assemblies(cls) -> list:
        """Returns list of assembly file types."""
#        return [cls.CONSENSUS_FILE, cls.CONTIGS_FILE, cls.SCAFFOLDS_FILE];
        return [cls.CONSENSUS, cls.CONTIGS, cls.SCAFFOLDS];


    @classmethod
    def list_reads(cls) -> list:
        """Returns list of raw reads file types."""
        return [cls.FWREAD, cls.RVREAD];
#        return [cls.FWREAD_FILE, cls.RVREAD_FILE];


    @classmethod
    def list_values(cls) -> list:
        return [item.value for item in cls];


    @classmethod
    def is_assembly(cls, item: "SeqFileTypes") -> bool:
        """Returns the database entry for corresponding field"""
        if item in cls.list_assemblies(): return True;
        return False;


    @classmethod
    def is_forward_read(cls, item: "SeqFileTypes") -> bool:
        if item == cls.FWREAD: return True;
        if item == cls.RVREAD: return False;
        return None;


    @classmethod
    def get_assembly_level(cls, item: "SeqFileTypes") -> AssemblyLevels:
        if item not in cls.list_assemblies(): return None;
        return AssemblyLevels[item.name];


    @classmethod
    def get_filename_extension(cls, item: "SeqFileTypes") -> str:
        if item in cls.list_assemblies():
            return item.name.lower();

        if item == cls.FWREAD: return "fwread";
        if item == cls.RVREAD: return "rvread";
        return None;


    @classmethod
    def get_path(cls, item: "SeqFileTypes") -> "os.path":
        if item in cls.list_assemblies():
            return "/uploads/samples/assemblies";
        if item in cls.list_reads():
            return "/uploads/samples/reads";
        return None;
