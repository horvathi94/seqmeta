SET @table_name = "purposes_of_sequencing";
CALL create_basic_table(@table_name);

CALL upsert_basic_table(@table_name, "baseline surveillance (random sampling)", 1);
