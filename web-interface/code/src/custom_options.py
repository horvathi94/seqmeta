from .base import Base
from .cursor import Cursor

class Hosts(Base):

    view_table_name = "view_hosts";
    submit_table_name = "hosts";

    def save_entries(self, hosts_list):

        cursor = Cursor();

        for host in hosts_list:
            args = (int(host["id"]), str(host["label"]), str(host["latin"]));
            cursor.call_procedure("UpsertHosts", args=args, commit=True);

        cursor.close();



class SamplingStrategies(Base):

    view_table_name = "sampling_strategies";
    submit_table_name = "smapling_strategies";

    def save_entries(self, samp_strats_list):

        cursor = Cursor();

        for ss in samp_strats_list:
            args = (int(ss["id"]), str(ss["label"]));
            cursor.call_procedure("UpsertSamplingStrategies",
                                  args=args, commit=True);

        cursor.close();


class PassageDetails(Base):

    view_table_name = "passage_details";
    submit_table_name = "passage_details";


    def save_entries(self, pass_dets_list):

        cursor = Cursor();

        for pd in pass_dets_list:
            args = (int(pd["id"]), str(pd["label"]));
            cursor.call_procedure("UpsertPassageDetails",
                                  args=args, commit=True);

        cursor.close();
