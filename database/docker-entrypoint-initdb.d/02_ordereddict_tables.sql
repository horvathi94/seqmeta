/*

	                --- OrderedDict table ---


Stores an ordered list of dictionary like items, each has a key and a value.

Table structure: | id | item_key | item_value | indx |
Columns:
	- id:         INT UNSIGNED -> PRIMARY KEY
	- item_key:   VARCHAR(200) -> key of the item	
	- item_value: VARCHAR(500) -> value of the item
	- indx:       INT UNSIGNED -> order of the rows, if 0 the row is ommited.

Procedures:
	`create_ordereddict_table`
		-> Create an ordereddict table.
			+ table_name: IN VARCHAR(100) -> the name of the table to be created.

	`create_ordereddict_view`
		-> Create view of an ordereddict table.
			+ view_name: IN VARCHAR(100) -> the name of the view to be created
			                                            based on the table
			+ table_name: IN VARCHAR(100) -> the name of the table based on which
			                                            the view will be created

	`upsert_ordereddict_table`
		-> Insert or update data in an ordereddict table.
		If the IN id is not 0, then updates row with that `id`.
		If the IN id is 0 and then updates the row where `item_key` is the same
		as the IN item_key.
		If the IN id is 0 and the IN item_key is not found in the table, then a row
		with `indx` 0 is updated with the IN data, if no such row is found then a 
		new row is inserted.
			+ table_name: IN VARCHAR(100) -> the table to be updated
			+ id:         IN INT UNSIGNED -> the id of the row to be updated
			+ item_key:   IN VARCHAR(200) -> the item_key of the item to be added or 
			                                                              updated
			+ item_value: IN VARCHAR(500) -> the item_value of the item to be added 
			                                                              or updated
			+ indx:       IN INT UNSIGNED	-> the index of the item to be added


*/


DELIMITER $$ 

CREATE PROCEDURE create_ordereddict_table(
	IN table_name VARCHAR(100)
)

	BEGIN

		SET @create_query = CONCAT(
			"CREATE TABLE IF NOT EXISTS `", table_name, "`(",
				"id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,",
				"item_key VARCHAR(200) NOT NULL,",
				"item_value VARCHAR(500),",
				"indx INT UNSIGNED);"
		);

		PREPARE stmt FROM @create_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

	END $$


CREATE PROCEDURE create_ordereddict_view(
	IN view_name VARCHAR(100),
	IN table_name VARCHAR(100)
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
