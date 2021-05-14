# sequence-uploader
Project for formatting sequencing metadata and data for upload to multiple databases.

A simple web interface where you can upload sequences to keep track in a local mysql database and aslo format metadata to readily upload to sequencing databases.


## Tips

To backup the mysql database use the `mysqldump` function via `docker exec`.
Example: 

`docker exec <mysql_container_name> mysqldump --user=<user> -p<password> sequencing_data > <path/to/backup_sql>`
