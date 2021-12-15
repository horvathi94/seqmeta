# SeqMeta

A simple Python Flask application for editing and managing SARS-CoV-2 sequencing metadata and data. The goal of the project is to help users with the upload of SARS-CoV-2 sequencing data the following repositories: 
- EpiCov from [GISAID](https://www.gisaid.org/)
- repositories hosted by [ENA](https://www.ebi.ac.uk/ena/browser/home) 
- SRA trough [NCBI](https://www.ncbi.nlm.nih.gov).

## Requirements

This project requires [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/).

## Setting up locally

In the local environment only the Flask application and the database container are spinned up. This means that the Flask app container also handles the routing of HTTP traffic. This is not recommended for production.

To run in a local environment run the *docker-compose.local.yaml* file with docker-compose: `docker-compose --env-file run.env --file docker-compose.local.yaml up -d`.


## Important!

1. The MySQL container will take some time to initialize the database. To follow the progress use the `docker logs <container-name> --follow` command. All tables of the database must be initialized when this process is finished and the following message is displayed: *MySQL init process done. Ready for start up.*. Sometimes it is necessary to restart the Flask app container as this requires connection to the fully initialized MySQL database. For this you can use the `docker restart <app-container-name>` command.
2. When starting the project locally or in development mode the entrypoint command for the web interface container is `tail -F uwsgi.ini`. This means that the Flask server must be started manually via the `docker exec` command from the host machine: `docker exec -it <container-name> python3 wsgi.py`
To modify this behaviour overwrite the entrypoint command to run the Flask app at startup. This can be done by editing the Dockerfile of the web-interface and uncommenting the following line: `CMD ["python3", "./wsgi.py"]`.


## Environment variables

The repo includes a basic configuration file with environment variables *run.env* with detailed explanation for all of them. A full list of all available environment variables:
- **MYSQL_DATABASE** the name of the MySQL database
- **MYSQL_USER** username for MySQL
- **MYSQL_PASSWORD** a password for the MySQL user
- **MYSQL_ROOT_PASSWORD** password for the root user
- **HOST_PORT** port on the host machine to which to bind the web application
- **MYSQL_DATABASE_DIR** the directory on the host machine where the database files is mounted. Use this environment variable for persistent data*.
- **MYSQL_BACKUPS_DIR** the directory on the host machine where */backups* directory of the container is mounted. This directory holds files produced by the *backup.sh* script are stored.
- **APP_SAMPLES_DIR** the directory on the host machine where the directory of the web interface container is mounted which holds uploaded sequence files.

\*: Data inside the Docker containers which is created during runtime is deleted if the container is stopped. Mounting these volumes to the host machine means that they will be available even after the container is removed. Read more about Docker volumes [here](https://docs.docker.com/storage/volumes/).



## Backing up and restoring the database

To perform backup of the database tables you may use the two scripts which can be found in the database container inside the `/scripts` directory.

The `backup.sh` script performs a `mysqldump` on some of the tables inside the database, the selection of the tables is performed usisng the `--data` option. The *sql* files are saved in the `/backups` directory, which can be mounted to your local machine. For more details please check the help menu:


`docker exec -it <container-name> /scripts/backup.sh --help`


The `restore.sh` script can be used to restore data saved from the *SQL* files created by the `backup.sh` script. The *SQL* files must be located in the `/backups` directory of the container. To see more options about the usage of the script please see the help menu:


`docker exec -it <container-name> /scripts/restore.sh --help`


## Running behind NGINX

There are two modes to run the application in this setup: *development* and *production*.
The *production* environment is recommended for main use. This runs the Flask application in uWSGI server mode, which enhances performance, but does not give feedback in case of any errors.
The *development* environment is recommended for debugging and developing. In this mode the Flask application is run directly with Python3 and accepts only HTTP requests. This is not ideal for production but gives a better feedback for error handling.



### Quickstart on Linux machines

To spin up the containers on a Linux machine you can use the `spinup.sh` script. For more information about the usage check out the help menu `./spinup.sh --help`.


### Starting manually

In the root directory of the project use the `docker-compose` command to spinup the containers.

Basic usage:
`docker-compose --file <compose-file> --file <compose-file-2> --env-file <environment-file> up --build -d`

Where:
- the `docker-compose up` command tells docker to spin up all containers in the compose file.
- the `--file` option specifies the docker-compose file from which the containers will be started. Link multiple files to overwrite options. 
- the `--env-file` option specifies the file which contains environment variables. 
- the `--build` option is important if it is the first time you are running the application as it tells Docker to build the images for the containers.
- the `-d` option is to run the command in detached mode, which means that it will run in the background and you will be free to use the terminal.


Example for running in development mode:
`docker-compose --file docker-compose.build.prod.yaml docker-compose.build.dev.yaml --env-file run.env up -d`

Example for running in production mode:
`docker-compose --file docker-compose.build.prod.yaml --env-fule run.env up -d`

Read more about extending docker-compose files [here](https://docs.docker.com/compose/extends/)



#### NGINX configuration

The build compose files includes an NGINX container to route data to the Flask container. The *nginx* directory contains two configuration files for NGINX, one for development (*nginx.dev.conf*) of the app, which simply passes all HTTP requests to the Flask container and one intended for production (*nginx.conf*), which serves static content directly and routes other requests trough WSGI format to the Flask app.
