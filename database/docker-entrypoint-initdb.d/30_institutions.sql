DELIMITER $$

CREATE PROCEDURE SelectInstitutions(
	IN id INT UNSIGNED
)

	BEGIN 

		IF ( id = 0 ) THEN

			SELECT *
				FROM `institutions`;

		ELSE

			SELECT *
				FROM `institutions`
				WHERE `id` = id;

		END IF;

	END $$


DELIMITER ; 
