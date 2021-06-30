CREATE OR REPLACE VIEW `view_isolate_ena` AS

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,

		health.subject_exposure AS `subject_exposure`,
		health.subject_exposure_duration AS `subject_exposure_duration`,
		health.type_exposure AS `type_exposure`,
		hosts.ppe AS `personal_protective_equipment`,
		health.hospitalization AS `hospitalisation`,	
		health.ilness_duration_days AS `ilness_duration`,
		health.ilness_symptoms AS `ilness_symptoms`,

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
		location.geo_loc_latitude AS `geographic_location_latitude`,
		location.geo_loc_longitude AS `geographic_location_longitude`,

		sampling.sample_capture_status AS `sample_capture_status`,

		health.host_disease_outcome AS `host_disease_outcome`,

		hosts.host_common_name AS host_common_name,
		hosts.host_scientific_name AS host_scientific_name,
		hosts.host_subject_id AS `host_subject_id`,
		hosts.patient_age AS `patient_age`,
		hosts.patient_gender_ena AS `patient_gender`,
		health.host_health_state AS `host_health_state`,
		
		collection.collector_abbreviated_middle_name AS `collector_name`, 
		sampling.originating_lab_name AS originating_lab_name,
		sampling.originating_lab_sample_name AS originating_lab_sample_name,
		sampling.submitting_lab_name AS submitting_lab_name,
		sampling.submitting_lab_sample_name AS submitting_lab_sample_name,

		sampling.sample_storage_conditions AS `sample_storage_conditions`,

		sampling.strain AS `strain`,

		hosts.host_habitat AS `host_habitat`,
		sampling.isolation_source_host_associated AS `isolation_source_host_associated`,
		hosts.host_description AS `host_description`,

		hosts.host_gravidity AS `gravidity`,
		hosts.host_behaviour AS `host behaviour`,

		sampling.isolation_source_non_host_associated AS `isolation_source_non-host-associated`

	FROM view_samples_base AS samples
	LEFT JOIN view_samples_health_status AS health
		ON samples.sample_id = health.sample_id
	LEFT JOIN view_samples_host AS hosts
		ON samples.sample_id = hosts.sample_id
	LEFT JOIN view_samples_collection AS collection
		ON samples.sample_id = collection.sample_id
	LEFT JOIN view_samples_location AS location
		ON samples.sample_id = location.sample_id
	LEFT JOIN view_samples_sampling AS sampling
		ON samples.sample_id = sampling.sample_id;




