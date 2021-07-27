# SeqMeta

A simple Python Flask application for editing and managing SARS-CoV-2 sequencing metadata and data. The goal of the project is to users to format metadata for upload to EpiCov from [GISAID](https://www.gisaid.org/), [ENA](https://www.ebi.ac.uk/ena/browser/home) and [NCBI](https://www.ncbi.nlm.nih.gov) databases.


## Howto run

Move into the main directory of the project (where the *docker-compose.yaml* file is located) and use the `docker-compose` command to spinup the containers:

`docker-compose up --build -d`

Where:
	- the `docker-compose up` command tells docker to spin up all containers in the compose file.
	- the `--build` option is important if it is the first time you are running the application as it tells Docker to build the images for the containers.
	- the `-d` option is to run the command in detached mode, which means that it will run in the background and you will be free to use the terminal.


The environment variables for the containers can be modified by editing the compose file or adding a .env file. More on environment variables [here](https://docs.docker.com/compose/environment-variables/).

Environment variables:
	- **MYSQL_DATABASE** the name of the MySQL database
	- **MYSQL_USER** username for MySQL
	- **MYSQL_PASSWORD** a password for the MySQL user
	- **MYSQL_ROOT_PASSWORD** password for the root user.
	- **STAGING_LEVEL** accepted values are *production* and *development*. The default value for this variable is *production*. Use *development* only if you would like to modify or further develop the application. 



## Tips


### Backup and restore the database

To backup the mysql database use the `mysqldump` function via `docker exec`.
Example: 

`docker exec -i <mysql_container_name> mysqldump --user=<user> -p<password> sequencing_data > <path/on/host/to/backup.sql>`


To restore from the backup run:

`docker exec -i <mysql_container_name> mysql --user=<username> -p<password> sequencing_data > <path/on/host/to/backup.sql>` 
