/*CREATE OR REPLACE VIEW `view_samples_ena` AS

	SELECT 

		samples.id AS sample_id,
		samples.name AS sample_name,
		CONCAT(samples.collection_year,  
			IF (samples.collection_month > 0 AND samples.collection_month IS NOT NULL,
				CONCAT("-", LPAD(samples.collection_month, 2, 0), 
					IF (samples.collection_day > 0 AND samples.collection_day IS NOT NULL,
						CONCAT("-", LPAD(samples.collection_day, 2, 0) ), "" ) ), 
					"") ) AS `collection date`,

		samples.subject_exposure AS `subject exposure`,
		samples.subject_exposure_duration AS `subject exposure duration`,
		samples.ppe AS `personal protective equipment`,
		IF (samples.hospitalization = "" OR samples.hospitalization IS NULL, "", 
			IF (samples.hospitalization = 1, "yes", "no")
		) AS hospitalisation,	
		IF (samples.ilness_duration <> 0 OR samples.ilness_duration IS NOT NULL,
			CONCAT(samples.ilness_duration, " ", "days"), "") AS `ilness duration`,
		samples.ilness_symptoms AS `ilness symptoms`,

		countries.label AS `geographic location (country and/or sea)`,
		samples.geo_loc_latitude AS `geographic location (latitude)`,
		samples.geo_loc_longitude AS `geographic location (longitude)`,
		CONCAT(samples.county, ", ", samples.city) AS `geographic location (region and locality)`,
		
		sample_capture_status.label AS `sample capture status`,
		host_disease_outcome.label AS `host disease outcome`,

		hosts.label AS `host common name`,
		samples.host_subject_id AS `host subject id`,
		samples.patient_age AS `host age`,
		IF (samples.patient_gender = "" OR samples.patient_gender IS NULL, "not provided", 
			IF (samples.patient_gender = 1, "male", "female")
		) AS `host sex`,
		host_health_states.label AS `host health state`,
		hosts.latin AS `host scientific name`,

		samples.submitting_lab_sample_name AS `virus identifier`,

		collectors.abbreviated_middle_name AS `collector name`,
		CONCAT(collecting_institution.name, ", ", collecting_institution.address) AS `collecting institution`,
		samples.sample_storage_conditions AS `sample storage conditions`,

		samples.definition_for_seropositive_sample AS `definition for seropositive sample`,
		samples.serotype AS `serotype (required for a seropositive sample)`,

		samples.isolate AS `isolate`,
		samples.strain AS `strain`,

		host_habitats.label AS `host habitat`,
		samples.isolation_source_host_associated AS `isolation source host associated`,
		samples.host_description AS `host description`,

		samples.gravidity AS `gravidity`,
		host_behaviours.label AS `host behaviour`,

		samples.isolation_source_non_host_associated AS `isolation source non-host-associated`

	FROM view_samples_base AS samples
	LEFT JOIN countries
		ON samples.country_id = countries.id
	LEFT JOIN sample_capture_status
		ON samples.sample_capture_status_id = sample_capture_status.id
	LEFT JOIN host_disease_outcome
		ON samples.host_disease_outcome_id = host_disease_outcome.id
	LEFT JOIN hosts
		ON samples.host_id = hosts.id
	LEFT JOIN host_health_states
		ON samples.host_health_state_id = host_health_states.id
	LEFT JOIN view_authors AS collectors
		ON samples.collector_name_id = collectors.id
	LEFT JOIN view_institutions AS collecting_institution
		ON samples.originating_lab_id = collecting_institution.id
	LEFT JOIN host_habitats
		ON samples.host_habitat_id = host_habitats.id
	LEFT JOIN host_behaviours
		ON samples.host_behaviour_id = host_behaviours.id
	*/
