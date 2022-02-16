SET @table_name = "purposes_of_sampling";
CALL create_basic_table(@table_name);

CALL upsert_basic_table(@table_name, "diagnostic testing", 1);
