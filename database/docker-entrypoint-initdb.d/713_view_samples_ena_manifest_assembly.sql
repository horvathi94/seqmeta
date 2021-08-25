/* View for selecting data for ENA manifest file for assemblies submission. */

CREATE OR REPLACE VIEW `view_samples_ena_manifest_assembly` AS 

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
		"<STUDY ACCESSION>" AS STUDY,
		samples.sample_name AS SAMPLE,
		"COVID-19 outbreak" AS ASSEMBLY_TYPE,
		samples.coverage AS COVERAGE,
		sequencing_platforms.label AS PLATFORM,
		( SELECT assembly_method
			FROM view_seqfiles AS seqfiles
			WHERE seqfiles.sample_id = samples.sample_id
				AND seqfiles.is_assembly IS TRUE
				AND assembly_level_string = "contigs"
		) AS contigs_assembly_method,
		( SELECT assembly_method
			FROM view_seqfiles AS seqfiles
			WHERE seqfiles.sample_id = samples.sample_id
				AND seqfiles.is_assembly IS TRUE
				AND assembly_level_string = "scaffolds"
		) AS scaffolds_assembly_method,
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
		LEFT JOIN sequencing_instruments
			ON samples.sequencing_instrument_id = sequencing_instruments.id
		LEFT JOIN sequencing_platforms
			ON sequencing_instruments.platform_id = sequencing_platforms.id
