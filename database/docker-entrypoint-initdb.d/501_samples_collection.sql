CREATE TABLE IF NOT EXISTS `samples_collection` (

	sample_id							INT UNSIGNED NOT NULL PRIMARY KEY,
	collection_year				SMALLINT UNSIGNED,
	collection_month			TINYINT UNSIGNED,
	collection_day				TINYINT UNSIGNED,
	collector_id					INT UNSIGNED,
	collection_device_id 	INT UNSIGNED

);


CREATE OR REPLACE VIEW `view_samples_collection` AS 

	SELECT 
	
		coll.sample_id AS sample_id,
		coll.collection_year AS collection_year,
		coll.collection_month AS collection_month,
		coll.collection_day AS collection_day,
		CONCAT(coll.collection_year,  
			IF (coll.collection_month > 0 AND coll.collection_month IS NOT NULL,
				CONCAT("-", LPAD(coll.collection_month, 2, 0), 
					IF (coll.collection_day > 0 AND coll.collection_day IS NOT NULL,
						CONCAT("-", LPAD(coll.collection_day, 2, 0) ), "" ) ), 
					"") ) AS collection_date,
		authors.abbreviated_middle_name AS collector_abbreviated_middle_name,
		coll_devices.label AS collection_device


		FROM samples_collection AS coll
		LEFT JOIN view_authors AS authors
			ON coll.collector_id = authors.id
		LEFT JOIN view_collection_devices AS coll_devices 
			ON coll_devices.id = coll.collection_device_id

