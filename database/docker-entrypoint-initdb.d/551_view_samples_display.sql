CREATE OR REPLACE VIEW view_samples_display AS 

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
		samples.sample_comment AS sample_comment,
		collection.collection_date AS collection_date,
		collection.author_group_name AS group_name,
		samples.gisaid_virusname AS gisaid_virusname,
		samples.isolate AS isolate
		
	FROM view_samples_base AS samples
	LEFT JOIN view_samples_collection AS collection
		ON samples.sample_id = collection.sample_id
