DELIMITER $$

CREATE PROCEDURE create_dict_table(
	IN table_name CHAR(100)
)

	BEGIN 

		SET @create_query = CONCAT(
			"CREATE TABLE IF NOT EXISTS `", table_name, "`(",
				"id 				INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,",
				"item_key		CHAR(200) NOT NULL UNIQUE,",
				"item_value	VARCHAR(500) );"
		);

		PREPARE stmt FROM @create_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

	END $$


CREATE PROCEDURE upsert_dict_table(
	IN table_name CHAR(100),
	IN id					INT UNSIGNED,
	IN item_key		CHAR(200),
	IN item_value	CHAR(200)
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

			SET @query = CONCAT(
				"INSERT INTO ", table_name,
				" (item_key, item_value)",
				" VALUES('", item_key, "', '", item_value , "');"
			);

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
