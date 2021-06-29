SET @table_name = "assembly_methods";
SET @view_name = "view_assembly_methods";


CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);


CALL upsert_basic_table(@table_name, "CLC Genomics Workbench 12", 1);
CALL upsert_basic_table(@table_name, "Geneious 10.2.4", 2);
CALL upsert_basic_table(@table_name, "SPAdes/MEGAHIT v1.2.9", 3);
CALL upsert_basic_table(@table_name, "UGENE v. 33", 4);
