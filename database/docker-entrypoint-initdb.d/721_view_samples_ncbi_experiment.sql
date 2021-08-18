/* View for selecting data for NCBI experiments submission. */


CREATE OR REPLACE VIEW `view_samples_ncbi_experiment` AS
	
	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
	
		library.library_id AS library_id,
		library.library_strategy AS library_strategy,
		library.library_source AS library_source,
		library.library_selection AS library_selection,
		library.library_layout_ncbi AS library_layout,
		library.library_design_description AS design_description,

		CONCAT(library.library_strategy, 
			" of SARS-CoV-2: ", 
			IF(host.patient_age IS NULL, "", 
				IF(host.patient_age >= 18, "adult ", "child ")),
			host.patient_gender_ena
		) AS title,

		sequencing.sequencing_platform AS platform,
		sequencing.sequencing_instrument AS instrument_model,
		( SELECT file_type 
			FROM view_seqfiles AS seqfiles 
			WHERE seqfiles.sample_id = samples.sample_id
				AND is_assembly IS FALSE
				AND is_forward_read IS TRUE
			) AS filetype,
		( SELECT filename 
			FROM view_seqfiles AS seqfiles 
			WHERE seqfiles.sample_id = samples.sample_id
				AND is_assembly IS FALSE
				AND is_forward_read IS TRUE
			) AS filename,
		( SELECT filename 
			FROM view_seqfiles AS seqfiles 
			WHERE seqfiles.sample_id = samples.sample_id
				AND is_assembly IS FALSE
				AND is_forward_read IS FALSE
			) AS filename2
		


	FROM view_samples_base AS samples
	LEFT JOIN view_samples_library AS library
		ON samples.sample_id = library.sample_id
	LEFT JOIN view_samples_sequencing AS sequencing
		ON samples.sample_id = sequencing.sample_id
	LEFT JOIN view_samples_host AS host
		ON samples.sample_id = host.sample_id
