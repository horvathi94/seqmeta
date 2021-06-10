CREATE OR REPLACE VIEW view_samples_gisaid AS

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,

		sampling.passage_details AS passage_details,
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
		hosts.last_vaccinated AS last_vaccinated,
		health.treatment AS treatment,
		sequencing.sequencing_instrument AS sequencing_technology,
		sequencing.assembly_method AS assembly_method,
		sequencing.coverage_x AS coverage,
		sampling.originating_lab_name AS originating_lab_name,
		sampling.originating_lab_address AS originating_lab_address,
		sampling.originating_lab_sample_name AS originating_lab_sample_name,
		sampling.submitting_lab_name AS submitting_lab_name,
		sampling.submitting_lab_address AS submitting_lab_address,
		sampling.submitting_lab_sample_name AS submitting_lab_sample_name,
		sampling.authors_list AS authors_list,

		seqfiles.filename AS seqfilename

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
	LEFT JOIN view_seqfiles AS seqfiles
		ON samples.sample_id = seqfiles.sample_id
