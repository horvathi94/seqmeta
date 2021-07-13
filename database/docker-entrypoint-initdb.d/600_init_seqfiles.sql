SET @table_name := "assembly_files";
CALL create_dict_table(@table_name);
CALL upsert_dict_table(@table_name, 0, "FASTA", "fa");
CALL upsert_dict_table(@table_name, 0, "BAM", "bam");


SET @table_name := "reads_files";
CALL create_dict_table(@table_name);
CALL upsert_dict_table(@table_name, 0, "FASTQ", "fastq.gz");


CREATE OR REPLACE VIEW `view_seqfiles` AS 

	SELECT 

		samples.sample_id AS sample_id,
		seqfiles.is_assembly AS is_assembly,
		seqfiles.is_forward_read AS is_forward_read,
		IF (seqfiles.is_assembly IS TRUE, 
			assembly_files.item_key,
			reads_files.item_key) AS file_type,
		IF (seqfiles.is_assembly IS TRUE, 
			assembly_files.item_value,
			reads_files.item_value) AS file_extension,
		CONCAT(samples.sample_name, 
			IF (seqfiles.is_assembly IS TRUE, 
				CONCAT(".", assembly_files.item_value),
				CONCAT(
					IF (seqfiles.is_forward_read,
						"_fw_read.", "_rv_read."),
						reads_files.item_value
				)
			) 
		) AS filename


	FROM seqfiles
	LEFT JOIN view_samples_base AS samples
		ON seqfiles.sample_id = samples.sample_id
	LEFT JOIN assembly_files 
		ON seqfiles.file_type_id = assembly_files.id
	LEFT JOIN reads_files 
		ON seqfiles.file_type_id = reads_files.id
