CREATE TABLE IF NOT EXISTS `samples_sampling` (

	sample_id															INT UNSIGNED NOT NULL PRIMARY KEY,
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
	serotype															VARCHAR(500)
	
);



CREATE OR REPLACE VIEW view_samples_sampling AS

	SELECT 
		
		sampling.sample_id AS sample_id,
		sampling_strategies.label AS sampling_strategy,
		sampling.strain AS strain,
		sampling.isolation_source_host_associated AS isolation_source_host_associated,
		sampling.isolation_source_non_host_associated AS isolation_source_non_host_associated,
		capture_statuses.label AS sample_capture_status,
		specimen_sources.label AS specimen_source,
		sampling.sample_storage_conditions AS sample_storage_conditions,
		sampling.definition_for_seropositive_sample AS definition_for_seropositive_sample,
		sampling.serotype AS serotype,
		sampling.passage_method AS passage_method,
		sampling.passage_number AS passage_number

	FROM samples_sampling AS sampling
	LEFT JOIN view_sampling_strategies AS sampling_strategies
		ON sampling.sampling_strategy_id = sampling_strategies.id
	LEFT JOIN sample_capture_status AS capture_statuses
		ON sampling.sample_capture_status_id = capture_statuses.id
	LEFT JOIN view_specimen_sources AS specimen_sources
		ON sampling.specimen_source_id = specimen_sources.id;
