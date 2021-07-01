CREATE TABLE IF NOT EXISTS `samples_host` (

	sample_id																INT UNSIGNED NOT NULL PRIMARY KEY,
	host_id																	INT UNSIGNED,
	host_subject_id													VARCHAR(200),
	additional_host_info										VARCHAR(200),
	patient_gender													BIT(1),
	patient_age															TINYINT UNSIGNED,
	patient_status_id												INT UNSIGNED,
	ppe																			VARCHAR(600),
	host_habitat_id													TINYINT UNSIGNED,
	host_behaviour_id												TINYINT UNSIGNED,
	host_description												VARCHAR(1000),
	gravidity																VARCHAR(500),

);


CREATE OR REPLACE VIEW view_samples_host AS 

	SELECT 

		host.sample_id AS sample_id,
		hosts.label AS host_common_name,
		hosts.latin AS host_scientific_name,
		CONCAT(hosts.label, " (", hosts.latin, ")") AS host_name,
		host.host_subject_id AS host_subject_id,
		host.additional_host_info AS additional_host_info,
		host.patient_age AS patient_age,
		IF (host.patient_gender IS NULL, "unknown", 
			IF (host.patient_gender IS TRUE, "Male", "Female")
		) AS patient_gender,
		IF (host.patient_gender IS NULL, "not provided", 
			IF (host.patient_gender IS TRUE, "male", "female")
		) AS patient_gender_ena,
		IF (host.patient_gender IS NULL, "missing", 
			IF (host.patient_gender IS TRUE, "male", "female")
		) AS patient_gender_ncbi,
		patient_statuses.label AS patient_status,
		host.ppe AS ppe,
		habitats.label AS host_habitat,
		behaviours.label AS host_behaviour,
		host.host_description AS host_description,
		host.gravidity AS host_gravidity,
		has_vaccinated.label AS	prior_sars_cov_2_vaccination

	FROM samples_host AS host
	LEFT JOIN hosts
		ON host.host_id = hosts.id
	LEFT JOIN patient_statuses
		ON host.patient_status_id = patient_statuses.id
	LEFT JOIN host_habitats AS habitats
		ON host.host_habitat_id = habitats.id
	LEFT JOIN host_behaviours AS behaviours
		ON host.host_behaviour_id = behaviours.id
	LEFT JOIN has_received_vaccine AS has_vaccinated
		ON host.prior_sars_cov_2_vaccination_id = has_vaccinated.id;

