import os
import time

from faker import Faker
import datetime
import pandas as pd
import random
from datetime import timedelta

from schemas.user import User
from schemas.account import Account
from schemas.card import Card
from schemas.charge import Charge
from schemas.payment import Payment

from controllers.users_controller import UsersController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from controllers.charge_controller import ChargeController
from controllers.payment_controller import PaymentController

from db.migrations import create_db

pd.set_option('display.max_columns', None)


def generate_fake_info(num_users):
    fake = Faker()
    for i in range(num_users):
        gender = random.choice(['M', 'F'])
        if gender == 'M':
            name = fake.name_male()
        else:
            name = fake.name_female()
        birthdate = fake.date_of_birth(minimum_age=18, maximum_age=65)
        today = datetime.date.today()
        address = fake.address()
        phone = fake.numerify('(###) ###-####')
        email = name.replace(' ', '_').replace('.', '') + "@outlook.com"
        password = fake.password()

        age = (today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day)))
        rfcp1 = name[0:2].upper() + (name.split()[1])[0:2].upper()
        rfcp2 = str(birthdate.year)[2:] + str(birthdate.month) + str(birthdate.day) + str(fake.msisdn()[0:5])
        rfc = rfcp1 + rfcp2
        user = UsersController.create_user(name=name,
                                           rfc=rfc,
                                           birthdate=birthdate,
                                           address=address,
                                           phone=phone,
                                           email=email,
                                           password=password,
                                           gender=gender,
                                           age=age)

        card_types = ['Blue', 'Gold', 'Platinum']

        balance = round(random.uniform(0, 10000), 2)
        limit = round(balance * random.uniform(1.1, 2.5), 2)
        card_type = random.choices(card_types, weights=(90, 8, 2), k=1)[0]
        opening_date = datetime.datetime.now() - timedelta(days=random.randint(365, 1000))

        cut_date = opening_date.day

        account = AccountController.create_account(user=user,
                                                   balance=balance,
                                                   cut=cut_date,
                                                   ac_type=card_type,
                                                   open_date=opening_date,
                                                   limit=limit)

        CardController.create_card(account=account,
                                   user=user,
                                   cvv=str(random.randint(111, 999)),
                                   exp_date=account.open_date + datetime.timedelta(days=5 * 365),
                                   nip=str(random.randint(1111, 9999)))


if __name__ == '__main__':
    create_db("db/stonks_database.db")
    generate_fake_info(5)

    print("Accounts: ")
    for a in Account.select():
        print(a.id, a.user_id, a.balance, a.cut, a.type, a.open_date, a.limit)

    card = CardController.get_card_by_id(2)
    ChargeController.receive_charge(card, datetime.datetime.today(), 100)

    card = CardController.get_card_by_id(4)
    ChargeController.receive_charge(card, datetime.datetime.today(), 100)

    card = CardController.get_card_by_id(5)
    ChargeController.receive_charge(card, datetime.datetime.today(), 100000)

    for i in range(1, 5+1):
        account = AccountController.get_account_by_id(i)
        req_pay = PaymentController.get_required_payment(account)
        PaymentController.make_payment(account, datetime.datetime.today(), req_pay)


    print("Users: ")
    for u in User.select():
        print(u.id, u.name, u.rfc, u.birthdate, u.address, u.phone, u.email, u.password, u.gender, u.age)

    print("Accounts: ")
    for a in Account.select():
        print(a.id, a.user_id, a.balance, a.cut, a.type, a.open_date, a.limit)

    print("Cards:")
    for c in Card.select():
        print(c.id, c.account_id, c.name, c.cvv, c.exp_date, c.nip)

    print("Charges:")
    for ch in Charge.select():
        print(ch.id, ch.card_id, ch.date_time, ch.amount)
        ChargeController.delete_charge(ch)

    print("Payments:")
    for p in Payment.select():
        print(p.id, p.account_id, p.date_time, p.amount)
        PaymentController.delete_payment(p)

    for c in Card.select():
        CardController.delete_card(c)

    for a in Account.select():
        AccountController.delete_account(a)

    for u in User.select():
        UsersController.delete_user(u)



