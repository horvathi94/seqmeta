SET @table_name := "collection_devices";
SET @view_name := "view_collection_devices";
CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);

CALL upsert_basic_table(@table_name, "swab", 1);


