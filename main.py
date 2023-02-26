import os

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
                                           phone=phone, email=email,
                                           password=password,
                                           gender=gender,
                                           age=age)

        # Create a list of card types
        card_types = ['Blue', 'Gold', 'Platinum']

        # Generate random balance and limit values
        balance = round(random.uniform(0, 10000), 2)
        limit = round(balance * random.uniform(1.1, 2.5), 2)
        # Generate a random card type
        card_type = random.choices(card_types, weights=(90, 8, 2))[0]
        # Generate a random opening date
        opening_date = datetime.datetime.now() - timedelta(days=random.randint(1, 1000))

        # Generate a random day of the month for the cut date
        cut_date = opening_date.day

        # Create a row of data for this user_id
        AccountController.create_account(user=user,
                                         balance=balance,
                                         cut=cut_date,
                                         ac_type=card_type,
                                         open_date=opening_date,
                                         limit=limit)




if __name__ == '__main__':
    create_db("db/stonks_database.db")
    generate_fake_info(10)
