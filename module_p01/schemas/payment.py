from peewee import *
from schemas.account import Account

db = SqliteDatabase("./db/db_stonks.db", timeout=10)


class Payment(Model):
    account_id = ForeignKeyField(Account, backref="payments")
    date_time = DateTimeField()
    amount = FloatField()

    class Meta:
        database = db


