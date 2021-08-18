/* Information about the sequencing of the samples.
 Is linked to the `samples` table trough the `sample_id` column. */


CREATE TABLE IF NOT EXISTS `samples_sequencing` (

	sample_id INT UNSIGNED NOT NULL PRIMARY KEY,
	sequencing_instrument_id INT UNSIGNED,
	assembly_method_id INT UNSIGNED,
	coverage MEDIUMINT UNSIGNED,
	sequencing_lab_id INT UNSIGNED

);


CREATE OR REPLACE VIEW view_samples_sequencing AS 

	SELECT 

		sequencing.sample_id AS sample_id,
		instruments.label AS sequencing_instrument,
		platforms.label AS sequencing_platform,
		assembly.label AS assembly_method,
		sequencing.coverage AS coverage,
		IF (sequencing.coverage IS NULL, "",
			CONCAT(sequencing.coverage, "x")) AS coverage_x,
		sequencing_lab.name AS sequencing_lab_name,
		sequencing_lab.address AS sequencing_lab_address

	FROM samples_sequencing AS sequencing
	LEFT JOIN assembly_methods AS assembly
		ON sequencing.assembly_method_id = assembly.id
	LEFT JOIN sequencing_instruments AS instruments
		ON sequencing.sequencing_instrument_id = instruments.id
	LEFT JOIN sequencing_platforms AS platforms
		ON instruments.platform_id = platforms.id
	LEFT JOIN view_institutions AS sequencing_lab
		ON sequencing.sequencing_lab_id = sequencing_lab.id;
	
