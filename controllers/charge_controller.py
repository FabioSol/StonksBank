from schemas.charge import Charge
from schemas.card import Card
import datetime
from typing import Optional
from controllers.account_controller import AccountController


class ChargeController:
    @staticmethod
    def receive_charge(card: Card,
                       date_time: datetime.datetime,
                       amount: float) -> Optional[Charge]:

        #card->account

        if AccountController.update_balance(account, amount) & (amount < 0):
            card_id = card.id
            charge = Charge(card_id=card_id, date_time=date_time, amount=amount)
            charge.save()
            return charge
        else:
            print("Failed Payment")
