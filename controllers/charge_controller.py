from schemas.charge import Charge
from schemas.card import Card
from schemas.account import Account
import datetime
from typing import Optional
from typing import Union


class ChargeController:

    # Create
    @staticmethod
    def receive_charge(card: Card,
                       date_time: datetime.datetime,
                       amount: float) -> Optional[Charge]:
        from controllers.account_controller import AccountController

        account = Account.get(id=card.account_id)

        if amount > 0:
            card_id = card.id
            charge = Charge(card_id=card_id, date_time=date_time, amount=amount)
            ub = False
            cs = False
            try:
                ub = AccountController.update_balance(account, amount)
                if ub:
                    cs = charge.save()
                return charge
            except:
                print("charge failed")
            finally:
                if ub & (not cs):
                    AccountController.update_balance(account, -amount)

        else:
            print("invalid amount")

    # Read
    @staticmethod
    def get_charge_by_id(id: int) -> Union[Charge, None]:
        try:
            return Charge.get(id=id)
        except Charge.DoesNotExist:
            print("Charge does not exist")
            return None

    @staticmethod
    def get_charges_by_card(card: Card) -> Union[list[Charge], None]:
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
