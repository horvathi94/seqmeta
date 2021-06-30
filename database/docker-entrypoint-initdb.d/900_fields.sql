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
	)
