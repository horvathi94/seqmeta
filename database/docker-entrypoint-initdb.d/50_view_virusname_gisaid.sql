CREATE OR REPLACE VIEW view_virusname_gisaid AS

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,

		sampling.passage_details AS passage_details,
		IF (collection.collection_year IS NULL, "", 
			collection.collection_year) AS collection_year,
		IF (collection.collection_month IS NULL, "", 
			collection.collection_month) AS collection_month,
		IF (collection.collection_day IS NULL, "", 
			collection.collection_day) AS collection_day,
		IF (location.continent IS NULL, "",
			location.continent) AS continent,
		IF (location.country IS NULL, "",
			location.country) AS country,
		IF (location.region IS NULL, "",
			location.region) AS region,
		IF (location.locality IS NULL, "",
			location.locality) AS locality,
		location.additional_location_info AS additional_location_info,
		hosts.host_common_name AS host_common_name,
		hosts.host_scientific_name AS host_scientific_name,
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
		sampling.originating_lab_sample_name AS originating_lab_sample_name,
		sampling.submitting_lab_name AS submitting_lab_name,
		sampling.submitting_lab_sample_name AS submitting_lab_sample_name


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
