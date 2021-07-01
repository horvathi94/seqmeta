CREATE TABLE IF NOT EXISTS `samples_health_status` (

	sample_id																INT UNSIGNED NOT NULL PRIMARY KEY,
	subject_exposure												VARCHAR(600),
	subject_exposure_duration								VARCHAR(600),
	type_exposure														VARCHAR(600),
	hospitalization													BIT(1),
	ilness_duration													SMALLINT UNSIGNED,
	ilness_symptoms													VARCHAR(600),
	host_disease_outcome_id									TINYINT UNSIGNED,
	host_health_state_id										TINYINT UNSIGNED,
	outbreak																VARCHAR(200),
	sars_cov_2_diag_gene_name_1_id					TINYINT UNSIGNED,
	sars_cov_2_diag_pcr_ct_value_1					TINYINT UNSIGNED,
	sars_cov_2_diag_gene_name_2_id					TINYINT UNSIGNED,
	sars_cov_2_diag_pcr_ct_value_2					TINYINT UNSIGNED

);



CREATE OR REPLACE VIEW view_samples_health_status AS 

	SELECT 

		health.sample_id AS sample_id,
		health.subject_exposure AS subject_exposure,
		health.subject_exposure_duration AS subject_exposure_duration,
		health.type_exposure AS type_exposure,
		IF (health.hospitalization IS NULL, "",
			IF(health.hospitalization IS TRUE, "yes", "no")) AS hospitalization,
		health.ilness_duration AS ilness_duration,
		IF(health.ilness_duration IS NULL, "",
			CONCAT(health.ilness_duration, " days")) AS ilness_duration_days,
		health.ilness_symptoms AS ilness_symptoms,
		outcome.label AS host_disease_outcome,
		health_states.label AS host_health_state,
		health.outbreak AS outbreak,
		genes_1.label AS sars_cov_2_diag_gene_name_1,
		health.sars_cov_2_diag_pcr_ct_value_1 AS sars_cov_2_diag_pcr_ct_value_1,
		genes_2.label AS sars_cov_2_diag_gene_name_2,
		health.sars_cov_2_diag_pcr_ct_value_2 AS sars_cov_2_diag_pcr_ct_value_2


	FROM samples_health_status AS health
	LEFT JOIN host_health_states AS health_states
		ON health.host_health_state_id = health_states.id 
	LEFT JOIN host_disease_outcome AS outcome
		ON health.host_disease_outcome_id = outcome.id
	LEFT JOIN sars_cov_2_genes AS genes_1
		ON health.sars_cov_2_diag_gene_name_1_id = genes_1.id
	LEFT JOIN sars_cov_2_genes AS genes_2
		ON health.sars_cov_2_diag_gene_name_2_id = genes_2.id;
	
