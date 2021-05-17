CREATE TABLE IF NOT EXISTS `sample_data` (
	id									INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name								CHAR(100) NOT NULL,
	submission_date			DATE NOT NULL,
	collection_date			DATE NOT NULL,
	patient_age					TINYINT,
	patient_gender			BIT(1) NOT NULL,
	patient_status			CHAR(100),
	originating_lab_id	INT UNSIGNED NOT NULL,
	submitting_lab_id		INT UNSIGNED NOT NULL,
	author_group_id			INT UNSIGNED NOT NULL,

	host_id								MEDIUMINT UNSIGNED NOT NULL,
	sampling_strategy_id	MEDIUMINT UNSIGNED,
	passage_details_id		MEDIUMINT UNSIGNED NOT NULL,
	location 							TEXT,
	additional_location_info 	TEXT,
	additional_host_info			TEXT,

	coverage									SMALLINT UNSIGNED,
	sequencing_technology_id 	MEDIUMINT UNSIGNED,
	assembly_method_id				MEDIUMINT UNSIGNED,

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



/* --- Sample extra data tables --- */

CREATE TABLE IF NOT EXISTS `hosts` (
	id			MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	label		CHAR(100),
	latin		CHAR(100)
);

CREATE TABLE IF NOT EXISTS `passage_details` (
	id			MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	label		CHAR(100)
);

CREATE TABLE IF NOT EXISTS `sampling_strategies` (
	id			MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	label		TEXT
);

CREATE TABLE IF NOT EXISTS `sequencing_technologies` (
	id			MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	label		TEXT
);

CREATE TABLE IF NOT EXISTS `assembly_methods` (
	id			MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	label		TEXT
);




