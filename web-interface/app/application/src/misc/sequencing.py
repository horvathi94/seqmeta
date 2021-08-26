from application.src.db.interface import DBInterface
from application.src.fields.radio import RadioValue, RadioList


class PassageDetails(DBInterface):

    display_table_name = "view_passage_details";
    edit_table_name = "view_passage_details";
    submit_table_name = "passage_details";
    save_procedure = "upsert_basic_table";



class AssemblyMethods(DBInterface):

    display_table_name = "view_assembly_methods";
    edit_table_name = "view_assembly_methods";
    submit_table_name = "assembly_methods";
    save_procedure = "upsert_basic_table";




class SequencingInstruments(DBInterface):

    display_table_name = "sequencing_instruments";



class SarsCovGenes(DBInterface):
    display_table_name = "sars_cov_2_genes";
