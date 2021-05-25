/* sample_capture_status */
SET @table_name = "sample_capture_status";
CALL create_basic_table(@table_name);

/* host_disease_outcome */
SET @table_name = "host_disease_outcome";
CALL create_basic_table(@table_name);

/* host_health_states */
SET @table_name = "host_health_states";
CALL create_basic_table(@table_name);
