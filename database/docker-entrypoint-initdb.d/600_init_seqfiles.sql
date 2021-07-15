SET @table_name := "assembly_files";
CALL create_dict_table(@table_name);
CALL upsert_dict_table(@table_name, 0, "FASTA", "fa");
CALL upsert_dict_table(@table_name, 0, "BAM", "bam");


SET @table_name := "reads_files";
CALL create_dict_table(@table_name);
CALL upsert_dict_table(@table_name, 0, "FASTQ", "fastq.gz");


SET @table_name := "assembly_levels";
CALL create_basic_table(@table_name);
CALL upsert_basic_table(@table_name, "contigs", 1);
CALL upsert_basic_table(@table_name, "scaffolds", 2);
CALL upsert_basic_table(@table_name, "consensus", 3);



CREATE TABLE IF NOT EXISTS `seqfiles` (

	id 								INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	sample_id					INT UNSIGNED NOT NULL,
	file_type_id			INT UNSIGNED,
	is_assembly				BIT(1),
	is_forward_read		BIT(1),
	assembly_level		TINYINT UNSIGNED

);




DELIMITER $$

CREATE PROCEDURE upsert_seqfiles (
	IN sample_id 				INT UNSIGNED,
	IN file_type_id 		INT UNSIGNED,
	IN is_assembly			BIT(1),
	IN is_forward_read	BIT(1),
	IN assembly_level		INT UNSIGNED
)

	BEGIN

		SET @working_id := 0;


		IF ( is_forward_read IS NULL ) THEN

			SELECT @working_id := id
				FROM seqfiles
				WHERE seqfiles.sample_id = sample_id
					AND seqfiles.is_assembly = is_assembly
					AND seqfiles.assembly_level = assembly_level;

		ELSE

			SELECT @working_id := id
				FROM seqfiles
				WHERE seqfiles.sample_id = sample_id
					AND seqfiles.is_assembly = is_assembly
					AND seqfiles.is_forward_read = is_forward_read;

		END IF;

		IF ( @working_id = 0 ) THEN

			INSERT INTO seqfiles (sample_id, file_type_id, is_assembly, is_forward_read, assembly_level)
				VALUES (sample_id, file_type_id, is_assembly, is_forward_read, assembly_level);

		ELSE

			UPDATE seqfiles
				SET file_type_id = file_type_id,
					is_assembly = is_assembly,
					is_forward_read = is_forward_read,
					assembly_level = assembly_level
				WHERE id = @working_id;

		END IF;

	END $$


DELIMITER ;


