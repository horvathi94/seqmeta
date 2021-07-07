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
		WHERE indx <> 0
		ORDER BY indx ASC, label ASC;


DELIMITER $$

CREATE PROCEDURE upsert_hosts(
	IN inlabel 	CHAR(200),
	IN inlatin	CHAR(200),
	IN inindx		INT UNSIGNED
)

	BEGIN

		IF ( inlabel <> "" AND inlabel IS NOT NULL ) THEN

			SET @id = 0;
			SELECT @id := id
				FROM hosts
				WHERE `label` = inlabel;

			IF ( @id = 0 ) THEN

				INSERT INTO `hosts` (`label`, `latin`, `indx`)
					VALUES (inlabel, inlatin, inindx);

			ELSE
			
				UPDATE `hosts`
					SET `label` = inlabel,
						`latin` = inlatin,
						`indx` = inindx
					WHERE id = @id;

			END IF;


		END IF;

	END $$

DELIMITER ;



CALL upsert_hosts("Human", "Homo sapiens", 1);
