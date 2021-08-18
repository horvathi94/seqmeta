/* View for selecting data for ENA manifest file for raw read submission. */

CREATE OR REPLACE VIEW `view_samples_ena_manifest` AS
        
  SELECT 

		samples.sample_id AS sample_id,
    "<STUDY ACCESSION>" AS STUDY,
    "<SAMPLE ACCESSION>" AS SAMPLE,
		samples.sample_name AS ASSEMBLYNAME,
		"COVID-19 outbreak" AS ASSEMBLY_TYPE,
		sequencing.coverage_x AS COVERAGE,
		sequencing.assembly_method AS PROGRAM,
		sequencing.sequencing_platform AS PLATFORM,
		"<MINGAPLENGTH>" AS MINGAPLENGTH,
		"viral RNA" AS MOLECULETYPE,
		samples.sample_description AS DESCRIPTION,
		"<RUN ACCESSIONS>" AS RUN_REF,
		( SELECT seqfiles.filename 
				FROM view_seqfiles AS seqfiles
				WHERE seqfiles.sample_id = samples.sample_id
					AND seqfiles.is_assembly = TRUE 
			) AS FASTA


	FROM view_samples_base AS samples
	LEFT JOIN view_samples_sequencing AS sequencing
		ON samples.sample_id = sequencing.sample_id
