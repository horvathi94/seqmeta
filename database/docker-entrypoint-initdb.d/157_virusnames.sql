SET @table_name = "virusnames";
CALL create_dict_table(@table_name);

CALL upsert_dict_table(@table_name, 0, "gisaid", 
	"hCoV-19{{continent}}/{{country}}_PV_{{sample_name}}/{{collection_year}}");
CALL upsert_dict_table(@table_name, 0, "ena-isolate",
	"Sars-CoV-2/{{host}}/{{continent}}/{{country}}-{{collection_month}}/{{collection_year}}");
