/* sample_capture_status */
SET @table_name = "sample_capture_status";
CALL create_basic_table(@table_name);

/* host_disease_outcome */
SET @table_name = "host_disease_outcome";
CALL create_basic_table(@table_name);

/* host_health_states */
SET @table_name = "host_health_states";
CALL create_basic_table(@table_name);

/* host_habitats */
SET @table_name = "host_habitats";
CALL create_basic_table(@table_name);

/* host_behaviours */
SET @table_name = "host_behaviours";
CALL create_basic_table(@table_name);


CREATE TABLE IF NOT EXISTS ena_studies (
	
	id										INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	project_name					VARCHAR(500) NOT NULL,
	project_title					VARCHAR(500) NOT NULL,
	project_alias					VARCHAR(500) NOT NULL UNIQUE,
	project_description		TEXT NOT NULL,

	project_link_db				CHAR(100),
	project_link_id				CHAR(200)

);
