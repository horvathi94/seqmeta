
DELIMITER $$

CREATE PROCEDURE upsert_ordereddict_table(
	IN table_name VARCHAR(100),
	IN id INT UNSIGNED,
	IN item_key VARCHAR(200),
	IN item_value VARCHAR(500),
	IN indx INT UNSIGNED
)

BEGIN

	IF ( id IS NOT NULL AND item_key IS NOT NULL ) THEN

		SET @working_id = 0;

		IF ( id = 0 ) THEN

			SET @reg_id := 0;
			SET @reg_id_query = CONCAT(
				"SELECT @reg_id := id",
				" FROM ", table_name,
				" WHERE item_key = '", item_key, "'",
				" LIMIT 1;"
			);

			PREPARE stmt FROM @reg_id_query;
			EXECUTE stmt;
			DEALLOCATE PREPARE stmt;
			SET @working_id = @reg_id;

			IF ( @reg_id = 0 ) THEN


				SET @id_query = CONCAT(
					"SELECT @working_id := id",
					" FROM ", table_name,
					" WHERE indx = 0",
					" LIMIT 1;"
				);

				PREPARE stmt FROM @id_query;
				EXECUTE stmt;
				DEALLOCATE PREPARE stmt;

		END IF;


	ELSE

		SET @working_id = id;

	END IF;


	IF ( @working_id = 0 ) THEN

		SET @query = CONCAT(
			"INSERT INTO ", table_name,
			" (item_key, item_value, indx)",
			" VALUES ('", item_key, "', '", item_value, "', ", indx, ");"
		);

	ELSE

		SET @query = CONCAT(
			"UPDATE ", table_name,
			" SET item_key = '", item_key, "',",
			" item_value = '", item_value, "',",
			" indx = ", indx,
			" WHERE id = ", @working_id, ";"
		);

	END IF;


	PREPARE stmt FROM @query;
	EXECUTE stmt;
	DEALLOCATE PREPARE stmt;


END IF;

END $$


DELIMITER ;
