CREATE TABLE IF NOT EXISTS samples (

	id														INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name													CHAR(200) UNIQUE NOT NULL,

	host_id												INT UNSIGNED,
	additional_host_info					VARCHAR(200),
	patient_gender								BIT(1),
	patient_age										TINYINT UNSIGNED,
	patient_status_id							INT UNSIGNED,

	originating_lab_id						INT UNSIGNED,
	originating_lab_sample_name		CHAR(200),
	submitting_lab_id							INT UNSIGNED,
	submitting_lab_sample_name		CHAR(200),
	author_group_id								INT UNSIGNED,

	sampling_strategy_id					INT UNSIGNED,
	passage_details_id						INT UNSIGNED,
	sequencing_instrument_id			INT UNSIGNED,
	assembly_method_id						INT UNSIGNED,
	coverage											MEDIUMINT UNSIGNED,

	specimen_source_id						INT UNSIGNED,
	outbreak											VARCHAR(200),
	last_vaccinated								VARCHAR(200),
	treatment											VARCHAR(200),

	subject_exposure 						VARCHAR(200),
	subject_exposure_duration		VARCHAR(200),
	type_exposure								VARCHAR(200),
	ppe													VARCHAR(200),
	hospitalization							BIT(1),
	ilness_duration							SMALLINT UNSIGNED,
	ilness_symptoms							VARCHAR(200),

	sample_capture_status_id 		TINYINT UNSIGNED,
	host_disease_outcome_id			TINYINT UNSIGNED,

	host_subject_id							CHAR(200),
	host_health_state_id				TINYINT UNSIGNED,
		
	receipt_date								DATE,
	sample_storage_conditions		VARCHAR(200),

	definition_for_seropositive_sample	VARCHAR(200),
	serotype														VARCHAR(200),

	isolate						VARCHAR(200),
	strain						VARCHAR(200),

	host_habitat_id												TINYINT UNSIGNED,
	host_behaviour_id											TINYINT UNSIGNED,
	isolation_source_host_associated			VARCHAR(200),
	host_description											VARCHAR(200),
	gravidity															VARCHAR(200),
	isolation_source_non_host_associated	VARCHAR(200),

	link_library_id 		INT UNSIGNED,
	link_collection_id	INT UNSIGNED,
	link_location_id		INT UNSIGNED

);
