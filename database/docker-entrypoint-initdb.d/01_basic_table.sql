/*  
		
	                         --- Basic table ---


Stores a list of VARCHAR values.

Table structure: | id | label | indx |
Columns:
	- id: 		INT UNSIGNED -> PRIMARY KEY
	- label: 	VARCHAR(200) -> holds data
	- indx:		INT UNSIGNED -> order of the rows, if 0 the row is ommited.

Procedures:
	`create_basic_table`
		-> Creates a basic table.
			+ table_name: IN VARCHAR(100) -> the name of the table to be created

	`create_basic_view` 
		-> Create view of a basic table.
			+ view_name: IN VARCHAR(100) -> the name of the view to be created
			                                             based on the table
			+ table_name: IN VARCHAR(100) -> the name of the table based on which
			                                             the view will be created
	
	`upsert_basic_table` 
		-> Insert or update data in a basic table.
		Updates the row where label is matched, if the label is not found in
		the table then it is inserted.
			+ table_name: IN VARCHAR(100) -> the table to be updated
			+ label:			IN VARCHAR(100) -> the label to be added or updated
			+ indx: 			IN INT UNSIGNED	-> the index of the item to be added

*/

DELIMITER $$


CREATE PROCEDURE create_basic_table(
	IN table_name	VARCHAR(100)
)

	BEGIN 

		SET @create_query = CONCAT(
			"CREATE TABLE IF NOT EXISTS `", table_name, "`(",
			"id			INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, ",
			"label	VARCHAR(200) UNIQUE, ",
			"indx		INT UNSIGNED );"
		);

		PREPARE stmt FROM @create_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

	END $$



CREATE PROCEDURE create_basic_view(
	IN view_name 	VARCHAR(100),
	IN table_name VARCHAR(100)
)

	BEGIN 

		SET @view_query = CONCAT(
			"CREATE OR REPLACE VIEW ", 
			view_name, " AS ",
			"SELECT id, label, indx FROM ",
			table_name,
			" WHERE indx <> 0",
			" ORDER BY indx ASC, label ASC;"
		);

		PREPARE stmt FROM @view_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;


	END $$


CREATE PROCEDURE upsert_basic_table(
	IN table_name 	VARCHAR(100),
	IN label				VARCHAR(200),
	IN indx					INT UNSIGNED
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

