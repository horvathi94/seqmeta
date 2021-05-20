CREATE TABLE IF NOT EXISTS `authors` (
	id						INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	first_name		CHAR(150),
	middle_name		CHAR(150),
	last_name			CHAR(150)
);


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





CREATE TABLE IF NOT EXISTS `author_groups` (
	id 			INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name		CHAR(200)
);


CREATE TABLE IF NOT EXISTS `authors_in_group` (
	id							INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	author_id				INT UNSIGNED NOT NULL,
	author_group_id	INT UNSIGNED NOT NULL,
	order_index			INT UNSIGNED
);


CREATE VIEW view_authors_in_groups AS

		SELECT 
			`groups`.id AS `group_id`,
			`groups`.name AS group_name,
			authors.id AS author_id,
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
		WHERE order_index > 0
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


DELIMITER $$

CREATE PROCEDURE upsert_authors_in_group(
	IN gid 		INT UNSIGNED,
	IN aid 		INT UNSIGNED,
	IN oindx 	INT UNSIGNED
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



CREATE PROCEDURE upsert_group(
	IN 	gid INT UNSIGNED,
	IN 	gname CHAR(200),
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
