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
	IN label				CHAR(200),
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

