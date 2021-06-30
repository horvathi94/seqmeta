CREATE OR REPLACE VIEW `view_samples_ena` AS

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
		samples.sample_name AS `virus identifier`,
		samples.sample_title AS sample_title,
		samples.sample_description AS sample_description,

		health.subject_exposure AS `subject exposure`,
		health.subject_exposure_duration AS `subject exposure duration`,
		health.type_exposure AS `type exposure`,
		hosts.ppe AS `personal protective equipment`,
		health.hospitalization AS `hospitalisation`,	
		health.ilness_duration_days AS `ilness duration`,
		health.ilness_symptoms AS `ilness symptoms`,

		collection.collection_date AS `collection date`,
		location.country AS `geographic location (country and/or sea)`,
		location.geo_loc_latitude AS `geographic location (latitude)`,
		location.geo_loc_longitude AS `geographic location (longitude)`,
	
		IF ( location.region = "" AND location.locality = "", "",
			IF ( location.region = "", location.locality, 
				IF ( location.locality = "", location.region, 
					CONCAT(location.region, ", ", location.locality)
				)
			)
		) `geographic location (region and locality)`,

		sampling.sample_capture_status AS `sample capture status`,

		health.host_disease_outcome AS `host disease outcome`,

		hosts.host_common_name AS `host common name`,
		hosts.host_subject_id AS `host subject id`,
		hosts.patient_age AS `host age`,
		hosts.patient_gender_ena AS `host sex`,
		health.host_health_state AS `host health state`,
		hosts.host_scientific_name AS `host scientific name`,
		
		IF (collection.collector_abbreviated_middle_name IS NULL, "not provided",
			collection.collector_abbreviated_middle_name) AS `collector name`, 
		CONCAT(sampling.originating_lab_name, ", ", sampling.originating_lab_address) AS `collecting institution`,
		sampling.sample_storage_conditions AS `sample storage conditions`,

		sampling.definition_for_seropositive_sample AS `definition for seropositive sample`,
		sampling.serotype AS `serotype (required for a seropositive sample)`,

		sampling.strain AS `strain`,

		hosts.host_habitat AS `host habitat`,
		sampling.isolation_source_host_associated AS `isolation source host associated`,
		hosts.host_description AS `host description`,

		hosts.host_gravidity AS `gravidity`,
		hosts.host_behaviour AS `host behaviour`,

		sampling.isolation_source_non_host_associated AS `isolation source non-host-associated`

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




