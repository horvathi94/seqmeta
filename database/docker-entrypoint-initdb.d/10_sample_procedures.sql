DELIMITER $$

CREATE PROCEDURE SelectSample(
	IN sid INT UNSIGNED
) 

BEGIN 

	SELECT 
		`sample`.`id` AS sample_id,
		`sample`.`name` AS sample_name,
		`sample`.`collection_date` AS collection_date,
		
		`agroup`.`id` AS author_group_id,
		`agroup`.`name` AS author_group_name,

		`originating_lab`.`id` AS originating_lab_id,
		`originating_lab`.`name` AS originating_lab_name,

		`submitting_lab`.`id` AS submitting_lab_id,
		`submitting_lab`.`name` AS submitting_lab_name

	FROM `sample_data` AS `sample`

	LEFT JOIN `author_groups` AS `agroup`
		ON `sample`.`author_group_id` = `agroup`.`id`

	LEFT JOIN `institutions` AS `originating_lab`
		ON `sample`.`originating_lab_id` = `originating_lab`.`id`

	LEFT JOIN `institutions` AS `submitting_lab`
		ON `sample`.`submitting_lab_id` = `submitting_lab`.`id`

	WHERE `sample`.`id` = sid;


END $$


DELIMITER ;
