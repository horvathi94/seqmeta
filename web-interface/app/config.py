from os import environ

class Config:

    DEBUG = True;


    JSON_SORT_KEYS  = False;


    SQLALCHEMY_DATABASE_URI = \
        "mysql://admin:12345@database:3306/sequencing_data";
    SQLALCHEMY_TRACK_MODIFICATIONS = False;
