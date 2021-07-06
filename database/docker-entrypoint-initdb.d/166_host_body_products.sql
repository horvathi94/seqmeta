SET @table_name = "host_body_products";
CALL create_basic_table(@table_name);

CALL upsert_basic_table(@table_name, "stool", 1);
CALL upsert_basic_table(@table_name, "mucus", 2);
CALL upsert_basic_table(@table_name, "saliva", 3);
