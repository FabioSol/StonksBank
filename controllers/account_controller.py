from __future__ import annotations

from schemas.account import Account
from schemas.user import User
from schemas.card import Card
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
    def get_account_by_name(name: str) -> Account:
        from users_controller import UsersController
        user = UsersController.get_user_by_name(name=name)
        return Account.get(user_id=user.id)

    @staticmethod
    def get_account_by_user(user: User) -> Account | None:
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
        balance = Account.balance + amount
        limit = Account.limit
        if balance <= limit:
            account.balance = balance
            account.save()
            return True
        else:
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
        from card_controller import CardController
        if CardController.get_cards_by_account(account)[0] is None:
            from payment_controller import PaymentController
            if PaymentController.get_payments_by_account(account) is None:
                account.delete_instance()
            else:
                print("You can´t delete the Account until you delete all Payments")
        else:
            print("You can´t delete the Account until you delete the Card")
