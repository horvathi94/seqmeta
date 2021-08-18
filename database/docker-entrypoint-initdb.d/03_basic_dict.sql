/*

	                --- Dict table ---


Stores a list of dictionary like items, each has a key and a value.

Table structure: | id | item_key | item_value |
Columns:
	- id:         INT UNSIGNED -> PRIMARY KEY
	- item_key:   VARCHAR(200) -> key of the item	
	- item_value: VARCHAR(500) -> value of the item

Procedures:
	`create_dict_table`
		-> Create a dict table.
			+ table_name: IN VARCHAR(100) -> the name of the table to be created.


	`upsert_dict_table`
		-> Insert or update data in a dict table.
		If the IN id is not 0, then updates row with that `id`.
		If the IN id is 0 and then updates the row where `item_key` is the same
		as the IN item_key.
		If the IN id is 0 and the IN item_key is not found in the table, then a 
		new row is inserted.
			+ table_name: IN VARCHAR(100) -> the table to be updated
			+ id:         IN INT UNSIGNED -> the id of the row to be updated
			+ item_key:   IN VARCHAR(200) -> the item_key of the item to be added or 
			                                                              updated
			+ item_value: IN VARCHAR(500) -> the item_value of the item to be added 
			                                                              or updated

*/



DELIMITER $$

CREATE PROCEDURE create_dict_table(
	IN table_name VARCHAR(100)
)

	BEGIN 

		SET @create_query = CONCAT(
			"CREATE TABLE IF NOT EXISTS `", table_name, "`(",
				"id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,",
				"item_key VARCHAR(200) NOT NULL UNIQUE,",
				"item_value VARCHAR(1000) );"
		);

		PREPARE stmt FROM @create_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

	END $$



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
