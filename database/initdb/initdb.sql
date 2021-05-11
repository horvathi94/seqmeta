CREATE TABLE IF NOT EXISTS `sample_data` (
	id								INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name							CHAR(100) NOT NULL,
	submission_date		DATE NOT NULL,
	PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `institutions` (
	id						INT UNSIGNED NOT NULL AUTO_INCREMENT,
	address				TEXT(200) NOT NULL,
	postal_code		MEDIUMINT UNSIGNED,
	county				CHAR(100),
	country				CHAR(100),
	PRIMARY KEY(`id`)
);


CREATE TABLE IF NOT EXISTS `authors` (
	id 						INT UNSIGNED NOT NULL AUTO_INCREMENT,
	first_name		CHAR(100) NOT NULL,
	middle_name		CHAR(100),
	last_name			CHAR(100) NOT NULL,
	PRIMARY KEY(`id`)
);
