CALL upsert_basic_table("sample_capture_status", "active surveillance in response to outbreak", 1);
CALL upsert_basic_table("sample_capture_status", "active surveillance not initiated by an outbreak", 2);
CALL upsert_basic_table("sample_capture_status", "farm sample", 3);
CALL upsert_basic_table("sample_capture_status", "market sample", 4);
CALL upsert_basic_table("sample_capture_status", "other", 5);
CALL upsert_basic_table("sample_capture_status", "pet sample", 6);
CALL upsert_basic_table("sample_capture_status", "zoo sample", 7);

CALL upsert_basic_table("host_disease_outcome", "dead", 1);
CALL upsert_basic_table("host_disease_outcome", "recovered", 2);
CALL upsert_basic_table("host_disease_outcome", "recovered with sequelae", 3);

CALL upsert_basic_table("host_health_states", "diseased", 1);
CALL upsert_basic_table("host_health_states", "healthy", 2);
CALL upsert_basic_table("host_health_states", "not applicable", 3);
CALL upsert_basic_table("host_health_states", "not collected", 4);
CALL upsert_basic_table("host_health_states", "not provided", 5);
CALL upsert_basic_table("host_health_states", "restricted access", 6);

CALL upsert_basic_table("host_habitats", "domestic:free-range farm", 1);
CALL upsert_basic_table("host_habitats", "domestic:indoor farm", 2);
CALL upsert_basic_table("host_habitats", "domestic:live market", 3);
CALL upsert_basic_table("host_habitats", "domestic:semi-enclosed housing", 4);
CALL upsert_basic_table("host_habitats", "other", 5);
CALL upsert_basic_table("host_habitats", "wild:migratory", 6);
CALL upsert_basic_table("host_habitats", "wild:resident", 7);

CALL upsert_basic_table("host_behaviours", "captive-wild (e.g. at zoo)", 1);
CALL upsert_basic_table("host_behaviours", "domestic", 2);
CALL upsert_basic_table("host_behaviours", "other", 3);
CALL upsert_basic_table("host_behaviours", "wild", 4);