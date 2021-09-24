import pytest

from fixtures.constants import ResponseText
from fixtures.auth.model import AuthUserResponse, AuthUser
from fixtures.register.model import RegisterUserResponse, RegisterUser


class TestLoginUser:
    def test_login_user_with_registered_data(self, app):
        """
        1. Try to login user with valid data
        2. Check that status code is 201
        3. Check response
        """
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert res.data.message == ResponseText.MESSAGE_REGISTER_USER
        res_auth = app.login.login(data=data, type_response=AuthUserResponse)
        assert res_auth.status_code == 200

    def test_login_user_with_unregistered_data(self, app):
        """
        1. Try to login user with invalid data
        2. Check that status code is 401
        3. Check response
        """
        data = AuthUser.random()
        res_auth = app.login.login(data=data)
        assert res_auth.status_code == 401

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_user_with_empty_data(self, app, field):
        """
        1. Try to login user with invalid data
        2. Check that status code is 401
        3. Check response
        """
        data = AuthUser.random()
        setattr(data, field, None)
        res_auth = app.login.login(data=data)
        assert res_auth.status_code == 401
