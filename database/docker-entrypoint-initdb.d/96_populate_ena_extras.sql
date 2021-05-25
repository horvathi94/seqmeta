CALL upsert_basic_table("sample_capture_status", "active surveillance in response to outbreak", 1);
CALL upsert_basic_table("sample_capture_status", "active surveillance not initiated by an outbreak", 2);
CALL upsert_basic_table("sample_capture_status", "farm sample", 3);
CALL upsert_basic_table("sample_capture_status", "market sample", 4);
CALL upsert_basic_table("sample_capture_status", "other", 5);
CALL upsert_basic_table("sample_capture_status", "pet sample", 6);
CALL upsert_basic_table("sample_capture_status", "zoo sample", 7);

CALL upsert_basic_table("host_disiease_outcome", "dead", 1);
CALL upsert_basic_table("host_disiease_outcome", "recovered", 2);
CALL upsert_basic_table("host_disiease_outcome", "recovered with sequelae", 3);

CALL upsert_basic_table("host_health_states", "diseased", 1);
CALL upsert_basic_table("host_health_states", "healthy", 2);
CALL upsert_basic_table("host_health_states", "not applicable", 3);
CALL upsert_basic_table("host_health_states", "not collected", 4);
CALL upsert_basic_table("host_health_states", "not provided", 5);
CALL upsert_basic_table("host_health_states", "restricted access", 6);
