CREATE OR REPLACE VIEW `view_default_values` AS 

	SELECT

		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "continent_id"
		) AS continent_id,
		
		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "country_id"
		) AS country_id,
		
		(SELECT 
			IF (`item_value` IS NULL, NULL, `item_value`)
			FROM `default_values`
			WHERE `item_key` = "region"
		) AS region,
		
		(SELECT 
			IF (`item_value` IS NULL, NULL, `item_value`)
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
		) AS geo_loc_longitude,
		
		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "host_id"
		) AS host_id,
		
		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "patient_status_id"
		) AS patient_status_id,
		
		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "sampling_strategy_id"
		) AS sampling_strategy_id,
		
		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "passage_details_id"
		) AS passage_details_id,

		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "assembly_method_id"
		) AS assembly_method_id,

		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "sequencing_instrument_id"
		) AS sequencing_instrument_id,
		
		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "specimen_source_id"
		) AS specimen_source_id,
		
		(SELECT 
			IF (`item_value` IS NULL, NULL, CAST(`item_value` AS UNSIGNED)) 
			FROM `default_values`
			WHERE `item_key` = "sample_capture_status_id"
		) AS sample_capture_status_id

