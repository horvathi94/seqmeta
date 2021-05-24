DELIMITER $$ 

CREATE PROCEDURE create_ordereddict_table(
	IN table_name CHAR(100)
)

	BEGIN

		SET @create_query = CONCAT(
			"CREATE TABLE IF NOT EXISTS `", table_name, "`(",
				"id 				INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,",
				"item_key		CHAR(200) NOT NULL,",
				"item_value	CHAR(200),",
				"indx				INT UNSIGNED);"
		);

		PREPARE stmt FROM @create_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

	END $$


CREATE PROCEDURE create_ordereddict_view(
	IN view_name 	CHAR(100),
	IN table_name CHAR(100)
)

	BEGIN 

		SET @view_query = CONCAT(
			"CREATE OR REPLACE VIEW ", 
			view_name, " AS ",
			"SELECT id, item_key, item_value, indx FROM ",
			table_name,
			" WHERE indx <> 0",
			" ORDER BY indx ASC, item_key ASC, item_value ASC;"
		);

		PREPARE stmt FROM @view_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;


	END $$



CREATE PROCEDURE upsert_ordereddict_table(
	IN table_name 	CHAR(100),
	IN id						INT UNSIGNED,
	IN item_key			CHAR(200),
	IN item_value		CHAR(200),
	IN indx					INT UNSIGNED 
)

	BEGIN

	IF ( id IS NOT NULL AND item_key IS NOT NULL ) THEN

		SET @working_id = 0;

		IF ( id = 0 ) THEN

			SET @id_query = CONCAT(
				"SELECT @working_id := id",
				" FROM ", table_name,
				" WHERE indx = 0",
				" LIMIT 1;"
			);

			PREPARE stmt FROM @id_query;
			EXECUTE stmt;
			DEALLOCATE PREPARE stmt;

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
