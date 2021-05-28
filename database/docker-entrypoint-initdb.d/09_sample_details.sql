CREATE TABLE IF NOT EXISTS `samples_library` (
	
	id 											INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	lib_id									VARCHAR(200) UNIQUE,
	layout_paired						BIT(1),					
	strategy_id							SMALLINT UNSIGNED,
	source_id								SMALLINT UNSIGNED,
	selection_id						SMALLINT UNSIGNED,
	design_description 			VARCHAR(1000)

);


CREATE TABLE IF NOT EXISTS `samples_collection` (

	id								INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	year							SMALLINT UNSIGNED NOT NULL,
	month							TINYINT UNSIGNED,
	day								TINYINT UNSIGNED,
	collector_id			INT UNSIGNED

);


CREATE TABLE IF NOT EXISTS `samples_location` (

	id 									INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	continent_id				TINYINT UNSIGNED,
	country_id					SMALLINT UNSIGNED,
	region							VARCHAR(150),
	locality						VARCHAR(150),
	additional_info			VARCHAR(1000),
	geo_loc_latitude		DECIMAL(5,3),
	geo_loc_longitude		DECIMAL(5,3)

);
