CREATE TABLE IF NOT EXISTS samples (

	id														INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name													CHAR(200) UNIQUE NOT NULL,

	collection_year								SMALLINT UNSIGNED NOT NULL,
	collection_month							TINYINT UNSIGNED,
	collection_day								TINYINT UNSIGNED,

	host_id												INT UNSIGNED,
	additional_host_info					TEXT,
	patient_gender								BIT(1),
	patient_age										TINYINT UNSIGNED,
	patient_status_id							INT UNSIGNED,

	continent_id									TINYINT UNSIGNED,
	country_id										SMALLINT UNSIGNED,
	county												CHAR(200),
	city													CHAR(200),
	additional_location_info			TEXT,

	originating_lab_id						INT UNSIGNED,
	originating_lab_sample_name		CHAR(200) UNIQUE,
	submitting_lab_id							INT UNSIGNED,
	submitting_lab_sample_name		CHAR(200) UNIQUE,
	author_group_id								INT UNSIGNED,

	sampling_strategy_id					INT UNSIGNED,
	passage_details_id						INT UNSIGNED,
	sequencing_technology_id			INT UNSIGNED,
	assembly_method_id						INT UNSIGNED,
	coverage											MEDIUMINT UNSIGNED,

	specimen_source_id						INT UNSIGNED,
	outbreak											TEXT,
	last_vaccinated								TEXT,
	treatment											TEXT,

	subject_exposure 					TEXT,
	subject_exposure_duration	TEXT,
	type_exposure			TEXT,
	ppe								TEXT,
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

	definition_for_seropositive_sample	TEXT,
	serotype														TEXT,

	isolate	TEXT,
	strain	TEXT,

	isolation_source_host_associated			TEXT,
	host_description											TEXT,
	gravidity															TEXT,
	isolation_source_non_host_associated	TEXT

);
