CREATE VIEW `view_samples` AS

	SELECT 
		`sample`.`id` AS sample_id,
		`sample`.`name` AS sample_name,
		`sample`.`collection_date` AS collection_date,

		`sample`.`patient_age` AS patient_age,
		IF (`sample`.`patient_gender` = 1, "Male", "Female") ) AS patient_gender,
		`sample`.`patient_status` AS patient_status,
		CONCAT(`hosts`.`label`, "-", `hosts`.`latin`) AS host,

		`agroup`.`id` AS author_group_id,
		`agroup`.`name` AS author_group_name,

		`originating_lab`.`id` AS originating_lab_id,
		`originating_lab`.`name` AS originating_lab_name,

		`submitting_lab`.`id` AS submitting_lab_id,
		`submitting_lab`.`name` AS submitting_lab_name,

		`passage_details`.`label` AS passage_details,
		`sampling_startegies`.`label` AS sampling_strategy

	FROM `sample_data` AS `sample`

	LEFT JOIN `author_groups` AS `agroup`
		ON `sample`.`author_group_id` = `agroup`.`id`

	LEFT JOIN `institutions` AS `originating_lab`
		ON `sample`.`originating_lab_id` = `originating_lab`.`id`

	LEFT JOIN `institutions` AS `submitting_lab`
		ON `sample`.`submitting_lab_id` = `submitting_lab`.`id`

	LEFT JOIN `hosts`
		ON `sample`.`host_id` = `hosts`.`id`

	LEFT JOIN `passage_details` 
		ON `sample`.`passage_details_id` = `passage_details`.`id`

	LEFT JOIN `sampling_strategies`
		ON `sample`.`sampling_strategy_id` = `samplig_startegies`.`id`
