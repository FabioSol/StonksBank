from peewee import *

db = SqliteDatabase("./db/db_stonks.db")


class User(Model):
    name = CharField()
    rfc = CharField()
    birthdate = DateField()
    address = CharField()
    phone = CharField()
    email = CharField()
    age = IntegerField()
    gender = CharField()
    password = CharField()

    class Meta:
        database = db


