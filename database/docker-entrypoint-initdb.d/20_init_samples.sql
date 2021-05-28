CREATE TABLE IF NOT EXISTS samples (

	id														INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name													CHAR(200) UNIQUE NOT NULL,

	collection_year								SMALLINT UNSIGNED NOT NULL,
	collection_month							TINYINT UNSIGNED,
	collection_day								TINYINT UNSIGNED,

	host_id												INT UNSIGNED,
	additional_host_info					VARCHAR(1000),
	patient_gender								BIT(1),
	patient_age										TINYINT UNSIGNED,
	patient_status_id							INT UNSIGNED,

	continent_id									TINYINT UNSIGNED,
	country_id										SMALLINT UNSIGNED,
	county												CHAR(200),
	city													CHAR(200),
	additional_location_info			VARCHAR(1000),

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
	outbreak											VARCHAR(2000),
	last_vaccinated								VARCHAR(600),
	treatment											VARCHAR(2000),

	subject_exposure 						VARCHAR(1000),
	subject_exposure_duration		VARCHAR(1000),
	type_exposure								VARCHAR(1000),
	ppe													VARHCAR(1000),
	hospitalization							BIT(1),
	ilness_duration							SMALLINT UNSIGNED,
	ilness_symptoms							VARCHAR(3000),

	geo_loc_latitude						DECIMAL(5,2),
	geo_loc_longitude 					DECIMAL(5,2),

	sample_capture_status_id 		TINYINT UNSIGNED,
	host_disease_outcome_id			TINYINT UNSIGNED,

	host_subject_id							CHAR(200),
	host_health_state_id				TINYINT UNSIGNED,
		
	collector_name_id						INT UNSIGNED,
	receipt_date								DATE,
	sample_storage_conditions		VARCHAR(3000),

	definition_for_seropositive_sample	VARCHAR(2000),
	serotype														VARCHAR(2000),

	isolate						VARCHAR(1000),
	strain						VARCHAR(1000),

	host_habitat_id												TINYINT UNSIGNED,
	host_behaviour_id											TINYINT UNSIGNED,
	isolation_source_host_associated			VARCHAR(3000),
	host_description											VARCHAR(2000),
	gravidity															VARCHAR(1000),
	isolation_source_non_host_associated	VARCHAR(2000)


	library_id							CHAR(200) UNIQUE,
	library_layout_paired		BIT(1),					
	library_strategy_id			INT UNSIGNED,
	library_sources_id			INT UNSIGNED,
	library_selection_id		INT UNSIGNED,
	design_description 			VARCHAR(1000)
);
