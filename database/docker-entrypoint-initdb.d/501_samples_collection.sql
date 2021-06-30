CREATE TABLE IF NOT EXISTS `samples_collection` (

	sample_id							INT UNSIGNED NOT NULL PRIMARY KEY,
	year									SMALLINT UNSIGNED,
	month									TINYINT UNSIGNED,
	day										TINYINT UNSIGNED,
	collector_id					INT UNSIGNED,
	collection_device_id 	INT UNSIGNED

);


CREATE OR REPLACE VIEW `view_samples_collection` AS 

	SELECT 
	
		coll.sample_id AS sample_id,
		coll.year AS collection_year,
		coll.month AS collection_month,
		coll.day AS collection_day,
		CONCAT(coll.year,  
			IF (coll.month > 0 AND coll.month IS NOT NULL,
				CONCAT("-", LPAD(coll.month, 2, 0), 
					IF (coll.day > 0 AND coll.day IS NOT NULL,
						CONCAT("-", LPAD(coll.day, 2, 0) ), "" ) ), 
					"") ) AS collection_date,
		authors.abbreviated_middle_name AS collector_abbreviated_middle_name,
		coll_devices.label AS collection_device


		FROM samples_collection AS coll
		LEFT JOIN view_authors AS authors
			ON coll.collector_id = authors.id
		LEFT JOIN view_collection_devices AS coll_devices 
			ON coll_devices.id = coll.collection_device_id

