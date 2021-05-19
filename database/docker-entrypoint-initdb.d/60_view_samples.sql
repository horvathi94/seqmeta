CREATE VIEW view_samples_list_display AS

	SELECT
			sample.id AS sample_id,
			sample.name AS sample_name,
			sample.collection_date AS collection_date,
		
			`groups`.group_name AS group_name,
			`groups`.full_names AS full_names,
			`groups`.abbreviated_middle_names AS abbreviated_middle_names

		FROM `sample_data` AS sample
		LEFT JOIN `view_authors_in_groups_condensed` AS `groups`
			ON sample.author_group_id = `groups`.`group_id`;


CREATE VIEW view_samples_details AS 

	SELECT 
		sample.id AS sample_id,
		sample.name AS sample_name,
		sample.collection_date AS collection_date,

		originating_lab.name AS originating_lab_name,
		submitting_lab.name AS submitting_lab_name,
		`groups`.group_name AS author_group_name,
		`groups`.abbreviated_middle_names AS authors_list,
		sample.location AS location,
		sample.additional_location_info AS additional_location_info,

		hosts.display_label AS host,
		sample.additional_host_info AS additional_host_info,
		sample.patient_age AS patient_age,
		IF (`sample`.`patient_gender` = 1, "Male", "Female") AS patient_gender,
		sample.patient_status AS patient_status,

		passage_details.label AS passage_details,
		sampling_strategies.label AS sampling_strategy,
		sequencing_technologies.label AS sequencing_technology,
		assembly_methods.label AS assembly_method,
		CONCAT(sample.coverage, "x") AS coverage

		FROM sample_data AS sample
		LEFT JOIN institutions AS originating_lab
			ON sample.originating_lab_id = originating_lab.id
		LEFT JOIN institutions AS submitting_lab
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


