import logging

import pytest

from fixtures.app import StoreApp
from fixtures.auth.model import AuthUserResponse, UserType
from fixtures.register.model import RegisterUser, RegisterUserResponse
from fixtures.user_info.model import UserData, UserInfoResponse

logger = logging.getLogger("api")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start api tests, url is {url}")
    return StoreApp(url)


@pytest.fixture
def auth_user(app):
    data = RegisterUser.random()
    res_register = app.register.register(data=data, type_response=RegisterUserResponse)
    res_auth = app.login.login(data=data, type_response=AuthUserResponse)
    uuid = res_register.data.uuid
    token = res_auth.data.access_token
    header = {"Authorization": f"JWT {token}"}
    return UserType(header=header, uuid=uuid)


@pytest.fixture
def user_info(app, auth_user):
    data = UserData.random()
    app.user_info.add_info(
        user_id=auth_user.uuid,
        data=data,
        type_response=UserInfoResponse,
        header=auth_user.header,
    )
    return UserType(header=auth_user.header, uuid=auth_user.uuid, data=data)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    ),
