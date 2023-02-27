from peewee import SqliteDatabase
from schemas.user import User
from schemas.account import Account
from schemas.card import Card
from schemas.payment import Payment
from schemas.charge import Charge
import time

db = SqliteDatabase("db_stonks.db")

time.sleep(1)

db.create_tables([User, Account, Card, Payment, Charge])


