/*
SELECT 
		GROUP_CONCAT(
			CONCAT(first_name, " ", 
					IF ( middle_name = "" OR middle_name IS NULL, "", CONCAT(LEFT(middle_name, 1), ".") ), 
					last_name)
			SEPARATOR ', ') AS authors
	FROM authors_in_group AS aig
	LEFT JOIN authors
		ON aig.author_id = authors.id
	WHERE author_group_id = 1
*/



	SELECT 
		`groups`.name AS group_name,
		COUNT(authors.id) AS members_count
		

	FROM author_groups as `groups`
	LEFT JOIN  authors_in_group AS `aig`
		ON aig.author_group_id = `groups`.id
	LEFT JOIN authors
		ON aig.author_id = authors.id
	GROUP BY `groups`.id
