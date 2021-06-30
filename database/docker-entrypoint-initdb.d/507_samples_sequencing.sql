CREATE TABLE IF NOT EXISTS `samples_sequencing` (

	sample_id											INT UNSIGNED NOT NULL PRIMARY KEY,
	sequencing_instrument_id			INT UNSIGNED,
	assembly_method_id						INT UNSIGNED,
	coverage											MEDIUMINT UNSIGNED

);


CREATE OR REPLACE VIEW view_samples_sequencing AS 

	SELECT 

		sequencing.sample_id AS sample_id,
		instruments.label AS sequencing_instrument,
		platforms.label AS sequencing_platform,
		assembly.label AS assembly_method,
		sequencing.coverage AS coverage,
		IF (sequencing.coverage IS NULL, "",
			CONCAT(sequencing.coverage, "x")) AS coverage_x

	FROM samples_sequencing AS sequencing
	LEFT JOIN assembly_methods AS assembly
		ON sequencing.assembly_method_id = assembly.id
	LEFT JOIN sequencing_instruments AS instruments
		ON sequencing.sequencing_instrument_id = instruments.id
	LEFT JOIN sequencing_platforms AS platforms
		ON instruments.platform_id = platforms.id;
	
	
