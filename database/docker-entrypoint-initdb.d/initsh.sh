mysql --user=root \
	-p$MYSQL_ROOT_PASSWORD \
	--database=$MYSQL_DATABASE < "/initdb/initdb.sql";
