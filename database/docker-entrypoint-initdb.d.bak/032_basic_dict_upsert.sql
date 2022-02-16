
DELIMITER $$

CREATE PROCEDURE upsert_dict_table(
	IN table_name VARCHAR(100),
	IN id INT UNSIGNED,
	IN item_key VARCHAR(200),
	IN item_value VARCHAR(1000)
)

BEGIN

	SET @working_id := 0;

	IF ( id = 0 ) THEN

		SET @id_query := CONCAT(
			"SELECT @working_id := id",
			" FROM ", table_name,
			" WHERE item_key = '", item_key, "';"
		);

		PREPARE stmt FROM @id_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

	END IF;

	IF ( @working_id = 0 ) THEN

		IF ( item_value IS NOT NULL ) THEN

			SET @query = CONCAT(
				"INSERT INTO ", table_name,
				" (item_key, item_value)",
				" VALUES('", item_key, "', '", item_value , "');"
			);

		ELSE

			SET @query = CONCAT(
				"INSERT INTO ", table_name,
				" (item_key, item_value)",
				" VALUES('", item_key, ",", NULL, ");"
			);

		END IF;

	ELSE

		SET @query = CONCAT(
			"UPDATE ", table_name,
			" SET item_value = '", item_value, "'"
			" WHERE id = ", @working_id
		);

	END IF;

	PREPARE stmt FROM @query;
	EXECUTE stmt;
	DEALLOCATE PREPARE stmt;

END $$

DELIMITER ;
