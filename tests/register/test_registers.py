import pytest

from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUser, RegisterUserResponse
from fixtures.user_info.model import UserInfoResponse


class TestRegisterUser:
    def test_register_user_with_valid_data(self, app):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        """
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert res.data.message == ResponseText.MESSAGE_REGISTER_USER

    @pytest.mark.parametrize("field", ["username", "password"])
    def test_register_user_without_required_data(self, app, field):
        """
        1. Try to register user without required fields
        2. Check that status code is 400
        3. Check response
        """
        data = RegisterUser.random()
        setattr(data, field, None)
        res = app.register.register(data=data, type_response=UserInfoResponse)
        assert res.status_code == 400
        assert res.data.message == ResponseText.REGISTRATION_ERROR_MESSAGE
