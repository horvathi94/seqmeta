FROM mysql:8.0
MAINTAINER horvathi

# SQL scripts needed to initialize the database
COPY ./docker-entrypoint-initdb.d /docker-entrypoint-initdb.d

# bash scripts for backing up the database
COPY ./scripts /scripts
RUN chmod 775 /scripts/* \
	&& mkdir /backups/

