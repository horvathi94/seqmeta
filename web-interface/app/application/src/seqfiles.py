import os.path
from .db.interface import DBInterface
from .db.cursor import Cursor

class SeqFileTypes(DBInterface):

    display_table_name = "seqfile_extensions";


class SeqFile(DBInterface):

    display_table_name = "view_seqfiles";

    @classmethod
    def save(cls, data):
        args = (data["sample_id"], int(data["file_type_id"]),
                data["is_assembly"], data["is_forward_read"]);
        Cursor.call_procedure("upsert_seqfiles", args=args, commit=True);


    @classmethod
    def fetch_entries_by_sample_id(cls, sample_id):
        seqfiles = Cursor.select(cls.display_table_name,
                      clauses="WHERE sample_id = {:d}".format(sample_id));
        return seqfiles;




class SeqFilesBunch:

    main_dir = "/uploads/samples";

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


    def todict(self):
        assembly = {};
        if self.assembly_file != None:
            assembly["filename"] = self.assembly_file["filename"];
            assembly["file_type"] = self.assembly_file["file_type"];
            assembly["exists"] = self.check_file(self.assembly_file);
        else:
            assembly["exists"] = False;
        return {
            "assembly_file": assembly,
            };
