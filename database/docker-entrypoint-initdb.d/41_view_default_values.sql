CREATE OR REPLACE VIEW `view_default_values` AS 

	SELECT

		(SELECT 
			IF (`item_value` IS NULL, 0, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "continent_id"
		) AS continent_id,
		
		(SELECT 
			IF (`item_value` IS NULL, 0, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "country_id"
		) AS country_id,
		
		(SELECT 
			`item_value`
			FROM `default_values`
			WHERE `item_key` = "region"
		) AS region,
		
		(SELECT 
			`item_value`
			FROM `default_values`
			WHERE `item_key` = "locality"
		) AS locality,
		
		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS DECIMAL(5,2))) 
			FROM `default_values`
			WHERE `item_key` = "geo_loc_latitude"
		) AS geo_loc_latitude,

		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS DECIMAL(5,2))) 
			FROM `default_values`
			WHERE `item_key` = "geo_loc_longitude"
		) AS geo_loc_longitude
