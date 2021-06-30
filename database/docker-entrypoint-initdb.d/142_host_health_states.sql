SET @table_name = "host_health_states";
CALL create_basic_table(@table_name);


CALL upsert_basic_table(@table_name, "diseased", 1);
CALL upsert_basic_table(@table_name, "healthy", 2);
CALL upsert_basic_table(@table_name, "not applicable", 3);
CALL upsert_basic_table(@table_name, "not collected", 4);
CALL upsert_basic_table(@table_name, "not provided", 5);
CALL upsert_basic_table(@table_name, "restricted access", 6);

