CREATE TABLE IF NOT EXISTS `samples_collection` (

	sample_id					INT UNSIGNED NOT NULL PRIMARY KEY,
	year							SMALLINT UNSIGNED,
	month							TINYINT UNSIGNED,
	day								TINYINT UNSIGNED,
	collector_id			INT UNSIGNED

);


CREATE TABLE IF NOT EXISTS `samples_location` (

	sample_id							INT UNSIGNED NOT NULL PRIMARY KEY,
	continent_id					TINYINT UNSIGNED,
	country_id						SMALLINT UNSIGNED,
	region								VARCHAR(150),
	locality							VARCHAR(150),
	additional_info				VARCHAR(1000),
	geo_loc_latitude			DECIMAL(5,2),
	geo_loc_longitude			DECIMAL(5,2)

);


CREATE TABLE IF NOT EXISTS `samples_library` (
	
	sample_id 							INT UNSIGNED NOT NULL PRIMARY KEY,
	lib_id									VARCHAR(200) UNIQUE,
	layout_paired						BIT(1),					
	strategy_id							SMALLINT UNSIGNED,
	source_id								SMALLINT UNSIGNED,
	selection_id						SMALLINT UNSIGNED,
	design_description 			VARCHAR(1000)

);



CREATE TABLE IF NOT EXISTS `samples_host` (

	sample_id										INT UNSIGNED NOT NULL PRIMARY KEY,
	host_id											INT UNSIGNED,
	host_subject_id							VARCHAR(200),
	additional_host_info				VARCHAR(200),
	patient_gender							BIT(1),
	patient_age									TINYINT UNSIGNED,
	patient_status_id						INT UNSIGNED,
	last_vaccinated							VARCHAR(200),
	ppe													VARCHAR(600),
	host_habitat_id							TINYINT UNSIGNED,
	host_behaviour_id						TINYINT UNSIGNED,
	host_description						VARCHAR(1000),
	gravidity										VARCHAR(500)

);


CREATE TABLE IF NOT EXISTS `samples_sampling` (

	sample_id															INT UNSIGNED NOT NULL PRIMARY KEY,
	originating_lab_id										INT UNSIGNED,
	originating_lab_sample_name						CHAR(200),
	submitting_lab_id											INT UNSIGNED,
	submitting_lab_sample_name						CHAR(200),
	author_group_id												INT UNSIGNED,
	receipt_date													DATE,
	sampling_strategy_id									INT UNSIGNED,
	passage_details_id										INT UNSIGNED,
	isolate																VARCHAR(500),
	strain																VARCHAR(500),
	isolation_source_host_associated			VARCHAR(600),
	isolation_source_non_host_associated	VARCHAR(600),
	sample_capture_status_id 							TINYINT UNSIGNED,
	specimen_source_id										INT UNSIGNED,
	sample_storage_conditions							VARCHAR(500),
	definition_for_seropositive_sample		VARCHAR(500),
	serotype															VARCHAR(500)

);


CREATE TABLE IF NOT EXISTS `samples_health_status` (

	sample_id										INT UNSIGNED NOT NULL PRIMARY KEY,
	subject_exposure 						VARCHAR(600),
	subject_exposure_duration		VARCHAR(600),
	type_exposure								VARCHAR(600),
	hospitalization							BIT(1),
	ilness_duration							SMALLINT UNSIGNED,
	ilness_symptoms							VARCHAR(600),
	host_disease_outcome_id			TINYINT UNSIGNED,
	host_health_state_id				TINYINT UNSIGNED,
	treatment										VARCHAR(500),
	outbreak										VARCHAR(200)

);


CREATE TABLE IF NOT EXISTS `samples_sequencing` (

	sample_id											INT UNSIGNED NOT NULL PRIMARY KEY,
	sequencing_instrument_id			INT UNSIGNED,
	assembly_method_id						INT UNSIGNED,
	coverage											MEDIUMINT UNSIGNED

);
