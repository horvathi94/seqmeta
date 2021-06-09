from .db.interface import DBInterface
from .db.cursor import Cursor

class SeqFileTypes(DBInterface):

    display_table_name = "seqfile_extensions";


class SeqFile(DBInterface):

    display_table_name = "view_samples_seqfiles";

    @classmethod
    def save(cls, data):
        args = (data["sample_id"], int(data["file_type_id"]),
                data["is_assembly"], data["is_forward_read"]);
        Cursor.call_procedure("upsert_seqfiles", args=args, commit=True);




