from schemas.account import Account
from schemas.user import User
from schemas.card import Card
from schemas.payment import Payment
from typing import Union
import datetime


class AccountController:
    # Create
    @staticmethod
    def create_account(user: User,
                       balance: float,
                       cut: int,
                       ac_type: str,
                       open_date: datetime.date,
                       limit: float) -> Account:
        account = Account(user_id=user.id, balance=balance, cut=cut, type=ac_type, open_date=open_date, limit=limit)
        account.save()
        return account

    # Read

    @staticmethod
    def get_account_by_id(id: int) -> Account:
        return Account.get(id=id)

    @staticmethod
    def get_account_by_name(name: str) -> Account:
        user = User.get(name=name)
        return Account.get(user_id=user.id)

    @staticmethod
    def get_account_by_user(user: User) -> Union[Account, None]:
        try:
            return Account.get(user_id=user.id)
        except Account.DoesNotExist:
            return None

    @staticmethod
    def get_account_by_card(card: Card):
        return Account.get(id=card.account_id)

    # Update
    @staticmethod
    def update_balance(account: Account, amount: float) -> bool:
        balance = account.balance + amount
        limit = account.limit
        if balance <= limit:
            account.balance = balance
            account.save()
            return True
        else:
            print("not enough credit")
            return False

    @staticmethod
    def update_cut(account: Account, cut: int) -> Account:
        if cut <= 31:
            account.cut = cut
            account.save()
            return account
        else:
            print("Not a valid day")

    @staticmethod
    def update_limit(account: Account, limit: int) -> Account:
        account.limit = limit
        account.save()
        return account

    # Delete
    @staticmethod
    def delete_account(account: Account):
        try:
            card = Card.get(account_id=account.id)
        except:
            card = None
        if card is None:
            try:
                payment = Payment.get(account_id=account.id)
            except:
                payment = None
            if payment is None:
                account.delete_instance()
            else:
                print("You can´t delete the Account until you delete all Payments")
        else:
            print("You can´t delete the Account until you delete the Card")
