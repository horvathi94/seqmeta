/* View for selecting data for ENA experiments submission. */

CREATE OR REPLACE VIEW `view_samples_ena_experiment` AS 

	SELECT

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_alias,

		library.library_id AS library_name,
		library.library_source AS library_source,
		library.library_strategy AS library_strategy,
		library.library_selection AS library_selection,
		library.library_design_description AS design_description,
		library.library_layout_paired AS is_paired,
		library.library_construction_protocol AS library_construction_protocol,
		library.library_insert_size AS insert_size,
/*		( SELECT filename 
			FROM view_seqfiles AS seqfiles 
			WHERE seqfiles.sample_id = samples.sample_id
				AND is_assembly IS FALSE
				AND is_forward_read IS TRUE
			) AS forward_file_name,*/
		"" AS forward_file_md5,
/*		( SELECT filename 
			FROM view_seqfiles AS seqfiles 
			WHERE seqfiles.sample_id = samples.sample_id
				AND is_assembly IS FALSE
				AND is_forward_read IS FALSE
			) AS reverse_file_name,*/
		"" AS reverse_file_md5,

		sequencing.sequencing_instrument AS instrument_model

	FROM view_samples_base AS samples
	LEFT JOIN view_samples_library AS library
		ON samples.sample_id = library.sample_id
	LEFT JOIN view_samples_sequencing AS sequencing
		ON samples.sample_id = sequencing.sample_id
