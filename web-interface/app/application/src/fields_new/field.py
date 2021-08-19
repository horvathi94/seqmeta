from dataclasses import dataclass, field as dfield
from . import requirements as rqs
from .sample_fields import SampleFields
from application.src.db.cursor import Cursor



import sys



@dataclass
class Input:

    name_single: str = "";
    multi_all: str = "";
    multi_template: str = "";
    defaults: str = "";
    class_name: str = "";
    onchange: str = "";
    maxlength: int = 0;
    min_val: int = 0;
    max_val: int = 0;



@dataclass
class Field:

    db_key: str = "";
    handle:  SampleFields = SampleFields.NONE;
    field_name: str = "";
    field_type: str = "";
    requirement: list = dfield(default_factory=list);
    edit_all: bool = False;
    input_tag: Input = None;





class DBField:

    display_table = "fields";


    @classmethod
    def fetch(cls, handle: str) -> dict:
        """Fetch field data from the database."""
        where_clause = f"WHERE handle = '{handle}'";
        entry ,= Cursor.select(cls.display_table, clauses=where_clause);
        return entry;


    @classmethod
    def parse_requirements(cls, raw: dict) -> list:
        requirements = [];
        for repo in rqs.RequirementRepos:
            rlevel = raw[repo.value];
            if rlevel is None: continue;
            req = rqs.Requirement(repo.value,
                                  rqs.RequirementLevels(rlevel).value);
            requirements.append(req);
        return requirements;


    @classmethod
    def parse_field_info(cls, raw: dict) -> Field:
        """Parse main data related to the field."""
        field = Field();
        field.handle = SampleFields(raw["handle"]);
        field.requirements = cls.parse_requirements(raw);
        field.db_key = raw["db_key"];
        field.edit_all = bool(raw["edit_all"]);
        return field;


    @classmethod
    def get_field(cls, handle: SampleFields) -> Field:
        raw = cls.fetch(handle.value);
        field = cls.parse_field_info(raw);


        for fd in SampleFields:
            print(f"Field: {fd}", file=sys.stderr)
        return field;




