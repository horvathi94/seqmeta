/* View to select data for GISAID virusname. */

CREATE OR REPLACE VIEW view_virusname_gisaid AS

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,

		collection.collection_year AS collection_year,
		collection.collection_month AS collection_month,
		collection.collection_day AS collection_day,
		location.continent AS continent,
		location.country AS country,
		location.region AS region,
		location.locality AS locality,
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
		treatment.antiviral_treatment_agent AS treatment,
		sequencing.sequencing_instrument AS sequencing_technology,
		sequencing.coverage_x AS coverage,
		collection.originating_lab_name AS originating_lab_name,
		collection.originating_lab_sample_name AS originating_lab_sample_name,
		collection.submitting_lab_name AS submitting_lab_name,
		collection.submitting_lab_sample_name AS submitting_lab_sample_name,
		sampling.passage_number AS passage_number,
		originating_lab.symbol AS originating_lab_symbol,
		submitting_lab.symbol AS submitting_lab_symbol


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
	LEFT JOIN view_institutions AS originating_lab
		ON samples.originating_lab_id = originating_lab.id
	LEFT JOIN view_institutions AS submitting_lab
		ON samples.submitting_lab_id = submitting_lab.id
