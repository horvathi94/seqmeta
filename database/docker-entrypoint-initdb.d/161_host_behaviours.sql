SET @table_name = "host_behaviours";
CALL create_basic_table(@table_name);


CALL upsert_basic_table(@table_name, "captive-wild (e.g. at zoo)", 1);
CALL upsert_basic_table(@table_name, "domestic", 2);
CALL upsert_basic_table(@table_name, "other", 3);
CALL upsert_basic_table(@table_name, "wild", 4);
