from application.src.db.interface import DBInterface
from application.src.db.cursor import Cursor
from .types import SeqFileTypes

class SeqFileTypes(DBInterface):

    display_table_name = "seqfile_extensions";


class AssemblyFileTypes(DBInterface):

    display_table_name = "assembly_files";

    @classmethod
    def fetch_select_list(cls) -> list:
        return cls.fetch_list_labeled(replace_key="item_key");


class ReadFileTypes(DBInterface):

    display_table_name = "reads_files";

    @classmethod
    def fetch_select_list(cls) -> list:
        return cls.fetch_list_labeled(replace_key="item_key");


import sys


class DBSeqFile(DBInterface):

    display_table_name = "view_seqfiles";

    @classmethod
    def save(cls, seqfile: "SeqFile") -> None:
        args = (seqfile.sample_id, seqfile.file_type_id,
                seqfile.is_assembly, seqfile.is_forward_read,
                int(seqfile.assembly_level.value));
        Cursor.call_procedure("upsert_seqfiles", args=args, commit=True);


    @classmethod
    def fetch_entries_by_sample_id(cls, sample_id):
        seqfiles = Cursor.select(cls.display_table_name,
                      clauses="WHERE sample_id = {:d}".format(sample_id));
        return seqfiles;


    @classmethod
    def fetch_filename_new(cls, seqfile: "SeqFile") -> str:
        print(f"WHERE: {seqfile.get_where_clause()}", file=sys.stderr);
        raw = Cursor.select(cls.display_table_name, fields=["filename"],
                            clauses=seqfile.get_where_clause());
        return str(raw[0]["filename"]);


    @classmethod
    def fetch_filename(cls, sample_id, ftype="assembly"):
        where_clause = f"WHERE sample_id = {sample_id}";
        if ftype == "assembly":
            where_clause+= " AND is_assembly IS TRUE";
            where_clause+= " AND assembly_level_string = 'consensus'";
        elif ftype == "fwread":
            where_clause+= " AND is_assembly IS FALSE";
            where_clause+= " AND is_forward_read IS TRUE";
        elif ftype == "rvread":
            where_clause+= " AND is_assembly IS FALSE";
            where_clause+= " AND is_forward_read IS FALSE";
        elif ftype == "contigs":
            where_clause+= " AND is_assembly IS TRUE";
            where_clause+= " AND assembly_level_string = 'contigs'";
        elif ftype == "scaffolds":
            where_clause+= " AND is_assembly IS TRUE";
            where_clause+= " AND assembly_level_string = 'scaffolds'";
        else:
            return "";
        raw = Cursor.select(cls.display_table_name,
                            fields=["filename"], clauses=where_clause);
        return str(raw[0]["filename"]);

