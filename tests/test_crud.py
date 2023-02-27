from datetime import datetime

import pytest

from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from controllers.charge_controller import ChargeController
from controllers.payment_controller import PaymentController
from controllers.users_controller import UsersController


def test_create_user_create_account_make_payment():
    user = UsersController.create_user(name='Beto Carlos del Toro',
                                       rfc='CDTB990817TEE',
                                       birthdate=datetime.strptime('17/08/1999', '%d/%m/%Y'),
                                       address='P. Sherman Wallaby Sydney',
                                       phone='4206966666',
                                       email='carlos@toro.com',
                                       password='P*neloco669',
                                       gender='F',
                                       age=23)
    assert user.name == 'Beto Carlos del Toro'
    assert user.rfc == 'CDTB990817TEE'
    assert user.birthdate == datetime.strptime('17/08/1999', '%d/%m/%Y')
    assert user.address == 'P. Sherman Wallaby Sydney'
    assert user.phone == '4206966666'
    assert user.email == 'carlos@toro.com'
    assert user.password == 'P*neloco669'
    assert user.gender == 'F'
    assert user.age == 23

    account = AccountController.create_account(user=user,
                                               balance=420,
                                               cut=datetime.strptime('17/08/2023', '%d/%m/%Y'),
                                               ac_type='Gold',
                                               open_date=datetime.today(),
                                               limit=666)

    assert account.user_id == user
    assert account.balance == 420
    assert account.cut == datetime.strptime('17/08/2023', '%d/%m/%Y')
    assert account.type == 'Gold'
    assert account.limit == 666

    payment_1 = PaymentController.make_payment(account=account,
                                               date_time=datetime.today(),
                                               amount=69)
    assert payment_1.account_id == account
    assert payment_1.amount == -69
    assert account.balance == 420 - 69

    required = PaymentController.get_required_payment(account=account)

    assert required == 420 - 69

    card_gold = CardController.create_card(account=account,
                                           user=user,
                                           cvv='666',
                                           exp_date=datetime.strptime('17/08/2026', '%d/%m/%Y'),
                                           nip='4201')

    charges = ChargeController.receive_charge(card_gold,
                                              date_time=datetime.today(),
                                              amount=51)
    assert charges.amount == 51
    assert account.balance == 420 - 69 + 51
