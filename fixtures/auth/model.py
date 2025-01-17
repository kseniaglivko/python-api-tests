from faker import Faker
import attr

from fixtures.base import BaseClass
from fixtures.user_info.model import UserData

fake = Faker()


@attr.s
class AuthUser(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return AuthUser(username=fake.email(), password=fake.password())


@attr.s
class AuthUserResponse:
    access_token: str = attr.ib()


@attr.s
class UserType:
    header: dict = attr.ib(default=None)
    uuid: int = attr.ib(default=None)
    data: UserData = attr.ib(default=None)
