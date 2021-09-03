from application.src.db.interface import DBInterface
from application.src.db.cursor import Cursor
from .seqfile import SeqFile
from .types import SeqFileTypes



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
        if seqfile.assembly_method_id == "":
            seqfile.assembly_method_id = None;
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
    def fetch_extension(cls, seqfile: "SeqFiles") -> dict:
        fields = ["file_extension_id", "file_extension"];
        raw ,= Cursor.select(cls.display_table_name, fields=fields,
                            clauses=seqfile.get_where_clause());
        return {fd: raw[fd] for fd in fields};


    @classmethod
    def fetch_filename(cls, seqfile: "SeqFile") -> str:
        raw = Cursor.select(cls.display_table_name, fields=["filename"],
                            clauses=seqfile.get_where_clause());
        return str(raw[0]["filename"]);


    @classmethod
    def get_seqfile(cls, sample_id: int, seqtype: SeqFileTypes) -> SeqFile:
        seqfile = SeqFile(seqtype, sample_id=sample_id);
        fields = ["sample_name",
                  "file_type", "file_extension_id", "file_extension",
                  "assembly_method_id", "assembly_method"];

        where = f"WHERE `sample_id` = {seqfile.sample_id}";
        where+= f" AND is_assembly IS {seqfile.is_assembly}";
        if seqfile.seqtype in SeqFileTypes.list_assemblies():
            where+= f" AND assembly_level = {seqfile.assembly_level.value}"
        if seqfile.seqtype in SeqFileTypes.list_reads():
            where+= f" AND is_forward_read IS {seqfile.is_forward_read}";

        raw ,= Cursor.select(cls.display_table_name,
                            fields=fields, clauses=where);

        seqfile.sample_name = raw["sample_name"];
        seqfile.file_type = raw["file_type"];
        seqfile.extension_id = raw["file_extension_id"];
        seqfile.extension = raw["file_extension"];
        seqfile.assembly_method_id = raw["assembly_method_id"];
        seqfile.assembly_method = raw["assembly_method"];
        return seqfile;
