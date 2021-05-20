CREATE VIEW view_samples_display AS 

	SELECT 
		samples.id AS sample_id,
		samples.name AS sample_name,
		DATE_FORMAT(samples.collection_date, "%Y-%m-%d") AS collection_date,
		
		`groups`.group_name AS group_name,
		`groups`.full_names AS full_names,
		`groups`.abbreviated_middle_names AS abbreviated_middle_names

	FROM samples
	LEFT JOIN view_authors_in_groups_condensed AS `groups`
		ON samples.author_group_id = `groups`.`group_id`;
