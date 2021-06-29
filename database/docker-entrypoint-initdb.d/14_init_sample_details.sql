CREATE TABLE IF NOT EXISTS `samples_collection` (

	sample_id							INT UNSIGNED NOT NULL PRIMARY KEY,
	year									SMALLINT UNSIGNED,
	month									TINYINT UNSIGNED,
	day										TINYINT UNSIGNED,
	collector_id					INT UNSIGNED,
	collection_device_id 	INT UNSIGNED

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
	lib_id									VARCHAR(200) NULL UNIQUE,
	layout_paired						BIT(1),					
	strategy_id							SMALLINT UNSIGNED,
	source_id								SMALLINT UNSIGNED,
	selection_id						SMALLINT UNSIGNED,
	design_description 			VARCHAR(1000),
	preparation_date				DATE,
	insert_size							VARCHAR(20)

);



CREATE TABLE IF NOT EXISTS `samples_host` (

	sample_id										INT UNSIGNED NOT NULL PRIMARY KEY,
	host_id											INT UNSIGNED,
	host_subject_id							VARCHAR(200),
	additional_host_info				VARCHAR(200),
	patient_gender							BIT(1),
	patient_age									TINYINT UNSIGNED,
	patient_status_id						INT UNSIGNED,
	ppe													VARCHAR(600),
	host_habitat_id							TINYINT UNSIGNED,
	host_behaviour_id						TINYINT UNSIGNED,
	host_description						VARCHAR(1000),
	gravidity										VARCHAR(500),

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
	passage_method												VARCHAR(200),
	passage_number												TINYINT UNSIGNED,
	strain																VARCHAR(500),
	isolation_source_host_associated			VARCHAR(600),
	isolation_source_non_host_associated	VARCHAR(600),
	sample_capture_status_id 							TINYINT UNSIGNED,
	specimen_source_id										INT UNSIGNED,
	sample_storage_conditions							VARCHAR(500),
	definition_for_seropositive_sample		VARCHAR(500),
	serotype															VARCHAR(500),
	
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
	outbreak										VARCHAR(200),
	treatment																VARCHAR(500),
	date_of_prior_sars_cov_2_vaccination		DATE,
	prior_sars_cov_2_antiviral_treatment		BIT(1),
	prior_sars_cov_2_infection							BIT(1),	
	prior_sars_cov_2_vaccination						TINYINT UNSIGNED,
	sars_cov_2_diag_gene_name_1							TINYINT UNSIGNED,
	sars_cov_2_diag_pcr_ct_value_1					TINYINT UNSIGNED,
	sars_cov_2_diag_gene_name_2							TINYINT UNSIGNED,
	sars_cov_2_diag_pcr_ct_value_2					TINYINT UNSIGNED,
	vaccine_received												VARCHAR(100),
	virus_isolate_of_prior_infection				VARCHAR(200)

);


CREATE TABLE IF NOT EXISTS `samples_sequencing` (

	sample_id											INT UNSIGNED NOT NULL PRIMARY KEY,
	sequencing_instrument_id			INT UNSIGNED,
	assembly_method_id						INT UNSIGNED,
	coverage											MEDIUMINT UNSIGNED

);

