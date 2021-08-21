
DELIMITER $$

CREATE PROCEDURE create_basic_view(
	IN view_name VARCHAR(100),
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

DELIMITER ;
