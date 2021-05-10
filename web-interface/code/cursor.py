import os
import mysql.connector
from collections import OrderedDict

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


    def list_and_save(self, table_name, items):
        pass;

