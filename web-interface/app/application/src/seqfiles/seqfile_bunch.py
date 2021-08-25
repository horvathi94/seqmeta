import os.path
import gzip
from Bio import SeqIO
from application.src.samples.samples import Samples
from application.src.metatemplates.base.tempfile import TempFile
from .db import DBSeqFile
from .types import SeqFileTypes
from .seqfile import SeqFile


import sys

class SeqFilesBunch(TempFile):

    main_dir = "/uploads/samples";
    tempfilename = "last_generated_assembly_file.fasta";
    attachement_prefix = "fasta_";
    extension = "fasta";


    def __init__(self, sample_id: int):
        self.sample_id = sample_id;
        self.sample = Samples.fetch("view_samples_base", self.sample_id);
        self.consensus_file = self._fetch_file(self.sample_id,
                                               SeqFileTypes.CONSENSUS_FILE);
        self.contigs_file = self._fetch_file(self.sample_id,
                                               SeqFileTypes.CONTIGS_FILE);
        self.scaffolds_file = self._fetch_file(self.sample_id,
                                               SeqFileTypes.SCAFFOLDS_FILE);
        self.read_files = self._get_reads();


    @classmethod
    def _fetch_file(cls, sample_id: int, sftype: SeqFileTypes) -> SeqFile:
        seqfile = DBSeqFile.get_seqfile(sample_id, sftype);
        seqfile.exists = seqfile.check_if_exists();
        return seqfile;


    def _get_reads(self) -> list:
        reads = [];
        if self.sample["library_layout_paired"]:
            sf = self._fetch_file(self.sample_id, SeqFileTypes.FWREAD_FILE);
            reads.append(sf);
            sf = self._fetch_file(self.sample_id, SeqFileTypes.RVREAD_FILE);
            reads.append(sf);
        return reads;


    def get_consensus_sequence(self):
        virusname = self.sample["gisaid_virusname"];
        return self.consensus_file.get_sequence(header=virusname);


    def write_gisiad_tempfile(self, file: str) -> None:
        if not self.consensus_file.exists:
            raise Exception("No consensus file found.");
        seqfile = self.consensus_file.get_file();
        seqdata = SeqIO.read(seqfile, self.consensus_file.extension);
        seqdata.id = self.sample["gisaid_virusname"];
        seqdata.name = "";
        seqdata.description = "";

        with open(file, "w") as outf:
            SeqIO.write(seqdata, outf, "fasta");


    def zip_file_data(self, in_file: "file", out_file: str) -> None:
        with open(in_file, 'rb') as f_in, gzip.open(out_file, 'wb') as f_out:
            f_out.writelines(f_in);


    def write_ena_contigs_tempfile(self, file: str) -> None:
        self.zip_file_data(self.contigs_file.get_file(), file);


    def write_ena_scaffolds_tempfile(self, file: str) -> None:
        self.zip_file_data(self.scaffolds_file.get_file(), file);


    def has_reads(self) -> bool:
        for read in self.read_files:
            if not read.exists: return False;
        return True;


    def get_display_details(self) -> dict:
        d = {};
        d["consensus"] = self.consensus_file.get_display_details();
        d["contigs"] = self.contigs_file.get_display_details();
        d["scaffolds"] = self.scaffolds_file.get_display_details();
        d["reads"] = [];
        for r in self.read_files:
            d["reads"].append(r.get_display_details());
        return d;
