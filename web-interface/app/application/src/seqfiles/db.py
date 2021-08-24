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



class DBSeqFile(DBInterface):

    display_table_name = "view_seqfiles";

    @classmethod
    def save(cls, seqfile: "SeqFile") -> None:
        alevel = None;
        if not seqfile.assembly_level is None:
            alevel = int(seqfile.assembly_level.value);
        args = (seqfile.sample_id, seqfile.file_type_id,
                seqfile.is_assembly, seqfile.is_forward_read,
                alevel, seqfile.assembly_method_id);
        Cursor.call_procedure("upsert_seqfiles", args=args, commit=True);


    @classmethod
    def fetch_entries_by_sample_id(cls, sample_id):
        seqfiles = Cursor.select(cls.display_table_name,
                      clauses=f"WHERE sample_id = {sample_id}");
        return seqfiles;


    @classmethod
    def fetch_assembly_method(cls, seqfile: "SeqFiles") -> dict:
        fields = ["assembly_method_id", "assembly_method"];
        raw ,= Cursor.select(cls.display_table_name, fields=fields,
                            clauses=seqfile.get_where_clause());
        return {fd: raw[fd] for fd in fields};


    @classmethod
    def fetch_filename(cls, seqfile: "SeqFile") -> str:
        raw = Cursor.select(cls.display_table_name, fields=["filename"],
                            clauses=seqfile.get_where_clause());
        return str(raw[0]["filename"]);
