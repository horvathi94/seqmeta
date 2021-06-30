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



CREATE OR REPLACE VIEW view_samples_sampling AS

	SELECT 
		
		sampling.sample_id AS sample_id,
		originating_lab.name AS originating_lab_name,
		originating_lab.address AS originating_lab_address,
		sampling.originating_lab_sample_name AS originating_lab_sample_name,
		submitting_lab.name AS submitting_lab_name,
		submitting_lab.address AS submitting_lab_address,
		sampling.submitting_lab_sample_name AS submitting_lab_sample_name,
		passage_details.label AS passage_details,
		sampling_strategies.label AS sampling_strategy,
		author_groups.group_name AS author_group_name,
		author_groups.abbreviated_middle_names AS authors_list,
		sampling.strain AS strain,
		sampling.isolation_source_host_associated AS isolation_source_host_associated,
		sampling.isolation_source_non_host_associated AS isolation_source_non_host_associated,
		capture_statuses.label AS sample_capture_status,
		specimen_sources.label AS specimen_source,
		sampling.sample_storage_conditions AS sample_storage_conditions,
		sampling.definition_for_seropositive_sample AS definition_for_seropositive_sample,
		sampling.serotype AS serotype

	FROM samples_sampling AS sampling
	LEFT JOIN view_institutions AS originating_lab
		ON sampling.originating_lab_id = originating_lab.id
	LEFT JOIN view_institutions AS submitting_lab
		ON sampling.submitting_lab_id = submitting_lab.id
	LEFT JOIN view_passage_details AS passage_details
		ON sampling.passage_details_id = passage_details.id
	LEFT JOIN view_sampling_strategies AS sampling_strategies
		ON sampling.sampling_strategy_id = sampling_strategies.id
	LEFT JOIN view_authors_in_groups_condensed AS author_groups
		ON sampling.author_group_id = author_groups.`group_id`
	LEFT JOIN sample_capture_status AS capture_statuses
		ON sampling.sample_capture_status_id = capture_statuses.id
	LEFT JOIN view_specimen_sources AS specimen_sources
		ON sampling.specimen_source_id = specimen_sources.id;
