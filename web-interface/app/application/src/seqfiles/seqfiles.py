import os.path
from .db import SeqFile
from Bio import SeqIO
from application.src.samples.nametemplates.virusname_gisaid import \
    VirusnameGisaid
from application.src.samples.samples import Samples
from application.src.metatemplates.base.tempfile import TempFile

class SeqFilesBunch(TempFile):

    main_dir = "/uploads/samples";
    tempfilename = "last_generated_assembly_file.fasta";
    attachement_prefix = "fasta_";
    extension = "fasta";

    def __init__(self, sample_id):
        self.sample_id = sample_id;
        self.assembly_file = None;
        self.forward_reads = [];
        self.reverse_reads = [];
        self.sort_files();

    def sort_files(self):
        files = SeqFile.fetch_entries_by_sample_id(self.sample_id);
        self.assembly_file = SeqFilesBunch.fetch_assembly_file(files);
        self.forward_reads = SeqFilesBunch.fetch_reads_files(files);
        self.reverse_reads = SeqFilesBunch.fetch_reads_files(files,
                                                        forward_read=False);

    @staticmethod
    def fetch_assembly_file(files):
        for f in files:
            if f["is_assembly"]:
                return f;
        return None;


    @staticmethod
    def fetch_reads_files(files, forward_read=True):
        reads = [];
        for f in files:
            if not f["is_assembly"]:
                if f["is_forward_read"] == forward_read:
                    reads.append(f);
        return reads;


    @classmethod
    def check_file(cls, fdata):
        if fdata["is_assembly"] == None:
            return False;
        path = "assemblies" if fdata["is_assembly"] else "reads";
        seqfile = os.path.join(cls.main_dir, path, fdata["filename"]);
        return os.path.isfile(seqfile);


    def has_assembly_file(self):
        if self.assembly_file == None:
            return False;
        if not self.check_file(self.assembly_file):
            return False;
        return True;

    def get_assembly_file(self):
        return os.path.join(self.main_dir, "assemblies",
                               self.assembly_file["filename"]);


    def todict(self):
        assembly = { "exists": self.has_assembly_file() };
        if assembly["exists"]:
            assembly["filename"] = self.assembly_file["filename"];
            assembly["file_type"] = self.assembly_file["file_type"];
        return {
            "assembly_file": assembly,
            };


    def get_assembly_sequence(self):
        if not self.has_assembly_file():
            return "";
        seqfile = self.get_assembly_file();
        seq = SeqIO.read(seqfile, self.assembly_file["file_type"]);
        return seq.seq;


    def get_assembly(self):
        if not self.has_assembly_file():
            return "";
        virusname = VirusnameGisaid.format_name(self.sample_id);
        seq = "> {:s}".format(virusname) + "\n";
        seq+= self.get_assembly_sequence() + "\n";
        return seq;


    def write_gisiad_tempfile(self):
        if not self.has_assembly_file():
            return;
        virusname = VirusnameGisaid.format_name(self.sample_id);
        seqfile = self.get_assembly_file();
        seqdata = SeqIO.read(seqfile, self.assembly_file["file_type"]);
        seqdata.id = virusname;
        seqdata.name = "";
        seqdata.description = "";

        with open(self.get_tempfile(), "w") as outf:
            SeqIO.write(seqdata, outf, "fasta");
