from application.src.db.interface import DBInterface
from application.src.db.cursor import Cursor

class SeqFileTypes(DBInterface):

    display_table_name = "seqfile_extensions";


class AssemblyFileTypes(DBInterface):

    display_table_name = "assembly_files";


class ReadFileTypes(DBInterface):

    display_table_name = "reads_files";



class SeqFile(DBInterface):

    display_table_name = "view_seqfiles";

    @classmethod
    def save(cls, data):
        args = (data["sample_id"], int(data["file_type_id"]),
                data["is_assembly"], data["is_forward_read"],
                data["assembly_level"]);
        Cursor.call_procedure("upsert_seqfiles", args=args, commit=True);


    @classmethod
    def fetch_entries_by_sample_id(cls, sample_id):
        seqfiles = Cursor.select(cls.display_table_name,
                      clauses="WHERE sample_id = {:d}".format(sample_id));
        return seqfiles;


    @classmethod
    def fetch_filename(cls, sample_id, ftype="assembly"):
        where_clause = "WHERE sample_id = {:d}".format(sample_id);
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

