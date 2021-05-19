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
