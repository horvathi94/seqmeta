CREATE TABLE IF NOT EXISTS samples (

	id									INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name								CHAR(200) UNIQUE NOT NULL

/*
	link_library_id 		INT UNSIGNED,
	link_collection_id	INT UNSIGNED,
	link_location_id		INT UNSIGNED,
	link_host_id				INT UNSIGNED,
	link_sampling_id		INT UNSIGNED,
	link_sequencing_id	INT UNSIGNED
*/
);
