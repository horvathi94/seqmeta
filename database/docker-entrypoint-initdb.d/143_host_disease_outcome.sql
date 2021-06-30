SET @table_name = "host_disease_outcome";
CALL create_basic_table(@table_name);

CALL upsert_basic_table(@table_name, "dead", 1);
CALL upsert_basic_table(@table_name, "recovered", 2);
CALL upsert_basic_table(@table_name, "recovered with sequelae", 3);
