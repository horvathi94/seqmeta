CREATE VIEW view_authors_in_groups AS

		SELECT 
			`groups`.id AS `group_id`,
			`groups`.name AS group_name,
			first_name,
			middle_name,
			last_name,
			full_name,
			abbreviated_middle_name,
			order_index

		FROM author_groups as `groups`
		LEFT JOIN  authors_in_group AS `aig`
			ON aig.author_group_id = `groups`.id
		LEFT JOIN view_authors AS authors
			ON aig.author_id = authors.id
		ORDER BY `group_id` ASC, order_index ASC;



CREATE VIEW view_authors_in_groups_condensed AS 

	SELECT 
		
		`group_id`,
		group_name,
		COUNT(`group_id`) AS members_count,
		GROUP_CONCAT(full_name 
				ORDER BY order_index 
				SEPARATOR ", ") AS full_names,
		GROUP_CONCAT(abbreviated_middle_name 
				ORDER BY order_index
				SEPARATOR ", ") AS abbreviated_middle_names	

		FROM view_authors_in_groups
		GROUP BY `group_id`;
