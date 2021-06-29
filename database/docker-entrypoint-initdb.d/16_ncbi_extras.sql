SET @table_name := "collection_devices";
CALL create_basic_table(@table_name);
CALL create_basic_view("view_collection_devices", @table_name);
CALL upsert_basic_table(@table_name, "swab", 1);


