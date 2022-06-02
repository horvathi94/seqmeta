from dataclasses import dataclass
from typing import List
from enum import Enum


class SeqFileType(Enum):

    READ = "read"
    ASSEMBLY = "assembly"
    CONTIGS = "contigs"
    SCAFFOLDS = "scaffolds"



@dataclass
class FileType:

    name: str
    main_extension: str
    extensions: List[str]
    valid_for: List[SeqFileType]
    ena_name: str = ""
    seqio_type: str = ""


    def is_valid_for(self, stype: SeqFileType) -> bool:
        for v in self.valid_for:
            if v == stype: return True
        return False


    def is_valid_extension(self, ext: str) -> bool:
        if ext in self.extensions: return True
        return False



FILE_TYPES = [
    FileType("fasta", "fa", ["fasta", "fa", "fna"],
             ena_name="fasta", seqio_type="fasta",
             valid_for=[SeqFileType.ASSEMBLY,
                        SeqFileType.CONTIGS, SeqFileType.SCAFFOLDS]),
    FileType("fastq", "fastq.gz", ["fastq.gz"],
             ena_name="fastq", seqio_type="",
             valid_for=[SeqFileType.READ]),
    FileType("bam", "bam", ["bam"],
             ena_name="bam", seqio_type="",
             valid_for=[SeqFileType.READ]),
    FileType("cram", "cram", ["cram"],
             ena_name="cram", seqio_type="",
             valid_for=[SeqFileType.READ]),
    FileType("nanopore", "tar.gz", ["tar.gz"],ena_name="OxfordNanopore_native",
             valid_for=[SeqFileType.READ]),
]

