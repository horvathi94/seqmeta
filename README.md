# sequence-uploader
Project for formatting sequencing metadata and data for upload to multiple databases.

A simple web interface where you can upload sequences to keep track in a local mysql database and aslo format metadata to readily upload to sequencing databases.


## Tips


### Backup and restore the database

To backup the mysql database use the `mysqldump` function via `docker exec`.
Example: 

`docker exec -i <mysql_container_name> mysqldump --user=<user> -p<password> sequencing_data > <path/on/host/to/backup.sql>`


To restore from the backup run:

`docker exec -i <mysql_container_name mysql --user=<user> -p<password> sequencing_data > < <path/on/host/to/backup.sql>` 

**Notice:** You can use the `-p` (password) option without sepcifying the password directly. In this case you will be prompted to enter the mysql password of the user.
