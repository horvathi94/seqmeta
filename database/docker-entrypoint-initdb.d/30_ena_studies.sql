CREATE TABLE IF NOT EXISTS ena_studies (
	
	id										INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	project_name					VARCHAR(500) NOT NULL,
	project_title					VARCHAR(500) NOT NULL,
	project_alias					VARCHAR(500) NOT NULL UNIQUE,
	project_description		TEXT NOT NULL,

	project_link_db				CHAR(100),
	project_link_id				CHAR(200)

);
