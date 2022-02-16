
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

DELIMITER ;
