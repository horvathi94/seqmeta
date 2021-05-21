CREATE VIEW view_samples_display AS 

	SELECT 
		samples.id AS sample_id,
		samples.name AS sample_name,
		CONCAT(samples.collection_year,  
			IF (samples.collection_month > 0 AND samples.collection_month IS NOT NULL,
				CONCAT("-", LPAD(samples.collection_month, 2, 0), 
					IF (samples.collection_day > 0 AND samples.collection_day IS NOT NULL,
						CONCAT("-", LPAD(samples.collection_day, 2, 0) ), "" ) ), 
					"") ) AS collection_date,
		
		`groups`.group_name AS group_name,
		`groups`.full_names AS full_names,
		`groups`.abbreviated_middle_names AS abbreviated_middle_names

	FROM samples
	LEFT JOIN view_authors_in_groups_condensed AS `groups`
		ON samples.author_group_id = `groups`.`group_id`;
