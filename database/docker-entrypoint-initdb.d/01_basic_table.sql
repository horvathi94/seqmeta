DELIMITER $$

CREATE PROCEDURE create_basic_table(
	IN table_name	CHAR(100)
)

	BEGIN 

		SET @create_query = CONCAT(
			"CREATE TABLE IF NOT EXISTS `", table_name, "`(",
			"id			INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, ",
			"label	CHAR(200) UNIQUE, ",
			"indx		INT UNSIGNED );"
		);

		PREPARE stmt FROM @create_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

	END $$



CREATE PROCEDURE create_basic_view(
	IN view_name 	CHAR(100),
	IN table_name CHAR(100)
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
	IN table_name 	CHAR(100),
	IN id 					INT UNSIGNED,
	IN label				CHAR(200),
	IN indx					INT UNSIGNED
)

	BEGIN

		IF ( label <> "" AND label IS NOT NULL ) THEN

			SET @query = "";
			SET @select_id = 0;

			IF (id = "" OR id = 0 OR id IS NULL) THEN
				SET @id_query = CONCAT(
					"SELECT @select_id := id",
					" FROM ", table_name,
					" WHERE label = \'", label, "\';"
				);

				PREPARE stmt FROM @id_query;
				EXECUTE stmt;
				DEALLOCATE PREPARE stmt;
		
			ELSE 
				
				SET @select_id = id;

			END IF;


			IF (@select_id = 0) THEN

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
					" WHERE id = ", @select_id, ";"
				);

			END IF;

			PREPARE stmt FROM @query;
			EXECUTE stmt;
			DEALLOCATE PREPARE stmt;

		END IF;

	END $$


DELIMITER ;

