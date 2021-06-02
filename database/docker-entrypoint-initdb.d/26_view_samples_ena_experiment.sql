CREATE OR REPLACE VIEW `view_samples_ena_experiment` AS 

	SELECT

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,

		library.library_id AS library_name,
		library.library_strategy AS library_strategy,
		library.library_source AS library_source,
		library.library_selection AS library_selection,
		library.library_design_description AS library_design_description,
		library.layout_paired AS is_paired,
		library.library_preparation_date AS library_preparation_date,

		sequencing.sequencing_platform AS sequencing_platform,
		sequencing.sequencing_instrument AS sequencing_instrument

	FROM view_samples_base AS samples
	LEFT JOIN view_samples_library AS library
		ON samples.sample_id = library.sample_id
	LEFT JOIN view_samples_sequencing AS sequencing
		ON samples.sample_id = sequencing.sample_id
