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
	WHERE `as_in_g`.`order_index` > 0
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
		AND `as_in_g`.`order_index` > 0
	ORDER BY `group_id` ASC, `order_index` ASC;

END $$




CREATE PROCEDURE UpdateGroup(
	IN gid INT UNSIGNED,
	IN aid INT UNSIGNED,
	IN oindx INT UNSIGNED
)


BEGIN

	SET @id := 0;
	SELECT @id := id 
		FROM `authors_in_group` 
		WHERE `author_group_id` = gid
			AND `author_id` = aid;


	IF ( @id > 0 ) THEN

		UPDATE `authors_in_group`
			SET `order_index` = oindx
			WHERE id = @id;

	ELSE

		INSERT INTO `authors_in_group` 
			(author_group_id, author_id, order_index) 
			VALUES (gid, aid, oindx);

	END IF;


END $$



DELIMITER ;




DELIMITER $$

CREATE PROCEDURE UpsertGroupNames(
	IN gid INT UNSIGNED,
	IN gname CHAR(100),
	OUT groupInsertedID INT UNSIGNED
)


BEGIN 

	IF ( gid = 0 ) THEN

		INSERT INTO `author_groups` (name)
			VALUES (gname);
		SELECT LAST_INSERT_ID() INTO groupInsertedID;

	ELSE

		UPDATE `author_groups`
			SET `name` = gname
		WHERE `id` = gid;

		SELECT gid INTO groupInsertedID;

	END IF;

END $$

DELIMITER ;
