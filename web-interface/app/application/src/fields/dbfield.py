from application.src.db.cursor import Cursor
from .field import Field


class DBField:

    display_table = "fields";


    @classmethod
    def fetch(cls, handle: str) -> dict:
        """Fetch field data from the database."""
        where_clause = f"WHERE handle = '{handle}'";
        entry ,= Cursor.select(cls.display_table, clauses=where_clause);
        entry["classes"] = entry["class"].split();
        del entry["class"];
        return entry;


    @classmethod
    def get_field(cls, handle: "SampleFields") -> Field:
        raw = cls.fetch(handle.value);
        field = Field(**raw);
        return field;
