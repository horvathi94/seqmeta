/* View for retrieving information about sequencing files */

CREATE OR REPLACE VIEW `view_seqfiles` AS 

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
		seqfiles.is_assembly AS is_assembly,
		seqfiles.is_forward_read AS is_forward_read,
		IF (seqfiles.is_assembly IS TRUE, 
			assembly_files.item_key,
			reads_files.item_key) AS file_type,
		seqfiles.file_type_id AS file_extension_id,
		IF (seqfiles.is_assembly IS TRUE, 
			assembly_files.item_value,
			reads_files.item_value) AS file_extension,
		CONCAT(samples.sample_name, 
			IF (seqfiles.is_assembly IS TRUE, 
				CONCAT("_", assembly_levels.label, ".", assembly_files.item_value),
				CONCAT(
					IF (seqfiles.is_forward_read,
						"_fw_read.", "_rv_read."),
						reads_files.item_value
				)
			) 
		) AS filename,
		seqfiles.assembly_level AS assembly_level,
		assembly_levels.label AS assembly_level_string,
		seqfiles.assembly_method_id AS assembly_method_id,
		assembly_methods.label AS assembly_method


	FROM seqfiles
	LEFT JOIN view_samples_base AS samples
		ON seqfiles.sample_id = samples.sample_id
	LEFT JOIN assembly_files 
		ON seqfiles.file_type_id = assembly_files.id
	LEFT JOIN reads_files 
		ON seqfiles.file_type_id = reads_files.id
	LEFT JOIN assembly_levels
		ON seqfiles.assembly_level = assembly_levels.id
	LEFT JOIN assembly_methods
		ON seqfiles.assembly_method_id = assembly_methods.id
