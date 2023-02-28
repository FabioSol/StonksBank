from schemas.user import User
from schemas.account import Account
import datetime


class UsersController:

    # Create
    @staticmethod
    def create_user(name: str,
                    rfc: str,
                    birthdate: datetime.date,
                    address: str,
                    phone: str,
                    email: str,
                    age: int,
                    gender: str,
                    password: str) -> User:
        user = User(name=name,
                    rfc=rfc,
                    birthdate=birthdate,
                    address=address,
                    phone=phone,
                    email=email,
                    age=age,
                    gender=gender,
                    password=password)
        user.save()
        return user

    # Read
    @staticmethod
    def get_user_by_id(id: int) -> User:
        return User.get(id=id)

    @staticmethod
    def get_user_by_name(name: str) -> User:
        return User.get(name=name)

    @staticmethod
    def get_user_by_rfc(rfc: str) -> User:
        return User.get(rfc=rfc)

    # Update
    @staticmethod
    def update_address(user: User, address: str) -> User:
        user.address = address
        user.save()
        return user

    @staticmethod
    def update_phone(user: User, phone: str) -> User:
        user.phone = phone
        user.save()
        return user

    @staticmethod
    def update_email(user: User, email: str) -> User:
        user.email = email
        user.save()
        return user

    @staticmethod
    def update_gender(user: User, gender: str) -> User:
        user.gender = gender
        user.save()
        return user

    # Delete
    @staticmethod
    def delete_user(user: User):
        try:
            account = Account.get(user_id=user.id)
        except:
            account = None
        if account is None:
            user.delete_instance()
        else:
            print("You can´t delete the user until you delete the account")
