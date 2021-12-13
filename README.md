# SeqMeta

A simple Python Flask application for editing and managing SARS-CoV-2 sequencing metadata and data. The goal of the project is to users to format metadata for upload to EpiCov from [GISAID](https://www.gisaid.org/), [ENA](https://www.ebi.ac.uk/ena/browser/home) and [NCBI](https://www.ncbi.nlm.nih.gov) databases.


## Howto run

There are two modes to run the application: *development* and *production*.
The *production* environment is recommended for use. This runs the Flask application with uWSGI server, which enhances performance, but does not give feedback in case of any errors.
The *development* environment is recommended for debugging and developing. In this mode the Flask application is run directly with `python3` command. This is not ideal for production but gives a better feedback for error handling.



### Quickstart on Linux:

To spin up the containers on a Linux machine you may use the `spinup.sh` script. For more information about the usage check out the help menu `./spinup.sh --help`.


### NGINX

The compose file includes an NGINX container to route data to the Flask container. The *nginx* directory contains two configuration files for NGINX, one for development of the app, which simply routes all http requests to the Flask container and one intended for production, which serves static content and routes other requests in uswgi format to the FLask app.


### Starting manually

Move into the main directory of the project (where the *docker-compose.yaml* file is located) and use the `docker-compose` command to spinup the containers:

`docker-compose --file <compose-file> --file <compose-file-2> --env-file <environment-file> up --build -d`

Where:
- the `docker-compose up` command tells docker to spin up all containers in the compose file.
- the `--file` options specify the docker-compose file based on which the containers will be deployed. To create the production environment simply specify the `docker-compose.yaml`. To deploy a development environment specify both the files: `--file docker-compose.yam --file docker-compose-build.yaml` in this order. Read more about extending docker-compose files [here](https://docs.docker.com/compose/extends/)
- use the `--env-file` to specify the file containing the environment variables. In this case you may use: `--env-file run.env`
- the `--build` option is important if it is the first time you are running the application as it tells Docker to build the images for the containers.
- the `-d` option is to run the command in detached mode, which means that it will run in the background and you will be free to use the terminal.


The environment variables for the containers can be modified by editing the compose file or adding a .env file. More on environment variables [here](https://docs.docker.com/compose/environment-variables/).

Environment variables:
- **MYSQL_DATABASE** the name of the MySQL database
- **MYSQL_USER** username for MySQL
- **MYSQL_PASSWORD** a password for the MySQL user
- **MYSQL_ROOT_PASSWORD** password for the root user.
- **HOST_PORT** port on host machine to which to bind the web application (port 80 of the NGINX container).
- **MYSQL_DATABASE_DIR** where the database is stored. Mount this to a directory on the host machine to not lose data when the container is stopped.
- **MYSQL_BACKUPS_DIR** where the files produced by the `backup.sh` script are stored
- **MYSQL_SAMPLES_DIR** where the uploaded files are stored (sequence reads and assembly files).


To locally mount the MySQL database volume uncomment line number 51 from the compose file and specify the **MYSQL_DIR** environment variable. Data inside the Docker containers which is created during runtime is deleted if the container is stopped mounting it locally will kepp this data persistent. Read more about Docker volumes [here](https://docs.docker.com/storage/volumes/).




## Tips


### Backup and restore the database

To perform backup of the database tables you may use the two scripts which can be found in the database container inside `/scripts` directory.

The `backup.sh` script performs a `mysqldump` on some of the tables inside the database, the selection of the tables is performed usisng the `--data` option. The *sql* files are saved in the `/backups` directory, which can be mounted to your local machine. For more details please check the help menu:


`docker exec -it <container-name> /scripts/backup.sh --help`


The `restore.sh` script can be used to restore data saved from the *SQL* files created by the `backup.sh` script. The *SQL* files must be located in the `/backups` directory of the container. To see more options about the usage of the scrpt please see the help menu:


`docker exec -it <container-name> /scripts/restore.sh --help`

