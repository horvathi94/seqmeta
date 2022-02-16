SET @table_name = "host_habitats";
CALL create_basic_table(@table_name);


CALL upsert_basic_table(@table_name, "domestic:free-range farm", 1);
CALL upsert_basic_table(@table_name, "domestic:indoor farm", 2);
CALL upsert_basic_table(@table_name, "domestic:live market", 3);
CALL upsert_basic_table(@table_name, "domestic:semi-enclosed housing", 4);
CALL upsert_basic_table(@table_name, "other", 5);
CALL upsert_basic_table(@table_name, "wild:migratory", 6);
CALL upsert_basic_table(@table_name, "wild:resident", 7);

