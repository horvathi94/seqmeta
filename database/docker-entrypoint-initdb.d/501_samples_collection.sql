CREATE TABLE IF NOT EXISTS `samples_collection` (

	sample_id															INT UNSIGNED NOT NULL PRIMARY KEY,
	collection_year												SMALLINT UNSIGNED,
	collection_month											TINYINT UNSIGNED,
	collection_day												TINYINT UNSIGNED,
	collector_id													INT UNSIGNED,
	collection_device_id									INT UNSIGNED,
	originating_lab_id										INT UNSIGNED,
	originating_lab_sample_name						CHAR(200),
	submitting_lab_id											INT UNSIGNED,
	submitting_lab_sample_name						CHAR(200),
	author_group_id												INT UNSIGNED

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
		coll_devices.label AS collection_device,
		
		originating_lab.name AS originating_lab_name,
		originating_lab.address AS originating_lab_address,
		coll.originating_lab_sample_name AS originating_lab_sample_name,
		submitting_lab.name AS submitting_lab_name,
		submitting_lab.address AS submitting_lab_address,
		coll.submitting_lab_sample_name AS submitting_lab_sample_name,
		author_groups.group_name AS author_group_name,
		author_groups.abbreviated_middle_names AS authors_list


		FROM samples_collection AS coll
		LEFT JOIN view_authors AS authors
			ON coll.collector_id = authors.id
		LEFT JOIN view_collection_devices AS coll_devices 
			ON coll_devices.id = coll.collection_device_id
		LEFT JOIN view_institutions AS originating_lab
			ON coll.originating_lab_id = originating_lab.id
		LEFT JOIN view_institutions AS submitting_lab
			ON coll.submitting_lab_id = submitting_lab.id
		LEFT JOIN view_authors_in_groups_condensed AS author_groups
			ON coll.author_group_id = author_groups.`group_id`

