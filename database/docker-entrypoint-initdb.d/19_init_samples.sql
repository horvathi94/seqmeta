CREATE TABLE IF NOT EXISTS samples (

	id									INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name								VARCHAR(200) UNIQUE NOT NULL,
	`comment`						VARCHAR(200),
	title								VARCHAR(200),
	description					VARCHAR(1000)

);
