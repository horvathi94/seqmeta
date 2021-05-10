import os
import mysql.connector
from collections import OrderedDict
import funcs

class Cursor:

    user = os.environ["MYSQL_USER"];
    password = os.environ["MYSQL_PASSWORD"];
    database = os.environ["MYSQL_DATABASE"];
    host = "database";

    def __init__(self):
        self.conn = None;
        self.cursor = None;
        self.open();

    def open(self):
        if self.cursor == None:

            if self.conn == None:
                self.conn = mysql.connector.connect(
                    user = self.user,
                    password = self.password,
                    host = self.host,
                    database = self.database );

            self.cursor = self.conn.cursor();

    def close(self):
        self.cursor.close();
        self.conn.close();


    def execute(self, sql):
        self.open();
        self.cursor.execute(sql);

    def execute_commit(self, sql, values):
        self.open();
        self.cursor.execute(sql, values);
        self.conn.commit();

    def describe(self, table_name):
        sql = "DESCRIBE `{:s}`".format(table_name);
        self.execute(sql);
        raw = self.cursor.fetchall();
        return raw;

    def select_all(self, table_name):
        sql = "SELECT * FROM `{:s}`".format(table_name);
        self.execute(sql);
        records = self.cursor.fetchall();
        column_names = self.cursor.column_names;

        res = [];
        for record in records:
            row_data = OrderedDict();
            for i, col in enumerate(column_names):
                row_data[col] = record[i];
            res.append(row_data);

        return res;

    def update_row(self, table_name, where_id, values_dict):
        sql = "UPDATE `{:s}` SET".format(table_name);

        values = [];
        for key in values_dict:
            if key == "id":
                continue;
#            if values_dict[key]:
            sql += " {:s}=".format(key);
            sql += "%s,";
            values.append(values_dict[key].strip());

        sql = sql[:-1];
        sql+= " WHERE id = {:d}".format(where_id);
        values = tuple(values);
        self.execute_commit(sql, values);


    def list_and_save(self, table_name, submitted):
        existent = self.select_all(table_name);

        for new_od in submitted:

            is_matched = False;

            for reg_od in existent:

                if reg_od["id"] != new_od["id"]:
                    continue;

                is_matched = True;
                if funcs.compare_ordereddicts(reg_od, new_od):
                    break;

                self.update_row(table_name, new_od["id"], new_od);

            if not is_matched:
                return "Insert new value";

        return "Finished";
