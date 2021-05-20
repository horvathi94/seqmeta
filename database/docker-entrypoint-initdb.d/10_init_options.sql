/* passage_details */
SET @table_name = "passage_details";
SET @view_name = "view_passage_details";
CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);

/* assembly_methods */
SET @table_name = "assembly_methods";
SET @view_name = "view_assembly_methods";
CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);

/* sequencing_technologies */
SET @table_name = "sequencing_technologies";
SET @view_name = "view_sequencing_technologies";
CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);

/* sampling_strategies */
SET @table_name = "sampling_strategies";
SET @view_name = "view_sampling_strategies";
CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);

/* patient_statuses */
SET @table_name = "patient_statuses";
SET @view_name = "view_patient_statuses";
CALL create_basic_table(@table_name);
CALL create_basic_view(@view_name, @table_name);


CREATE TABLE IF NOT EXISTS `hosts` (
	id			INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	label		CHAR(200) UNIQUE,
	latin		CHAR(200),
	indx		INT UNSIGNED
);


CREATE VIEW `view_hosts` AS

	SELECT 
		`id`, 
		`label`,
		`latin`,
		CONCAT(`label`, " (", `latin`, ")" ) AS display_label,
		`indx`
		FROM `hosts`
		WHERE id <> 0
		ORDER BY indx ASC, label ASC;


DELIMITER $$

CREATE PROCEDURE upsert_hosts(
	IN id 		INT UNSIGNED,
	IN label 	CHAR(200),
	IN latin	CHAR(200),
	IN indx		INT UNSIGNED
)

	BEGIN

		IF ( id <> "" AND id IS NOT NULL ) THEN

			SET @select_id = 0;

			IF ( id = "" OR id = 0 OR id IS NULL ) THEN

				SELECT @select_id = id
					FROM hosts
					WHERE label = label;

			ELSE

				SET @select_id = id;

			END IF;

			IF ( @select_id = 0 ) THEN

				INSERT INTO `hosts` (label, latin, indx)
					VALUES (label, latin, indx);

			ELSE
			
				UPDATE `hosts`
					SET label = label,
						latin = latin,
						indx = indx
					WHERE id = @select_id;

			END IF;


		END IF;

	END $$

DELIMITER ;