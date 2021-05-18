CREATE VIEW view_authors AS

	SELECT 
		id,
		first_name,
		middle_name,
		last_name,
		CONCAT(first_name, " ",
				IF(middle_name = "" OR middle_name IS NULL, "", CONCAT(middle_name, " ")),
				last_name) AS full_name,

		CONCAT(first_name, " ",
				IF(middle_name = "" OR middle_name IS NULL, "", CONCAT(LEFT(middle_name, 1), ". ")),
				last_name) AS abbreviated_middle_name

		FROM `authors`;

