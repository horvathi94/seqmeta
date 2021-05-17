CREATE VIEW `view_hosts` AS

	SELECT 
		`id`, 
		`label`,
		`latin`,
		CONCAT(`label`, " (", `latin`, ")" ) AS display_label
		FROM `hosts`

	
