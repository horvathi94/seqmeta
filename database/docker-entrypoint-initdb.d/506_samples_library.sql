CREATE TABLE IF NOT EXISTS `samples_library` (
	
	sample_id 							INT UNSIGNED NOT NULL PRIMARY KEY,
	lib_id									VARCHAR(200) NULL UNIQUE,
	layout_paired						BIT(1),					
	strategy_id							SMALLINT UNSIGNED,
	source_id								SMALLINT UNSIGNED,
	selection_id						SMALLINT UNSIGNED,
	design_description 			VARCHAR(1000),
	preparation_date				DATE,
	insert_size							VARCHAR(20)

);



CREATE OR REPLACE VIEW view_samples_library AS 

	SELECT

		library.sample_id AS sample_id,
		library.lib_id AS library_id,
		library.layout_paired AS layout_paired,
		IF( library.layout_paired	IS NULL, "",
			IF (library.layout_paired IS TRUE, "Paired-End", "Single") ) AS library_layout,
		strategies.item_key AS library_strategy,
		sources.item_key AS library_source,
		selections.item_key AS library_selection,
		library.design_description AS library_design_description,
		IF(library.preparation_date IS NULL, "",
			DATE_FORMAT(library.preparation_date, "%Y-%m-%d")) AS library_preparation_date,
		library.insert_size AS library_insert_size

	FROM samples_library AS library
	LEFT JOIN library_strategies AS strategies
		ON library.strategy_id = strategies.id
	LEFT JOIN library_sources AS sources
		ON library.source_id = sources.id
	LEFT JOIN library_selections AS selections
		ON library.selection_id = selections.id;
	

