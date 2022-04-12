CREATE TABLE IF NOT EXISTS `templates` (

	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(200) NOT NULL UNIQUE,

	PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS `attributes` (

	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`general_name` VARCHAR(100) NOT NULL,
	`label` VARCHAR(100) NOT NULL,
	`template_id` INT UNSIGNED NOT NULL,
	`type_` VARCHAR(20) NOT NULL,
	`description` VARCHAR(500) DEFAULT NULL,
	`template` VARCHAR(200) DEFAULT NULL,
	`default` VARCHAR(200) DEFAULT NULL,
	`pattern` VARCHAR(200) DEFAULT NULL,
	`options` TEXT DEFAULT NULL,
	`ena_name` VARCHAR(200),
	`ena_requirement` VARCHAR(50),
	`gisaid_name` VARCHAR(200),
	`gisaid_requirement` VARCHAR(50),


	PRIMARY KEY (id),

	FOREIGN KEY (template_id)
		REFERENCES templates(id)
		ON DELETE CASCADE

);

/*
CREATE TABLE IF NOT EXISTS `options`(

	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`attribute_id` INT UNSIGNED NOT NULL,
	`option` VARCHAR(100) NOT NULL,

	PRIMARY KEY (id),

	FOREIGN KEY (attribute_id)
		REFERENCES attributes(id)
		ON DELETE CASCADE

);
*/
