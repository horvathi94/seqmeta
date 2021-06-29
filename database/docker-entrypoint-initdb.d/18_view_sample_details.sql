




CREATE OR REPLACE VIEW view_samples_library AS 

	SELECT

		library.sample_id AS sample_id,
		library.lib_id AS library_id,
		library.layout_paired AS layout_paired,
		IF( library.layout_paired	IS NULL, "",
			IF (library.layout_paired IS TRUE, "Paired-End", "Single") ) AS library_layout,
		strategies.item_key AS library_strategy,
		sources.item_key AS library_source,
		selections.item_key AS library_selection,
		library.design_description AS library_design_description,
		IF(library.preparation_date IS NULL, "",
			DATE_FORMAT(library.preparation_date, "%Y-%m-%d")) AS library_preparation_date,
		library.insert_size AS library_insert_size

	FROM samples_library AS library
	LEFT JOIN library_strategies AS strategies
		ON library.strategy_id = strategies.id
	LEFT JOIN library_sources AS sources
		ON library.source_id = sources.id
	LEFT JOIN library_selections AS selections
		ON library.selection_id = selections.id;
	



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


CREATE OR REPLACE VIEW view_samples_sequencing AS 

	SELECT 

		sequencing.sample_id AS sample_id,
		instruments.label AS sequencing_instrument,
		platforms.label AS sequencing_platform,
		assembly.label AS assembly_method,
		sequencing.coverage AS coverage,
		IF (sequencing.coverage IS NULL, "",
			CONCAT(sequencing.coverage, "x")) AS coverage_x

	FROM samples_sequencing AS sequencing
	LEFT JOIN assembly_methods AS assembly
		ON sequencing.assembly_method_id = assembly.id
	LEFT JOIN sequencing_instruments AS instruments
		ON sequencing.sequencing_instrument_id = instruments.id
	LEFT JOIN sequencing_platforms AS platforms
		ON instruments.platform_id = platforms.id;
	
	
