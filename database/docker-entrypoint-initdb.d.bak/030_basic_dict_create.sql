
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

DELIMITER ;
