import os.path
from Bio import SeqIO
from application.src.samples.samples import Samples
from application.src.metatemplates.base.tempfile import TempFile


from .db import DBSeqFile
from .types import SeqFileTypes
from .seqfile import SeqFile


class SeqFilesBunchNew(TempFile):

    main_dir = "/uploads/samples";
    tempfilename = "last_generated_assembly_file.fasta";
    attachement_prefix = "fasta_";
    extension = "fasta";


    def __init__(self, sample_id: int):
        self.sample_id = sample_id;
        self.sample = Samples.fetch("view_samples_base", self.sample_id);
        self.consensus_file = self._fetch_file(self.sample_id,
                                               SeqFileTypes.CONSENSUS_FILE);
        self.read_files = self._get_reads();


    @classmethod
    def _fetch_file(cls, sample_id: int, sftype: SeqFileTypes) -> SeqFile:
        seqfile = SeqFile(sample_id, sftype);
        seqfile.filename = DBSeqFile.fetch_filename_new(seqfile);
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


    def write_ena_contigs(self, file: str) -> None:
        pass;


    def write_ena_scaffolds(self, file: str) -> None:
        pass;


    def write_ena_reads(self, file: str) -> None:

        pass;




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
        files = DBSeqFile.fetch_entries_by_sample_id(self.sample_id);
        self.assembly_file = SeqFilesBunch.fetch_assembly_file(files);
        self.forward_reads = SeqFilesBunch.fetch_reads_files(files);
        self.reverse_reads = SeqFilesBunch.fetch_reads_files(files,
                                                        forward_read=False);

    @staticmethod
    def fetch_assembly_file(files):
        for f in files:
            if f["is_assembly"]: return f;
        return None;


    @staticmethod
    def fetch_reads_files(files, forward_read=True):
        reads = [];
        for f in files:
            if not f["is_assembly"]:
                if f["is_forward_read"] == forward_read: reads.append(f);
        return reads;


    @classmethod
    def check_file(cls, fdata):
        if fdata["is_assembly"] == None: return False;
        path = "assemblies" if fdata["is_assembly"] else "raw";
        seqfile = os.path.join(cls.main_dir, path, fdata["filename"]);
        return os.path.isfile(seqfile);


    def has_assembly_file(self):
        if self.assembly_file == None: return False;
        if not self.check_file(self.assembly_file): return False;
        return True;


    def has_fwreads_file(self):
        if len(self.forward_reads) == 0: return False;
        fwread = self.forward_reads[0];
        if fwread == None: return False;
        if not self.check_file(fwread): return False;
        return True;


    def has_rvreads_file(self):
        if len(self.reverse_reads) == 0: return False;
        rvread = self.reverse_reads[0];
        if rvread == None: return False;
        if not self.check_file(rvread): return False;
        return True;


    def get_assembly_file(self):
        return os.path.join(self.main_dir, "assemblies",
                               self.assembly_file["filename"]);


    def get_reads_file(self, tp="fwread"):
        if tp == "fwread": f = self.forward_reads[0];
        if tp == "rvread": f = self.reverse_reads[0];
        return os.path.join(self.main_dir, "raw", f["filename"]);


    def todict(self):
        assembly = { "exists": self.has_assembly_file() };
        if assembly["exists"]:
            assembly["filename"] = self.assembly_file["filename"];
            assembly["file_type"] = self.assembly_file["file_type"];
        return {"assembly_file": assembly,};


    def get_assembly_sequence(self):
        if not self.has_assembly_file():
            return "";
        seqfile = self.get_assembly_file();
        seq = SeqIO.read(seqfile, self.assembly_file["file_type"]);
        return seq.seq;


    def get_assembly(self):
        if not self.has_assembly_file():
            return "";
        sample ,= Samples.fetch_entries("view_samples_base",
                                       sample_ids=[self.sample_id]);
        virusname = sample["gisaid_virusname"];
        seq = "> {:s}".format(virusname) + "\n";
        seq+= self.get_assembly_sequence() + "\n";
        return seq;


    def write_gisiad_tempfile(self):
        if not self.has_assembly_file(): return;
        sample ,= Samples.fetch_entries("view_samples_base",
                                       sample_ids=[self.sample_id]);
        virusname = sample["gisaid_virusname"];
        seqfile = self.get_assembly_file();
        seqdata = SeqIO.read(seqfile, self.assembly_file["file_type"]);
        seqdata.id = virusname;
        seqdata.name = "";
        seqdata.description = "";

        with open(self.get_tempfile(), "w") as outf:
            SeqIO.write(seqdata, outf, "fasta");


    def get_reads(self, tp="fwread"):
        if tp == "fwread":
            reads = self.forward_reads;
        elif tp == "rvread":
            reads = self.reverse_reads;
        else:
            return None;

        if len(reads) == 0: return None;
        read = reads[0];

        if self.check_file(read):
            return self.get_reads_file(tp=tp);

        return None;
