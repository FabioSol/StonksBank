from peewee import SqliteDatabase
from schemas.user import User
from schemas.account import Account
from schemas.card import Card
from schemas.payment import Payment
from schemas.charge import Charge
import time
import os


def create_db(path: str) -> bool:
    if not os.path.isfile(path):
        db = SqliteDatabase(path)
        time.sleep(1)
        db.create_tables([User, Account, Card, Payment, Charge])
        return True
