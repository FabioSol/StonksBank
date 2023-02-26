from peewee import *
from schemas.card import Card

db = SqliteDatabase("../db/db_stonks.db")


class Charge(Model):
    card_id = ForeignKeyField(Card, backref="charges")
    date_time = DateTimeField()
    amount = FloatField()

    class Meta:
        database = db



