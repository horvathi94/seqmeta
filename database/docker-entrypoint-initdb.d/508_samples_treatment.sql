CREATE TABLE IF NOT EXISTS samples_patient_treatment (

	sample_id																INT UNSIGNED NOT NULL PRIMARY KEY,
	prior_sars_cov_2_antiviral_treat				BIT(1),
	date_of_prior_antiviral_treat						DATE,
	prior_sars_cov_2_infection							BIT(1),	
	date_of_prior_sars_cov_2_infection			DATE,
	prior_sars_cov_2_vaccination_id					TINYINT UNSIGNED,
	date_of_prior_sars_cov_2_vaccination		DATE,
	virus_isolate_of_prior_infection				VARCHAR(200),
	vaccine_received												VARCHAR(100),
	antiviral_treatment_agent								VARCHAR(200)

);


CREATE OR REPLACE VIEW view_samples_patient_treatment AS

	SELECT 

		treatment.sample_id AS sample_id,
		IF( treatment.prior_sars_cov_2_antiviral_treat IS NULL, "",
			IF ( treatment.prior_sars_cov_2_antiviral_treat IS TRUE, "yes", "no" )
		) AS prior_sars_cov_2_antiviral_treat,
		treatment.date_of_prior_antiviral_treat AS date_of_prior_antiviral_treat,
		IF( treatment.prior_sars_cov_2_infection IS NULL, "",
			IF ( treatment.prior_sars_cov_2_infection IS TRUE, "yes", "no")
		) AS prior_sars_cov_2_infection,
		treatment.date_of_prior_sars_cov_2_infection AS date_of_prior_sars_cov_2_infection,
		has_vaccine.label AS prior_sars_cov_2_vaccination,
		treatment.date_of_prior_sars_cov_2_vaccination AS date_of_prior_sars_cov_2_vaccination,
		treatment.virus_isolate_of_prior_infection AS virus_isolate_of_prior_infection,
		treatment.vaccine_received AS vaccine_received,
		treatment.antiviral_treatment_agent AS antiviral_treatment_agent

	FROM samples_patient_treatment AS treatment
	LEFT JOIN has_received_vaccine AS has_vaccine
		ON treatment.prior_sars_cov_2_vaccination_id = has_vaccine.id
