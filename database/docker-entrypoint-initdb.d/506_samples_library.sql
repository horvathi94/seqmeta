CREATE TABLE IF NOT EXISTS `samples_library` (
	
	sample_id 											INT UNSIGNED NOT NULL PRIMARY KEY,
	library_id											VARCHAR(200) NULL UNIQUE,
	library_layout_paired						BIT(1),					
	library_strategy_id							SMALLINT UNSIGNED,
	library_source_id								SMALLINT UNSIGNED,
	library_selection_id						SMALLINT UNSIGNED,
	library_design_description 			VARCHAR(1000),
	library_preparation_date				DATE,
	insert_size											MEDIUMINT UNSIGNED,
	library_construction_protocol		VARCHAR(500)

);



CREATE OR REPLACE VIEW view_samples_library AS 

	SELECT

		library.sample_id AS sample_id,
		library.library_id AS library_id,
		library.library_layout_paired AS library_layout_paired,
		IF( library.library_layout_paired	IS NULL, "",
			IF (library.library_layout_paired IS TRUE, "Paired-End", "Single") ) AS library_layout,
		strategies.item_key AS library_strategy,
		sources.item_key AS library_source,
		selections.item_key AS library_selection,
		library.library_design_description AS library_design_description,
		IF(library.library_preparation_date IS NULL, "",
			DATE_FORMAT(library.library_preparation_date, "%Y-%m-%d")) AS library_preparation_date,
		library.insert_size AS library_insert_size,
		library.library_construction_protocol AS library_construction_protocol

	FROM samples_library AS library
	LEFT JOIN library_strategies AS strategies
		ON library.library_strategy_id = strategies.id
	LEFT JOIN library_sources AS sources
		ON library.library_source_id = sources.id
	LEFT JOIN library_selections AS selections
		ON library.library_selection_id = selections.id;
	

