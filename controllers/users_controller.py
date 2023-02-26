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
