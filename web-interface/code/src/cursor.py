import os
from .base.cursor import CursorBase

class Cursor(CursorBase):

    user = os.environ["MYSQL_USER"];
    password = os.environ["MYSQL_PASSWORD"];
    database = os.environ["MYSQL_DATABASE"];
    host = "database";
