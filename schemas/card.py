from peewee import *
from schemas.account import Account

db = SqliteDatabase("./db/db_stonks.db", timeout=10)


class Card(Model):
    account_id = ForeignKeyField(Account, backref="cards")
    name = CharField()
    cvv = CharField()
    exp_date = DateField()
    nip = CharField()


    class Meta:
        database = db

