from schemas.user import User
import datetime


class UsersController:
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
        user = User(name, rfc, birthdate, address, phone, email, age, gender, password)
        user.save()
        return user


