SET @table_name = "virusnames";
CALL create_dict_table(@table_name);

CALL upsert_dict_table(@table_name, 0, "gisaid", 
	"hCoV-19{{location}}_PV_{{sample_name}}{{collection_year}}");

CALL create_dict_table("library_strategies");
CALL create_dict_table("library_sources");
CALL create_dict_table("library_selections");


/*SET @table_name = "virusname_gisaid";
SET @view_name = "view_virusname_gisaid";
CALL create_ordereddict_table(@table_name);
CALL create_ordereddict_view(@view_name, @table_name);*/
