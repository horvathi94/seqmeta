/* View for selecting data to be imported when editing multiple samples */

CREATE OR REPLACE VIEW `view_samples_import` AS

	SELECT 

		samples.id AS `sample_id`,
		samples.title AS `sample-title`,
		samples.description AS `sample-description`,

		collection.collection_year AS `collection-year`,
		collection.collection_month AS `collection-month`,
		collection.collection_day AS `collection-day`,
		collection.collector_id AS `collector-name`,
		collection.originating_lab_id AS `originating-lab`,
		collection.originating_lab_sample_name AS `originating-lab-sample-name`,
		collection.submitting_lab_id AS `submitting-lab`,
		collection.submitting_lab_sample_name AS `submitting-lab-sample-name`,
		collection.author_group_id AS `author-group`,
		collection.collection_device_id AS `collection-device`,

		location.continent_id AS `continent`,
		location.country_id AS `country`,
		location.region AS `region`,
		location.locality AS `locality`,
		location.geo_loc_latitude AS `geo-loc-latitude`,
		location.geo_loc_longitude AS `geo-loc-longitude`,
		location.additional_location_info AS `location-additional-info`,
		location.geo_loc_exposure_id AS `geo-loc-exposure`,

		treatment.prior_sars_cov_2_antiviral_treat AS `prior-sars-cov-2-antiviral-treat`,
		DATE_FORMAT(treatment.date_of_prior_antiviral_treat, 
			"%Y-%m-%d") AS `date-of-prior-antiviral-treat`,
		treatment.prior_sars_cov_2_infection AS `prior-sars-cov-2-infection`,
		DATE_FORMAT(treatment.date_of_prior_sars_cov_2_infection, 
			"%Y-%m-%d") AS `date-of-prior-sars-cov-2-infection`,
		treatment.prior_sars_cov_2_vaccination_id AS `prior-sars-cov-2-vaccination-id`,
		DATE_FORMAT(treatment.date_of_prior_sars_cov_2_vaccination, 
			"%Y-%m-%d") AS `date-of-prior-sars-cov-2-vaccination`,
		treatment.virus_isolate_of_prior_infection AS `virus-isolate-of-prior-infection`,
		treatment.vaccine_received AS `vaccine-received`,
		treatment.antiviral_treatment_agent AS `antiviral-treatment-agent`,

		host.host_id AS `host`,
		host.host_subject_id AS	`host-subject-id`,
		host.additional_host_info	AS `additional-host-info`,
		host.patient_gender	AS `patient-gender`,
		host.patient_age AS `patient-age`,
		host.patient_status_id AS	`patient-status`,
		host.ppe AS	`ppe`,
		host.host_habitat_id AS `host-habitat-id`,
		host.host_behaviour_id AS	`host-behaviour-id`,
		host.host_description	AS `host-description`,
		host.gravidity AS	`host-gravidity`,
		host.host_recent_travel_loc	AS `host-recent-travel-loc`,			
		DATE_FORMAT(host.host_recent_travel_return_date,
			"%Y-%m-%d") AS `host-recent-travel-return-date`,

		/*sampling.receipt_date AS receipt_date,*/
		sampling.sampling_strategy_id AS `sampling-strategy`,
		sampling.strain AS `strain`,
		sampling.isolation_source_host_associated AS `isolation-source-host-associated`,
		sampling.isolation_source_non_host_associated	`isolation-source-non-host-associated`,
		sampling.sample_capture_status_id AS `sample-capture-status`,
		sampling.specimen_source_id AS `specimen-source`,
		sampling.sample_storage_conditions AS `sample-storage-conditions`,
		sampling.definition_for_seropositive_sample AS `definition_for_seropositive_sample`,
		sampling.serotype AS `serotype`,
		sampling.passage_method AS `passage-method`,
		sampling.passage_number AS `passage-number`,
		sampling.host_anatomical_material_id AS `host-anatomical-material`,
		sampling.host_body_product_id AS `host-body-product`,
		sampling.purpose_of_sampling_id AS `purpose-of-sampling`,
		sampling.purpose_of_sequencing_id AS `purpose-of-sequencing`,
		
		health.subject_exposure AS `subject-exposure`,
		health.subject_exposure_duration AS `subject-exposure-duration`,	
		health.type_exposure AS `type-exposure`,
		health.hospitalization AS `hospitalisation`,
		health.ilness_duration AS `ilness-duration`,
		health.ilness_symptoms AS `ilness-symptoms`,
		health.host_disease_outcome_id AS `ilness-disease-outcome`,
		health.host_health_state_id AS `host-health-state`,
		health.outbreak AS `outbreak`,
		health.sars_cov_2_diag_gene_name_1_id AS `sars-cov-2-diag-gene-name-1`,
		health.sars_cov_2_diag_pcr_ct_value_1 AS `sars-cov-2-diag-pcr-ct-value-1`,
		health.sars_cov_2_diag_gene_name_2_id AS `sars-cov-2-diag-gene-name-2`,
		health.sars_cov_2_diag_pcr_ct_value_2 AS `sars-cov-2-diag-pcr-ct-value-2`,

		sequencing.sequencing_instrument_id AS `sequencing-instrument`,
		sequencing.coverage AS `coverage`,
		sequencing.sequencing_lab_id AS `sequencing-lab`,

		library.library_layout_paired AS `library-layout`,
		library.library_strategy_id AS `library-strategy`,
		library.library_source_id AS `library-source`,
		library.library_selection_id AS `library-selection`,
		library.library_design_description AS `library-design-description`,
		DATE_FORMAT(library.library_preparation_date,
			"%Y-%m-%d") AS `library-preparation-date`,
		library.insert_size AS `insert-size`,
		library.library_construction_protocol AS `library-construction-protocol`


		FROM samples
		LEFT JOIN samples_location AS location
			ON samples.id = location.sample_id
		LEFT JOIN samples_collection AS collection
			ON samples.id = collection.sample_id
		LEFT JOIN samples_library AS library
			ON samples.id = library.sample_id
		LEFT JOIN samples_host AS host
			ON samples.id = host.sample_id
		LEFT JOIN samples_sampling AS sampling
			ON samples.id = sampling.sample_id
		LEFT JOIN samples_health_status AS health
			ON samples.id = health.sample_id
		LEFT JOIN samples_sequencing AS sequencing
			ON samples.id = sequencing.sample_id
		LEFT JOIN samples_patient_treatment AS treatment
			ON samples.id = treatment.sample_id
