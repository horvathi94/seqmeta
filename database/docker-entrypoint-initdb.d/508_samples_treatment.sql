CREATE TABLE IF NOT EXISTS samples_patient_treatment (

	sample_id																INT UNSIGNED NOT NULL PRIMARY KEY,
	prior_sars_cov_2_antiviral_treat				BIT(1),
	date_of_prior_antiviral_treat						DATE,
	prior_sars_cov_2_infection							BIT(1),	
	date_of_prior_sars_cov_2_infection			DATE,
	prior_sars_cov_2_vaccination_id					TINYINT UNSIGNED,
	date_of_prior_sars_cov_2_vaccination		DATE,
	virus_isolate_of_prior_infection				VARCHAR(200),
	vaccine_received												VARCHAR(100)

);


CREATE OR REPLACE VIEW view_samples_patient_treatment AS

	SELECT 

		treatment.sample_id AS sample_id,
		treatment.prior_sars_cov_2_antiviral_treat AS prior_sars_cov_2_antiviral_treat,
		treatment.date_of_prior_antiviral_treat AS date_of_prior_antiviral_treat

	FROM samples_patient_treatment AS treatment
