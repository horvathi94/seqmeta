SET @table_name = "specimen_sources";
SET @view_name = "view_specimen_sources";

CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);

CALL upsert_basic_table(@table_name, "Sputum", 1);
CALL upsert_basic_table(@table_name, "Alveolar lavage fluid", 2);
CALL upsert_basic_table(@table_name, "Oro-pharyngeal swab", 3);
CALL upsert_basic_table(@table_name, "Blood", 4);
CALL upsert_basic_table(@table_name, "Tracheal swab", 5);
CALL upsert_basic_table(@table_name, "Urine", 6);
CALL upsert_basic_table(@table_name, "Stool", 7);
CALL upsert_basic_table(@table_name, "Cloakal swab", 8);
CALL upsert_basic_table(@table_name, "Organ", 9);
CALL upsert_basic_table(@table_name, "Feces", 10);
CALL upsert_basic_table(@table_name, "Other ", 11);


