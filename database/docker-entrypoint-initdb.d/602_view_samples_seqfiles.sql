/* View for linking samples to the sequencing files */

CREATE OR REPLACE VIEW `view_samples_seqfiles` AS

	SELECT 

		samples.sample_id AS sample_id,

		seqfiles.file_type AS file_type,
		seqfiles.is_assembly AS is_assembly,
		seqfiles.is_forward_read AS is_forward_read


	FROM view_samples_base AS samples
	LEFT JOIN view_seqfiles AS seqfiles
		ON samples.sample_id = seqfiles.sample_id
