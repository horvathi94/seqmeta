from os import environ
from .base.cursor import CursorBase


class Cursor(CursorBase):

    user = environ["MYSQL_USER"];
    password = environ["MYSQL_PASSWORD"];
    database = environ["MYSQL_DATABASE"];
    host = "database";
