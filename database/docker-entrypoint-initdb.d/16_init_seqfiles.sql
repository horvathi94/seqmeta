CREATE TABLE IF NOT EXISTS `seqfiles` (

	id 								INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	sample_id					INT UNSIGNED NOT NULL,
	file_type_id			INT UNSIGNED,
	is_assembly				BIT(1),
	is_forward_read		BIT(1)

);

SET @table_name := "seqfile_extensions";
CALL create_dict_table(@table_name);
CALL upsert_dict_table(@table_name, 1, "fasta", "fasta");
CALL upsert_dict_table(@table_name, 2, "bam", "bam");
CALL upsert_dict_table(@table_name, 3, "sam", "sam");
CALL upsert_dict_table(@table_name, 4, "fastq", "fastq");


CREATE OR REPLACE VIEW `view_seqfiles` AS 

	SELECT 

		samples.sample_id AS sample_id,
		exts.item_key AS file_type,
		exts.item_value AS file_extension,
		is_assembly,
		is_forward_read,
		IF (is_assembly IS TRUE, 
			CONCAT(samples.sample_name, ".", exts.item_value), ""
			) AS filename
	
	FROM seqfiles
	LEFT JOIN view_samples_base AS samples
		ON seqfiles.sample_id = samples.sample_id
	LEFT JOIN seqfile_extensions AS exts
		ON seqfiles.file_type_id = exts.id;


DELIMITER $$

CREATE PROCEDURE upsert_seqfiles (
	IN sample_id 				INT UNSIGNED,
	IN file_type_id 		INT UNSIGNED, 
	IN is_assembly			INT UNSIGNED,
	IN is_forward_read	INT UNSIGNED
)

	BEGIN

		SET @working_id := 0;


		SELECT @working_id := id 
			FROM seqfiles 
			WHERE seqfiles.sample_id = sample_id 
				AND seqfiles.is_assembly = is_assembly
				AND seqfiles.is_forward_read = is_forward_read;

		IF ( @working_id = 0 ) THEN 

			INSERT INTO seqfiles (sample_id, file_type_id, is_assembly, is_forward_read)
				VALUES (sample_id, file_type_id, is_assembly, is_forward_read);

		ELSE

			UPDATE seqfiles
				SET file_type_id = file_type_id,
					is_assembly = is_assembly,
					is_forward_read = is_forward_read
				WHERE id = @working_id;

		END IF;


	END $$


DELIMITER ;
