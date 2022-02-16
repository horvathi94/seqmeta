SET @table_name = "reference_genomes";
SET @view_name = "view_reference_genomes";

CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);
