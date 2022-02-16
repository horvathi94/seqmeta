SET @table_name = "sampling_strategies";
SET @view_name = "view_sampling_strategies";


CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);


CALL upsert_basic_table(@table_name, "Sentinel surveillance (ILI)", 1);
CALL upsert_basic_table(@table_name, "Sentinel surveillance (ARI)", 2);
CALL upsert_basic_table(@table_name, "Sentinel surveillance (SARI)", 3);
CALL upsert_basic_table(@table_name, "Non-sentinel-surveillance (hospital)", 3);
CALL upsert_basic_table(@table_name, "Non-sentinel-surveillance (GP network)", 4);
CALL upsert_basic_table(@table_name, "Longitudinal sampling on same patient(s)", 5);
CALL upsert_basic_table(@table_name, "S gene dropout", 6);

