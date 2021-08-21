
DELIMITER $
CREATE PROCEDURE create_basic_table(
	IN table_name	VARCHAR(100)
)

BEGIN

	SET @create_query = CONCAT(
		"CREATE TABLE IF NOT EXISTS `", table_name, "`(",
			"id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, ",
			"label VARCHAR(200) UNIQUE, ",
			"indx INT UNSIGNED );"
		);

		PREPARE stmt FROM @create_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

END $$
DELIMITER ;
