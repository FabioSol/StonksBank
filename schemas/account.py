from peewee import *
from schemas.user import User

db = SqliteDatabase("./db/db_stonks.db")


class Account(Model):
    user_id = ForeignKeyField(User, backref="accounts")
    balance = FloatField()
    cut = DateField()
    type = CharField()
    open_date = DateField()
    limit = FloatField()

    class Meta:
        database = db
