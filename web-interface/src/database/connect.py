import os
import mysql.connector
from typing import List


class Connect:

    host = "database"


    def __init__(self):
        self.user = os.environ["MYSQL_USER"]
        self.password = os.environ["MYSQL_PASSWORD"]
        self.database = os.environ["MYSQL_DATABASE"]
        self.connection = None
        self.cursor = None


    def connect(self) -> None:
        try:
            self.connection = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database)
            self.cursor = self.connection.cursor(dictionary=True)
        except Exception as e:
            raise Exception(f"Failed to connect to database. {e}")


    def close(self) -> None:
        self.cursor.close()
        if self.connection is None: return
        self.connection.close()
        del self.connection


    def execute_sql(self, sql: str, values: any,
                    commit: bool=True,
                    last_insert: bool=False) -> int:
        self.connect()
        self.cursor.execute(sql, values)
        if commit: self.connection.commit()
        ret = self.cursor.lastrowid if last_insert else None
        self.close()
        return ret


    def call_procedure(self, proc_name: str,
                       values: tuple,
                       commit: bool=True) -> None:
        self.connect()
        res = self.cursor.callproc(proc_name, values)
        if commit: self.connection.commit()
        self.close()
        return res


    def fetchall(self, sql: str) -> List[dict]:
        self.connect()
        self.cursor.execute(sql)
        raw = self.cursor.fetchall()
        self.close()
        return raw


    def fetchone(self, sql: str) -> dict:
        self.connect()
        self.cursor.execute(sql)
        raw = self.cursor.fetchone()
        self.close()
        return raw
