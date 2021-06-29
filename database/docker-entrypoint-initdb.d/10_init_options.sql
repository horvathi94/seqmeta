/* patient_statuses */
SET @table_name = "patient_statuses";
SET @view_name = "view_patient_statuses";
CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);

/* specimen_sources */
SET @table_name = "specimen_sources";
SET @view_name = "view_specimen_sources";
CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);



/* reference_genomes */
SET @table_name = "reference_genomes";
SET @view_name = "view_reference_genomes";
CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);


