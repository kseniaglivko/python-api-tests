from fixtures.user_info.model import UserData, UserInfoResponse


class TestLoginUser:
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
