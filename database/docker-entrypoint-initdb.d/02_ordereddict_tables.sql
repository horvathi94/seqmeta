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

/*
CREATE PROCEDURE upsert_ordereddict_table(
	IN table_name 	CHAR(100),
	IN label				CHAR(200),
	IN indx					INT UNSIGNED
)

	BEGIN
	
		IF ( key <> "" AND key IS NOT NULL ) THEN


			IF



			PREPARE stmt FROM @query;
			EXECUTE stmt;
			DEALLOCATE PREPARE stmt;

		END IF;

	END $$




*/

DELIMITER ;
