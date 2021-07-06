CREATE OR REPLACE VIEW view_samples_gisaid AS

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
		samples.gisaid_virusname AS gisaid_virusname,

		collection.collection_date AS collection_date,
		collection.collection_year AS collection_year,
		collection.collection_month AS collection_month,
		collection.collection_day AS collection_day,
		location.location AS location,
		location.continent AS continet,
		location.country AS country,
		location.region AS region,
		location.locality AS locality,
		location.additional_location_info AS additional_location_info,
		hosts.host_common_name AS host,
		hosts.additional_host_info AS additional_host_info,
		sampling.sampling_strategy AS sampling_strategy,
		hosts.patient_gender AS patient_gender,
		hosts.patient_age AS patient_age,
		hosts.patient_status AS patient_status,
		sampling.specimen_source AS specimen_source,
		health.outbreak AS outbreak,
		treatment.antiviral_treatment_agent AS treatment,
		sequencing.sequencing_instrument AS sequencing_technology,
		sequencing.assembly_method AS assembly_method,
		sequencing.coverage_x AS coverage,
		collection.originating_lab_name AS originating_lab_name,
		collection.originating_lab_address AS originating_lab_address,
		collection.originating_lab_sample_name AS originating_lab_sample_name,
		collection.submitting_lab_name AS submitting_lab_name,
		collection.submitting_lab_address AS submitting_lab_address,
		collection.submitting_lab_sample_name AS submitting_lab_sample_name,
		collection.authors_list AS authors_list,
		IF (sampling.passage_number IS NULL, "",
			IF (sampling.passage_number = 0, "Original",
				CONCAT(sampling.passage_method, " passage number: ", sampling.passage_number)
			)
		) AS passage_details,
		IF (treatment.prior_sars_cov_2_vaccination IS NULL, "unknown",
			IF (treatment.prior_sars_cov_2_vaccination = "no", "Not vaccinated",
				CONCAT(
					treatment.prior_sars_cov_2_vaccination, " ", 
					IF (treatment.vaccine_received IS NULL OR treatment.vaccine_received = "", "",
						treatment.vaccine_received ),
					IF (treatment.date_of_prior_sars_cov_2_vaccination IS NULL, "",
						CONCAT("first dose received on: ", treatment.date_of_prior_sars_cov_2_vaccination))
				)
			)
		) AS last_vaccinated,

		( SELECT filename 
			FROM view_seqfiles
			WHERE sample_id = samples.sample_id
				AND is_assembly = TRUE ) AS seqfilename

	FROM view_samples_base AS samples
	LEFT JOIN view_samples_sampling AS sampling
		ON samples.sample_id = sampling.sample_id
	LEFT JOIN view_samples_collection AS collection
		ON samples.sample_id = collection.sample_id
	LEFT JOIN view_samples_location AS location
		ON samples.sample_id = location.sample_id
	LEFT JOIN view_samples_host AS hosts
		ON samples.sample_id = hosts.sample_id
	LEFT JOIN view_samples_health_status AS health
		ON samples.sample_id = health.sample_id
	LEFT JOIN view_samples_sequencing AS sequencing
		ON samples.sample_id = sequencing.sample_id
	LEFT JOIN view_samples_patient_treatment AS treatment
		ON samples.sample_id = treatment.sample_id
