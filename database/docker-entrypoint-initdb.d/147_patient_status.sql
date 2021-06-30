SET @table_name = "patient_statuses";
SET @view_name = "view_patient_statuses";

CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);

CALL upsert_basic_table(@table_name, "Live", 1);
CALL upsert_basic_table(@table_name, "Hospitalized", 2);
CALL upsert_basic_table(@table_name, "Released", 3);
CALL upsert_basic_table(@table_name, "Deceased", 4);
CALL upsert_basic_table(@table_name, "unknown ", 5);
