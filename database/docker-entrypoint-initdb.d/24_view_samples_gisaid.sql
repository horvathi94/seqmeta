CREATE VIEW view_samples_gisaid AS

	SELECT 
		samples.id AS sample_id,
		samples.name AS sample_name,
		CONCAT(samples.collection_year,  
			IF (samples.collection_month > 0 AND samples.collection_month IS NOT NULL,
				CONCAT("-", LPAD(samples.collection_month, 2, 0), 
					IF (samples.collection_day > 0 AND samples.collection_day IS NOT NULL,
						CONCAT("-", LPAD(samples.collection_day, 2, 0) ), "" ) ), 
					"") ) AS collection_date,

		samples.collection_year AS collection_year,
		LPAD(samples.collection_month, 2, 0) AS collection_month,
		LPAD(samples.collection_day, 2, 0) AS collection_day,

		hosts.label AS host,
		samples.additional_host_info AS additional_host_info,
		samples.patient_age AS patient_age,
		IF (samples.patient_gender = "" OR samples.patient_gender IS NULL, "unknown", 
			IF (samples.patient_gender = 1, "Male", "Female")
		) AS patient_gender,
		patient_statuses.label AS patient_status,

		CONCAT(continents.label, " / ", countries.label, 
			IF(samples.county IS NOT NULL, CONCAT(" / ", samples.county), ""),
			IF(samples.city IS NOT NULL, CONCAT(" / ", samples.city), "")
			) AS location,
		samples.additional_location_info AS additional_location_info,
		originating_lab.name AS originating_lab_name,
		originating_lab.address AS originating_lab_address,
		samples.originating_lab_sample_name AS originating_lab_sample_name,
		submitting_lab.name AS submitting_lab_name,
		submitting_lab.address AS submitting_lab_address,
		samples.submitting_lab_sample_name AS submitting_lab_sample_name,
		`groups`.abbreviated_middle_names AS authors_list,

		passage_details.label AS passage_details,
		sampling_strategies.label AS sampling_strategy,
		sequencing_instruments.label AS sequencing_technology,
		assembly_methods.label AS assembly_method,
		CONCAT(samples.coverage, "x") AS coverage,

		specimen_sources.label AS specimen_source,
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
	LEFT JOIN sequencing_instruments
		ON samples.sequencing_instrument_id = sequencing_instruments.id
	LEFT JOIN assembly_methods
		ON samples.assembly_method_id = assembly_methods.id
	LEFT JOIN specimen_sources
		ON samples.specimen_source_id = specimen_sources.id
	LEFT JOIN continents
		ON samples.continent_id = continents.id
	LEFT JOIN countries
		ON samples.country_id = countries.id

