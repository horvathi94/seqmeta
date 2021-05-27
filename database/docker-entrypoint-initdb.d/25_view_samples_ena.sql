CREATE OR REPLACE VIEW `view_samples_ena` AS

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
		host_health_states.label AS `host health state`,
		hosts.latin AS `host scientific name`
		

	FROM samples
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
		
