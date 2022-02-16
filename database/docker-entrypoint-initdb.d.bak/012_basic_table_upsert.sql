
DELIMITER $$

CREATE PROCEDURE upsert_basic_table(
	IN table_name VARCHAR(100),
	IN label VARCHAR(200),
	IN indx INT UNSIGNED
)

BEGIN

	IF ( label <> "" AND label IS NOT NULL ) THEN

		SET @query = "";
		SET @id = 0;
		SET @id_query = CONCAT(
			"SELECT @id := id",
			" FROM ", table_name,
			" WHERE label = \'", label, "\';"
		);

		PREPARE stmt FROM @id_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;


		IF ( @id = 0 ) THEN

			SET @query = CONCAT(
				"INSERT INTO ", table_name,
				" (label, indx)",
				" VALUES (\'", label, "\', ", indx, ");"
			);

		ELSE

			SET @query = CONCAT(
				"UPDATE ", table_name,
				" SET label = \'", label, "\',"
				" indx = ", indx,
				" WHERE id = ", @id, ";"
			);

		END IF;

		PREPARE stmt FROM @query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

	END IF;

END $$


DELIMITER ;

