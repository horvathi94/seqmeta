DELIMITER $$

CREATE PROCEDURE UpsertHosts(
	IN host_id 			MEDIUMINT UNSIGNED,
	IN host_label 	CHAR(100),
	IN host_latin		CHAR(100)
)

	BEGIN

		IF ( host_id = 0 ) THEN

			IF ( host_label <> '' ) THEN

				INSERT INTO `hosts` (label, latin) 
					VALUES (host_label, host_latin);

			END IF;


		ELSE 

			IF ( host_label = '' ) THEN

				DELETE 
					FROM `hosts` 
					WHERE id = host_id;

			ELSE

				UPDATE `hosts` 
					SET `label` = host_label,
							`latin` = host_latin
					WHERE id = host_id;
			

			END IF;


		END IF;


	END $$



DELIMITER ;
