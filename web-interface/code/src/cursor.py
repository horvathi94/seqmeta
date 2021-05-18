import os
import mysql.connector
from collections import OrderedDict

from .cursor_base.cursor import CursorBase

class CursorNew(CursorBase):

    user = os.environ["MYSQL_USER"];
    password = os.environ["MYSQL_PASSWORD"];
    database = os.environ["MYSQL_DATABASE"];
    host = "database";


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
                    database = self.database )

            self.cursor = self.conn.cursor();


    def close(self):

        self.cursor.close();
        self.conn.close();


    def execute(self, sql, values=[], commit=False):

        self.open();
        if len(values) == 0:
            self.cursor.execute(sql);
        else:
            self.cursor.execute(sql, values);
        if commit:
            self.conn.commit();


    def describe(self, table_name):
        sql = "DESCRIBE `{:s}`".format(table_name);
        self.execute(sql);
        raw = self.cursor.fetchall();
        return raw;


    def record_to_ordereddict(self, record, column_names):
        row_data = OrderedDict();
        for i, col in enumerate(column_names):
            row_data[col] = record[i];
        return row_data;


    def parse_records(self, records, column_names):
        res = [];
        for record in records:
            res.append(self.record_to_ordereddict(record, column_names));
        return res;


    def select_all(self, table_name, extra=""):
        sql = "SELECT * FROM `{:s}`".format(table_name);
        if extra:
            sql+= " " + extra;
        self.execute(sql);
        records = self.cursor.fetchall();
        column_names = self.cursor.column_names;
        res = self.parse_records(records, column_names);
        return res;


    def select(self, table_name, fields=[], where_clause=""):
        sql = "SELECT ";
        if len(fields) == 0:
            sql+= "* ";
        else:
            for field in fields:
               sql+= "`{:s}`,".format(field);
            sql = sql[:-1] + " ";

        sql+= "FROM {:s} ".format(table_name);
        sql+= where_clause;

        self.execute(sql);
        records = self.cursor.fetchall();
        column_names = self.cursor.column_names;

        res = [];
        for record in records:
            res.append(self.record_to_ordereddict(record, column_names));

        return res;


    def create_empty_ordereddict(self, table_name):

        describe = self.describe(table_name);
        empty_od = OrderedDict();
        empty_od["id"] = 0;

        for col in describe:
            if str(col[0]) == "id":
                continue;

            dtype = "text";
            val = "";
            if "int" in str(col[1]):
                dtype = "int";
                val = 0;
            elif "decimal" in str(col[1]):
                dtype = "float"
                val = 0;

            if col[4] != None:
                if dtype == "int":
                    val = int(col[4]);
                elif dtype == "float":
                    val = float(col[4]);
                elif dtype == "text":
                    val = str(col[4]);

            empty_od[str(col[0])] = val;

        return empty_od;


    def select_by_id(self, table_name, where_id):

        if where_id != 0:
            sql = """SELECT * FROM `{:s}`
                    WHERE `id` = {:d}
                    """.format(table_name, int(where_id));
            self.execute(sql);
            column_names = self.cursor.column_names;
            record = self.cursor.fetchone();
            res = self.record_to_ordereddict(record, column_names);
            return res;

        return self.create_empty_ordereddict(table_name);


    def update_row(self, table_name, where_id, values_dict):
        sql = "UPDATE `{:s}` SET".format(table_name);

        values = [];
        for key in values_dict:
            if key == "id":
                continue;
            sql += " {:s}=".format(key);
            sql += "%s,";

            value = values_dict[key];
            if isinstance(value, str):
                value = value.strip();
            values.append(value);

        sql = sql[:-1];
        sql+= " WHERE id = {:d}".format(where_id);
        values = tuple(values);
        self.execute(sql, values, commit=True);


    def insert_item(self, table_name, data_dict):

        sql = "INSERT INTO {:s} (".format(table_name);
        values_sql = "(";

        values = [];
        for key in data_dict:
            if key == "id":
                continue;
            sql += "{:s},".format(str(key));
            values_sql+= "%s,";

            value = data_dict[key];
            if isinstance(value, str):
                value = value.strip();
            values.append(value);

        sql = sql[:-1];
        values_sql = values_sql[:-1];
        sql+= ") VALUES ";
        values_sql+= ")";

        sql+= values_sql;
        self.execute(sql, values, commit=True);


    def count_entries(self, table_name, where_clause="", count_col="id"):

        sql = """
            SELECT COUNT(`{:s}`)
            FROM `{:s}`
            """.format(count_col, table_name);
        sql+= " ";
        sql+= where_clause;
        self.execute(sql);
        res = self.cursor.fetchone();
        res = int(res[0]);
        return res;


    def call_procedure(self, procedure, args=(), commit=False):

        self.open();
        if len(args) == 0:
            res = self.cursor.callproc(procedure);
        else:
            res = self.cursor.callproc(procedure, args);

        if commit:
            self.conn.commit();

        return res;

