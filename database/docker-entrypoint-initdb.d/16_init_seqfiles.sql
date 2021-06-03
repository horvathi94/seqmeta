CREATE TABLE IF NOT EXISTS `seqfiles` (

	id 								INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	sample_id					INT UNSIGNED NOT NULL,
	file_type					VARCHAR(10),
	is_assembly				BIT(1),
	is_forward_read		BIT(1)

);


CREATE OR REPLACE VIEW `view_seqfiles` AS 

	SELECT 

		sample_id,
		file_type,
		is_assembly,
		is_forward_read,
		IF (is_assembly IS TRUE, 
			CONCAT(samples.name, ".", file_type),
			)filename
	
	FROM seqfiles
	LEFT JOIN samples 
		ON samples.id = seqfiles.sample_id
