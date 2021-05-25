CREATE TABLE IF NOT EXISTS `ena_samples_extra` (

	id					INT UNSIGNED NOT NULL AUTO_INCEREMENT PRIMARY KEY,
	sample_id		INT UNSIGNED NOT NULL,

	subject_exposure 	TEXT,
	subject_duration	TEXT,
	type_exposure			TEXT
	personal_protective_equipment TEXT,
	hospitalization		BIT(1),
	ilness_duration		TEXT,
	ilness_symptoms		TEXT,

	geo_loc_latitude	CHAR(200),
	geo_loc_longitude	CHAR(200),

	sample_capture_status_id 	TINYINT UNSIGNED,
	host_disease_outcome_id		TINYINT UNSIGNED,

	host_subject_id						CHAR(200),
	host_health_state_id			TINYINT UNSIGNED,
		
	collector_name_id					INT UNSIGNED,
	receipt_date							DATE,
	sample_storage_conditions	TEXT,

)
