SET @table_name = "sample_capture_status";
CALL create_basic_table(@table_name);

CALL upsert_basic_table(@table_name, "active surveillance in response to outbreak", 1);
CALL upsert_basic_table(@table_name, "active surveillance not initiated by an outbreak", 2);
CALL upsert_basic_table(@table_name, "farm sample", 3);
CALL upsert_basic_table(@table_name, "market sample", 4);
CALL upsert_basic_table(@table_name, "other", 5);
CALL upsert_basic_table(@table_name, "pet sample", 6);
CALL upsert_basic_table(@table_name, "zoo sample", 7);
