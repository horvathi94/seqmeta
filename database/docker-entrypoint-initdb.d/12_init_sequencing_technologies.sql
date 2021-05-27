/* sequencing_platforms */
SET @table_name = "sequencing_platforms";
CALL create_basic_table(@table_name);


CREATE TABLE IF NOT EXISTS `sequencing_instruments` (
	id						INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	platform_id		INT UNSIGNED,
	label					CHAR(200) UNIQUE
);
