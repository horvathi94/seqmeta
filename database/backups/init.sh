#!/bin/bash

mysql --user=$MYSQL_USER \
	-p$MYSQL_PASSWORD \
	$MYSQL_DATABASE 
