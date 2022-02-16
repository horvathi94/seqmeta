
DELIMITER $$

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

DELIMITER ;
