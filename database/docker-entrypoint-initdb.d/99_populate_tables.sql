
CALL upsert_basic_table("patient_statuses", "Live", 1);
CALL upsert_basic_table("patient_statuses", "Hospitalized", 2);
CALL upsert_basic_table("patient_statuses", "Released", 3);
CALL upsert_basic_table("patient_statuses", "Deceased", 4);
CALL upsert_basic_table("patient_statuses", "unknown ", 5);
 
CALL upsert_basic_table("specimen_sources", "Sputum", 1);
CALL upsert_basic_table("specimen_sources", "Alveolar lavage fluid", 2);
CALL upsert_basic_table("specimen_sources", "Oro-pharyngeal swab", 3);
CALL upsert_basic_table("specimen_sources", "Blood", 4);
CALL upsert_basic_table("specimen_sources", "Tracheal swab", 5);
CALL upsert_basic_table("specimen_sources", "Urine", 6);
CALL upsert_basic_table("specimen_sources", "Stool", 7);
CALL upsert_basic_table("specimen_sources", "Cloakal swab", 8);
CALL upsert_basic_table("specimen_sources", "Organ", 9);
CALL upsert_basic_table("specimen_sources", "Feces", 10);
CALL upsert_basic_table("specimen_sources", "Other ", 11);


