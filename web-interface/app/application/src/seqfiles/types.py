from enum import Enum


class AssemblyLevels(Enum):

    CONTIGS = 1;
    SCAFFOLDS = 2;
    CONSENSUS = 3;




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

