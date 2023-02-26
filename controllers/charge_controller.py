from schemas.charge import Charge
from schemas.account import Account
import datetime
from typing import Optional
from controllers.account_controller import AccountController


class ChargeController:
    @staticmethod
    def receive_charge(account: Account,
                       date_time: datetime.datetime,
                       amount: float) -> Optional[Charge]:
        if AccountController.update_balance(account, amount) & (amount < 0):
            account_id = account.id
            charge = Charge(account_id, date_time, amount)
            charge.save()
            return charge
        else:
            print("Failed Payment")
