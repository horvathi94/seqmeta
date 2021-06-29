CREATE TABLE IF NOT EXISTS `hosts` (
	id			INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	label		CHAR(200) UNIQUE,
	latin		CHAR(200),
	indx		INT UNSIGNED
);


CREATE OR REPLACE VIEW `view_hosts` AS

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
	IN label 	CHAR(200),
	IN latin	CHAR(200),
	IN indx		INT UNSIGNED
)

	BEGIN

		IF ( label <> "" AND label IS NOT NULL ) THEN

			SET @id = 0;
			SELECT @id := id
				FROM hosts
				WHERE label = label;

			IF ( @id = 0 ) THEN

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



CALL upsert_hosts("Human", "Homo sapiens", 1);
