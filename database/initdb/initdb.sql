CREATE TABLE IF NOT EXISTS `sample_data` (
	id									INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name								CHAR(100) NOT NULL,
	submission_date			DATE NOT NULL,
	collection_date			DATE NOT NULL,
	patient_age					TINYINT,
	patient_gender			BIT(1),
	originating_lab_id	INT UNSIGNED NOT NULL,
	submitting_lab_id		INT UNSIGNED NOT NULL,
	author_group_id			INT UNSIGNED NOT NULL,
	assembly_method			CHAR(100),
	PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `institutions` (
	id						INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name					CHAR(100),
	address				TEXT(200) NOT NULL,
	postal_code		MEDIUMINT UNSIGNED,
	county				CHAR(100),
	country				CHAR(100),
	city					CHAR(100),
	PRIMARY KEY(`id`)
);



/* --- Author tables --- */

CREATE TABLE IF NOT EXISTS `authors` (
	id 						INT UNSIGNED NOT NULL AUTO_INCREMENT,
	first_name		CHAR(100) NOT NULL,
	middle_name		CHAR(100),
	last_name			CHAR(100) NOT NULL,
	PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `author_groups` (
	id		INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name	CHAR(100),
	PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `authors_in_group` (
	id							INT UNSIGNED NOT NULL AUTO_INCREMENT,
	author_id				INT UNSIGNED,
	author_group_id	INT UNSIGNED,
	order_index			TINYINT UNSIGNED,
	PRIMARY KEY(`id`)
);




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

