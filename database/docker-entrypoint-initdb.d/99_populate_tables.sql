CALL upsert_hosts("Human", "Homo-sapiens", 1);

CALL upsert_basic_table("passage_details", "Original", 1);
CALL upsert_basic_table("passage_details", "Vero", 2);

CALL upsert_basic_table("sampling_strategies", "Sentinel surveillance (ILI)", 1);
CALL upsert_basic_table("sampling_strategies", "Sentinel surveillance (ARI)", 2);
CALL upsert_basic_table("sampling_strategies", "Sentinel surveillance (SARI)", 3);
CALL upsert_basic_table("sampling_strategies", "Non-sentinel-surveillance (hospital)", 3);
CALL upsert_basic_table("sampling_strategies", "Non-sentinel-surveillance (GP network)", 4);
CALL upsert_basic_table("sampling_strategies", "Longitudinal sampling on same patient(s)", 5);
CALL upsert_basic_table("sampling_strategies", "S gene dropout", 6);

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

CALL upsert_basic_table("assembly_methods", "CLC Genomics Workbench 12", 1);
CALL upsert_basic_table("assembly_methods", "Geneious 10.2.4", 2);
CALL upsert_basic_table("assembly_methods", "SPAdes/MEGAHIT v1.2.9", 3);
CALL upsert_basic_table("assembly_methods", "UGENE v. 33", 4);

CALL upsert_basic_table("sequencing_technologies", "Illumina Miseq", 1);
 
