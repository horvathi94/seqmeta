/* Table and view for holding institution data.
	Symbols are used in virusname and isolate templates.*/

CREATE TABLE IF NOT EXISTS `institutions` (
	id							INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name						CHAR(200),
	street_address	TEXT(200) NOT NULL,
	postal_code			MEDIUMINT UNSIGNED,
	country_id			INT UNSIGNED,
	region					CHAR(100),
	locality				CHAR(100),
	symbol					VARCHAR(20)
);


CREATE OR REPLACE VIEW view_institutions AS

	SELECT 
		institutions.id AS id,
		name,
		CONCAT(street_address, ", ",
						locality, " ",
						postal_code, ", ",
						region, ", ",
						countries.label
					) AS address,
		symbol AS symbol
		FROM institutions
		LEFT JOIN view_countries AS countries
			ON institutions.country_id = countries.id;
