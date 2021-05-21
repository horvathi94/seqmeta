from .db_interface import DBInterface

class VirusnameGisaid(DBInterface):

    display_table_name = "view_virusname_gisaid";


    @classmethod
    def create_name(cls, sample):
        order = cls.fetch_list();
        virusname = "";
        for item in order:
            if item["item_key"] == "key":
                if item["item_value"] in sample:
                    virusname += str(sample[item["item_value"]]);
            elif item["item_key"] == "string":
                virusname += str(item["item_value"]);
        return virusname;

