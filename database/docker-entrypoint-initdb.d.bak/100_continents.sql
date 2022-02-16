SET @table_name = "continents";
SET @view_name = "view_continents";

CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);

CALL upsert_basic_table(@table_name, "Asia", 1);
CALL upsert_basic_table(@table_name, "Africa", 2);
CALL upsert_basic_table(@table_name, "Europe", 3);
CALL upsert_basic_table(@table_name, "North America", 4);
CALL upsert_basic_table(@table_name, "South America", 5);
CALL upsert_basic_table(@table_name, "Australia/Oceania", 6);
CALL upsert_basic_table(@table_name, "Antartica", 7);
