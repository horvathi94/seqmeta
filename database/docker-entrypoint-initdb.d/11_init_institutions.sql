CREATE TABLE IF NOT EXISTS `institutions` (
	id							INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name						CHAR(200),
	street_address	TEXT(200) NOT NULL,
	postal_code			MEDIUMINT UNSIGNED,
	county					CHAR(100),
	country					CHAR(100),
	city						CHAR(100)
);


CREATE VIEW view_institutions AS

	SELECT 
		id,
		name,
		CONCAT(street_address, ", ",
						city, " ",
						postal_code, ", ",
						county, ", ",
						country
					) AS address
		FROM institutions;
