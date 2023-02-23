from schemas.card import Card
from schemas.account import Account
from schemas.user import User
import datetime


class CardController:
    @staticmethod
    def create_card(account: Account,
                    user: User,
                    cvv: str,
                    exp_date: datetime.date,
                    nip: str) -> Card:
        card = Card(account.id, user.name, cvv, exp_date, nip)
        card.save()
        return card
