from schemas.payment import Payment
from schemas.account import Account
import datetime
from typing import Optional, List


class PaymentController:
    # Create
    @staticmethod
    def make_payment(account: Account,
                     date_time: datetime.datetime,
                     amount: float) -> Optional[Payment]:

        from controllers.account_controller import AccountController
        amount = -amount
        if AccountController.update_balance(account, amount) & (amount < 0):
            account_id = account.id
            payment = Payment(account_id=account_id, date_time=date_time, amount=amount)
            payment.save()
            return payment
        else:
            print("Failed Payment")

    # Read
    @staticmethod
    def get_required_payment(account: Account) -> float:
        debt = account.balance
        today = datetime.date.today()
        days_left = account.cut.day - today.day
        print(f"You have {days_left} days left to pay")
        return debt

    @staticmethod
    def get_payment_by_id(id:str) -> Payment or None:
        try:
            return Payment.get(id=id)
        except Payment.DoesNotExist:
            return None

    @staticmethod
    def get_payments_by_account(account: Account) -> List or None:
        try:
            return list(Payment.filter(account_id=account.id))
        except Payment.DoesNotExist:
            return None

    # Update
        # that's illegal

    # Delete
    @staticmethod
    def delete_payment(payment: Payment):
        payment.delete_instance()




