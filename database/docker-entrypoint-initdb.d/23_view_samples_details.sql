CREATE VIEW view_samples_details AS

	SELECT 
		samples.id AS sample_id,
		samples.name AS sample_name,
		DATE_FORMAT(samples.collection_date, "%Y-%m-%d") AS collection_date,

		hosts.display_label AS host,
		samples.additional_host_info AS additional_host_info,
		samples.patient_age AS patient_age,
		IF (samples.patient_gender = "" OR samples.patient_gender IS NULL, "unknown", 
			IF (samples.patient_gender = 1, "Male", "Female")
		) AS patient_gender,
		patient_statuses.label AS patient_status,

		samples.location AS location,
		samples.additional_location_info AS additional_location_info,
		originating_lab.name AS originating_lab_name,
		samples.originating_lab_sample_name AS originating_lab_sample_name,
		submitting_lab.name AS submitting_lab_name,
		samples.submitting_lab_sample_name AS submitting_lab_sample_name,
		`groups`.group_name AS author_group_name,
		`groups`.abbreviated_middle_names AS authors_list,

		passage_details.label AS passage_details,
		sampling_strategies.label AS sampling_strategy,
		sequencing_technologies.label AS sequencing_technology,
		assembly_methods.label AS assembly_method,
		CONCAT(samples.coverage, "x") AS coverage,

		samples.specimen_source AS specimen_source,
		samples.outbreak AS outbreak,
		samples.last_vaccinated AS last_vaccinated,
		samples.treatment AS treatment


	FROM samples
	LEFT JOIN view_hosts AS hosts
		ON samples.host_id = hosts.id
	LEFT JOIN patient_statuses
		ON samples.patient_status_id = patient_statuses.id
	LEFT JOIN view_institutions AS originating_lab
		ON samples.originating_lab_id = originating_lab.id
	LEFT JOIN view_institutions AS submitting_lab
		ON samples.submitting_lab_id = submitting_lab.id
	LEFT JOIN view_authors_in_groups_condensed AS `groups`
		ON samples.author_group_id = `groups`.`group_id`
	LEFT JOIN passage_details
		ON samples.passage_details_id = passage_details.id
	LEFT JOIN sampling_strategies
		ON samples.sampling_strategy_id = sampling_strategies.id	
	LEFT JOIN sequencing_technologies
		ON samples.sequencing_technology_id = sequencing_technologies.id
	LEFT JOIN assembly_methods
		ON samples.assembly_method_id = assembly_methods.id
