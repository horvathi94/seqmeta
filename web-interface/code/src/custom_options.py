from .base import Base
from .cursor import Cursor

class Hosts(Base):

    view_table_name = "view_hosts";
    submit_table_name = "hosts";
    save_procedure = "UpsertHosts";

    def save_by_procedure(self, items):

        cursor = Cursor();

        for item in items:
            args = (int(item["id"]), str(item["label"]), str(item["latin"]));
            cursor.call_procedure(self.save_procedure, args=args, commit=True);

        cursor.close();



class SamplingStrategies(Base):

    view_table_name = "sampling_strategies";
    submit_table_name = "smapling_strategies";
    save_procedure = "UpsertSamplingStrategies";



class PassageDetails(Base):

    view_table_name = "passage_details";
    submit_table_name = "passage_details";
    save_procedure = "UpsertPassageDetails";



class SequencingTechs(Base):

    view_table_name = "sequencing_technologies";
    submit_table_name = "sequencing_technologies";
    save_procedure = "UpsertSequencingTechnologies";



class AssemblyMethods(Base):

    view_table_name = "assembly_methods";
    submit_table_name = "assembly_methods";
    save_procedure = "UpsertAssemblyMethods";
