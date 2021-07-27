# SeqMeta

A simple Python Flask application for editing and managing SARS-CoV-2 sequencing metadata and data.

The goal of the project is to users to format metadata for upload to EpiCov from [GISAID](https://www.gisaid.org/), ENA and NCBI databases.





## Tips


### Backup and restore the database

To backup the mysql database use the `mysqldump` function via `docker exec`.
Example: 

`docker exec -i <mysql_container_name> mysqldump --user=<user> -p<password> sequencing_data > <path/on/host/to/backup.sql>`


To restore from the backup run:

`docker exec -i <mysql_container_name mysql --user=<user> -p<password> sequencing_data > < <path/on/host/to/backup.sql>` 

**Notice:** You can use the `-p` (password) option without sepcifying the password directly. In this case you will be prompted to enter the mysql password of the user.
