from typing import List

from schemas.card import Card
from schemas.account import Account
from schemas.user import User
import datetime


class CardController:

    # Create
    @staticmethod
    def create_card(account: Account,
                    user: User,
                    cvv: str,
                    exp_date: datetime.date,
                    nip: str) -> Card:
        card = Card(account_id=account.id, name=user.name, cvv=cvv, exp_date=exp_date, nip=nip)
        card.save()
        return card

    # Read

    @staticmethod
    def get_cards_by_id(id: int) -> List or None:
        try:
            return list(Card.filter(id=id))
        except Card.DoesNotExist:
            return None

    @staticmethod
    def get_cards_by_account(account: Account) -> List or None:
        try:
            return list(Card.filter(account_id=account.id))
        except Card.DoesNotExist:
            return None

    @staticmethod
    def get_cards_by_name(name: str) -> List or None:
        try:
            return list(Card.filter(name=name))
        except Card.DoesNotExist:
            return None

    # Update
    @staticmethod
    def update_nip(card: Card, nip: str):
        if nip.isnumeric() & (len(nip) == 4):
            card.nip = nip
        else:
            print("not a valid nip")

    # Delete
    @staticmethod
    def delete_card(card: Card):
        from account_controller import AccountController
        account = AccountController.get_account_by_card(card)
        balance = account.balance
        if balance <= 0:
            from charge_controller import ChargeController
            if ChargeController.get_charges_by_card(card) is None:
                card.delete_instance()
            else:
                print("There are charges left to delete")
        else:
            print("To delete Card balance need to be 0")
