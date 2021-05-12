DELIMITER $$


CREATE PROCEDURE ConcatAuthorsAndGroups()

BEGIN

	SELECT 
		`groups`.`id` AS group_id,
		`groups`.`name` AS group_name,
		`authors`.`id` AS author_id,
		`authors`.`first_name` AS first_name,
		`authors`.`middle_name` AS middle_name,
		`authors`.`last_name` AS last_name,
		`as_in_g`.`order_index` AS order_index
	FROM `author_groups` AS `groups`
	LEFT JOIN `authors_in_group` AS `as_in_g` 
		ON `groups`.`id` = `as_in_g`.`author_group_id`
	LEFT JOIN `authors`
		ON `as_in_g`.`author_id` = `authors`.`id`
	ORDER BY `group_id` ASC, `order_index` ASC;

END $$

DELIMITER ;





DELIMITER $$

CREATE PROCEDURE SelectGroup(
	IN gid INT UNSIGNED
)

BEGIN 

	SELECT 
		`groups`.`id` AS group_id,
		`groups`.`name` AS group_name,
		`authors`.`id` AS author_id,
		`authors`.`first_name` AS first_name,
		`authors`.`middle_name` AS middle_name,
		`authors`.`last_name` AS last_name,
		`as_in_g`.`order_index` AS order_index
	FROM `author_groups` AS `groups`
	LEFT JOIN `authors_in_group` AS `as_in_g` 
		ON `groups`.`id` = `as_in_g`.`author_group_id`
	LEFT JOIN `authors`
		ON `as_in_g`.`author_id` = `authors`.`id`
	WHERE `groups`.`id` = gid
	ORDER BY `group_id` ASC, `order_index` ASC;

END $$

DELIMITER ;
