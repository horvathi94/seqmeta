/* View for selecting data for ENA manifest file for assemblies submission. */

CREATE OR REPLACE VIEW `view_samples_ena_manifest_assembly` AS 

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
		"<STUDY ACCESSION>" AS STUDY,
		samples.sample_name AS SAMPLE,
		"COVID-19 outbreak" AS ASSEMBLY_TYPE,
		samples.coverage AS COVERAGE,
		assembly_methods.label AS PROGRAM,
		sequencing_platforms.label AS PLATFORM,
		samples.sample_description AS DESCRIPTION,
		"<RUN REF>" AS RUN_REF,
		( SELECT filename
			FROM view_seqfiles AS seqfiles
			WHERE seqfiles.sample_id = samples.sample_id
				AND seqfiles.is_assembly IS TRUE
				AND assembly_level_string = "contigs"
		) AS contigs_filename,
		( SELECT filename
			FROM view_seqfiles AS seqfiles
			WHERE seqfiles.sample_id = samples.sample_id
				AND seqfiles.is_assembly IS TRUE
				AND assembly_level_string = "scaffolds"
		) AS scaffolds_filename


		FROM view_samples_base AS samples
		LEFT JOIN assembly_methods
			ON samples.assembly_method_id = assembly_methods.id
		LEFT JOIN sequencing_instruments
			ON samples.sequencing_instrument_id = sequencing_instruments.id
		LEFT JOIN sequencing_platforms
			ON sequencing_instruments.id = sequencing_platforms.id
