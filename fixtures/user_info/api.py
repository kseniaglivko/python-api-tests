from requests import Response

from fixtures.user_info.model import UserData
from fixtures.validator import Validator
from common.deco import logging as log


class UserInfo(Validator):
    def __init__(self, app):
        self.app = app

    POST_USER_INFO = "/user_info/{}"

    @log("Add user info")
    def add_info(
        self, user_id: int, data: UserData, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/auserInfoAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    PUT_USER_INFO = "/user_info/{}"

    @log("Update user info")
    def update_info(
        self, user_id: int, data: UserData, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoUpdate # noqa
        """
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.PUT_USER_INFO.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)
