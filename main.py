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

import db.migrations

pd.set_option('display.max_columns', None)

'''
# creamos usuarios
def generate_fake_users(num_users):
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

        age = str(today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day)))
        rfcp1 = name[0:2].upper() + (name.split()[1])[0:2].upper()
        rfcp2 = str(birthdate.year)[2:] + str(birthdate.month) + str(birthdate.day) + str(fake.msisdn()[0:5])
        rfc = rfcp1 + rfcp2
        print(name)
        UsersController.create_user(name=name, rfc=rfc, birthdate=birthdate, address=address, phone=phone, email=email, password=password, gender=gender, age=age)


if __name__ == '__main__':
    generate_fake_users(10)
'''

