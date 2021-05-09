mysql --user=${MYSQL_USER} \
	-p${MYSQL_PASSWORD} \
	--database=${MYSQL_DATABASE} < "/initdb/initdb.sql";
