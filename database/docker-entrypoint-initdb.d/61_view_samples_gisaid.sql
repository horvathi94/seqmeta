CREATE VIEW `view_samples_for_gisaid` AS

	SELECT 
		
		sample.id AS sample_id,

		passage_details.label AS passage_details,
		sample.collection_date AS collection_date,
		sample.location AS location,
		sample.additional_location_info AS additional_location_info,
		hosts.label AS host,
		sample.additional_host_info AS additional_host_info,
		sampling_strategies.label AS sampling_strategy,
		IF (sample.patient_gender = "" OR sample.patient_gender IS NULL, "unknown",
			IF (sample.patient_gender = 1, "Male", "Female")) AS patient_gender,
		sample.patient_age AS patient_age,
		sample.patient_status AS patient_status,
		sequencing_technologies.label AS sequencing_technology,
		assembly_methods.label AS assembly_method,
		CONCAT(sample.coverage, "x") AS coverage,
		originating_lab.name AS originating_lab_name,
		originating_lab.address AS originating_lab_address,
		submitting_lab.name AS submitting_lab_name,
		submitting_lab.address AS submitting_lab_address,

		sample.specimen_source AS specimen_source,
		sample.outbreak AS outbreak,
		sample.last_vaccinated AS last_vaccinated,
		sample.treatment AS treatment,

		sample.name AS sample_name,
		`groups`.abbreviated_middle_names AS authors_list


		FROM sample_data AS sample
		LEFT JOIN view_institutions AS originating_lab
			ON sample.originating_lab_id = originating_lab.id
		LEFT JOIN view_institutions AS submitting_lab
			ON sample.submitting_lab_id = submitting_lab.id
		LEFT JOIN view_authors_in_groups_condensed AS `groups`
			ON sample.author_group_id = `groups`.`group_id`
		LEFT JOIN view_hosts AS hosts
			ON sample.host_id = hosts.id
		LEFT JOIN passage_details
			ON sample.passage_details_id = passage_details.id
		LEFT JOIN sampling_strategies
			ON sample.sampling_strategy_id = sampling_strategies.id
		LEFT JOIN sequencing_technologies
			ON sample.sequencing_technology_id = sequencing_technologies.id
		LEFT JOIN assembly_methods
			ON sample.assembly_method_id = assembly_methods.id;


