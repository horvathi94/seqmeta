CREATE OR REPLACE VIEW view_samples_display AS 

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
		collection.collection_date AS collection_date,
		sampling.author_group_name AS group_name
		

	FROM view_samples_base AS samples
	LEFT JOIN view_samples_collection AS collection
		ON samples.sample_id = collection.sample_id
	LEFT JOIN view_samples_sampling AS sampling
		ON samples.sample_id = sampling.sample_id
