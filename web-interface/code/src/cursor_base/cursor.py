import mysql.connector
from collections import OrderedDict
from .parse_functions import parse_records, \
    create_empty_ordereddict, \
    clean_value

class CursorBase:

    user = "";
    password = "";
    database = "";
    host = "";

    def __init__(self):
        pass;


    @classmethod
    def open_connection(cls):
        conn = mysql.connector.connect(
            user = cls.user,
            password = cls.password,
            host = cls.host,
            database = cls.database);
        return conn;


    @classmethod
    def create_cursor(cls):
        conn = cls.open_connection();
        cursor = conn.cursor();
        return conn, cursor;


    @staticmethod
    def close(conn, cursor):
        cursor.close();
        conn.close();


    @classmethod
    def describe(cls, table_name, cursor=None):
        sql = "DESCRIBE `{:s}`".format(table_name);
        if cursor == None:
            conn, c = cls.create_cursor();
        else:
            conn = None;
            c = cursor;
        c.execute(sql);
        raw = c.fetchall();
        if cursor == None:
            cls.close(conn, c);
        return raw;


    @classmethod
    def empty_ordereddict(cls, table_name, cursor=None):
        describe = cls.describe(table_name, cursor=cursor);
        return create_empty_ordereddict(describe);


    @classmethod
    def select(cls, table_name, fields=[], clauses=""):
        sql = "SELECT ";
        if len(fields) == 0:
            sql+= "*";
        else:
            for field in fields:
                sql += "`{:s}`, ".format(field);
            sql = sql[:-2];
        sql+= " FROM `{:s}` ".format(table_name) + clauses;

        conn, cursor = cls.create_cursor();
        cursor.execute(sql);
        records = cursor.fetchall();
        column_names = cursor.column_names;

        result = parse_records(records, column_names);
        if len(result) == 0:
            result = cls.empty_ordereddict(table_name, cursor=cursor);

        cls.close(conn, cursor);
        return result;


    @classmethod
    def select_all(cls, table_name, clauses=""):
        return cls.select(table_name, clauses=clauses);


    @classmethod
    def update_row(cls, table_name, where_clause, values_dict):
        sql = "UPDATE `{:s}` SET ".format(table_name);
        values = [clean_value(values_dict[key]) for key in values_dict];
        for key in values_dict:
            if key == "id":
                continue;
            sql += "{:s}=%s, ".format(key);
        sql = sql[:-2] + " " + where_clause;
        conn, cursor = cls.create_cursor();
        cursor.execute(sql, tuple(values));
        conn.commit();
        cls.close(conn, cursor);


    @classmethod
    def insert_row(cls, table_name, values_dict):
        sql = "INSERT INTO {:s} (".format(table_name);
        values = [clean_value(values_dict[key]) for key in values_dict];
        values_sql = "(";
        for key in values_dict:
            if key == "id":
                continue;
            sql += "{:s}, ".format(str(key));
            values_sql+= "%s, ";
        sql = sql[:-2] +  ") VALUES ";
        sql+= values_sql[:-2] + ")";
        conn, cursor = cls.create_cursor();
        cursor.execute(sql, tuple(values);
        conn.commit();
        cls.close(conn, cursor);


    @classmethod
    def call_procedure(cls, procedure, args=(), commit=False):
        conn, cursor = cls.create_cursor();

        if len(args) == 0:
            res = cursor.callproc(procedure);
        else:
            res = cursor.callproc(procedure, args);

        if commit:
            conn.commit();

        cls.close(conn, cursor);
        return res;







