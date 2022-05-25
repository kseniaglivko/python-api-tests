import pytest

from fixtures.user_info.model import UserInfoResponse


class TestGetUserInfo:
    @pytest.mark.xfail(reason="BUG: Response is 404 User info not found")
    def test_get_user_info(self, app, auth_user):
        """
        1. Try to get user info with valid data
        2. Check that status code is 200
        3. Check response
        """
        res = app.user_info.get_info(
            user_id=auth_user.uuid,
            type_response=UserInfoResponse,
            header=auth_user.header,
        )
        assert res.status_code == 200

    @pytest.mark.parametrize("user_id", ["100", None])
    def test_get_user_by_invalid_id(self, app, auth_user, user_id):
        """
        1. Try to get user info by in invalid it
        2. Check that status code is 404
        """
        res = app.user_info.get_info(
            user_id=user_id,
            type_response=None,
            header=auth_user.header,
        )
        assert res.status_code == 404
