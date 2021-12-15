#!/bin/bash

# A script to set environment variables for docker-compose and run the docker-compose.




function help(){
	# Displays help screen
	echo "A script to set the environment variables and run docker-compose."
	echo
	echo "Syntax $0 [-m|-h]"
	echo "options:" 
	echo "  -m, --mode    Mode in which to run containers."
	echo "  -h, --help    Show this help screen"
	echo
	echo "Modes: "
	echo "  development   Environment for debugging."
	echo "  production    Normal usage (default)."
	echo "  down          Stop and remove resources"
}




mode="production"


for opt in $@; do

	case $opt in

		-m=*|--mode=*)
			mode="${opt#*=}"
			shift
			;;

		-h|--help)
			help;
			exit;
			;;

		*)
			echo "Invalid options given. Please check the help menu."
			exit 1;;

	esac;

done;



case $mode in 

	development)
		echo "Running in development mode...";
		echo "Binding to port: $HOST_PORT on localhost..."
		docker-compose -f docker-compose.build.prod.yaml -f docker-compose.build.dev.yaml \
			--env-file run.env \
			up -d --build
		;;

	production)
    echo "Running in production mode...";
    docker-compose -f docker-compose.build.prod.yaml \
			--env-file run.env \
			up -d --build
		;;

	down)
		echo "Shutting down...";
		docker-compose -env-file run.env down
		;;

	*)
		echo "Invalid option specified. Please check the help menu.";
		exit 1;
		;;

esac;



