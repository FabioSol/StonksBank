from schemas.card import Card
from schemas.charge import Charge
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
    def get_card_by_id(id: int) -> Card | None:
        try:
            return Card.get(id=id)
        except Card.DoesNotExist:
            return None

    @staticmethod
    def get_cards_by_account(account: Account) -> list[Card] | None:
        try:
            return list(Card.filter(account_id=account.id))
        except Card.DoesNotExist:
            return None

    @staticmethod
    def get_cards_by_name(name: str) -> list[Card] | None:
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
        account = Account.get(id=card.account_id)
        balance = account.balance
        if balance <= 0:
            try:
                charge = Charge.get(card_id=card.id)
            except:
                charge = None
            if charge is None:
                card.delete_instance()
            else:
                print("There are charges left to delete")
        else:
            print("To delete Card balance need to be 0")
