import pytest

from fixtures.user_info.model import UserData, UserInfoResponse


class TestAddUserInfo:
    def test_add_user_info(self, app, auth_user):
        """
        1. Try to add user info with valid data
        2. Check that status code is 201
        3. Check response
        """
        data = UserData.random()
        res = app.user_info.add_info(
            user_id=auth_user.uuid,
            data=data,
            type_response=UserInfoResponse,
            header=auth_user.header,
        )
        assert res.status_code == 200

    @pytest.mark.parametrize("user_id", ["100", None])
    def test_add_user_by_invalid_id(self, app, auth_user, user_id):
        """
        1. Try to add user info by in invalid it
        2. Check that status code is 404
        """
        data = UserData.random()
        res = app.user_info.add_info(
            user_id=user_id,
            data=data,
            type_response=None,
            header=auth_user.header,
        )
        assert res.status_code == 404
