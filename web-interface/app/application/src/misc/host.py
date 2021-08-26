from application.src.db.cursor import Cursor
from application.src.db.interface import DBInterface
from application.src.fields.radio import RadioValue, RadioList


class Hosts(DBInterface):

    display_table_name = "view_hosts";
    edit_table_name = "view_hosts";
    submit_table_name = "hosts";
    save_procedure = "upsert_hosts";

    @classmethod
    def save_by_procedure(cls, items):
        for item in items:
            args = (str(item["label"]),
                    str(item["latin"]),
                    int(item["indx"]));
            Cursor.call_procedure(cls.save_procedure, args=args, commit=True);


class Genders(RadioList):

    items = [
        RadioValue(),
        RadioValue("Male", 1, 1, True),
        RadioValue("Female", 2, 0, False),
    ];



class HostHabitats(DBInterface):

    display_table_name = "host_habitats";



class HostBehaviours(DBInterface):

    display_table_name = "host_behaviours";
