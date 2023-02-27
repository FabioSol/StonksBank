from schemas.charge import Charge
from schemas.card import Card
from schemas.account import Account
import datetime
from typing import Optional


class ChargeController:

    # Create
    @staticmethod
    def receive_charge(card: Card,
                       date_time: datetime.datetime,
                       amount: float) -> Optional[Charge]:
        from controllers.account_controller import AccountController
        
        account = Account.get(id=card.account_id)

        if AccountController.update_balance(account, amount) & (amount > 0):
            card_id = card.id
            charge = Charge(card_id=card_id, date_time=date_time, amount=amount)
            charge.save()
            return charge
        else:
            print("Failed Payment")


    # Read
    @staticmethod
    def get_charges_by_id(id: int) -> Charge or None:
        try:
            return Charge.get(id=id)
        except Charge.DoesNotExist:
            print("Charge does not exist")
            return None
    @staticmethod
    def get_charges_by_card(card: Card) -> list or None:
        try:
            return list(Charge.filter(card_id=card.id))
        except Charge.DoesNotExist:
            print("There are no charges")
            return None

    # Update
        # that's illegal

    # Delete
    @staticmethod
    def delete_charge(charge: Charge):
        charge.delete_instance()





