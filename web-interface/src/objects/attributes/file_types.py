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
    extensions: List[str]
    valid_for: List[SeqFileType]
    ena_name: str = ""


    def is_valid_for(self, stype: SeqFileType) -> bool:
        for v in self.valid_for:
            if v == stype: return True
        return False



FILE_TYPES = [
    FileType("fasta", ["fasta", "fa", "fna"], ena_name="fasta",
             valid_for=[SeqFileType.ASSEMBLY,
                        SeqFileType.CONTIGS, SeqFileType.SCAFFOLDS]),
    FileType("fastq", ["fastq.gz"], ena_name="fastq",
             valid_for=[SeqFileType.READ]),
    FileType("bam", ["bam"], ena_name="bam",
             valid_for=[SeqFileType.READ]),
    FileType("cram", ["cram"], ena_name="cram",
             valid_for=[SeqFileType.READ]),
    FileType("nanopore", ["tar.gz"], ena_name="OxfordNanopore_native",
             valid_for=[SeqFileType.READ]),
]

