from schemas.payment import Payment
from schemas.account import Account
from account_controller import update_balance
import datetime


class PaymentController:
    @staticmethod
    def make_payment(account: Account,
                     date_time: datetime.datetime,
                     amount: float) -> Payment:
        account_id = account.id
        payment = Payment(account_id, date_time, amount)
        payment.save()
        update_balance
        return payment
