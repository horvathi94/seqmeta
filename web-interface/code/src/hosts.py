from .base import Base
from .cursor import Cursor

class Hosts(Base):

    view_table_name = "hosts";
    submit_table_name = "hosts";

    def save_entries(self, hosts_list):

        cursor = Cursor();

        for host in hosts_list:
            args = (int(host["id"]), str(host["label"]), str(host["latin"]));
            cursor.call_procedure("UpsertHosts", args=args, commit=True);

        cursor.close();
