DROP TABLE IF EXISTS fields;

CREATE TABLE IF NOT EXISTS fields (

	handle				VARCHAR(100) NOT NULL PRIMARY KEY,

	field_name		VARCHAR(200),
	field_type		VARCHAR(100),
	gisaid				TINYINT UNSIGNED,
	ena						TINYINT UNSIGNED,
	ncbi					TINYINT UNSIGNED,
	
	name					VARCHAR(100),
	class					VARCHAR(100),
	min_val				INT,
	max_val				INT,
	step					DECIMAL(5,3),

	prefix				VARCHAR(100),

	description		VARCHAR(2000)

);


INSERT INTO fields 
	(	`handle`,
		`field_name`, `field_type`, `gisaid`, `ena`, `ncbi`,
		`name`, `class`, `min_val`, `max_val`, `step`,
		`prefix`, 
		`description`)
	VALUES

	/* --- Basic sample data --- */
	
	("sample_name",
		"Sample name", "text", NULL, NULL, NULL,
		"sample_name", "sample-name", 0, 200, NULL,
		"sample",
		"Name of the sequenced files. Use this to keep track of your samples in the database."
	),
	("sample_comment",
		"Sample comment", "text", NULL, NULL, NULL,
		"sample_comment", "sample-comment", 0, 200, NULL,
		"sample",
		"A comment to more easily identify the sample. This will not be used for any of the uploads."
	),
	("sample_title",
		"Sample title", "text", NULL, 3, NULL,
		"sample_title", "sample-title", 0, 200, NULL,
		"sample",
		"A title for the sample."
	),
	("sample_description",
		"Sample description", "text", NULL, 2, NULL,
		"sample_description", "sample-description", 0, 200, 1,
		"sample",
		"A short description of the sample."
	),

	/* --- Collection data --- */
	("collection_year",
		"Collection year", "number", 3, 2, NULL,
		"year", "collection-year", 2019, NULL, 1,
		"collection",
		"Collection date of the sample."
	),
	("collection_month",
		"Collection month", "number", 3, 2, NULL,
		"month", "collection-month", 0, 12, 1,
		"collection",
		"Collection date of the sample."
	),
	("collection_day",
		"Collection day", "number", 3, 2, NULL,
		"day", "collection-day", 0, 31, 1,
		"collection",
		"Collection date of the sample."
	),
	("collector_name",
		"Collector name", "select", NULL, 3, NULL,
		"collector_id", "collector-name", NULL, NULL, NULL,
		"collection",
		"Person who collected the sample."
	),


	/* --- Location data --- */
	("location_continent",
		"Continent", "select", 3, NULL, NULL,
		"continent_id", "continent", NULL, NULL, NULL,
		"location",
		"The geographical location of the sample as defined by the continent."
	),
	("location_country",
		"Country", "select", 3, NULL, NULL,
		"country_id", "country", NULL, NULL, NULL,
		"location",
		"The geographical origin of the sample as defined by the country or sea. 
ntry or sea names should be chosen from the <a target='_blank' href='http://insdc.org/country.html'>INSDC country list</a>"
	),
	("location_region",
		"Region", "text", 1, 2, NULL,
		"region", "region", NULL, 200, NULL,
		"location",
		"The geographical location of the sample as defined by the region."
	),
	("location_locality",
		"Locality", "text", 1, 2, NULL,
		"locality", "locality", NULL, 200, NULL,
		"location",
		"The geographical location of the sample as defined by the locality."
	),
	("location_additional_info",
		"Additional location informatio", "text", 1, NULL, NULL,
		"additional_info", "location-additional-info", NULL, 1000, NULL,
		"location",
		"<em> e.g. Cruise ship, Convention, Live animal market </em>"
	),
	("geo_loc_latitude",
		"Geographic location (latitude) (DD)", "number", NULL, 2, NULL,
		"geo_loc_latitude", "geo-loc-latitude", -90, 90, 0.01,
		"location",
		"The geographical origin of the sample as defined by the latitude. Minimum value: -90 and maximum value: 90."
	),
	("geo_loc_longitude",
		"Geographic location (longitude) (DD)", "number", NULL, 2, NULL,
		"geo_loc_longitude", "geo-loc-longitude", -180, 180, 0.01,
		"location",
		"The geographical origin of the sample as defined by the longitude. Minimum value: -180 and maximum value: 180."
	)


;
