from schemas.account import Account
from schemas.user import User
import datetime


class AccountController:
    @staticmethod
    def create_account(user: User,
                       balance: float,
                       cut: datetime.date,
                       ac_type: str,
                       open_date: datetime.date,
                       limit: float) -> Account:
        account = Account(user.id, balance, cut, ac_type, open_date, limit)
        account.save()
        return account

    @staticmethod
    def update_balance(account: Account, amount: float) -> bool:
        balance = Account.balance + amount
        limit = Account.limit
        if balance >= limit:
            account.balance = balance
            account.save()
            return True
        else:
            return False


