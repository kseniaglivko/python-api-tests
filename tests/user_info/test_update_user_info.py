import pytest

from fixtures.user_info.model import UserData, UpdateUserInfo, UpdateUserInfoResponse


class TestUpdateUserInfo:
    def test_update_userinfo(self, app, user_info):
        """
        Steps.
            1. Try to login user with valid data
            2. Add user info
            3. Change user data
            4. Check that status code is 200
            5. Check response
        """
        data = UpdateUserInfo.random()
        res = app.user_info.update_info(
            user_id=user_info.uuid,
            data=data,
            type_response=UpdateUserInfoResponse,
            header=user_info.header,
        )
        assert res.status_code == 200

    @pytest.mark.parametrize("uuid", ["fffdddaass", -10000, "@#*/%", True])
    def test_update_user_info_invalid_id(self, app, user_info, uuid):
        """
        Steps:
            1. Login with valid data.
            2. Change user data with invalid uuid.
            3. Check status code is 404.
        """
        data = UserData.random()
        res = app.user_info.update_info(
            user_id=uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 404

    def test_update_user_info_not_existing_id(self, app, user_info, uuid=1000):
        """
        Steps:
            1. Login with valid data.
            2. Change user data with not existing uuid: uuid "1000" doesn't exist.
            3. Check status code is 404.
        """
        data = UserData.random()
        res = app.user_info.update_info(
            user_id=uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 404

    @pytest.mark.xfail
    def test_update_user_info_long_phone_number(
        self, app, user_info, phone="1" * 10000
    ):
        """
        Steps:
            1. Login with valid data.
            2. Change user data with long phone number (10000 digits long).
            3. Check status code is 404.
        """
        data = UserData.random()
        setattr(data, "phone", phone)
        res = app.user_info.update_info(
            user_id=user_info.uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 400

    def test_update_user_info_empty_header(self, app, user_info):
        """
        Steps:
            1. Login with valid data.
            2. Change user data with empty header.
            3. Check status code is 404.
        """
        data = UserData.random()
        res = app.user_info.update_info(
            user_id=user_info.uuid,
            data=data,
            type_response=None,
            header=None,
        )
        assert res.status_code == 401

    def test_update_user_info_invalid_header(self, app, user_info):
        """
        Steps:
            1. Login with valid data.
            2. Change user data with invalid header.
            3. Check status code is 404.
        """
        data = UserData.random()
        res = app.user_info.update_info(
            user_id=user_info.uuid,
            data=data,
            type_response=None,
            header={"Authorization": "JWT 6d4gerg4re6g46er4g6r854"},
        )
        assert res.status_code == 401
