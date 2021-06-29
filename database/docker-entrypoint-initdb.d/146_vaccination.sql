SET @table_name := "has_received_vaccine";
CALL create_basic_table(@table_name);

CALL upsert_basic_table(@table_name, "no", 1);
CALL upsert_basic_table(@table_name, "yes - completed", 2);
CALL upsert_basic_table(@table_name, "yes - partially completed", 3);
