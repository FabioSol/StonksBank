from schemas.payment import Payment
from schemas.account import Account
import datetime
from typing import Optional
from controllers.account_controller import AccountController


class PaymentController:
    @staticmethod
    def make_payment(account: Account,
                     date_time: datetime.datetime,
                     amount: float) -> Optional[Payment]:
        if AccountController.update_balance(account, amount):
            account_id = account.id
            payment = Payment(account_id=account_id, date_time=date_time, amount=amount)
            payment.save()
            return payment
        else:
            print("Failed Payment")
