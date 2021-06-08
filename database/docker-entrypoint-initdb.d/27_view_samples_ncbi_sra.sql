CREATE OR REPLACE VIEW `view_samples_ncbi_sra` AS
	
	SELECT 

		samples.sample_id AS sample_id,
	
		library.library_id AS library_name,
		library.library_strategy AS library_strategy,
		library.library_source AS library_source,
		library.library_selection AS library_selection,
		IF (library.layout_paired IS NULL, "", 
			IF(library.layout_paired IS TRUE, "Paired-End", "Single")) AS library_layout,
		library.library_design_description AS library_design_description,

		CONCAT(library.library_strategy, 
			" of SARS-CoV-2: ", 
			IF(host.patient_age IS NULL, "", 
				IF(host.patient_age >= 18, "adult ", "child ")),
			host.patient_gender_ena
		) AS title,

		sequencing.sequencing_platform AS sequencing_platform,
		sequencing.sequencing_instrument AS sequencing_instrument


	FROM view_samples_base AS samples
	LEFT JOIN view_samples_library AS library
		ON samples.sample_id = library.sample_id
	LEFT JOIN view_samples_sequencing AS sequencing
		ON samples.sample_id = sequencing.sample_id
	LEFT JOIN view_samples_host AS host
		ON samples.sample_id = host.sample_id
